import asyncio
from playwright.async_api import async_playwright
import os
import tempfile
from bs4 import BeautifulSoup
import aiohttp

class WebCrawler:
    def __init__(self):
        self.temp_dir = tempfile.mkdtemp()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

    async def _extract_text_with_playwright(self, url):
        """Extract text content from a URL using Playwright"""
        async with async_playwright() as p:
            browser = await p.chromium.launch()
            page = await browser.new_page()
            await page.goto(url)
            content = await page.content()
            await browser.close()
            
            soup = BeautifulSoup(content, 'html.parser')
            # Remove script and style elements
            for script in soup(["script", "style"]):
                script.decompose()
            
            # Get text and clean it
            text = soup.get_text(separator='\n', strip=True)
            metadata = f"Source URL: {url}\n\n"
            return metadata + text

    async def _extract_text_with_requests(self, url):
        """Extract text content from a URL using aiohttp"""
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=self.headers) as response:
                html = await response.text()
                soup = BeautifulSoup(html, 'html.parser')
                
                # Remove script and style elements
                for script in soup(["script", "style"]):
                    script.decompose()
                
                # Get text and clean it
                text = soup.get_text(separator='\n', strip=True)
                metadata = f"Source URL: {url}\n\n"
                return metadata + text

    async def crawl_single_url(self, url):
        """Crawl a single URL and save content to MD file"""
        try:
            try:
                # First try with aiohttp
                content = await self._extract_text_with_requests(url)
            except:
                # If that fails, try with Playwright
                content = await self._extract_text_with_playwright(url)
            
            file_path = os.path.join(self.temp_dir, 'crawled_content.md')
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return file_path
        except Exception as e:
            raise Exception(f"Error crawling URL: {str(e)}")

    async def crawl_sitemap(self, sitemap_url):
        """Crawl entire sitemap and save content to MD file"""
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(sitemap_url, headers=self.headers) as response:
                    sitemap_content = await response.text()
                    
            soup = BeautifulSoup(sitemap_content, 'xml')
            urls = [loc.text for loc in soup.find_all('loc')]
            
            all_content = []
            for url in urls:
                try:
                    content = await self._extract_text_with_requests(url)
                    all_content.append(content)
                except:
                    try:
                        content = await self._extract_text_with_playwright(url)
                        all_content.append(content)
                    except Exception as e:
                        print(f"Error crawling {url}: {str(e)}")
                        continue
            
            file_path = os.path.join(self.temp_dir, 'sitemap_content.md')
            with open(file_path, 'w', encoding='utf-8') as f:
                for content in all_content:
                    f.write(content + '\n---\n')
            return file_path
        except Exception as e:
            raise Exception(f"Error crawling sitemap: {str(e)}")

    def cleanup(self):
        """Clean up temporary files"""
        import shutil
        shutil.rmtree(self.temp_dir)

    # Synchronous wrapper methods for compatibility
    def crawl_single_url_sync(self, url):
        return asyncio.run(self.crawl_single_url(url))

    def crawl_sitemap_sync(self, sitemap_url):
        return asyncio.run(self.crawl_sitemap(sitemap_url)) 