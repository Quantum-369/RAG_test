# Scraped Content

# URL: https://docs.crawl4ai.com/

[Crawl4AI Documentation](https://docs.crawl4ai.com/<https:/docs.crawl4ai.com/>)
  * [ Home ](https://docs.crawl4ai.com/<.>)
  * [ Quick Start ](https://docs.crawl4ai.com/<core/quickstart/>)
  * [ Search ](https://docs.crawl4ai.com/<#>)


  * Home
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/<core/installation/>)
    * [Docker Deployment](https://docs.crawl4ai.com/<core/docker-deploymeny/>)
  * [Quick Start](https://docs.crawl4ai.com/<core/quickstart/>)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/<blog/>)
    * [Changelog](https://docs.crawl4ai.com/<https:/github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md>)
  * Core
    * [Simple Crawling](https://docs.crawl4ai.com/<core/simple-crawling/>)
    * [Crawler Result](https://docs.crawl4ai.com/<core/crawler-result/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/<core/browser-crawler-config/>)
    * [Markdown Generation](https://docs.crawl4ai.com/<core/markdown-generation/>)
    * [Fit Markdown](https://docs.crawl4ai.com/<core/fit-markdown/>)
    * [Page Interaction](https://docs.crawl4ai.com/<core/page-interaction/>)
    * [Content Selection](https://docs.crawl4ai.com/<core/content-selection/>)
    * [Cache Modes](https://docs.crawl4ai.com/<core/cache-modes/>)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/<core/local-files/>)
    * [Link & Media](https://docs.crawl4ai.com/<core/link-media/>)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/<advanced/advanced-features/>)
    * [File Downloading](https://docs.crawl4ai.com/<advanced/file-downloading/>)
    * [Lazy Loading](https://docs.crawl4ai.com/<advanced/lazy-loading/>)
    * [Hooks & Auth](https://docs.crawl4ai.com/<advanced/hooks-auth/>)
    * [Proxy & Security](https://docs.crawl4ai.com/<advanced/proxy-security/>)
    * [Session Management](https://docs.crawl4ai.com/<advanced/session-management/>)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/<advanced/multi-url-crawling/>)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/<advanced/crawl-dispatcher/>)
    * [Identity Based Crawling](https://docs.crawl4ai.com/<advanced/identity-based-crawling/>)
    * [SSL Certificate](https://docs.crawl4ai.com/<advanced/ssl-certificate/>)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/<extraction/no-llm-strategies/>)
    * [LLM Strategies](https://docs.crawl4ai.com/<extraction/llm-strategies/>)
    * [Clustering Strategies](https://docs.crawl4ai.com/<extraction/clustring-strategies/>)
    * [Chunking](https://docs.crawl4ai.com/<extraction/chunking/>)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/<api/async-webcrawler/>)
    * [arun()](https://docs.crawl4ai.com/<api/arun/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/<api/parameters/>)
    * [CrawlResult](https://docs.crawl4ai.com/<api/crawl-result/>)
    * [Strategies](https://docs.crawl4ai.com/<api/strategies/>)


  * [🚀🤖 Crawl4AI: Open-Source LLM-Friendly Web Crawler & Scraper](https://docs.crawl4ai.com/<#crawl4ai-open-source-llm-friendly-web-crawler-scraper>)
  * [Quick Start](https://docs.crawl4ai.com/<#quick-start>)
  * [What Does Crawl4AI Do?](https://docs.crawl4ai.com/<#what-does-crawl4ai-do>)
  * [Documentation Structure](https://docs.crawl4ai.com/<#documentation-structure>)
  * [How You Can Support](https://docs.crawl4ai.com/<#how-you-can-support>)
  * [Quick Links](https://docs.crawl4ai.com/<#quick-links>)


# 🚀🤖 Crawl4AI: Open-Source LLM-Friendly Web Crawler & Scraper
[ ![unclecode%2Fcrawl4ai | Trendshift](https://trendshift.io/api/badge/repositories/11716) ](https://docs.crawl4ai.com/<https:/trendshift.io/repositories/11716>)
[ ![GitHub Stars](https://img.shields.io/github/stars/unclecode/crawl4ai?style=social) ](https://docs.crawl4ai.com/<https:/github.com/unclecode/crawl4ai/stargazers>) [ ![GitHub Forks](https://img.shields.io/github/forks/unclecode/crawl4ai?style=social) ](https://docs.crawl4ai.com/<https:/github.com/unclecode/crawl4ai/network/members>) [ ![PyPI version](https://badge.fury.io/py/crawl4ai.svg) ](https://docs.crawl4ai.com/<https:/badge.fury.io/py/crawl4ai>)
[ ![Python Version](https://img.shields.io/pypi/pyversions/crawl4ai) ](https://docs.crawl4ai.com/<https:/pypi.org/project/crawl4ai/>) [ ![Downloads](https://static.pepy.tech/badge/crawl4ai/month) ](https://docs.crawl4ai.com/<https:/pepy.tech/project/crawl4ai>) [ ![License](https://img.shields.io/github/license/unclecode/crawl4ai) ](https://docs.crawl4ai.com/<https:/github.com/unclecode/crawl4ai/blob/main/LICENSE>)
Crawl4AI is the #1 trending GitHub repository, actively maintained by a vibrant community. It delivers blazing-fast, AI-ready web crawling tailored for large language models, AI agents, and data pipelines. Fully open source, flexible, and built for real-time performance, **Crawl4AI** empowers developers with unmatched speed, precision, and deployment ease.
> **Note** : If you're looking for the old documentation, you can access it [here](https://docs.crawl4ai.com/<https:/old.docs.crawl4ai.com>).
## Quick Start
Here's a quick example to show you how easy it is to use Crawl4AI with its asynchronous capabilities:
```
import asyncio
from crawl4ai import AsyncWebCrawler
async def main():
  # Create an instance of AsyncWebCrawler
  async with AsyncWebCrawler() as crawler:
    # Run the crawler on a URL
    result = await crawler.arun(url="https://crawl4ai.com")
    # Print the extracted content
    print(result.markdown)
# Run the async main function
asyncio.run(main())

```

## What Does Crawl4AI Do?
Crawl4AI is a feature-rich crawler and scraper that aims to:
1. **Generate Clean Markdown** : Perfect for RAG pipelines or direct ingestion into LLMs. 2. **Structured Extraction** : Parse repeated patterns with CSS, XPath, or LLM-based extraction. 3. **Advanced Browser Control** : Hooks, proxies, stealth modes, session re-use—fine-grained control. 4. **High Performance** : Parallel crawling, chunk-based extraction, real-time use cases. 5. **Open Source** : No forced API keys, no paywalls—everyone can access their data. 
**Core Philosophies** : - **Democratize Data** : Free to use, transparent, and highly configurable. - **LLM Friendly** : Minimally processed, well-structured text, images, and metadata, so AI models can easily consume it.
## Documentation Structure
To help you get started, we’ve organized our docs into clear sections:
  * **Setup & Installation** Basic instructions to install Crawl4AI via pip or Docker. 
  * **Quick Start** A hands-on introduction showing how to do your first crawl, generate Markdown, and do a simple extraction. 
  * **Core** Deeper guides on single-page crawling, advanced browser/crawler parameters, content filtering, and caching. 
  * **Advanced** Explore link & media handling, lazy loading, hooking & authentication, proxies, session management, and more. 
  * **Extraction** Detailed references for no-LLM (CSS, XPath) vs. LLM-based strategies, chunking, and clustering approaches. 
  * **API Reference** Find the technical specifics of each class and method, including `AsyncWebCrawler`, `arun()`, and `CrawlResult`.


Throughout these sections, you’ll find code samples you can **copy-paste** into your environment. If something is missing or unclear, raise an issue or PR.
## How You Can Support
  * **Star & Fork**: If you find Crawl4AI helpful, star the repo on GitHub or fork it to add your own features. 
  * **File Issues** : Encounter a bug or missing feature? Let us know by filing an issue, so we can improve. 
  * **Pull Requests** : Whether it’s a small fix, a big feature, or better docs—contributions are always welcome. 
  * **Join Discord** : Come chat about web scraping, crawling tips, or AI workflows with the community. 
  * **Spread the Word** : Mention Crawl4AI in your blog posts, talks, or on social media. 


**Our mission** : to empower everyone—students, researchers, entrepreneurs, data scientists—to access, parse, and shape the world’s data with speed, cost-efficiency, and creative freedom.
## Quick Links
  * **[GitHub Repo](https://docs.crawl4ai.com/<https:/github.com/unclecode/crawl4ai>)**
  * **[Installation Guide](https://docs.crawl4ai.com/<core/installation/>)**
  * **[Quick Start](https://docs.crawl4ai.com/<core/quickstart/>)**
  * **[API Reference](https://docs.crawl4ai.com/<api/async-webcrawler/>)**
  * **[Changelog](https://docs.crawl4ai.com/<https:/github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md>)**


Thank you for joining me on this journey. Let’s keep building an **open, democratic** approach to data extraction and AI together.
Happy Crawling! — _Unclecde, Founder & Maintainer of Crawl4AI_
Site built with [MkDocs](https://docs.crawl4ai.com/<http:/www.mkdocs.org>) and [Terminal for MkDocs](https://docs.crawl4ai.com/<https:/github.com/ntno/mkdocs-terminal>). 
##### Search
xClose
Type to start searching


==================================================

# URL: https://docs.crawl4ai.com/advanced/advanced-features/

[Crawl4AI Documentation](https://docs.crawl4ai.com/advanced/advanced-features/<https:/docs.crawl4ai.com/>)
  * [ Home ](https://docs.crawl4ai.com/advanced/advanced-features/<../..>)
  * [ Quick Start ](https://docs.crawl4ai.com/advanced/advanced-features/core/quickstart/>)
  * [ Search ](https://docs.crawl4ai.com/advanced/advanced-features/<#>)


  * [Home](https://docs.crawl4ai.com/advanced/advanced-features/<../..>)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/advanced/advanced-features/core/installation/>)
    * [Docker Deployment](https://docs.crawl4ai.com/advanced/advanced-features/core/docker-deploymeny/>)
  * [Quick Start](https://docs.crawl4ai.com/advanced/advanced-features/core/quickstart/>)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/advanced/advanced-features/blog/>)
    * [Changelog](https://docs.crawl4ai.com/advanced/advanced-features/<https:/github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md>)
  * Core
    * [Simple Crawling](https://docs.crawl4ai.com/advanced/advanced-features/core/simple-crawling/>)
    * [Crawler Result](https://docs.crawl4ai.com/advanced/advanced-features/core/crawler-result/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/advanced/advanced-features/core/browser-crawler-config/>)
    * [Markdown Generation](https://docs.crawl4ai.com/advanced/advanced-features/core/markdown-generation/>)
    * [Fit Markdown](https://docs.crawl4ai.com/advanced/advanced-features/core/fit-markdown/>)
    * [Page Interaction](https://docs.crawl4ai.com/advanced/advanced-features/core/page-interaction/>)
    * [Content Selection](https://docs.crawl4ai.com/advanced/advanced-features/core/content-selection/>)
    * [Cache Modes](https://docs.crawl4ai.com/advanced/advanced-features/core/cache-modes/>)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/advanced/advanced-features/core/local-files/>)
    * [Link & Media](https://docs.crawl4ai.com/advanced/advanced-features/core/link-media/>)
  * Advanced
    * Overview
    * [File Downloading](https://docs.crawl4ai.com/advanced/advanced-features/<../file-downloading/>)
    * [Lazy Loading](https://docs.crawl4ai.com/advanced/advanced-features/<../lazy-loading/>)
    * [Hooks & Auth](https://docs.crawl4ai.com/advanced/advanced-features/<../hooks-auth/>)
    * [Proxy & Security](https://docs.crawl4ai.com/advanced/advanced-features/<../proxy-security/>)
    * [Session Management](https://docs.crawl4ai.com/advanced/advanced-features/<../session-management/>)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/advanced/advanced-features/<../multi-url-crawling/>)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/advanced/advanced-features/<../crawl-dispatcher/>)
    * [Identity Based Crawling](https://docs.crawl4ai.com/advanced/advanced-features/<../identity-based-crawling/>)
    * [SSL Certificate](https://docs.crawl4ai.com/advanced/advanced-features/<../ssl-certificate/>)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/advanced/advanced-features/extraction/no-llm-strategies/>)
    * [LLM Strategies](https://docs.crawl4ai.com/advanced/advanced-features/extraction/llm-strategies/>)
    * [Clustering Strategies](https://docs.crawl4ai.com/advanced/advanced-features/extraction/clustring-strategies/>)
    * [Chunking](https://docs.crawl4ai.com/advanced/advanced-features/extraction/chunking/>)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/advanced/advanced-features/api/async-webcrawler/>)
    * [arun()](https://docs.crawl4ai.com/advanced/advanced-features/api/arun/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/advanced/advanced-features/api/parameters/>)
    * [CrawlResult](https://docs.crawl4ai.com/advanced/advanced-features/api/crawl-result/>)
    * [Strategies](https://docs.crawl4ai.com/advanced/advanced-features/api/strategies/>)


  * [Overview of Some Important Advanced Features](https://docs.crawl4ai.com/advanced/advanced-features/<#overview-of-some-important-advanced-features>)
  * [1. Proxy Usage](https://docs.crawl4ai.com/advanced/advanced-features/<#1-proxy-usage>)
  * [2. Capturing PDFs & Screenshots](https://docs.crawl4ai.com/advanced/advanced-features/<#2-capturing-pdfs-screenshots>)
  * [3. Handling SSL Certificates](https://docs.crawl4ai.com/advanced/advanced-features/<#3-handling-ssl-certificates>)
  * [4. Custom Headers](https://docs.crawl4ai.com/advanced/advanced-features/<#4-custom-headers>)
  * [5. Session Persistence & Local Storage](https://docs.crawl4ai.com/advanced/advanced-features/<#5-session-persistence-local-storage>)
  * [Putting It All Together](https://docs.crawl4ai.com/advanced/advanced-features/<#putting-it-all-together>)
  * [Conclusion & Next Steps](https://docs.crawl4ai.com/advanced/advanced-features/<#conclusion-next-steps>)


# Overview of Some Important Advanced Features
(Proxy, PDF, Screenshot, SSL, Headers, & Storage State)
Crawl4AI offers multiple power-user features that go beyond simple crawling. This tutorial covers:
1. **Proxy Usage** 2. **Capturing PDFs & Screenshots** 3. **Handling SSL Certificates** 4. **Custom Headers** 5. **Session Persistence & Local Storage**
> **Prerequisites** - You have a basic grasp of [AsyncWebCrawler Basics](https://docs.crawl4ai.com/advanced/advanced-features/core/simple-crawling/>) - You know how to run or configure your Python environment with Playwright installed
## 1. Proxy Usage
If you need to route your crawl traffic through a proxy—whether for IP rotation, geo-testing, or privacy—Crawl4AI supports it via `BrowserConfig.proxy_config`.
```
import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig
async def main():
  browser_cfg = BrowserConfig(
    proxy_config={
      "server": "http://proxy.example.com:8080",
      "username": "myuser",
      "password": "mypass",
    },
    headless=True
  )
  crawler_cfg = CrawlerRunConfig(
    verbose=True
  )
  async with AsyncWebCrawler(config=browser_cfg) as crawler:
    result = await crawler.arun(
      url="https://www.whatismyip.com/",
      config=crawler_cfg
    )
    if result.success:
      print("[OK] Page fetched via proxy.")
      print("Page HTML snippet:", result.html[:200])
    else:
      print("[ERROR]", result.error_message)
if __name__ == "__main__":
  asyncio.run(main())

```

**Key Points** - **`proxy_config`**expects a dict with`server` and optional auth credentials. - Many commercial proxies provide an HTTP/HTTPS “gateway” server that you specify in `server`. - If your proxy doesn’t need auth, omit `username`/`password`.
## 2. Capturing PDFs & Screenshots
Sometimes you need a visual record of a page or a PDF “printout.” Crawl4AI can do both in one pass:
```
import os, asyncio
from base64 import b64decode
from crawl4ai import AsyncWebCrawler, CacheMode
async def main():
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(
      url="https://en.wikipedia.org/wiki/List_of_common_misconceptions",
      cache_mode=CacheMode.BYPASS,
      pdf=True,
      screenshot=True
    )
    if result.success:
      # Save screenshot
      if result.screenshot:
        with open("wikipedia_screenshot.png", "wb") as f:
          f.write(b64decode(result.screenshot))
      # Save PDF
      if result.pdf:
        with open("wikipedia_page.pdf", "wb") as f:
          f.write(result.pdf)
      print("[OK] PDF & screenshot captured.")
    else:
      print("[ERROR]", result.error_message)
if __name__ == "__main__":
  asyncio.run(main())

```

**Why PDF + Screenshot?** - Large or complex pages can be slow or error-prone with “traditional” full-page screenshots. - Exporting a PDF is more reliable for very long pages. Crawl4AI automatically converts the first PDF page into an image if you request both. 
**Relevant Parameters** - **`pdf=True`**: Exports the current page as a PDF (base64-encoded in`result.pdf`). - **`screenshot=True`**: Creates a screenshot (base64-encoded in`result.screenshot`). - **`scan_full_page`**or advanced hooking can further refine how the crawler captures content.
## 3. Handling SSL Certificates
If you need to verify or export a site’s SSL certificate—for compliance, debugging, or data analysis—Crawl4AI can fetch it during the crawl:
```
import asyncio, os
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
async def main():
  tmp_dir = os.path.join(os.getcwd(), "tmp")
  os.makedirs(tmp_dir, exist_ok=True)
  config = CrawlerRunConfig(
    fetch_ssl_certificate=True,
    cache_mode=CacheMode.BYPASS
  )
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(url="https://example.com", config=config)
    if result.success and result.ssl_certificate:
      cert = result.ssl_certificate
      print("\nCertificate Information:")
      print(f"Issuer (CN): {cert.issuer.get('CN', '')}")
      print(f"Valid until: {cert.valid_until}")
      print(f"Fingerprint: {cert.fingerprint}")
      # Export in multiple formats:
      cert.to_json(os.path.join(tmp_dir, "certificate.json"))
      cert.to_pem(os.path.join(tmp_dir, "certificate.pem"))
      cert.to_der(os.path.join(tmp_dir, "certificate.der"))
      print("\nCertificate exported to JSON/PEM/DER in 'tmp' folder.")
    else:
      print("[ERROR] No certificate or crawl failed.")
if __name__ == "__main__":
  asyncio.run(main())

```

**Key Points** - **`fetch_ssl_certificate=True`**triggers certificate retrieval. -`result.ssl_certificate` includes methods (`to_json`, `to_pem`, `to_der`) for saving in various formats (handy for server config, Java keystores, etc.).
## 4. Custom Headers
Sometimes you need to set custom headers (e.g., language preferences, authentication tokens, or specialized user-agent strings). You can do this in multiple ways:
```
import asyncio
from crawl4ai import AsyncWebCrawler
async def main():
  # Option 1: Set headers at the crawler strategy level
  crawler1 = AsyncWebCrawler(
    # The underlying strategy can accept headers in its constructor
    crawler_strategy=None # We'll override below for clarity
  )
  crawler1.crawler_strategy.update_user_agent("MyCustomUA/1.0")
  crawler1.crawler_strategy.set_custom_headers({
    "Accept-Language": "fr-FR,fr;q=0.9"
  })
  result1 = await crawler1.arun("https://www.example.com")
  print("Example 1 result success:", result1.success)
  # Option 2: Pass headers directly to `arun()`
  crawler2 = AsyncWebCrawler()
  result2 = await crawler2.arun(
    url="https://www.example.com",
    headers={"Accept-Language": "es-ES,es;q=0.9"}
  )
  print("Example 2 result success:", result2.success)
if __name__ == "__main__":
  asyncio.run(main())

```

**Notes** - Some sites may react differently to certain headers (e.g., `Accept-Language`). - If you need advanced user-agent randomization or client hints, see [Identity-Based Crawling (Anti-Bot)](https://docs.crawl4ai.com/advanced/advanced-features/<../identity-based-crawling/>) or use `UserAgentGenerator`.
## 5. Session Persistence & Local Storage
Crawl4AI can preserve cookies and localStorage so you can continue where you left off—ideal for logging into sites or skipping repeated auth flows.
### 5.1 `storage_state`
```
import asyncio
from crawl4ai import AsyncWebCrawler
async def main():
  storage_dict = {
    "cookies": [
      {
        "name": "session",
        "value": "abcd1234",
        "domain": "example.com",
        "path": "/",
        "expires": 1699999999.0,
        "httpOnly": False,
        "secure": False,
        "sameSite": "None"
      }
    ],
    "origins": [
      {
        "origin": "https://example.com",
        "localStorage": [
          {"name": "token", "value": "my_auth_token"}
        ]
      }
    ]
  }
  # Provide the storage state as a dictionary to start "already logged in"
  async with AsyncWebCrawler(
    headless=True,
    storage_state=storage_dict
  ) as crawler:
    result = await crawler.arun("https://example.com/protected")
    if result.success:
      print("Protected page content length:", len(result.html))
    else:
      print("Failed to crawl protected page")
if __name__ == "__main__":
  asyncio.run(main())

```

### 5.2 Exporting & Reusing State
You can sign in once, export the browser context, and reuse it later—without re-entering credentials.
  * **`await context.storage_state(path="my_storage.json")`**: Exports cookies, localStorage, etc. to a file.
  * Provide `storage_state="my_storage.json"` on subsequent runs to skip the login step.


**See** : [Detailed session management tutorial](https://docs.crawl4ai.com/advanced/advanced-features/<../session-management/>) or [Explanations → Browser Context & Managed Browser](https://docs.crawl4ai.com/advanced/advanced-features/<../identity-based-crawling/>) for more advanced scenarios (like multi-step logins, or capturing after interactive pages).
## Putting It All Together
Here’s a snippet that combines multiple “advanced” features (proxy, PDF, screenshot, SSL, custom headers, and session reuse) into one run. Normally, you’d tailor each setting to your project’s needs.
```
import os, asyncio
from base64 import b64decode
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
async def main():
  # 1. Browser config with proxy + headless
  browser_cfg = BrowserConfig(
    proxy_config={
      "server": "http://proxy.example.com:8080",
      "username": "myuser",
      "password": "mypass",
    },
    headless=True,
  )
  # 2. Crawler config with PDF, screenshot, SSL, custom headers, and ignoring caches
  crawler_cfg = CrawlerRunConfig(
    pdf=True,
    screenshot=True,
    fetch_ssl_certificate=True,
    cache_mode=CacheMode.BYPASS,
    headers={"Accept-Language": "en-US,en;q=0.8"},
    storage_state="my_storage.json", # Reuse session from a previous sign-in
    verbose=True,
  )
  # 3. Crawl
  async with AsyncWebCrawler(config=browser_cfg) as crawler:
    result = await crawler.arun(
      url = "https://secure.example.com/protected", 
      config=crawler_cfg
    )
    if result.success:
      print("[OK] Crawled the secure page. Links found:", len(result.links.get("internal", [])))
      # Save PDF & screenshot
      if result.pdf:
        with open("result.pdf", "wb") as f:
          f.write(b64decode(result.pdf))
      if result.screenshot:
        with open("result.png", "wb") as f:
          f.write(b64decode(result.screenshot))
      # Check SSL cert
      if result.ssl_certificate:
        print("SSL Issuer CN:", result.ssl_certificate.issuer.get("CN", ""))
    else:
      print("[ERROR]", result.error_message)
if __name__ == "__main__":
  asyncio.run(main())

```

## Conclusion & Next Steps
You’ve now explored several **advanced** features:
  * **Proxy Usage**
  * **PDF & Screenshot** capturing for large or critical pages 
  * **SSL Certificate** retrieval & exporting 
  * **Custom Headers** for language or specialized requests 
  * **Session Persistence** via storage state


With these power tools, you can build robust scraping workflows that mimic real user behavior, handle secure sites, capture detailed snapshots, and manage sessions across multiple runs—streamlining your entire data collection pipeline.
**Last Updated** : 2025-01-01
Site built with [MkDocs](https://docs.crawl4ai.com/advanced/advanced-features/<http:/www.mkdocs.org>) and [Terminal for MkDocs](https://docs.crawl4ai.com/advanced/advanced-features/<https:/github.com/ntno/mkdocs-terminal>). 
##### Search
xClose
Type to start searching


==================================================

# URL: https://docs.crawl4ai.com/advanced/crawl-dispatcher/

[Crawl4AI Documentation](https://docs.crawl4ai.com/advanced/crawl-dispatcher/<https:/docs.crawl4ai.com/>)
  * [ Home ](https://docs.crawl4ai.com/advanced/crawl-dispatcher/<../..>)
  * [ Quick Start ](https://docs.crawl4ai.com/advanced/crawl-dispatcher/core/quickstart/>)
  * [ Search ](https://docs.crawl4ai.com/advanced/crawl-dispatcher/<#>)


  * [Home](https://docs.crawl4ai.com/advanced/crawl-dispatcher/<../..>)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/advanced/crawl-dispatcher/core/installation/>)
    * [Docker Deployment](https://docs.crawl4ai.com/advanced/crawl-dispatcher/core/docker-deploymeny/>)
  * [Quick Start](https://docs.crawl4ai.com/advanced/crawl-dispatcher/core/quickstart/>)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/advanced/crawl-dispatcher/blog/>)
    * [Changelog](https://docs.crawl4ai.com/advanced/crawl-dispatcher/<https:/github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md>)
  * Core
    * [Simple Crawling](https://docs.crawl4ai.com/advanced/crawl-dispatcher/core/simple-crawling/>)
    * [Crawler Result](https://docs.crawl4ai.com/advanced/crawl-dispatcher/core/crawler-result/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/advanced/crawl-dispatcher/core/browser-crawler-config/>)
    * [Markdown Generation](https://docs.crawl4ai.com/advanced/crawl-dispatcher/core/markdown-generation/>)
    * [Fit Markdown](https://docs.crawl4ai.com/advanced/crawl-dispatcher/core/fit-markdown/>)
    * [Page Interaction](https://docs.crawl4ai.com/advanced/crawl-dispatcher/core/page-interaction/>)
    * [Content Selection](https://docs.crawl4ai.com/advanced/crawl-dispatcher/core/content-selection/>)
    * [Cache Modes](https://docs.crawl4ai.com/advanced/crawl-dispatcher/core/cache-modes/>)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/advanced/crawl-dispatcher/core/local-files/>)
    * [Link & Media](https://docs.crawl4ai.com/advanced/crawl-dispatcher/core/link-media/>)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/advanced/crawl-dispatcher/<../advanced-features/>)
    * [File Downloading](https://docs.crawl4ai.com/advanced/crawl-dispatcher/<../file-downloading/>)
    * [Lazy Loading](https://docs.crawl4ai.com/advanced/crawl-dispatcher/<../lazy-loading/>)
    * [Hooks & Auth](https://docs.crawl4ai.com/advanced/crawl-dispatcher/<../hooks-auth/>)
    * [Proxy & Security](https://docs.crawl4ai.com/advanced/crawl-dispatcher/<../proxy-security/>)
    * [Session Management](https://docs.crawl4ai.com/advanced/crawl-dispatcher/<../session-management/>)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/advanced/crawl-dispatcher/<../multi-url-crawling/>)
    * Crawl Dispatcher
    * [Identity Based Crawling](https://docs.crawl4ai.com/advanced/crawl-dispatcher/<../identity-based-crawling/>)
    * [SSL Certificate](https://docs.crawl4ai.com/advanced/crawl-dispatcher/<../ssl-certificate/>)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/advanced/crawl-dispatcher/extraction/no-llm-strategies/>)
    * [LLM Strategies](https://docs.crawl4ai.com/advanced/crawl-dispatcher/extraction/llm-strategies/>)
    * [Clustering Strategies](https://docs.crawl4ai.com/advanced/crawl-dispatcher/extraction/clustring-strategies/>)
    * [Chunking](https://docs.crawl4ai.com/advanced/crawl-dispatcher/extraction/chunking/>)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/advanced/crawl-dispatcher/api/async-webcrawler/>)
    * [arun()](https://docs.crawl4ai.com/advanced/crawl-dispatcher/api/arun/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/advanced/crawl-dispatcher/api/parameters/>)
    * [CrawlResult](https://docs.crawl4ai.com/advanced/crawl-dispatcher/api/crawl-result/>)
    * [Strategies](https://docs.crawl4ai.com/advanced/crawl-dispatcher/api/strategies/>)


  * [Crawl Dispatcher](https://docs.crawl4ai.com/advanced/crawl-dispatcher/<#crawl-dispatcher>)


# Crawl Dispatcher
We’re excited to announce a **Crawl Dispatcher** module that can handle **thousands** of crawling tasks simultaneously. By efficiently managing system resources (memory, CPU, network), this dispatcher ensures high-performance data extraction at scale. It also provides **real-time monitoring** of each crawler’s status, memory usage, and overall progress.
Stay tuned—this feature is **coming soon** in an upcoming release of Crawl4AI! For the latest news, keep an eye on our changelogs and follow [@unclecode](https://docs.crawl4ai.com/advanced/crawl-dispatcher/<https:/twitter.com/unclecode>) on X.
Below is a **sample** of how the dispatcher’s performance monitor might look in action:
![Crawl Dispatcher Performance Monitor](https://docs.crawl4ai.com/assets/images/dispatcher.png)
We can’t wait to bring you this streamlined, **scalable** approach to multi-URL crawling—**watch this space** for updates!
Site built with [MkDocs](https://docs.crawl4ai.com/advanced/crawl-dispatcher/<http:/www.mkdocs.org>) and [Terminal for MkDocs](https://docs.crawl4ai.com/advanced/crawl-dispatcher/<https:/github.com/ntno/mkdocs-terminal>). 
##### Search
xClose
Type to start searching


==================================================

# URL: https://docs.crawl4ai.com/advanced/file-downloading/

[Crawl4AI Documentation](https://docs.crawl4ai.com/advanced/file-downloading/<https:/docs.crawl4ai.com/>)
  * [ Home ](https://docs.crawl4ai.com/advanced/file-downloading/<../..>)
  * [ Quick Start ](https://docs.crawl4ai.com/advanced/file-downloading/core/quickstart/>)
  * [ Search ](https://docs.crawl4ai.com/advanced/file-downloading/<#>)


  * [Home](https://docs.crawl4ai.com/advanced/file-downloading/<../..>)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/advanced/file-downloading/core/installation/>)
    * [Docker Deployment](https://docs.crawl4ai.com/advanced/file-downloading/core/docker-deploymeny/>)
  * [Quick Start](https://docs.crawl4ai.com/advanced/file-downloading/core/quickstart/>)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/advanced/file-downloading/blog/>)
    * [Changelog](https://docs.crawl4ai.com/advanced/file-downloading/<https:/github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md>)
  * Core
    * [Simple Crawling](https://docs.crawl4ai.com/advanced/file-downloading/core/simple-crawling/>)
    * [Crawler Result](https://docs.crawl4ai.com/advanced/file-downloading/core/crawler-result/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/advanced/file-downloading/core/browser-crawler-config/>)
    * [Markdown Generation](https://docs.crawl4ai.com/advanced/file-downloading/core/markdown-generation/>)
    * [Fit Markdown](https://docs.crawl4ai.com/advanced/file-downloading/core/fit-markdown/>)
    * [Page Interaction](https://docs.crawl4ai.com/advanced/file-downloading/core/page-interaction/>)
    * [Content Selection](https://docs.crawl4ai.com/advanced/file-downloading/core/content-selection/>)
    * [Cache Modes](https://docs.crawl4ai.com/advanced/file-downloading/core/cache-modes/>)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/advanced/file-downloading/core/local-files/>)
    * [Link & Media](https://docs.crawl4ai.com/advanced/file-downloading/core/link-media/>)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/advanced/file-downloading/<../advanced-features/>)
    * File Downloading
    * [Lazy Loading](https://docs.crawl4ai.com/advanced/file-downloading/<../lazy-loading/>)
    * [Hooks & Auth](https://docs.crawl4ai.com/advanced/file-downloading/<../hooks-auth/>)
    * [Proxy & Security](https://docs.crawl4ai.com/advanced/file-downloading/<../proxy-security/>)
    * [Session Management](https://docs.crawl4ai.com/advanced/file-downloading/<../session-management/>)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/advanced/file-downloading/<../multi-url-crawling/>)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/advanced/file-downloading/<../crawl-dispatcher/>)
    * [Identity Based Crawling](https://docs.crawl4ai.com/advanced/file-downloading/<../identity-based-crawling/>)
    * [SSL Certificate](https://docs.crawl4ai.com/advanced/file-downloading/<../ssl-certificate/>)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/advanced/file-downloading/extraction/no-llm-strategies/>)
    * [LLM Strategies](https://docs.crawl4ai.com/advanced/file-downloading/extraction/llm-strategies/>)
    * [Clustering Strategies](https://docs.crawl4ai.com/advanced/file-downloading/extraction/clustring-strategies/>)
    * [Chunking](https://docs.crawl4ai.com/advanced/file-downloading/extraction/chunking/>)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/advanced/file-downloading/api/async-webcrawler/>)
    * [arun()](https://docs.crawl4ai.com/advanced/file-downloading/api/arun/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/advanced/file-downloading/api/parameters/>)
    * [CrawlResult](https://docs.crawl4ai.com/advanced/file-downloading/api/crawl-result/>)
    * [Strategies](https://docs.crawl4ai.com/advanced/file-downloading/api/strategies/>)


  * [Download Handling in Crawl4AI](https://docs.crawl4ai.com/advanced/file-downloading/<#download-handling-in-crawl4ai>)
  * [Enabling Downloads](https://docs.crawl4ai.com/advanced/file-downloading/<#enabling-downloads>)
  * [Specifying Download Location](https://docs.crawl4ai.com/advanced/file-downloading/<#specifying-download-location>)
  * [Triggering Downloads](https://docs.crawl4ai.com/advanced/file-downloading/<#triggering-downloads>)
  * [Accessing Downloaded Files](https://docs.crawl4ai.com/advanced/file-downloading/<#accessing-downloaded-files>)
  * [Example: Downloading Multiple Files](https://docs.crawl4ai.com/advanced/file-downloading/<#example-downloading-multiple-files>)
  * [Important Considerations](https://docs.crawl4ai.com/advanced/file-downloading/<#important-considerations>)


# Download Handling in Crawl4AI
This guide explains how to use Crawl4AI to handle file downloads during crawling. You'll learn how to trigger downloads, specify download locations, and access downloaded files.
## Enabling Downloads
To enable downloads, set the `accept_downloads` parameter in the `BrowserConfig` object and pass it to the crawler.
```
from crawl4ai.async_configs import BrowserConfig, AsyncWebCrawler
async def main():
  config = BrowserConfig(accept_downloads=True) # Enable downloads globally
  async with AsyncWebCrawler(config=config) as crawler:
    # ... your crawling logic ...
asyncio.run(main())

```

## Specifying Download Location
Specify the download directory using the `downloads_path` attribute in the `BrowserConfig` object. If not provided, Crawl4AI defaults to creating a "downloads" directory inside the `.crawl4ai` folder in your home directory.
```
from crawl4ai.async_configs import BrowserConfig
import os
downloads_path = os.path.join(os.getcwd(), "my_downloads") # Custom download path
os.makedirs(downloads_path, exist_ok=True)
config = BrowserConfig(accept_downloads=True, downloads_path=downloads_path)
async def main():
  async with AsyncWebCrawler(config=config) as crawler:
    result = await crawler.arun(url="https://example.com")
    # ...

```

## Triggering Downloads
Downloads are typically triggered by user interactions on a web page, such as clicking a download button. Use `js_code` in `CrawlerRunConfig` to simulate these actions and `wait_for` to allow sufficient time for downloads to start.
```
from crawl4ai.async_configs import CrawlerRunConfig
config = CrawlerRunConfig(
  js_code="""
    const downloadLink = document.querySelector('a[href$=".exe"]');
    if (downloadLink) {
      downloadLink.click();
    }
  """,
  wait_for=5 # Wait 5 seconds for the download to start
)
result = await crawler.arun(url="https://www.python.org/downloads/", config=config)

```

## Accessing Downloaded Files
The `downloaded_files` attribute of the `CrawlResult` object contains paths to downloaded files.
```
if result.downloaded_files:
  print("Downloaded files:")
  for file_path in result.downloaded_files:
    print(f"- {file_path}")
    file_size = os.path.getsize(file_path)
    print(f"- File size: {file_size} bytes")
else:
  print("No files downloaded.")

```

## Example: Downloading Multiple Files
```
from crawl4ai.async_configs import BrowserConfig, CrawlerRunConfig
import os
from pathlib import Path
async def download_multiple_files(url: str, download_path: str):
  config = BrowserConfig(accept_downloads=True, downloads_path=download_path)
  async with AsyncWebCrawler(config=config) as crawler:
    run_config = CrawlerRunConfig(
      js_code="""
        const downloadLinks = document.querySelectorAll('a[download]');
        for (const link of downloadLinks) {
          link.click();
          // Delay between clicks
          await new Promise(r => setTimeout(r, 2000)); 
        }
      """,
      wait_for=10 # Wait for all downloads to start
    )
    result = await crawler.arun(url=url, config=run_config)
    if result.downloaded_files:
      print("Downloaded files:")
      for file in result.downloaded_files:
        print(f"- {file}")
    else:
      print("No files downloaded.")
# Usage
download_path = os.path.join(Path.home(), ".crawl4ai", "downloads")
os.makedirs(download_path, exist_ok=True)
asyncio.run(download_multiple_files("https://www.python.org/downloads/windows/", download_path))

```

## Important Considerations
  * **Browser Context:** Downloads are managed within the browser context. Ensure `js_code` correctly targets the download triggers on the webpage.
  * **Timing:** Use `wait_for` in `CrawlerRunConfig` to manage download timing.
  * **Error Handling:** Handle errors to manage failed downloads or incorrect paths gracefully.
  * **Security:** Scan downloaded files for potential security threats before use.


This revised guide ensures consistency with the `Crawl4AI` codebase by using `BrowserConfig` and `CrawlerRunConfig` for all download-related configurations. Let me know if further adjustments are needed!
Site built with [MkDocs](https://docs.crawl4ai.com/advanced/file-downloading/<http:/www.mkdocs.org>) and [Terminal for MkDocs](https://docs.crawl4ai.com/advanced/file-downloading/<https:/github.com/ntno/mkdocs-terminal>). 
##### Search
xClose
Type to start searching


==================================================

# URL: https://docs.crawl4ai.com/advanced/hooks-auth/

[Crawl4AI Documentation](https://docs.crawl4ai.com/advanced/hooks-auth/<https:/docs.crawl4ai.com/>)
  * [ Home ](https://docs.crawl4ai.com/advanced/hooks-auth/<../..>)
  * [ Quick Start ](https://docs.crawl4ai.com/advanced/hooks-auth/core/quickstart/>)
  * [ Search ](https://docs.crawl4ai.com/advanced/hooks-auth/<#>)


  * [Home](https://docs.crawl4ai.com/advanced/hooks-auth/<../..>)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/advanced/hooks-auth/core/installation/>)
    * [Docker Deployment](https://docs.crawl4ai.com/advanced/hooks-auth/core/docker-deploymeny/>)
  * [Quick Start](https://docs.crawl4ai.com/advanced/hooks-auth/core/quickstart/>)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/advanced/hooks-auth/blog/>)
    * [Changelog](https://docs.crawl4ai.com/advanced/hooks-auth/<https:/github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md>)
  * Core
    * [Simple Crawling](https://docs.crawl4ai.com/advanced/hooks-auth/core/simple-crawling/>)
    * [Crawler Result](https://docs.crawl4ai.com/advanced/hooks-auth/core/crawler-result/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/advanced/hooks-auth/core/browser-crawler-config/>)
    * [Markdown Generation](https://docs.crawl4ai.com/advanced/hooks-auth/core/markdown-generation/>)
    * [Fit Markdown](https://docs.crawl4ai.com/advanced/hooks-auth/core/fit-markdown/>)
    * [Page Interaction](https://docs.crawl4ai.com/advanced/hooks-auth/core/page-interaction/>)
    * [Content Selection](https://docs.crawl4ai.com/advanced/hooks-auth/core/content-selection/>)
    * [Cache Modes](https://docs.crawl4ai.com/advanced/hooks-auth/core/cache-modes/>)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/advanced/hooks-auth/core/local-files/>)
    * [Link & Media](https://docs.crawl4ai.com/advanced/hooks-auth/core/link-media/>)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/advanced/hooks-auth/<../advanced-features/>)
    * [File Downloading](https://docs.crawl4ai.com/advanced/hooks-auth/<../file-downloading/>)
    * [Lazy Loading](https://docs.crawl4ai.com/advanced/hooks-auth/<../lazy-loading/>)
    * Hooks & Auth
    * [Proxy & Security](https://docs.crawl4ai.com/advanced/hooks-auth/<../proxy-security/>)
    * [Session Management](https://docs.crawl4ai.com/advanced/hooks-auth/<../session-management/>)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/advanced/hooks-auth/<../multi-url-crawling/>)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/advanced/hooks-auth/<../crawl-dispatcher/>)
    * [Identity Based Crawling](https://docs.crawl4ai.com/advanced/hooks-auth/<../identity-based-crawling/>)
    * [SSL Certificate](https://docs.crawl4ai.com/advanced/hooks-auth/<../ssl-certificate/>)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/advanced/hooks-auth/extraction/no-llm-strategies/>)
    * [LLM Strategies](https://docs.crawl4ai.com/advanced/hooks-auth/extraction/llm-strategies/>)
    * [Clustering Strategies](https://docs.crawl4ai.com/advanced/hooks-auth/extraction/clustring-strategies/>)
    * [Chunking](https://docs.crawl4ai.com/advanced/hooks-auth/extraction/chunking/>)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/advanced/hooks-auth/api/async-webcrawler/>)
    * [arun()](https://docs.crawl4ai.com/advanced/hooks-auth/api/arun/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/advanced/hooks-auth/api/parameters/>)
    * [CrawlResult](https://docs.crawl4ai.com/advanced/hooks-auth/api/crawl-result/>)
    * [Strategies](https://docs.crawl4ai.com/advanced/hooks-auth/api/strategies/>)


  * [Hooks & Auth in AsyncWebCrawler](https://docs.crawl4ai.com/advanced/hooks-auth/<#hooks-auth-in-asyncwebcrawler>)
  * [Example: Using Hooks in AsyncWebCrawler](https://docs.crawl4ai.com/advanced/hooks-auth/<#example-using-hooks-in-asyncwebcrawler>)
  * [Hook Lifecycle Summary](https://docs.crawl4ai.com/advanced/hooks-auth/<#hook-lifecycle-summary>)
  * [When to Handle Authentication](https://docs.crawl4ai.com/advanced/hooks-auth/<#when-to-handle-authentication>)
  * [Additional Considerations](https://docs.crawl4ai.com/advanced/hooks-auth/<#additional-considerations>)
  * [Conclusion](https://docs.crawl4ai.com/advanced/hooks-auth/<#conclusion>)


# Hooks & Auth in AsyncWebCrawler
Crawl4AI’s **hooks** let you customize the crawler at specific points in the pipeline:
1. **`on_browser_created`**– After browser creation. 2.**`on_page_context_created`**– After a new context & page are created. 3. **`before_goto`**– Just before navigating to a page. 4.**`after_goto`**– Right after navigation completes. 5.**`on_user_agent_updated`**– Whenever the user agent changes. 6.**`on_execution_started`**– Once custom JavaScript execution begins. 7.**`before_retrieve_html`**– Just before the crawler retrieves final HTML. 8.**`before_return_html`**– Right before returning the HTML content.
**Important** : Avoid heavy tasks in `on_browser_created` since you don’t yet have a page context. If you need to _log in_ , do so in **`on_page_context_created`**.
> note "Important Hook Usage Warning" **Avoid Misusing Hooks** : Do not manipulate page objects in the wrong hook or at the wrong time, as it can crash the pipeline or produce incorrect results. A common mistake is attempting to handle authentication prematurely—such as creating or closing pages in `on_browser_created`. 
> **Use the Right Hook for Auth** : If you need to log in or set tokens, use `on_page_context_created`. This ensures you have a valid page/context to work with, without disrupting the main crawling flow.
> **Identity-Based Crawling** : For robust auth, consider identity-based crawling (or passing a session ID) to preserve state. Run your initial login steps in a separate, well-defined process, then feed that session to your main crawl—rather than shoehorning complex authentication into early hooks. Check out [Identity-Based Crawling](https://docs.crawl4ai.com/advanced/hooks-auth/<../identity-based-crawling/>) for more details.
> **Be Cautious** : Overwriting or removing elements in the wrong hook can compromise the final crawl. Keep hooks focused on smaller tasks (like route filters, custom headers), and let your main logic (crawling, data extraction) proceed normally.
Below is an example demonstration.
## Example: Using Hooks in AsyncWebCrawler
```
import asyncio
import json
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from playwright.async_api import Page, BrowserContext
async def main():
  print("🔗 Hooks Example: Demonstrating recommended usage")
  # 1) Configure the browser
  browser_config = BrowserConfig(
    headless=True,
    verbose=True
  )
  # 2) Configure the crawler run
  crawler_run_config = CrawlerRunConfig(
    js_code="window.scrollTo(0, document.body.scrollHeight);",
    wait_for="body",
    cache_mode=CacheMode.BYPASS
  )
  # 3) Create the crawler instance
  crawler = AsyncWebCrawler(config=browser_config)
  #
  # Define Hook Functions
  #
  async def on_browser_created(browser, **kwargs):
    # Called once the browser instance is created (but no pages or contexts yet)
    print("[HOOK] on_browser_created - Browser created successfully!")
    # Typically, do minimal setup here if needed
    return browser
  async def on_page_context_created(page: Page, context: BrowserContext, **kwargs):
    # Called right after a new page + context are created (ideal for auth or route config).
    print("[HOOK] on_page_context_created - Setting up page & context.")
    # Example 1: Route filtering (e.g., block images)
    async def route_filter(route):
      if route.request.resource_type == "image":
        print(f"[HOOK] Blocking image request: {route.request.url}")
        await route.abort()
      else:
        await route.continue_()
    await context.route("**", route_filter)
    # Example 2: (Optional) Simulate a login scenario
    # (We do NOT create or close pages here, just do quick steps if needed)
    # e.g., await page.goto("https://example.com/login")
    # e.g., await page.fill("input[name='username']", "testuser")
    # e.g., await page.fill("input[name='password']", "password123")
    # e.g., await page.click("button[type='submit']")
    # e.g., await page.wait_for_selector("#welcome")
    # e.g., await context.add_cookies([...])
    # Then continue
    # Example 3: Adjust the viewport
    await page.set_viewport_size({"width": 1080, "height": 600})
    return page
  async def before_goto(
    page: Page, context: BrowserContext, url: str, **kwargs
  ):
    # Called before navigating to each URL.
    print(f"[HOOK] before_goto - About to navigate: {url}")
    # e.g., inject custom headers
    await page.set_extra_http_headers({
      "Custom-Header": "my-value"
    })
    return page
  async def after_goto(
    page: Page, context: BrowserContext, 
    url: str, response, **kwargs
  ):
    # Called after navigation completes.
    print(f"[HOOK] after_goto - Successfully loaded: {url}")
    # e.g., wait for a certain element if we want to verify
    try:
      await page.wait_for_selector('.content', timeout=1000)
      print("[HOOK] Found .content element!")
    except:
      print("[HOOK] .content not found, continuing anyway.")
    return page
  async def on_user_agent_updated(
    page: Page, context: BrowserContext, 
    user_agent: str, **kwargs
  ):
    # Called whenever the user agent updates.
    print(f"[HOOK] on_user_agent_updated - New user agent: {user_agent}")
    return page
  async def on_execution_started(page: Page, context: BrowserContext, **kwargs):
    # Called after custom JavaScript execution begins.
    print("[HOOK] on_execution_started - JS code is running!")
    return page
  async def before_retrieve_html(page: Page, context: BrowserContext, **kwargs):
    # Called before final HTML retrieval.
    print("[HOOK] before_retrieve_html - We can do final actions")
    # Example: Scroll again
    await page.evaluate("window.scrollTo(0, document.body.scrollHeight);")
    return page
  async def before_return_html(
    page: Page, context: BrowserContext, html: str, **kwargs
  ):
    # Called just before returning the HTML in the result.
    print(f"[HOOK] before_return_html - HTML length: {len(html)}")
    return page
  #
  # Attach Hooks
  #
  crawler.crawler_strategy.set_hook("on_browser_created", on_browser_created)
  crawler.crawler_strategy.set_hook(
    "on_page_context_created", on_page_context_created
  )
  crawler.crawler_strategy.set_hook("before_goto", before_goto)
  crawler.crawler_strategy.set_hook("after_goto", after_goto)
  crawler.crawler_strategy.set_hook(
    "on_user_agent_updated", on_user_agent_updated
  )
  crawler.crawler_strategy.set_hook(
    "on_execution_started", on_execution_started
  )
  crawler.crawler_strategy.set_hook(
    "before_retrieve_html", before_retrieve_html
  )
  crawler.crawler_strategy.set_hook(
    "before_return_html", before_return_html
  )
  await crawler.start()
  # 4) Run the crawler on an example page
  url = "https://example.com"
  result = await crawler.arun(url, config=crawler_run_config)
  if result.success:
    print("\nCrawled URL:", result.url)
    print("HTML length:", len(result.html))
  else:
    print("Error:", result.error_message)
  await crawler.close()
if __name__ == "__main__":
  asyncio.run(main())

```

## Hook Lifecycle Summary
1. **`on_browser_created`**: - Browser is up, but**no** pages or contexts yet. - Light setup only—don’t try to open or close pages here (that belongs in `on_page_context_created`).
2. **`on_page_context_created`**: - Perfect for advanced**auth** or route blocking. - You have a **page** + **context** ready but haven’t navigated to the target URL yet.
3. **`before_goto`**: - Right before navigation. Typically used for setting**custom headers** or logging the target URL.
4. **`after_goto`**: - After page navigation is done. Good place for verifying content or waiting on essential elements.
5. **`on_user_agent_updated`**: - Whenever the user agent changes (for stealth or different UA modes).
6. **`on_execution_started`**: - If you set`js_code` or run custom scripts, this runs once your JS is about to start.
7. **`before_retrieve_html`**: - Just before the final HTML snapshot is taken. Often you do a final scroll or lazy-load triggers here.
8. **`before_return_html`**: - The last hook before returning HTML to the`CrawlResult`. Good for logging HTML length or minor modifications.
## When to Handle Authentication
**Recommended** : Use **`on_page_context_created`**if you need to:
  * Navigate to a login page or fill forms
  * Set cookies or localStorage tokens
  * Block resource routes to avoid ads


This ensures the newly created context is under your control **before** `arun()` navigates to the main URL.
## Additional Considerations
  * **Session Management** : If you want multiple `arun()` calls to reuse a single session, pass `session_id=` in your `CrawlerRunConfig`. Hooks remain the same. 
  * **Performance** : Hooks can slow down crawling if they do heavy tasks. Keep them concise. 
  * **Error Handling** : If a hook fails, the overall crawl might fail. Catch exceptions or handle them gracefully. 
  * **Concurrency** : If you run `arun_many()`, each URL triggers these hooks in parallel. Ensure your hooks are thread/async-safe.


## Conclusion
Hooks provide **fine-grained** control over:
  * **Browser** creation (light tasks only)
  * **Page** and **context** creation (auth, route blocking)
  * **Navigation** phases
  * **Final HTML** retrieval


Follow the recommended usage: - **Login** or advanced tasks in `on_page_context_created` - **Custom headers** or logs in `before_goto` / `after_goto` - **Scrolling** or final checks in `before_retrieve_html` / `before_return_html`
Site built with [MkDocs](https://docs.crawl4ai.com/advanced/hooks-auth/<http:/www.mkdocs.org>) and [Terminal for MkDocs](https://docs.crawl4ai.com/advanced/hooks-auth/<https:/github.com/ntno/mkdocs-terminal>). 
##### Search
xClose
Type to start searching


==================================================

# URL: https://docs.crawl4ai.com/advanced/identity-based-crawling/

[Crawl4AI Documentation](https://docs.crawl4ai.com/advanced/identity-based-crawling/<https:/docs.crawl4ai.com/>)
  * [ Home ](https://docs.crawl4ai.com/advanced/identity-based-crawling/<../..>)
  * [ Quick Start ](https://docs.crawl4ai.com/advanced/identity-based-crawling/core/quickstart/>)
  * [ Search ](https://docs.crawl4ai.com/advanced/identity-based-crawling/<#>)


  * [Home](https://docs.crawl4ai.com/advanced/identity-based-crawling/<../..>)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/advanced/identity-based-crawling/core/installation/>)
    * [Docker Deployment](https://docs.crawl4ai.com/advanced/identity-based-crawling/core/docker-deploymeny/>)
  * [Quick Start](https://docs.crawl4ai.com/advanced/identity-based-crawling/core/quickstart/>)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/advanced/identity-based-crawling/blog/>)
    * [Changelog](https://docs.crawl4ai.com/advanced/identity-based-crawling/<https:/github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md>)
  * Core
    * [Simple Crawling](https://docs.crawl4ai.com/advanced/identity-based-crawling/core/simple-crawling/>)
    * [Crawler Result](https://docs.crawl4ai.com/advanced/identity-based-crawling/core/crawler-result/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/advanced/identity-based-crawling/core/browser-crawler-config/>)
    * [Markdown Generation](https://docs.crawl4ai.com/advanced/identity-based-crawling/core/markdown-generation/>)
    * [Fit Markdown](https://docs.crawl4ai.com/advanced/identity-based-crawling/core/fit-markdown/>)
    * [Page Interaction](https://docs.crawl4ai.com/advanced/identity-based-crawling/core/page-interaction/>)
    * [Content Selection](https://docs.crawl4ai.com/advanced/identity-based-crawling/core/content-selection/>)
    * [Cache Modes](https://docs.crawl4ai.com/advanced/identity-based-crawling/core/cache-modes/>)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/advanced/identity-based-crawling/core/local-files/>)
    * [Link & Media](https://docs.crawl4ai.com/advanced/identity-based-crawling/core/link-media/>)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/advanced/identity-based-crawling/<../advanced-features/>)
    * [File Downloading](https://docs.crawl4ai.com/advanced/identity-based-crawling/<../file-downloading/>)
    * [Lazy Loading](https://docs.crawl4ai.com/advanced/identity-based-crawling/<../lazy-loading/>)
    * [Hooks & Auth](https://docs.crawl4ai.com/advanced/identity-based-crawling/<../hooks-auth/>)
    * [Proxy & Security](https://docs.crawl4ai.com/advanced/identity-based-crawling/<../proxy-security/>)
    * [Session Management](https://docs.crawl4ai.com/advanced/identity-based-crawling/<../session-management/>)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/advanced/identity-based-crawling/<../multi-url-crawling/>)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/advanced/identity-based-crawling/<../crawl-dispatcher/>)
    * Identity Based Crawling
    * [SSL Certificate](https://docs.crawl4ai.com/advanced/identity-based-crawling/<../ssl-certificate/>)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/advanced/identity-based-crawling/extraction/no-llm-strategies/>)
    * [LLM Strategies](https://docs.crawl4ai.com/advanced/identity-based-crawling/extraction/llm-strategies/>)
    * [Clustering Strategies](https://docs.crawl4ai.com/advanced/identity-based-crawling/extraction/clustring-strategies/>)
    * [Chunking](https://docs.crawl4ai.com/advanced/identity-based-crawling/extraction/chunking/>)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/advanced/identity-based-crawling/api/async-webcrawler/>)
    * [arun()](https://docs.crawl4ai.com/advanced/identity-based-crawling/api/arun/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/advanced/identity-based-crawling/api/parameters/>)
    * [CrawlResult](https://docs.crawl4ai.com/advanced/identity-based-crawling/api/crawl-result/>)
    * [Strategies](https://docs.crawl4ai.com/advanced/identity-based-crawling/api/strategies/>)


  * [Preserve Your Identity with Crawl4AI](https://docs.crawl4ai.com/advanced/identity-based-crawling/<#preserve-your-identity-with-crawl4ai>)
  * [1. Managed Browsers: Your Digital Identity Solution](https://docs.crawl4ai.com/advanced/identity-based-crawling/<#1-managed-browsers-your-digital-identity-solution>)
  * [3. Using Managed Browsers in Crawl4AI](https://docs.crawl4ai.com/advanced/identity-based-crawling/<#3-using-managed-browsers-in-crawl4ai>)
  * [4. Magic Mode: Simplified Automation](https://docs.crawl4ai.com/advanced/identity-based-crawling/<#4-magic-mode-simplified-automation>)
  * [5. Comparing Managed Browsers vs. Magic Mode](https://docs.crawl4ai.com/advanced/identity-based-crawling/<#5-comparing-managed-browsers-vs-magic-mode>)
  * [6. Summary](https://docs.crawl4ai.com/advanced/identity-based-crawling/<#6-summary>)


# Preserve Your Identity with Crawl4AI
Crawl4AI empowers you to navigate and interact with the web using your **authentic digital identity** , ensuring you’re recognized as a human and not mistaken for a bot. This tutorial covers:
1. **Managed Browsers** – The recommended approach for persistent profiles and identity-based crawling. 2. **Magic Mode** – A simplified fallback solution for quick automation without persistent identity.
## 1. Managed Browsers: Your Digital Identity Solution
**Managed Browsers** let developers create and use **persistent browser profiles**. These profiles store local storage, cookies, and other session data, letting you browse as your **real self** —complete with logins, preferences, and cookies.
### Key Benefits
  * **Authentic Browsing Experience** : Retain session data and browser fingerprints as though you’re a normal user. 
  * **Effortless Configuration** : Once you log in or solve CAPTCHAs in your chosen data directory, you can re-run crawls without repeating those steps. 
  * **Empowered Data Access** : If you can see the data in your own browser, you can automate its retrieval with your genuine identity.


Below is a **partial update** to your **Managed Browsers** tutorial, specifically the section about **creating a user-data directory** using **Playwright’s Chromium** binary rather than a system-wide Chrome/Edge. We’ll show how to **locate** that binary and launch it with a `--user-data-dir` argument to set up your profile. You can then point `BrowserConfig.user_data_dir` to that folder for subsequent crawls.
### Creating a User Data Directory (Command-Line Approach via Playwright)
If you installed Crawl4AI (which installs Playwright under the hood), you already have a Playwright-managed Chromium on your system. Follow these steps to launch that **Chromium** from your command line, specifying a **custom** data directory:
1. **Find** the Playwright Chromium binary: - On most systems, installed browsers go under a `~/.cache/ms-playwright/` folder or similar path. - To see an overview of installed browsers, run: 
```
python -m playwright install --dry-run

```

or 
```
playwright install --dry-run

```

(depending on your environment). This shows where Playwright keeps Chromium. 
  * For instance, you might see a path like: 
```
~/.cache/ms-playwright/chromium-1234/chrome-linux/chrome

```

on Linux, or a corresponding folder on macOS/Windows.


2. **Launch** the Playwright Chromium binary with a **custom** user-data directory: 
```
# Linux example
~/.cache/ms-playwright/chromium-1234/chrome-linux/chrome \
  --user-data-dir=/home/<you>/my_chrome_profile

```

```
# macOS example (Playwright’s internal binary)
~/Library/Caches/ms-playwright/chromium-1234/chrome-mac/Chromium.app/Contents/MacOS/Chromium \
  --user-data-dir=/Users/<you>/my_chrome_profile

```

```
# Windows example (PowerShell/cmd)
"C:\Users\<you>\AppData\Local\ms-playwright\chromium-1234\chrome-win\chrome.exe" ^
  --user-data-dir="C:\Users\<you>\my_chrome_profile"

```

**Replace** the path with the actual subfolder indicated in your `ms-playwright` cache structure. - This **opens** a fresh Chromium with your new or existing data folder. - **Log into** any sites or configure your browser the way you want. - **Close** when done—your profile data is saved in that folder.
3. **Use** that folder in **`BrowserConfig.user_data_dir`**:
```
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig
browser_config = BrowserConfig(
  headless=True,
  use_managed_browser=True,
  user_data_dir="/home/<you>/my_chrome_profile",
  browser_type="chromium"
)

```

- Next time you run your code, it reuses that folder—**preserving** your session data, cookies, local storage, etc. 
## 3. Using Managed Browsers in Crawl4AI
Once you have a data directory with your session data, pass it to **`BrowserConfig`**:
```
import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig
async def main():
  # 1) Reference your persistent data directory
  browser_config = BrowserConfig(
    headless=True,       # 'True' for automated runs
    verbose=True,
    use_managed_browser=True, # Enables persistent browser strategy
    browser_type="chromium",
    user_data_dir="/path/to/my-chrome-profile"
  )
  # 2) Standard crawl config
  crawl_config = CrawlerRunConfig(
    wait_for="css:.logged-in-content"
  )
  async with AsyncWebCrawler(config=browser_config) as crawler:
    result = await crawler.arun(url="https://example.com/private", config=crawl_config)
    if result.success:
      print("Successfully accessed private data with your identity!")
    else:
      print("Error:", result.error_message)
if __name__ == "__main__":
  asyncio.run(main())

```

### Workflow
1. **Login** externally (via CLI or your normal Chrome with `--user-data-dir=...`). 2. **Close** that browser. 3. **Use** the same folder in `user_data_dir=` in Crawl4AI. 4. **Crawl** – The site sees your identity as if you’re the same user who just logged in.
## 4. Magic Mode: Simplified Automation
If you **don’t** need a persistent profile or identity-based approach, **Magic Mode** offers a quick way to simulate human-like browsing without storing long-term data.
```
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
async with AsyncWebCrawler() as crawler:
  result = await crawler.arun(
    url="https://example.com",
    config=CrawlerRunConfig(
      magic=True, # Simplifies a lot of interaction
      remove_overlay_elements=True,
      page_timeout=60000
    )
  )

```

**Magic Mode** :
  * Simulates a user-like experience 
  * Randomizes user agent & navigator
  * Randomizes interactions & timings 
  * Masks automation signals 
  * Attempts pop-up handling 


**But** it’s no substitute for **true** user-based sessions if you want a fully legitimate identity-based solution.
## 5. Comparing Managed Browsers vs. Magic Mode
Feature | **Managed Browsers** | **Magic Mode**  
---|---|---  
**Session Persistence** | Full localStorage/cookies retained in user_data_dir | No persistent data (fresh each run)  
**Genuine Identity** | Real user profile with full rights & preferences | Emulated user-like patterns, but no actual identity  
**Complex Sites** | Best for login-gated sites or heavy config | Simple tasks, minimal login or config needed  
**Setup** | External creation of user_data_dir, then use in Crawl4AI | Single-line approach (`magic=True`)  
**Reliability** | Extremely consistent (same data across runs) | Good for smaller tasks, can be less stable  
## 6. Summary
  * **Create** your user-data directory by launching Chrome/Chromium externally with `--user-data-dir=/some/path`. 
  * **Log in** or configure sites as needed, then close the browser. 
  * **Reference** that folder in `BrowserConfig(user_data_dir="...")` + `use_managed_browser=True`. 
  * Enjoy **persistent** sessions that reflect your real identity. 
  * If you only need quick, ephemeral automation, **Magic Mode** might suffice.


**Recommended** : Always prefer a **Managed Browser** for robust, identity-based crawling and simpler interactions with complex sites. Use **Magic Mode** for quick tasks or prototypes where persistent data is unnecessary.
With these approaches, you preserve your **authentic** browsing environment, ensuring the site sees you exactly as a normal user—no repeated logins or wasted time.
Site built with [MkDocs](https://docs.crawl4ai.com/advanced/identity-based-crawling/<http:/www.mkdocs.org>) and [Terminal for MkDocs](https://docs.crawl4ai.com/advanced/identity-based-crawling/<https:/github.com/ntno/mkdocs-terminal>). 
##### Search
xClose
Type to start searching


==================================================

# URL: https://docs.crawl4ai.com/advanced/lazy-loading/

[Crawl4AI Documentation](https://docs.crawl4ai.com/advanced/lazy-loading/<https:/docs.crawl4ai.com/>)
  * [ Home ](https://docs.crawl4ai.com/advanced/lazy-loading/<../..>)
  * [ Quick Start ](https://docs.crawl4ai.com/advanced/lazy-loading/core/quickstart/>)
  * [ Search ](https://docs.crawl4ai.com/advanced/lazy-loading/<#>)


  * [Home](https://docs.crawl4ai.com/advanced/lazy-loading/<../..>)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/advanced/lazy-loading/core/installation/>)
    * [Docker Deployment](https://docs.crawl4ai.com/advanced/lazy-loading/core/docker-deploymeny/>)
  * [Quick Start](https://docs.crawl4ai.com/advanced/lazy-loading/core/quickstart/>)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/advanced/lazy-loading/blog/>)
    * [Changelog](https://docs.crawl4ai.com/advanced/lazy-loading/<https:/github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md>)
  * Core
    * [Simple Crawling](https://docs.crawl4ai.com/advanced/lazy-loading/core/simple-crawling/>)
    * [Crawler Result](https://docs.crawl4ai.com/advanced/lazy-loading/core/crawler-result/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/advanced/lazy-loading/core/browser-crawler-config/>)
    * [Markdown Generation](https://docs.crawl4ai.com/advanced/lazy-loading/core/markdown-generation/>)
    * [Fit Markdown](https://docs.crawl4ai.com/advanced/lazy-loading/core/fit-markdown/>)
    * [Page Interaction](https://docs.crawl4ai.com/advanced/lazy-loading/core/page-interaction/>)
    * [Content Selection](https://docs.crawl4ai.com/advanced/lazy-loading/core/content-selection/>)
    * [Cache Modes](https://docs.crawl4ai.com/advanced/lazy-loading/core/cache-modes/>)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/advanced/lazy-loading/core/local-files/>)
    * [Link & Media](https://docs.crawl4ai.com/advanced/lazy-loading/core/link-media/>)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/advanced/lazy-loading/<../advanced-features/>)
    * [File Downloading](https://docs.crawl4ai.com/advanced/lazy-loading/<../file-downloading/>)
    * Lazy Loading
    * [Hooks & Auth](https://docs.crawl4ai.com/advanced/lazy-loading/<../hooks-auth/>)
    * [Proxy & Security](https://docs.crawl4ai.com/advanced/lazy-loading/<../proxy-security/>)
    * [Session Management](https://docs.crawl4ai.com/advanced/lazy-loading/<../session-management/>)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/advanced/lazy-loading/<../multi-url-crawling/>)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/advanced/lazy-loading/<../crawl-dispatcher/>)
    * [Identity Based Crawling](https://docs.crawl4ai.com/advanced/lazy-loading/<../identity-based-crawling/>)
    * [SSL Certificate](https://docs.crawl4ai.com/advanced/lazy-loading/<../ssl-certificate/>)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/advanced/lazy-loading/extraction/no-llm-strategies/>)
    * [LLM Strategies](https://docs.crawl4ai.com/advanced/lazy-loading/extraction/llm-strategies/>)
    * [Clustering Strategies](https://docs.crawl4ai.com/advanced/lazy-loading/extraction/clustring-strategies/>)
    * [Chunking](https://docs.crawl4ai.com/advanced/lazy-loading/extraction/chunking/>)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/advanced/lazy-loading/api/async-webcrawler/>)
    * [arun()](https://docs.crawl4ai.com/advanced/lazy-loading/api/arun/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/advanced/lazy-loading/api/parameters/>)
    * [CrawlResult](https://docs.crawl4ai.com/advanced/lazy-loading/api/crawl-result/>)
    * [Strategies](https://docs.crawl4ai.com/advanced/lazy-loading/api/strategies/>)


  * [Handling Lazy-Loaded Images](https://docs.crawl4ai.com/advanced/lazy-loading/<#handling-lazy-loaded-images>)
  * [Example: Ensuring Lazy Images Appear](https://docs.crawl4ai.com/advanced/lazy-loading/<#example-ensuring-lazy-images-appear>)
  * [Combining with Other Link & Media Filters](https://docs.crawl4ai.com/advanced/lazy-loading/<#combining-with-other-link-media-filters>)
  * [Tips & Troubleshooting](https://docs.crawl4ai.com/advanced/lazy-loading/<#tips-troubleshooting>)


## Handling Lazy-Loaded Images
Many websites now load images **lazily** as you scroll. If you need to ensure they appear in your final crawl (and in `result.media`), consider:
1. **`wait_for_images=True`**– Wait for images to fully load. 2.**`scan_full_page`**– Force the crawler to scroll the entire page, triggering lazy loads. 3.**`scroll_delay`**– Add small delays between scroll steps.
**Note** : If the site requires multiple “Load More” triggers or complex interactions, see the [Page Interaction docs](https://docs.crawl4ai.com/advanced/lazy-loading/core/page-interaction/>).
### Example: Ensuring Lazy Images Appear
```
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, BrowserConfig
from crawl4ai.async_configs import CacheMode
async def main():
  config = CrawlerRunConfig(
    # Force the crawler to wait until images are fully loaded
    wait_for_images=True,
    # Option 1: If you want to automatically scroll the page to load images
    scan_full_page=True, # Tells the crawler to try scrolling the entire page
    scroll_delay=0.5,   # Delay (seconds) between scroll steps
    # Option 2: If the site uses a 'Load More' or JS triggers for images,
    # you can also specify js_code or wait_for logic here.
    cache_mode=CacheMode.BYPASS,
    verbose=True
  )
  async with AsyncWebCrawler(config=BrowserConfig(headless=True)) as crawler:
    result = await crawler.arun("https://www.example.com/gallery", config=config)
    if result.success:
      images = result.media.get("images", [])
      print("Images found:", len(images))
      for i, img in enumerate(images[:5]):
        print(f"[Image {i}] URL: {img['src']}, Score: {img.get('score','N/A')}")
    else:
      print("Error:", result.error_message)
if __name__ == "__main__":
  asyncio.run(main())

```

**Explanation** :
  * **`wait_for_images=True`**The crawler tries to ensure images have finished loading before finalizing the HTML.
  * **`scan_full_page=True`**Tells the crawler to attempt scrolling from top to bottom. Each scroll step helps trigger lazy loading.
  * **`scroll_delay=0.5`**Pause half a second between each scroll step. Helps the site load images before continuing.


**When to Use** :
  * **Lazy-Loading** : If images appear only when the user scrolls into view, `scan_full_page` + `scroll_delay` helps the crawler see them. 
  * **Heavier Pages** : If a page is extremely long, be mindful that scanning the entire page can be slow. Adjust `scroll_delay` or the max scroll steps as needed.


## Combining with Other Link & Media Filters
You can still combine **lazy-load** logic with the usual **exclude_external_images** , **exclude_domains** , or link filtration:
```
config = CrawlerRunConfig(
  wait_for_images=True,
  scan_full_page=True,
  scroll_delay=0.5,
  # Filter out external images if you only want local ones
  exclude_external_images=True,
  # Exclude certain domains for links
  exclude_domains=["spammycdn.com"],
)

```

This approach ensures you see **all** images from the main domain while ignoring external ones, and the crawler physically scrolls the entire page so that lazy-loading triggers.
## Tips & Troubleshooting
1. **Long Pages** - Setting `scan_full_page=True` on extremely long or infinite-scroll pages can be resource-intensive. - Consider using [hooks](https://docs.crawl4ai.com/advanced/lazy-loading/core/page-interaction/>) or specialized logic to load specific sections or “Load More” triggers repeatedly.
2. **Mixed Image Behavior** - Some sites load images in batches as you scroll. If you’re missing images, increase your `scroll_delay` or call multiple partial scrolls in a loop with JS code or hooks.
3. **Combining with Dynamic Wait** - If the site has a placeholder that only changes to a real image after a certain event, you might do `wait_for="css:img.loaded"` or a custom JS `wait_for`.
4. **Caching** - If `cache_mode` is enabled, repeated crawls might skip some network fetches. If you suspect caching is missing new images, set `cache_mode=CacheMode.BYPASS` for fresh fetches.
With **lazy-loading** support, **wait_for_images** , and **scan_full_page** settings, you can capture the entire gallery or feed of images you expect—even if the site only loads them as the user scrolls. Combine these with the standard media filtering and domain exclusion for a complete link & media handling strategy.
Site built with [MkDocs](https://docs.crawl4ai.com/advanced/lazy-loading/<http:/www.mkdocs.org>) and [Terminal for MkDocs](https://docs.crawl4ai.com/advanced/lazy-loading/<https:/github.com/ntno/mkdocs-terminal>). 
##### Search
xClose
Type to start searching


==================================================

# URL: https://docs.crawl4ai.com/advanced/multi-url-crawling/

[Crawl4AI Documentation](https://docs.crawl4ai.com/advanced/multi-url-crawling/<https:/docs.crawl4ai.com/>)
  * [ Home ](https://docs.crawl4ai.com/advanced/multi-url-crawling/<../..>)
  * [ Quick Start ](https://docs.crawl4ai.com/advanced/multi-url-crawling/core/quickstart/>)
  * [ Search ](https://docs.crawl4ai.com/advanced/multi-url-crawling/<#>)


  * [Home](https://docs.crawl4ai.com/advanced/multi-url-crawling/<../..>)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/advanced/multi-url-crawling/core/installation/>)
    * [Docker Deployment](https://docs.crawl4ai.com/advanced/multi-url-crawling/core/docker-deploymeny/>)
  * [Quick Start](https://docs.crawl4ai.com/advanced/multi-url-crawling/core/quickstart/>)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/advanced/multi-url-crawling/blog/>)
    * [Changelog](https://docs.crawl4ai.com/advanced/multi-url-crawling/<https:/github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md>)
  * Core
    * [Simple Crawling](https://docs.crawl4ai.com/advanced/multi-url-crawling/core/simple-crawling/>)
    * [Crawler Result](https://docs.crawl4ai.com/advanced/multi-url-crawling/core/crawler-result/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/advanced/multi-url-crawling/core/browser-crawler-config/>)
    * [Markdown Generation](https://docs.crawl4ai.com/advanced/multi-url-crawling/core/markdown-generation/>)
    * [Fit Markdown](https://docs.crawl4ai.com/advanced/multi-url-crawling/core/fit-markdown/>)
    * [Page Interaction](https://docs.crawl4ai.com/advanced/multi-url-crawling/core/page-interaction/>)
    * [Content Selection](https://docs.crawl4ai.com/advanced/multi-url-crawling/core/content-selection/>)
    * [Cache Modes](https://docs.crawl4ai.com/advanced/multi-url-crawling/core/cache-modes/>)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/advanced/multi-url-crawling/core/local-files/>)
    * [Link & Media](https://docs.crawl4ai.com/advanced/multi-url-crawling/core/link-media/>)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/advanced/multi-url-crawling/<../advanced-features/>)
    * [File Downloading](https://docs.crawl4ai.com/advanced/multi-url-crawling/<../file-downloading/>)
    * [Lazy Loading](https://docs.crawl4ai.com/advanced/multi-url-crawling/<../lazy-loading/>)
    * [Hooks & Auth](https://docs.crawl4ai.com/advanced/multi-url-crawling/<../hooks-auth/>)
    * [Proxy & Security](https://docs.crawl4ai.com/advanced/multi-url-crawling/<../proxy-security/>)
    * [Session Management](https://docs.crawl4ai.com/advanced/multi-url-crawling/<../session-management/>)
    * Multi-URL Crawling
    * [Crawl Dispatcher](https://docs.crawl4ai.com/advanced/multi-url-crawling/<../crawl-dispatcher/>)
    * [Identity Based Crawling](https://docs.crawl4ai.com/advanced/multi-url-crawling/<../identity-based-crawling/>)
    * [SSL Certificate](https://docs.crawl4ai.com/advanced/multi-url-crawling/<../ssl-certificate/>)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/advanced/multi-url-crawling/extraction/no-llm-strategies/>)
    * [LLM Strategies](https://docs.crawl4ai.com/advanced/multi-url-crawling/extraction/llm-strategies/>)
    * [Clustering Strategies](https://docs.crawl4ai.com/advanced/multi-url-crawling/extraction/clustring-strategies/>)
    * [Chunking](https://docs.crawl4ai.com/advanced/multi-url-crawling/extraction/chunking/>)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/advanced/multi-url-crawling/api/async-webcrawler/>)
    * [arun()](https://docs.crawl4ai.com/advanced/multi-url-crawling/api/arun/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/advanced/multi-url-crawling/api/parameters/>)
    * [CrawlResult](https://docs.crawl4ai.com/advanced/multi-url-crawling/api/crawl-result/>)
    * [Strategies](https://docs.crawl4ai.com/advanced/multi-url-crawling/api/strategies/>)


  * [Optimized Multi-URL Crawling](https://docs.crawl4ai.com/advanced/multi-url-crawling/<#optimized-multi-url-crawling>)
  * [1. Why Avoid Simple Loops per URL?](https://docs.crawl4ai.com/advanced/multi-url-crawling/<#1-why-avoid-simple-loops-per-url>)
  * [2. Sequential Crawling with Session Reuse](https://docs.crawl4ai.com/advanced/multi-url-crawling/<#2-sequential-crawling-with-session-reuse>)
  * [3. Parallel Crawling with Browser Reuse](https://docs.crawl4ai.com/advanced/multi-url-crawling/<#3-parallel-crawling-with-browser-reuse>)
  * [4. Performance Tips](https://docs.crawl4ai.com/advanced/multi-url-crawling/<#4-performance-tips>)
  * [5. Summary](https://docs.crawl4ai.com/advanced/multi-url-crawling/<#5-summary>)


# Optimized Multi-URL Crawling
> **Note** : We’re developing a new **executor module** that uses a sophisticated algorithm to dynamically manage multi-URL crawling, optimizing for speed and memory usage. The approaches in this document remain fully valid, but keep an eye on **Crawl4AI** ’s upcoming releases for this powerful feature! Follow [@unclecode](https://docs.crawl4ai.com/advanced/multi-url-crawling/<https:/twitter.com/unclecode>) on X and check the changelogs to stay updated.
Crawl4AI’s **AsyncWebCrawler** can handle multiple URLs in a single run, which can greatly reduce overhead and speed up crawling. This guide shows how to:
1. **Sequentially** crawl a list of URLs using the **same** session, avoiding repeated browser creation. 2. **Parallel** -crawl subsets of URLs in batches, again reusing the same browser. 
When the entire process finishes, you close the browser once—**minimizing** memory and resource usage.
## 1. Why Avoid Simple Loops per URL?
If you naively do:
```
for url in urls:
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(url)

```

You end up:
  1. Spinning up a **new** browser for each URL 
  2. Closing it immediately after the single crawl 
  3. Potentially using a lot of CPU/memory for short-living browsers 
  4. Missing out on session reusability if you have login or ongoing states


**Better** approaches ensure you **create** the browser once, then crawl multiple URLs with minimal overhead.
## 2. Sequential Crawling with Session Reuse
### 2.1 Overview
1. **One** `AsyncWebCrawler` instance for **all** URLs. 2. **One** session (via `session_id`) so we can preserve local storage or cookies across URLs if needed. 3. The crawler is only closed at the **end**.
**This** is the simplest pattern if your workload is moderate (dozens to a few hundred URLs).
### 2.2 Example Code
```
import asyncio
from typing import List
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
async def crawl_sequential(urls: List[str]):
  print("\n=== Sequential Crawling with Session Reuse ===")
  browser_config = BrowserConfig(
    headless=True,
    # For better performance in Docker or low-memory environments:
    extra_args=["--disable-gpu", "--disable-dev-shm-usage", "--no-sandbox"],
  )
  crawl_config = CrawlerRunConfig(
    markdown_generator=DefaultMarkdownGenerator()
  )
  # Create the crawler (opens the browser)
  crawler = AsyncWebCrawler(config=browser_config)
  await crawler.start()
  try:
    session_id = "session1" # Reuse the same session across all URLs
    for url in urls:
      result = await crawler.arun(
        url=url,
        config=crawl_config,
        session_id=session_id
      )
      if result.success:
        print(f"Successfully crawled: {url}")
        # E.g. check markdown length
        print(f"Markdown length: {len(result.markdown_v2.raw_markdown)}")
      else:
        print(f"Failed: {url} - Error: {result.error_message}")
  finally:
    # After all URLs are done, close the crawler (and the browser)
    await crawler.close()
async def main():
  urls = [
    "https://example.com/page1",
    "https://example.com/page2",
    "https://example.com/page3"
  ]
  await crawl_sequential(urls)
if __name__ == "__main__":
  asyncio.run(main())

```

**Why It’s Good** :
  * **One** browser launch. 
  * Minimal memory usage. 
  * If the site requires login, you can log in once in `session_id` context and preserve auth across all URLs.


## 3. Parallel Crawling with Browser Reuse
### 3.1 Overview
To speed up crawling further, you can crawl multiple URLs in **parallel** (batches or a concurrency limit). The crawler still uses **one** browser, but spawns different sessions (or the same, depending on your logic) for each task.
### 3.2 Example Code
For this example make sure to install the [psutil](https://docs.crawl4ai.com/advanced/multi-url-crawling/<https:/pypi.org/project/psutil/>) package.
```
pip install psutil

```

Then you can run the following code:
```
import os
import sys
import psutil
import asyncio
__location__ = os.path.dirname(os.path.abspath(__file__))
__output__ = os.path.join(__location__, "output")
# Append parent directory to system path
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)
from typing import List
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
async def crawl_parallel(urls: List[str], max_concurrent: int = 3):
  print("\n=== Parallel Crawling with Browser Reuse + Memory Check ===")
  # We'll keep track of peak memory usage across all tasks
  peak_memory = 0
  process = psutil.Process(os.getpid())
  def log_memory(prefix: str = ""):
    nonlocal peak_memory
    current_mem = process.memory_info().rss # in bytes
    if current_mem > peak_memory:
      peak_memory = current_mem
    print(f"{prefix} Current Memory: {current_mem // (1024 * 1024)} MB, Peak: {peak_memory // (1024 * 1024)} MB")
  # Minimal browser config
  browser_config = BrowserConfig(
    headless=True,
    verbose=False,  # corrected from 'verbos=False'
    extra_args=["--disable-gpu", "--disable-dev-shm-usage", "--no-sandbox"],
  )
  crawl_config = CrawlerRunConfig(cache_mode=CacheMode.BYPASS)
  # Create the crawler instance
  crawler = AsyncWebCrawler(config=browser_config)
  await crawler.start()
  try:
    # We'll chunk the URLs in batches of 'max_concurrent'
    success_count = 0
    fail_count = 0
    for i in range(0, len(urls), max_concurrent):
      batch = urls[i : i + max_concurrent]
      tasks = []
      for j, url in enumerate(batch):
        # Unique session_id per concurrent sub-task
        session_id = f"parallel_session_{i + j}"
        task = crawler.arun(url=url, config=crawl_config, session_id=session_id)
        tasks.append(task)
      # Check memory usage prior to launching tasks
      log_memory(prefix=f"Before batch {i//max_concurrent + 1}: ")
      # Gather results
      results = await asyncio.gather(*tasks, return_exceptions=True)
      # Check memory usage after tasks complete
      log_memory(prefix=f"After batch {i//max_concurrent + 1}: ")
      # Evaluate results
      for url, result in zip(batch, results):
        if isinstance(result, Exception):
          print(f"Error crawling {url}: {result}")
          fail_count += 1
        elif result.success:
          success_count += 1
        else:
          fail_count += 1
    print(f"\nSummary:")
    print(f" - Successfully crawled: {success_count}")
    print(f" - Failed: {fail_count}")
  finally:
    print("\nClosing crawler...")
    await crawler.close()
    # Final memory log
    log_memory(prefix="Final: ")
    print(f"\nPeak memory usage (MB): {peak_memory // (1024 * 1024)}")
async def main():
  urls = [
    "https://example.com/page1",
    "https://example.com/page2",
    "https://example.com/page3",
    "https://example.com/page4"
  ]
  await crawl_parallel(urls, max_concurrent=2)
if __name__ == "__main__":
  asyncio.run(main())

```

**Notes** :
  * We **reuse** the same `AsyncWebCrawler` instance for all parallel tasks, launching **one** browser. 
  * Each parallel sub-task might get its own `session_id` so they don’t share cookies/localStorage (unless that’s desired). 
  * We limit concurrency to `max_concurrent=2` or 3 to avoid saturating CPU/memory.


## 4. Performance Tips
1. **Extra Browser Args** - `--disable-gpu`, `--no-sandbox` can help in Docker or restricted environments. - `--disable-dev-shm-usage` avoids using `/dev/shm` which can be small on some systems.
2. **Session Reuse** - If your site requires a login or you want to maintain local data across URLs, share the **same** `session_id`. - If you want isolation (each URL fresh), create unique sessions.
3. **Batching** - If you have **many** URLs (like thousands), you can do parallel crawling in chunks (like `max_concurrent=5`). - Use `arun_many()` for a built-in approach if you prefer, but the example above is often more flexible.
4. **Cache** - If your pages share many resources or you’re re-crawling the same domain repeatedly, consider setting `cache_mode=CacheMode.ENABLED` in `CrawlerRunConfig`. - If you need fresh data each time, keep `cache_mode=CacheMode.BYPASS`.
5. **Hooks** - You can set up global hooks for each crawler (like to block images) or per-run if you want. - Keep them consistent if you’re reusing sessions.
## 5. Summary
  * **One** `AsyncWebCrawler` + multiple calls to `.arun()` is far more efficient than launching a new crawler per URL. 
  * **Sequential** approach with a shared session is simple and memory-friendly for moderate sets of URLs. 
  * **Parallel** approach can speed up large crawls by concurrency, but keep concurrency balanced to avoid overhead. 
  * Close the crawler once at the end, ensuring the browser is only opened/closed once.


For even more advanced memory optimizations or dynamic concurrency patterns, see future sections on hooking or distributed crawling. The patterns above suffice for the majority of multi-URL scenarios—**giving you speed, simplicity, and minimal resource usage**. Enjoy your optimized crawling!
Site built with [MkDocs](https://docs.crawl4ai.com/advanced/multi-url-crawling/<http:/www.mkdocs.org>) and [Terminal for MkDocs](https://docs.crawl4ai.com/advanced/multi-url-crawling/<https:/github.com/ntno/mkdocs-terminal>). 
##### Search
xClose
Type to start searching


==================================================

# URL: https://docs.crawl4ai.com/advanced/proxy-security/

[Crawl4AI Documentation](https://docs.crawl4ai.com/advanced/proxy-security/<https:/docs.crawl4ai.com/>)
  * [ Home ](https://docs.crawl4ai.com/advanced/proxy-security/<../..>)
  * [ Quick Start ](https://docs.crawl4ai.com/advanced/proxy-security/core/quickstart/>)
  * [ Search ](https://docs.crawl4ai.com/advanced/proxy-security/<#>)


  * [Home](https://docs.crawl4ai.com/advanced/proxy-security/<../..>)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/advanced/proxy-security/core/installation/>)
    * [Docker Deployment](https://docs.crawl4ai.com/advanced/proxy-security/core/docker-deploymeny/>)
  * [Quick Start](https://docs.crawl4ai.com/advanced/proxy-security/core/quickstart/>)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/advanced/proxy-security/blog/>)
    * [Changelog](https://docs.crawl4ai.com/advanced/proxy-security/<https:/github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md>)
  * Core
    * [Simple Crawling](https://docs.crawl4ai.com/advanced/proxy-security/core/simple-crawling/>)
    * [Crawler Result](https://docs.crawl4ai.com/advanced/proxy-security/core/crawler-result/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/advanced/proxy-security/core/browser-crawler-config/>)
    * [Markdown Generation](https://docs.crawl4ai.com/advanced/proxy-security/core/markdown-generation/>)
    * [Fit Markdown](https://docs.crawl4ai.com/advanced/proxy-security/core/fit-markdown/>)
    * [Page Interaction](https://docs.crawl4ai.com/advanced/proxy-security/core/page-interaction/>)
    * [Content Selection](https://docs.crawl4ai.com/advanced/proxy-security/core/content-selection/>)
    * [Cache Modes](https://docs.crawl4ai.com/advanced/proxy-security/core/cache-modes/>)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/advanced/proxy-security/core/local-files/>)
    * [Link & Media](https://docs.crawl4ai.com/advanced/proxy-security/core/link-media/>)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/advanced/proxy-security/<../advanced-features/>)
    * [File Downloading](https://docs.crawl4ai.com/advanced/proxy-security/<../file-downloading/>)
    * [Lazy Loading](https://docs.crawl4ai.com/advanced/proxy-security/<../lazy-loading/>)
    * [Hooks & Auth](https://docs.crawl4ai.com/advanced/proxy-security/<../hooks-auth/>)
    * Proxy & Security
    * [Session Management](https://docs.crawl4ai.com/advanced/proxy-security/<../session-management/>)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/advanced/proxy-security/<../multi-url-crawling/>)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/advanced/proxy-security/<../crawl-dispatcher/>)
    * [Identity Based Crawling](https://docs.crawl4ai.com/advanced/proxy-security/<../identity-based-crawling/>)
    * [SSL Certificate](https://docs.crawl4ai.com/advanced/proxy-security/<../ssl-certificate/>)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/advanced/proxy-security/extraction/no-llm-strategies/>)
    * [LLM Strategies](https://docs.crawl4ai.com/advanced/proxy-security/extraction/llm-strategies/>)
    * [Clustering Strategies](https://docs.crawl4ai.com/advanced/proxy-security/extraction/clustring-strategies/>)
    * [Chunking](https://docs.crawl4ai.com/advanced/proxy-security/extraction/chunking/>)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/advanced/proxy-security/api/async-webcrawler/>)
    * [arun()](https://docs.crawl4ai.com/advanced/proxy-security/api/arun/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/advanced/proxy-security/api/parameters/>)
    * [CrawlResult](https://docs.crawl4ai.com/advanced/proxy-security/api/crawl-result/>)
    * [Strategies](https://docs.crawl4ai.com/advanced/proxy-security/api/strategies/>)


  * [Proxy](https://docs.crawl4ai.com/advanced/proxy-security/<#proxy>)
  * [Basic Proxy Setup](https://docs.crawl4ai.com/advanced/proxy-security/<#basic-proxy-setup>)
  * [Authenticated Proxy](https://docs.crawl4ai.com/advanced/proxy-security/<#authenticated-proxy>)
  * [Rotating Proxies](https://docs.crawl4ai.com/advanced/proxy-security/<#rotating-proxies>)


# Proxy
## Basic Proxy Setup
Simple proxy configuration with `BrowserConfig`:
```
from crawl4ai.async_configs import BrowserConfig
# Using proxy URL
browser_config = BrowserConfig(proxy="http://proxy.example.com:8080")
async with AsyncWebCrawler(config=browser_config) as crawler:
  result = await crawler.arun(url="https://example.com")
# Using SOCKS proxy
browser_config = BrowserConfig(proxy="socks5://proxy.example.com:1080")
async with AsyncWebCrawler(config=browser_config) as crawler:
  result = await crawler.arun(url="https://example.com")

```

## Authenticated Proxy
Use an authenticated proxy with `BrowserConfig`:
```
from crawl4ai.async_configs import BrowserConfig
proxy_config = {
  "server": "http://proxy.example.com:8080",
  "username": "user",
  "password": "pass"
}
browser_config = BrowserConfig(proxy_config=proxy_config)
async with AsyncWebCrawler(config=browser_config) as crawler:
  result = await crawler.arun(url="https://example.com")

```

## Rotating Proxies
Example using a proxy rotation service and updating `BrowserConfig` dynamically:
```
from crawl4ai.async_configs import BrowserConfig
async def get_next_proxy():
  # Your proxy rotation logic here
  return {"server": "http://next.proxy.com:8080"}
browser_config = BrowserConfig()
async with AsyncWebCrawler(config=browser_config) as crawler:
  # Update proxy for each request
  for url in urls:
    proxy = await get_next_proxy()
    browser_config.proxy_config = proxy
    result = await crawler.arun(url=url, config=browser_config)

```

Site built with [MkDocs](https://docs.crawl4ai.com/advanced/proxy-security/<http:/www.mkdocs.org>) and [Terminal for MkDocs](https://docs.crawl4ai.com/advanced/proxy-security/<https:/github.com/ntno/mkdocs-terminal>). 
##### Search
xClose
Type to start searching


==================================================

# URL: https://docs.crawl4ai.com/advanced/session-management/

[Crawl4AI Documentation](https://docs.crawl4ai.com/advanced/session-management/<https:/docs.crawl4ai.com/>)
  * [ Home ](https://docs.crawl4ai.com/advanced/session-management/<../..>)
  * [ Quick Start ](https://docs.crawl4ai.com/advanced/session-management/core/quickstart/>)
  * [ Search ](https://docs.crawl4ai.com/advanced/session-management/<#>)


  * [Home](https://docs.crawl4ai.com/advanced/session-management/<../..>)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/advanced/session-management/core/installation/>)
    * [Docker Deployment](https://docs.crawl4ai.com/advanced/session-management/core/docker-deploymeny/>)
  * [Quick Start](https://docs.crawl4ai.com/advanced/session-management/core/quickstart/>)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/advanced/session-management/blog/>)
    * [Changelog](https://docs.crawl4ai.com/advanced/session-management/<https:/github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md>)
  * Core
    * [Simple Crawling](https://docs.crawl4ai.com/advanced/session-management/core/simple-crawling/>)
    * [Crawler Result](https://docs.crawl4ai.com/advanced/session-management/core/crawler-result/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/advanced/session-management/core/browser-crawler-config/>)
    * [Markdown Generation](https://docs.crawl4ai.com/advanced/session-management/core/markdown-generation/>)
    * [Fit Markdown](https://docs.crawl4ai.com/advanced/session-management/core/fit-markdown/>)
    * [Page Interaction](https://docs.crawl4ai.com/advanced/session-management/core/page-interaction/>)
    * [Content Selection](https://docs.crawl4ai.com/advanced/session-management/core/content-selection/>)
    * [Cache Modes](https://docs.crawl4ai.com/advanced/session-management/core/cache-modes/>)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/advanced/session-management/core/local-files/>)
    * [Link & Media](https://docs.crawl4ai.com/advanced/session-management/core/link-media/>)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/advanced/session-management/<../advanced-features/>)
    * [File Downloading](https://docs.crawl4ai.com/advanced/session-management/<../file-downloading/>)
    * [Lazy Loading](https://docs.crawl4ai.com/advanced/session-management/<../lazy-loading/>)
    * [Hooks & Auth](https://docs.crawl4ai.com/advanced/session-management/<../hooks-auth/>)
    * [Proxy & Security](https://docs.crawl4ai.com/advanced/session-management/<../proxy-security/>)
    * Session Management
    * [Multi-URL Crawling](https://docs.crawl4ai.com/advanced/session-management/<../multi-url-crawling/>)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/advanced/session-management/<../crawl-dispatcher/>)
    * [Identity Based Crawling](https://docs.crawl4ai.com/advanced/session-management/<../identity-based-crawling/>)
    * [SSL Certificate](https://docs.crawl4ai.com/advanced/session-management/<../ssl-certificate/>)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/advanced/session-management/extraction/no-llm-strategies/>)
    * [LLM Strategies](https://docs.crawl4ai.com/advanced/session-management/extraction/llm-strategies/>)
    * [Clustering Strategies](https://docs.crawl4ai.com/advanced/session-management/extraction/clustring-strategies/>)
    * [Chunking](https://docs.crawl4ai.com/advanced/session-management/extraction/chunking/>)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/advanced/session-management/api/async-webcrawler/>)
    * [arun()](https://docs.crawl4ai.com/advanced/session-management/api/arun/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/advanced/session-management/api/parameters/>)
    * [CrawlResult](https://docs.crawl4ai.com/advanced/session-management/api/crawl-result/>)
    * [Strategies](https://docs.crawl4ai.com/advanced/session-management/api/strategies/>)


  * [Session Management](https://docs.crawl4ai.com/advanced/session-management/<#session-management>)
  * [Basic Session Usage](https://docs.crawl4ai.com/advanced/session-management/<#basic-session-usage>)
  * [Dynamic Content with Sessions](https://docs.crawl4ai.com/advanced/session-management/<#dynamic-content-with-sessions>)
  * [Example 1: Basic Session-Based Crawling](https://docs.crawl4ai.com/advanced/session-management/<#example-1-basic-session-based-crawling>)
  * [Advanced Technique 1: Custom Execution Hooks](https://docs.crawl4ai.com/advanced/session-management/<#advanced-technique-1-custom-execution-hooks>)
  * [Advanced Technique 2: Integrated JavaScript Execution and Waiting](https://docs.crawl4ai.com/advanced/session-management/<#advanced-technique-2-integrated-javascript-execution-and-waiting>)


# Session Management
Session management in Crawl4AI is a powerful feature that allows you to maintain state across multiple requests, making it particularly suitable for handling complex multi-step crawling tasks. It enables you to reuse the same browser tab (or page object) across sequential actions and crawls, which is beneficial for:
  * **Performing JavaScript actions before and after crawling.**
  * **Executing multiple sequential crawls faster** without needing to reopen tabs or allocate memory repeatedly.


**Note:** This feature is designed for sequential workflows and is not suitable for parallel operations.
#### Basic Session Usage
Use `BrowserConfig` and `CrawlerRunConfig` to maintain state with a `session_id`:
```
from crawl4ai.async_configs import BrowserConfig, CrawlerRunConfig
async with AsyncWebCrawler() as crawler:
  session_id = "my_session"
  # Define configurations
  config1 = CrawlerRunConfig(
    url="https://example.com/page1", session_id=session_id
  )
  config2 = CrawlerRunConfig(
    url="https://example.com/page2", session_id=session_id
  )
  # First request
  result1 = await crawler.arun(config=config1)
  # Subsequent request using the same session
  result2 = await crawler.arun(config=config2)
  # Clean up when done
  await crawler.crawler_strategy.kill_session(session_id)

```

#### Dynamic Content with Sessions
Here's an example of crawling GitHub commits across multiple pages while preserving session state:
```
from crawl4ai.async_configs import CrawlerRunConfig
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
from crawl4ai.cache_context import CacheMode
async def crawl_dynamic_content():
  async with AsyncWebCrawler() as crawler:
    session_id = "github_commits_session"
    url = "https://github.com/microsoft/TypeScript/commits/main"
    all_commits = []
    # Define extraction schema
    schema = {
      "name": "Commit Extractor",
      "baseSelector": "li.Box-sc-g0xbh4-0",
      "fields": [{
        "name": "title", "selector": "h4.markdown-title", "type": "text"
      }],
    }
    extraction_strategy = JsonCssExtractionStrategy(schema)
    # JavaScript and wait configurations
    js_next_page = """document.querySelector('a[data-testid="pagination-next-button"]').click();"""
    wait_for = """() => document.querySelectorAll('li.Box-sc-g0xbh4-0').length > 0"""
    # Crawl multiple pages
    for page in range(3):
      config = CrawlerRunConfig(
        url=url,
        session_id=session_id,
        extraction_strategy=extraction_strategy,
        js_code=js_next_page if page > 0 else None,
        wait_for=wait_for if page > 0 else None,
        js_only=page > 0,
        cache_mode=CacheMode.BYPASS
      )
      result = await crawler.arun(config=config)
      if result.success:
        commits = json.loads(result.extracted_content)
        all_commits.extend(commits)
        print(f"Page {page + 1}: Found {len(commits)} commits")
    # Clean up session
    await crawler.crawler_strategy.kill_session(session_id)
    return all_commits

```

## Example 1: Basic Session-Based Crawling
A simple example using session-based crawling:
```
import asyncio
from crawl4ai.async_configs import BrowserConfig, CrawlerRunConfig
from crawl4ai.cache_context import CacheMode
async def basic_session_crawl():
  async with AsyncWebCrawler() as crawler:
    session_id = "dynamic_content_session"
    url = "https://example.com/dynamic-content"
    for page in range(3):
      config = CrawlerRunConfig(
        url=url,
        session_id=session_id,
        js_code="document.querySelector('.load-more-button').click();" if page > 0 else None,
        css_selector=".content-item",
        cache_mode=CacheMode.BYPASS
      )
      result = await crawler.arun(config=config)
      print(f"Page {page + 1}: Found {result.extracted_content.count('.content-item')} items")
    await crawler.crawler_strategy.kill_session(session_id)
asyncio.run(basic_session_crawl())

```

This example shows: 1. Reusing the same `session_id` across multiple requests. 2. Executing JavaScript to load more content dynamically. 3. Properly closing the session to free resources.
## Advanced Technique 1: Custom Execution Hooks
> Warning: You might feel confused by the end of the next few examples 😅, so make sure you are comfortable with the order of the parts before you start this.
Use custom hooks to handle complex scenarios, such as waiting for content to load dynamically:
```
async def advanced_session_crawl_with_hooks():
  first_commit = ""
  async def on_execution_started(page):
    nonlocal first_commit
    try:
      while True:
        await page.wait_for_selector("li.commit-item h4")
        commit = await page.query_selector("li.commit-item h4")
        commit = await commit.evaluate("(element) => element.textContent").strip()
        if commit and commit != first_commit:
          first_commit = commit
          break
        await asyncio.sleep(0.5)
    except Exception as e:
      print(f"Warning: New content didn't appear: {e}")
  async with AsyncWebCrawler() as crawler:
    session_id = "commit_session"
    url = "https://github.com/example/repo/commits/main"
    crawler.crawler_strategy.set_hook("on_execution_started", on_execution_started)
    js_next_page = """document.querySelector('a.pagination-next').click();"""
    for page in range(3):
      config = CrawlerRunConfig(
        url=url,
        session_id=session_id,
        js_code=js_next_page if page > 0 else None,
        css_selector="li.commit-item",
        js_only=page > 0,
        cache_mode=CacheMode.BYPASS
      )
      result = await crawler.arun(config=config)
      print(f"Page {page + 1}: Found {len(result.extracted_content)} commits")
    await crawler.crawler_strategy.kill_session(session_id)
asyncio.run(advanced_session_crawl_with_hooks())

```

This technique ensures new content loads before the next action.
## Advanced Technique 2: Integrated JavaScript Execution and Waiting
Combine JavaScript execution and waiting logic for concise handling of dynamic content:
```
async def integrated_js_and_wait_crawl():
  async with AsyncWebCrawler() as crawler:
    session_id = "integrated_session"
    url = "https://github.com/example/repo/commits/main"
    js_next_page_and_wait = """
    (async () => {
      const getCurrentCommit = () => document.querySelector('li.commit-item h4').textContent.trim();
      const initialCommit = getCurrentCommit();
      document.querySelector('a.pagination-next').click();
      while (getCurrentCommit() === initialCommit) {
        await new Promise(resolve => setTimeout(resolve, 100));
      }
    })();
    """
    for page in range(3):
      config = CrawlerRunConfig(
        url=url,
        session_id=session_id,
        js_code=js_next_page_and_wait if page > 0 else None,
        css_selector="li.commit-item",
        js_only=page > 0,
        cache_mode=CacheMode.BYPASS
      )
      result = await crawler.arun(config=config)
      print(f"Page {page + 1}: Found {len(result.extracted_content)} commits")
    await crawler.crawler_strategy.kill_session(session_id)
asyncio.run(integrated_js_and_wait_crawl())

```

#### Common Use Cases for Sessions
1. **Authentication Flows** : Login and interact with secured pages.
2. **Pagination Handling** : Navigate through multiple pages.
3. **Form Submissions** : Fill forms, submit, and process results.
4. **Multi-step Processes** : Complete workflows that span multiple actions.
5. **Dynamic Content Navigation** : Handle JavaScript-rendered or event-triggered content.
Site built with [MkDocs](https://docs.crawl4ai.com/advanced/session-management/<http:/www.mkdocs.org>) and [Terminal for MkDocs](https://docs.crawl4ai.com/advanced/session-management/<https:/github.com/ntno/mkdocs-terminal>). 
##### Search
xClose
Type to start searching


==================================================

# URL: https://docs.crawl4ai.com/advanced/ssl-certificate/

[Crawl4AI Documentation](https://docs.crawl4ai.com/advanced/ssl-certificate/<https:/docs.crawl4ai.com/>)
  * [ Home ](https://docs.crawl4ai.com/advanced/ssl-certificate/<../..>)
  * [ Quick Start ](https://docs.crawl4ai.com/advanced/ssl-certificate/core/quickstart/>)
  * [ Search ](https://docs.crawl4ai.com/advanced/ssl-certificate/<#>)


  * [Home](https://docs.crawl4ai.com/advanced/ssl-certificate/<../..>)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/advanced/ssl-certificate/core/installation/>)
    * [Docker Deployment](https://docs.crawl4ai.com/advanced/ssl-certificate/core/docker-deploymeny/>)
  * [Quick Start](https://docs.crawl4ai.com/advanced/ssl-certificate/core/quickstart/>)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/advanced/ssl-certificate/blog/>)
    * [Changelog](https://docs.crawl4ai.com/advanced/ssl-certificate/<https:/github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md>)
  * Core
    * [Simple Crawling](https://docs.crawl4ai.com/advanced/ssl-certificate/core/simple-crawling/>)
    * [Crawler Result](https://docs.crawl4ai.com/advanced/ssl-certificate/core/crawler-result/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/advanced/ssl-certificate/core/browser-crawler-config/>)
    * [Markdown Generation](https://docs.crawl4ai.com/advanced/ssl-certificate/core/markdown-generation/>)
    * [Fit Markdown](https://docs.crawl4ai.com/advanced/ssl-certificate/core/fit-markdown/>)
    * [Page Interaction](https://docs.crawl4ai.com/advanced/ssl-certificate/core/page-interaction/>)
    * [Content Selection](https://docs.crawl4ai.com/advanced/ssl-certificate/core/content-selection/>)
    * [Cache Modes](https://docs.crawl4ai.com/advanced/ssl-certificate/core/cache-modes/>)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/advanced/ssl-certificate/core/local-files/>)
    * [Link & Media](https://docs.crawl4ai.com/advanced/ssl-certificate/core/link-media/>)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/advanced/ssl-certificate/<../advanced-features/>)
    * [File Downloading](https://docs.crawl4ai.com/advanced/ssl-certificate/<../file-downloading/>)
    * [Lazy Loading](https://docs.crawl4ai.com/advanced/ssl-certificate/<../lazy-loading/>)
    * [Hooks & Auth](https://docs.crawl4ai.com/advanced/ssl-certificate/<../hooks-auth/>)
    * [Proxy & Security](https://docs.crawl4ai.com/advanced/ssl-certificate/<../proxy-security/>)
    * [Session Management](https://docs.crawl4ai.com/advanced/ssl-certificate/<../session-management/>)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/advanced/ssl-certificate/<../multi-url-crawling/>)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/advanced/ssl-certificate/<../crawl-dispatcher/>)
    * [Identity Based Crawling](https://docs.crawl4ai.com/advanced/ssl-certificate/<../identity-based-crawling/>)
    * SSL Certificate
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/advanced/ssl-certificate/extraction/no-llm-strategies/>)
    * [LLM Strategies](https://docs.crawl4ai.com/advanced/ssl-certificate/extraction/llm-strategies/>)
    * [Clustering Strategies](https://docs.crawl4ai.com/advanced/ssl-certificate/extraction/clustring-strategies/>)
    * [Chunking](https://docs.crawl4ai.com/advanced/ssl-certificate/extraction/chunking/>)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/advanced/ssl-certificate/api/async-webcrawler/>)
    * [arun()](https://docs.crawl4ai.com/advanced/ssl-certificate/api/arun/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/advanced/ssl-certificate/api/parameters/>)
    * [CrawlResult](https://docs.crawl4ai.com/advanced/ssl-certificate/api/crawl-result/>)
    * [Strategies](https://docs.crawl4ai.com/advanced/ssl-certificate/api/strategies/>)


  * [SSLCertificate Reference](https://docs.crawl4ai.com/advanced/ssl-certificate/<#sslcertificate-reference>)
  * [1. Overview](https://docs.crawl4ai.com/advanced/ssl-certificate/<#1-overview>)
  * [2. Construction & Fetching](https://docs.crawl4ai.com/advanced/ssl-certificate/<#2-construction-fetching>)
  * [3. Common Properties](https://docs.crawl4ai.com/advanced/ssl-certificate/<#3-common-properties>)
  * [4. Export Methods](https://docs.crawl4ai.com/advanced/ssl-certificate/<#4-export-methods>)
  * [5. Example Usage in Crawl4AI](https://docs.crawl4ai.com/advanced/ssl-certificate/<#5-example-usage-in-crawl4ai>)
  * [6. Notes & Best Practices](https://docs.crawl4ai.com/advanced/ssl-certificate/<#6-notes-best-practices>)


# `SSLCertificate` Reference
The **`SSLCertificate`**class encapsulates an SSL certificate’s data and allows exporting it in various formats (PEM, DER, JSON, or text). It’s used within**Crawl4AI** whenever you set **`fetch_ssl_certificate=True`**in your**`CrawlerRunConfig`**.
## 1. Overview
**Location** : `crawl4ai/ssl_certificate.py`
```
class SSLCertificate:
  """
  Represents an SSL certificate with methods to export in various formats.
  Main Methods:
  - from_url(url, timeout=10)
  - from_file(file_path)
  - from_binary(binary_data)
  - to_json(filepath=None)
  - to_pem(filepath=None)
  - to_der(filepath=None)
  ...
  Common Properties:
  - issuer
  - subject
  - valid_from
  - valid_until
  - fingerprint
  """

```

### Typical Use Case
  1. You **enable** certificate fetching in your crawl by: 
```
CrawlerRunConfig(fetch_ssl_certificate=True, ...)

```

  2. After `arun()`, if `result.ssl_certificate` is present, it’s an instance of **`SSLCertificate`**.
  3. You can **read** basic properties (issuer, subject, validity) or **export** them in multiple formats.


## 2. Construction & Fetching
### 2.1 **`from_url(url, timeout=10)`**
Manually load an SSL certificate from a given URL (port 443). Typically used internally, but you can call it directly if you want:
```
cert = SSLCertificate.from_url("https://example.com")
if cert:
  print("Fingerprint:", cert.fingerprint)

```

### 2.2 **`from_file(file_path)`**
Load from a file containing certificate data in ASN.1 or DER. Rarely needed unless you have local cert files:
```
cert = SSLCertificate.from_file("/path/to/cert.der")

```

### 2.3 **`from_binary(binary_data)`**
Initialize from raw binary. E.g., if you captured it from a socket or another source:
```
cert = SSLCertificate.from_binary(raw_bytes)

```

## 3. Common Properties
After obtaining a **`SSLCertificate`**instance (e.g.`result.ssl_certificate` from a crawl), you can read:
1. **`issuer`**_(dict)_ - E.g. `{"CN": "My Root CA", "O": "..."}` 2. **`subject`**_(dict)_ - E.g. `{"CN": "example.com", "O": "ExampleOrg"}` 3. **`valid_from`**_(str)_ - NotBefore date/time. Often in ASN.1/UTC format. 4. **`valid_until`**_(str)_ - NotAfter date/time. 5. **`fingerprint`**_(str)_ - The SHA-256 digest (lowercase hex). - E.g. `"d14d2e..."`
## 4. Export Methods
Once you have a **`SSLCertificate`**object, you can**export** or **inspect** it:
### 4.1 **`to_json(filepath=None)`→`Optional[str]`**
  * Returns a JSON string containing the parsed certificate fields. 
  * If `filepath` is provided, saves it to disk instead, returning `None`.


**Usage** : 
```
json_data = cert.to_json() # returns JSON string
cert.to_json("certificate.json") # writes file, returns None

```

### 4.2 **`to_pem(filepath=None)`→`Optional[str]`**
  * Returns a PEM-encoded string (common for web servers). 
  * If `filepath` is provided, saves it to disk instead.


```
pem_str = cert.to_pem()       # in-memory PEM string
cert.to_pem("/path/to/cert.pem")   # saved to file

```

### 4.3 **`to_der(filepath=None)`→`Optional[bytes]`**
  * Returns the original DER (binary ASN.1) bytes. 
  * If `filepath` is specified, writes the bytes there instead.


```
der_bytes = cert.to_der()
cert.to_der("certificate.der")

```

### 4.4 (Optional) **`export_as_text()`**
  * If you see a method like `export_as_text()`, it typically returns an OpenSSL-style textual representation. 
  * Not always needed, but can help for debugging or manual inspection.


## 5. Example Usage in Crawl4AI
Below is a minimal sample showing how the crawler obtains an SSL cert from a site, then reads or exports it. The code snippet:
```
import asyncio
import os
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
async def main():
  tmp_dir = "tmp"
  os.makedirs(tmp_dir, exist_ok=True)
  config = CrawlerRunConfig(
    fetch_ssl_certificate=True,
    cache_mode=CacheMode.BYPASS
  )
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun("https://example.com", config=config)
    if result.success and result.ssl_certificate:
      cert = result.ssl_certificate
      # 1. Basic Info
      print("Issuer CN:", cert.issuer.get("CN", ""))
      print("Valid until:", cert.valid_until)
      print("Fingerprint:", cert.fingerprint)
      # 2. Export
      cert.to_json(os.path.join(tmp_dir, "certificate.json"))
      cert.to_pem(os.path.join(tmp_dir, "certificate.pem"))
      cert.to_der(os.path.join(tmp_dir, "certificate.der"))
if __name__ == "__main__":
  asyncio.run(main())

```

## 6. Notes & Best Practices
1. **Timeout** : `SSLCertificate.from_url` internally uses a default **10s** socket connect and wraps SSL. 2. **Binary Form** : The certificate is loaded in ASN.1 (DER) form, then re-parsed by `OpenSSL.crypto`. 3. **Validation** : This does **not** validate the certificate chain or trust store. It only fetches and parses. 4. **Integration** : Within Crawl4AI, you typically just set `fetch_ssl_certificate=True` in `CrawlerRunConfig`; the final result’s `ssl_certificate` is automatically built. 5. **Export** : If you need to store or analyze a cert, the `to_json` and `to_pem` are quite universal.
### Summary
  * **`SSLCertificate`**is a convenience class for capturing and exporting the**TLS certificate** from your crawled site(s). 
  * Common usage is in the **`CrawlResult.ssl_certificate`**field, accessible after setting`fetch_ssl_certificate=True`. 
  * Offers quick access to essential certificate details (`issuer`, `subject`, `fingerprint`) and is easy to export (PEM, DER, JSON) for further analysis or server usage.


Use it whenever you need **insight** into a site’s certificate or require some form of cryptographic or compliance check.
Site built with [MkDocs](https://docs.crawl4ai.com/advanced/ssl-certificate/<http:/www.mkdocs.org>) and [Terminal for MkDocs](https://docs.crawl4ai.com/advanced/ssl-certificate/<https:/github.com/ntno/mkdocs-terminal>). 
##### Search
xClose
Type to start searching


==================================================

# URL: https://docs.crawl4ai.com/api/arun/

[Crawl4AI Documentation](https://docs.crawl4ai.com/api/arun/<https:/docs.crawl4ai.com/>)
  * [ Home ](https://docs.crawl4ai.com/api/arun/<../..>)
  * [ Quick Start ](https://docs.crawl4ai.com/api/arun/core/quickstart/>)
  * [ Search ](https://docs.crawl4ai.com/api/arun/<#>)


  * [Home](https://docs.crawl4ai.com/api/arun/<../..>)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/api/arun/core/installation/>)
    * [Docker Deployment](https://docs.crawl4ai.com/api/arun/core/docker-deploymeny/>)
  * [Quick Start](https://docs.crawl4ai.com/api/arun/core/quickstart/>)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/api/arun/blog/>)
    * [Changelog](https://docs.crawl4ai.com/api/arun/<https:/github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md>)
  * Core
    * [Simple Crawling](https://docs.crawl4ai.com/api/arun/core/simple-crawling/>)
    * [Crawler Result](https://docs.crawl4ai.com/api/arun/core/crawler-result/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/api/arun/core/browser-crawler-config/>)
    * [Markdown Generation](https://docs.crawl4ai.com/api/arun/core/markdown-generation/>)
    * [Fit Markdown](https://docs.crawl4ai.com/api/arun/core/fit-markdown/>)
    * [Page Interaction](https://docs.crawl4ai.com/api/arun/core/page-interaction/>)
    * [Content Selection](https://docs.crawl4ai.com/api/arun/core/content-selection/>)
    * [Cache Modes](https://docs.crawl4ai.com/api/arun/core/cache-modes/>)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/api/arun/core/local-files/>)
    * [Link & Media](https://docs.crawl4ai.com/api/arun/core/link-media/>)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/api/arun/advanced/advanced-features/>)
    * [File Downloading](https://docs.crawl4ai.com/api/arun/advanced/file-downloading/>)
    * [Lazy Loading](https://docs.crawl4ai.com/api/arun/advanced/lazy-loading/>)
    * [Hooks & Auth](https://docs.crawl4ai.com/api/arun/advanced/hooks-auth/>)
    * [Proxy & Security](https://docs.crawl4ai.com/api/arun/advanced/proxy-security/>)
    * [Session Management](https://docs.crawl4ai.com/api/arun/advanced/session-management/>)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/api/arun/advanced/multi-url-crawling/>)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/api/arun/advanced/crawl-dispatcher/>)
    * [Identity Based Crawling](https://docs.crawl4ai.com/api/arun/advanced/identity-based-crawling/>)
    * [SSL Certificate](https://docs.crawl4ai.com/api/arun/advanced/ssl-certificate/>)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/api/arun/extraction/no-llm-strategies/>)
    * [LLM Strategies](https://docs.crawl4ai.com/api/arun/extraction/llm-strategies/>)
    * [Clustering Strategies](https://docs.crawl4ai.com/api/arun/extraction/clustring-strategies/>)
    * [Chunking](https://docs.crawl4ai.com/api/arun/extraction/chunking/>)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/api/arun/<../async-webcrawler/>)
    * arun()
    * [Browser & Crawler Config](https://docs.crawl4ai.com/api/arun/<../parameters/>)
    * [CrawlResult](https://docs.crawl4ai.com/api/arun/<../crawl-result/>)
    * [Strategies](https://docs.crawl4ai.com/api/arun/<../strategies/>)


  * [arun() Parameter Guide (New Approach)](https://docs.crawl4ai.com/api/arun/<#arun-parameter-guide-new-approach>)
  * [1. Core Usage](https://docs.crawl4ai.com/api/arun/<#1-core-usage>)
  * [2. Cache Control](https://docs.crawl4ai.com/api/arun/<#2-cache-control>)
  * [3. Content Processing & Selection](https://docs.crawl4ai.com/api/arun/<#3-content-processing-selection>)
  * [4. Page Navigation & Timing](https://docs.crawl4ai.com/api/arun/<#4-page-navigation-timing>)
  * [5. Session Management](https://docs.crawl4ai.com/api/arun/<#5-session-management>)
  * [6. Screenshot, PDF & Media Options](https://docs.crawl4ai.com/api/arun/<#6-screenshot-pdf-media-options>)
  * [7. Extraction Strategy](https://docs.crawl4ai.com/api/arun/<#7-extraction-strategy>)
  * [8. Comprehensive Example](https://docs.crawl4ai.com/api/arun/<#8-comprehensive-example>)
  * [9. Best Practices](https://docs.crawl4ai.com/api/arun/<#9-best-practices>)
  * [10. Conclusion](https://docs.crawl4ai.com/api/arun/<#10-conclusion>)


# `arun()` Parameter Guide (New Approach)
In Crawl4AI’s **latest** configuration model, nearly all parameters that once went directly to `arun()` are now part of **`CrawlerRunConfig`**. When calling`arun()` , you provide:
```
await crawler.arun(
  url="https://example.com", 
  config=my_run_config
)

```

Below is an organized look at the parameters that can go inside `CrawlerRunConfig`, divided by their functional areas. For **Browser** settings (e.g., `headless`, `browser_type`), see [BrowserConfig](https://docs.crawl4ai.com/api/arun/<../parameters/>).
## 1. Core Usage
```
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
async def main():
  run_config = CrawlerRunConfig(
    verbose=True,      # Detailed logging
    cache_mode=CacheMode.ENABLED, # Use normal read/write cache
    # ... other parameters
  )
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(
      url="https://example.com",
      config=run_config
    )
    print(result.cleaned_html[:500])

```

**Key Fields** : - `verbose=True` logs each crawl step. - `cache_mode` decides how to read/write the local crawl cache.
## 2. Cache Control
**`cache_mode`**(default:`CacheMode.ENABLED`) Use a built-in enum from `CacheMode`: - `ENABLED`: Normal caching—reads if available, writes if missing. - `DISABLED`: No caching—always refetch pages. - `READ_ONLY`: Reads from cache only; no new writes. - `WRITE_ONLY`: Writes to cache but doesn’t read existing data. - `BYPASS`: Skips reading cache for this crawl (though it might still write if set up that way).
```
run_config = CrawlerRunConfig(
  cache_mode=CacheMode.BYPASS
)

```

**Additional flags** : - `bypass_cache=True` acts like `CacheMode.BYPASS`. - `disable_cache=True` acts like `CacheMode.DISABLED`. - `no_cache_read=True` acts like `CacheMode.WRITE_ONLY`. - `no_cache_write=True` acts like `CacheMode.READ_ONLY`.
## 3. Content Processing & Selection
### 3.1 Text Processing
```
run_config = CrawlerRunConfig(
  word_count_threshold=10,  # Ignore text blocks <10 words
  only_text=False,      # If True, tries to remove non-text elements
  keep_data_attributes=False # Keep or discard data-* attributes
)

```

### 3.2 Content Selection
```
run_config = CrawlerRunConfig(
  css_selector=".main-content", # Focus on .main-content region only
  excluded_tags=["form", "nav"], # Remove entire tag blocks
  remove_forms=True,       # Specifically strip <form> elements
  remove_overlay_elements=True, # Attempt to remove modals/popups
)

```

### 3.3 Link Handling
```
run_config = CrawlerRunConfig(
  exclude_external_links=True,     # Remove external links from final content
  exclude_social_media_links=True,   # Remove links to known social sites
  exclude_domains=["ads.example.com"], # Exclude links to these domains
  exclude_social_media_domains=["facebook.com","twitter.com"], # Extend the default list
)

```

### 3.4 Media Filtering
```
run_config = CrawlerRunConfig(
  exclude_external_images=True # Strip images from other domains
)

```

## 4. Page Navigation & Timing
### 4.1 Basic Browser Flow
```
run_config = CrawlerRunConfig(
  wait_for="css:.dynamic-content", # Wait for .dynamic-content
  delay_before_return_html=2.0,  # Wait 2s before capturing final HTML
  page_timeout=60000,       # Navigation & script timeout (ms)
)

```

**Key Fields** : - `wait_for`: - `"css:selector"` or - `"js:() => boolean"` e.g. `js:() => document.querySelectorAll('.item').length > 10`.
  * `mean_delay` & `max_range`: define random delays for `arun_many()` calls. 
  * `semaphore_count`: concurrency limit when crawling multiple URLs.


### 4.2 JavaScript Execution
```
run_config = CrawlerRunConfig(
  js_code=[
    "window.scrollTo(0, document.body.scrollHeight);",
    "document.querySelector('.load-more')?.click();"
  ],
  js_only=False
)

```

  * `js_code` can be a single string or a list of strings. 
  * `js_only=True` means “I’m continuing in the same session with new JS steps, no new full navigation.”


### 4.3 Anti-Bot
```
run_config = CrawlerRunConfig(
  magic=True,
  simulate_user=True,
  override_navigator=True
)

```

- `magic=True` tries multiple stealth features. - `simulate_user=True` mimics mouse movements or random delays. - `override_navigator=True` fakes some navigator properties (like user agent checks). 
## 5. Session Management
**`session_id`**:
```
run_config = CrawlerRunConfig(
  session_id="my_session123"
)

```

If re-used in subsequent `arun()` calls, the same tab/page context is continued (helpful for multi-step tasks or stateful browsing). 
## 6. Screenshot, PDF & Media Options
```
run_config = CrawlerRunConfig(
  screenshot=True,       # Grab a screenshot as base64
  screenshot_wait_for=1.0,   # Wait 1s before capturing
  pdf=True,          # Also produce a PDF
  image_description_min_word_threshold=5, # If analyzing alt text
  image_score_threshold=3,        # Filter out low-score images
)

```

**Where they appear** : - `result.screenshot` → Base64 screenshot string. - `result.pdf` → Byte array with PDF data. 
## 7. Extraction Strategy
**For advanced data extraction** (CSS/LLM-based), set `extraction_strategy`:
```
run_config = CrawlerRunConfig(
  extraction_strategy=my_css_or_llm_strategy
)

```

The extracted data will appear in `result.extracted_content`.
## 8. Comprehensive Example
Below is a snippet combining many parameters:
```
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
async def main():
  # Example schema
  schema = {
    "name": "Articles",
    "baseSelector": "article.post",
    "fields": [
      {"name": "title", "selector": "h2", "type": "text"},
      {"name": "link", "selector": "a", "type": "attribute", "attribute": "href"}
    ]
  }
  run_config = CrawlerRunConfig(
    # Core
    verbose=True,
    cache_mode=CacheMode.ENABLED,
    # Content
    word_count_threshold=10,
    css_selector="main.content",
    excluded_tags=["nav", "footer"],
    exclude_external_links=True,
    # Page & JS
    js_code="document.querySelector('.show-more')?.click();",
    wait_for="css:.loaded-block",
    page_timeout=30000,
    # Extraction
    extraction_strategy=JsonCssExtractionStrategy(schema),
    # Session
    session_id="persistent_session",
    # Media
    screenshot=True,
    pdf=True,
    # Anti-bot
    simulate_user=True,
    magic=True,
  )
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun("https://example.com/posts", config=run_config)
    if result.success:
      print("HTML length:", len(result.cleaned_html))
      print("Extraction JSON:", result.extracted_content)
      if result.screenshot:
        print("Screenshot length:", len(result.screenshot))
      if result.pdf:
        print("PDF bytes length:", len(result.pdf))
    else:
      print("Error:", result.error_message)
if __name__ == "__main__":
  asyncio.run(main())

```

**What we covered** : 1. **Crawling** the main content region, ignoring external links. 2. Running **JavaScript** to click “.show-more”. 3. **Waiting** for “.loaded-block” to appear. 4. Generating a **screenshot** & **PDF** of the final page. 5. Extracting repeated “article.post” elements with a **CSS-based** extraction strategy.
## 9. Best Practices
1. **Use`BrowserConfig` for global browser** settings (headless, user agent). 2. **Use`CrawlerRunConfig`** to handle the **specific** crawl needs: content filtering, caching, JS, screenshot, extraction, etc. 3. Keep your **parameters consistent** in run configs—especially if you’re part of a large codebase with multiple crawls. 4. **Limit** large concurrency (`semaphore_count`) if the site or your system can’t handle it. 5. For dynamic pages, set `js_code` or `scan_full_page` so you load all content.
## 10. Conclusion
All parameters that used to be direct arguments to `arun()` now belong in **`CrawlerRunConfig`**. This approach:
  * Makes code **clearer** and **more maintainable**. 
  * Minimizes confusion about which arguments affect global vs. per-crawl behavior. 
  * Allows you to create **reusable** config objects for different pages or tasks.


For a **full** reference, check out the [CrawlerRunConfig Docs](https://docs.crawl4ai.com/api/arun/<../parameters/>). 
Happy crawling with your **structured, flexible** config approach!
Site built with [MkDocs](https://docs.crawl4ai.com/api/arun/<http:/www.mkdocs.org>) and [Terminal for MkDocs](https://docs.crawl4ai.com/api/arun/<https:/github.com/ntno/mkdocs-terminal>). 
##### Search
xClose
Type to start searching


==================================================

# URL: https://docs.crawl4ai.com/api/async-webcrawler/

[Crawl4AI Documentation](https://docs.crawl4ai.com/api/async-webcrawler/<https:/docs.crawl4ai.com/>)
  * [ Home ](https://docs.crawl4ai.com/api/async-webcrawler/<../..>)
  * [ Quick Start ](https://docs.crawl4ai.com/api/async-webcrawler/core/quickstart/>)
  * [ Search ](https://docs.crawl4ai.com/api/async-webcrawler/<#>)


  * [Home](https://docs.crawl4ai.com/api/async-webcrawler/<../..>)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/api/async-webcrawler/core/installation/>)
    * [Docker Deployment](https://docs.crawl4ai.com/api/async-webcrawler/core/docker-deploymeny/>)
  * [Quick Start](https://docs.crawl4ai.com/api/async-webcrawler/core/quickstart/>)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/api/async-webcrawler/blog/>)
    * [Changelog](https://docs.crawl4ai.com/api/async-webcrawler/<https:/github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md>)
  * Core
    * [Simple Crawling](https://docs.crawl4ai.com/api/async-webcrawler/core/simple-crawling/>)
    * [Crawler Result](https://docs.crawl4ai.com/api/async-webcrawler/core/crawler-result/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/api/async-webcrawler/core/browser-crawler-config/>)
    * [Markdown Generation](https://docs.crawl4ai.com/api/async-webcrawler/core/markdown-generation/>)
    * [Fit Markdown](https://docs.crawl4ai.com/api/async-webcrawler/core/fit-markdown/>)
    * [Page Interaction](https://docs.crawl4ai.com/api/async-webcrawler/core/page-interaction/>)
    * [Content Selection](https://docs.crawl4ai.com/api/async-webcrawler/core/content-selection/>)
    * [Cache Modes](https://docs.crawl4ai.com/api/async-webcrawler/core/cache-modes/>)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/api/async-webcrawler/core/local-files/>)
    * [Link & Media](https://docs.crawl4ai.com/api/async-webcrawler/core/link-media/>)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/api/async-webcrawler/advanced/advanced-features/>)
    * [File Downloading](https://docs.crawl4ai.com/api/async-webcrawler/advanced/file-downloading/>)
    * [Lazy Loading](https://docs.crawl4ai.com/api/async-webcrawler/advanced/lazy-loading/>)
    * [Hooks & Auth](https://docs.crawl4ai.com/api/async-webcrawler/advanced/hooks-auth/>)
    * [Proxy & Security](https://docs.crawl4ai.com/api/async-webcrawler/advanced/proxy-security/>)
    * [Session Management](https://docs.crawl4ai.com/api/async-webcrawler/advanced/session-management/>)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/api/async-webcrawler/advanced/multi-url-crawling/>)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/api/async-webcrawler/advanced/crawl-dispatcher/>)
    * [Identity Based Crawling](https://docs.crawl4ai.com/api/async-webcrawler/advanced/identity-based-crawling/>)
    * [SSL Certificate](https://docs.crawl4ai.com/api/async-webcrawler/advanced/ssl-certificate/>)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/api/async-webcrawler/extraction/no-llm-strategies/>)
    * [LLM Strategies](https://docs.crawl4ai.com/api/async-webcrawler/extraction/llm-strategies/>)
    * [Clustering Strategies](https://docs.crawl4ai.com/api/async-webcrawler/extraction/clustring-strategies/>)
    * [Chunking](https://docs.crawl4ai.com/api/async-webcrawler/extraction/chunking/>)
  * API Reference
    * AsyncWebCrawler
    * [arun()](https://docs.crawl4ai.com/api/async-webcrawler/<../arun/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/api/async-webcrawler/<../parameters/>)
    * [CrawlResult](https://docs.crawl4ai.com/api/async-webcrawler/<../crawl-result/>)
    * [Strategies](https://docs.crawl4ai.com/api/async-webcrawler/<../strategies/>)


  * [AsyncWebCrawler](https://docs.crawl4ai.com/api/async-webcrawler/<#asyncwebcrawler>)
  * [1. Constructor Overview](https://docs.crawl4ai.com/api/async-webcrawler/<#1-constructor-overview>)
  * [2. Lifecycle: Start/Close or Context Manager](https://docs.crawl4ai.com/api/async-webcrawler/<#2-lifecycle-startclose-or-context-manager>)
  * [3. Primary Method: arun()](https://docs.crawl4ai.com/api/async-webcrawler/<#3-primary-method-arun>)
  * [4. Helper Methods](https://docs.crawl4ai.com/api/async-webcrawler/<#4-helper-methods>)
  * [5. CrawlResult Output](https://docs.crawl4ai.com/api/async-webcrawler/<#5-crawlresult-output>)
  * [6. Quick Example](https://docs.crawl4ai.com/api/async-webcrawler/<#6-quick-example>)
  * [7. Best Practices & Migration Notes](https://docs.crawl4ai.com/api/async-webcrawler/<#7-best-practices-migration-notes>)
  * [8. Summary](https://docs.crawl4ai.com/api/async-webcrawler/<#8-summary>)


# AsyncWebCrawler
The **`AsyncWebCrawler`**is the core class for asynchronous web crawling in Crawl4AI. You typically create it**once** , optionally customize it with a **`BrowserConfig`**(e.g., headless, user agent), then**run** multiple **`arun()`**calls with different**`CrawlerRunConfig`**objects.
**Recommended usage** : 1. **Create** a `BrowserConfig` for global browser settings. 2. **Instantiate** `AsyncWebCrawler(config=browser_config)`. 3. **Use** the crawler in an async context manager (`async with`) or manage start/close manually. 4. **Call** `arun(url, config=crawler_run_config)` for each page you want.
## 1. Constructor Overview
```
class AsyncWebCrawler:
  def __init__(
    self,
    crawler_strategy: Optional[AsyncCrawlerStrategy] = None,
    config: Optional[BrowserConfig] = None,
    always_bypass_cache: bool = False,      # deprecated
    always_by_pass_cache: Optional[bool] = None, # also deprecated
    base_directory: str = ...,
    thread_safe: bool = False,
    **kwargs,
  ):
    """
    Create an AsyncWebCrawler instance.
    Args:
      crawler_strategy: 
        (Advanced) Provide a custom crawler strategy if needed.
      config: 
        A BrowserConfig object specifying how the browser is set up.
      always_bypass_cache: 
        (Deprecated) Use CrawlerRunConfig.cache_mode instead.
      base_directory:   
        Folder for storing caches/logs (if relevant).
      thread_safe: 
        If True, attempts some concurrency safeguards. Usually False.
      **kwargs: 
        Additional legacy or debugging parameters.
    """
  )
### Typical Initialization
```python
from crawl4ai import AsyncWebCrawler, BrowserConfig
browser_cfg = BrowserConfig(
  browser_type="chromium",
  headless=True,
  verbose=True
)
crawler = AsyncWebCrawler(config=browser_cfg)

```

**Notes** : - **Legacy** parameters like `always_bypass_cache` remain for backward compatibility, but prefer to set **caching** in `CrawlerRunConfig`.
## 2. Lifecycle: Start/Close or Context Manager
### 2.1 Context Manager (Recommended)
```
async with AsyncWebCrawler(config=browser_cfg) as crawler:
  result = await crawler.arun("https://example.com")
  # The crawler automatically starts/closes resources

```

When the `async with` block ends, the crawler cleans up (closes the browser, etc.).
### 2.2 Manual Start & Close
```
crawler = AsyncWebCrawler(config=browser_cfg)
await crawler.start()
result1 = await crawler.arun("https://example.com")
result2 = await crawler.arun("https://another.com")
await crawler.close()

```

Use this style if you have a **long-running** application or need full control of the crawler’s lifecycle.
## 3. Primary Method: `arun()`
```
async def arun(
  self,
  url: str,
  config: Optional[CrawlerRunConfig] = None,
  # Legacy parameters for backward compatibility...
) -> CrawlResult:
  ...

```

### 3.1 New Approach
You pass a `CrawlerRunConfig` object that sets up everything about a crawl—content filtering, caching, session reuse, JS code, screenshots, etc.
```
import asyncio
from crawl4ai import CrawlerRunConfig, CacheMode
run_cfg = CrawlerRunConfig(
  cache_mode=CacheMode.BYPASS,
  css_selector="main.article",
  word_count_threshold=10,
  screenshot=True
)
async with AsyncWebCrawler(config=browser_cfg) as crawler:
  result = await crawler.arun("https://example.com/news", config=run_cfg)
  print("Crawled HTML length:", len(result.cleaned_html))
  if result.screenshot:
    print("Screenshot base64 length:", len(result.screenshot))

```

### 3.2 Legacy Parameters Still Accepted
For **backward** compatibility, `arun()` can still accept direct arguments like `css_selector=...`, `word_count_threshold=...`, etc., but we strongly advise migrating them into a **`CrawlerRunConfig`**.
## 4. Helper Methods
### 4.1 `arun_many()`
```
async def arun_many(
  self,
  urls: List[str],
  config: Optional[CrawlerRunConfig] = None,
  # Legacy parameters...
) -> List[CrawlResult]:
  ...

```

Crawls multiple URLs in concurrency. Accepts the same style `CrawlerRunConfig`. Example:
```
run_cfg = CrawlerRunConfig(
  # e.g., concurrency, wait_for, caching, extraction, etc.
  semaphore_count=5
)
async with AsyncWebCrawler(config=browser_cfg) as crawler:
  results = await crawler.arun_many(
    urls=["https://example.com", "https://another.com"],
    config=run_cfg
  )
  for r in results:
    print(r.url, ":", len(r.cleaned_html))

```

### 4.2 `start()` & `close()`
Allows manual lifecycle usage instead of context manager:
```
crawler = AsyncWebCrawler(config=browser_cfg)
await crawler.start()
# Perform multiple operations
resultA = await crawler.arun("https://exampleA.com", config=run_cfg)
resultB = await crawler.arun("https://exampleB.com", config=run_cfg)
await crawler.close()

```

## 5. `CrawlResult` Output
Each `arun()` returns a **`CrawlResult`**containing:
  * `url`: Final URL (if redirected).
  * `html`: Original HTML.
  * `cleaned_html`: Sanitized HTML.
  * `markdown_v2` (or future `markdown`): Markdown outputs (raw, fit, etc.).
  * `extracted_content`: If an extraction strategy was used (JSON for CSS/LLM strategies).
  * `screenshot`, `pdf`: If screenshots/PDF requested.
  * `media`, `links`: Information about discovered images/links.
  * `success`, `error_message`: Status info.


For details, see [CrawlResult doc](https://docs.crawl4ai.com/api/async-webcrawler/<../crawl-result/>).
## 6. Quick Example
Below is an example hooking it all together:
```
import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
import json
async def main():
  # 1. Browser config
  browser_cfg = BrowserConfig(
    browser_type="firefox",
    headless=False,
    verbose=True
  )
  # 2. Run config
  schema = {
    "name": "Articles",
    "baseSelector": "article.post",
    "fields": [
      {
        "name": "title", 
        "selector": "h2", 
        "type": "text"
      },
      {
        "name": "url", 
        "selector": "a", 
        "type": "attribute", 
        "attribute": "href"
      }
    ]
  }
  run_cfg = CrawlerRunConfig(
    cache_mode=CacheMode.BYPASS,
    extraction_strategy=JsonCssExtractionStrategy(schema),
    word_count_threshold=15,
    remove_overlay_elements=True,
    wait_for="css:.post" # Wait for posts to appear
  )
  async with AsyncWebCrawler(config=browser_cfg) as crawler:
    result = await crawler.arun(
      url="https://example.com/blog",
      config=run_cfg
    )
    if result.success:
      print("Cleaned HTML length:", len(result.cleaned_html))
      if result.extracted_content:
        articles = json.loads(result.extracted_content)
        print("Extracted articles:", articles[:2])
    else:
      print("Error:", result.error_message)
asyncio.run(main())

```

**Explanation** : - We define a **`BrowserConfig`**with Firefox, no headless, and`verbose=True`. - We define a **`CrawlerRunConfig`**that**bypasses cache** , uses a **CSS** extraction schema, has a `word_count_threshold=15`, etc. - We pass them to `AsyncWebCrawler(config=...)` and `arun(url=..., config=...)`.
## 7. Best Practices & Migration Notes
1. **Use** `BrowserConfig` for **global** settings about the browser’s environment. 2. **Use** `CrawlerRunConfig` for **per-crawl** logic (caching, content filtering, extraction strategies, wait conditions). 3. **Avoid** legacy parameters like `css_selector` or `word_count_threshold` directly in `arun()`. Instead:
```
run_cfg = CrawlerRunConfig(css_selector=".main-content", word_count_threshold=20)
result = await crawler.arun(url="...", config=run_cfg)

```

4. **Context Manager** usage is simplest unless you want a persistent crawler across many calls.
## 8. Summary
**AsyncWebCrawler** is your entry point to asynchronous crawling:
  * **Constructor** accepts **`BrowserConfig`**(or defaults).
  * **`arun(url, config=CrawlerRunConfig)`**is the main method for single-page crawls.
  * **`arun_many(urls, config=CrawlerRunConfig)`**handles concurrency across multiple URLs.
  * For advanced lifecycle control, use `start()` and `close()` explicitly. 


**Migration** : - If you used `AsyncWebCrawler(browser_type="chromium", css_selector="...")`, move browser settings to `BrowserConfig(...)` and content/crawl logic to `CrawlerRunConfig(...)`.
This modular approach ensures your code is **clean** , **scalable** , and **easy to maintain**. For any advanced or rarely used parameters, see the [BrowserConfig docs](https://docs.crawl4ai.com/api/async-webcrawler/<../parameters/>).
Site built with [MkDocs](https://docs.crawl4ai.com/api/async-webcrawler/<http:/www.mkdocs.org>) and [Terminal for MkDocs](https://docs.crawl4ai.com/api/async-webcrawler/<https:/github.com/ntno/mkdocs-terminal>). 
##### Search
xClose
Type to start searching


==================================================

# URL: https://docs.crawl4ai.com/api/crawl-result/

[Crawl4AI Documentation](https://docs.crawl4ai.com/api/crawl-result/<https:/docs.crawl4ai.com/>)
  * [ Home ](https://docs.crawl4ai.com/api/crawl-result/<../..>)
  * [ Quick Start ](https://docs.crawl4ai.com/api/crawl-result/core/quickstart/>)
  * [ Search ](https://docs.crawl4ai.com/api/crawl-result/<#>)


  * [Home](https://docs.crawl4ai.com/api/crawl-result/<../..>)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/api/crawl-result/core/installation/>)
    * [Docker Deployment](https://docs.crawl4ai.com/api/crawl-result/core/docker-deploymeny/>)
  * [Quick Start](https://docs.crawl4ai.com/api/crawl-result/core/quickstart/>)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/api/crawl-result/blog/>)
    * [Changelog](https://docs.crawl4ai.com/api/crawl-result/<https:/github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md>)
  * Core
    * [Simple Crawling](https://docs.crawl4ai.com/api/crawl-result/core/simple-crawling/>)
    * [Crawler Result](https://docs.crawl4ai.com/api/crawl-result/core/crawler-result/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/api/crawl-result/core/browser-crawler-config/>)
    * [Markdown Generation](https://docs.crawl4ai.com/api/crawl-result/core/markdown-generation/>)
    * [Fit Markdown](https://docs.crawl4ai.com/api/crawl-result/core/fit-markdown/>)
    * [Page Interaction](https://docs.crawl4ai.com/api/crawl-result/core/page-interaction/>)
    * [Content Selection](https://docs.crawl4ai.com/api/crawl-result/core/content-selection/>)
    * [Cache Modes](https://docs.crawl4ai.com/api/crawl-result/core/cache-modes/>)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/api/crawl-result/core/local-files/>)
    * [Link & Media](https://docs.crawl4ai.com/api/crawl-result/core/link-media/>)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/api/crawl-result/advanced/advanced-features/>)
    * [File Downloading](https://docs.crawl4ai.com/api/crawl-result/advanced/file-downloading/>)
    * [Lazy Loading](https://docs.crawl4ai.com/api/crawl-result/advanced/lazy-loading/>)
    * [Hooks & Auth](https://docs.crawl4ai.com/api/crawl-result/advanced/hooks-auth/>)
    * [Proxy & Security](https://docs.crawl4ai.com/api/crawl-result/advanced/proxy-security/>)
    * [Session Management](https://docs.crawl4ai.com/api/crawl-result/advanced/session-management/>)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/api/crawl-result/advanced/multi-url-crawling/>)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/api/crawl-result/advanced/crawl-dispatcher/>)
    * [Identity Based Crawling](https://docs.crawl4ai.com/api/crawl-result/advanced/identity-based-crawling/>)
    * [SSL Certificate](https://docs.crawl4ai.com/api/crawl-result/advanced/ssl-certificate/>)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/api/crawl-result/extraction/no-llm-strategies/>)
    * [LLM Strategies](https://docs.crawl4ai.com/api/crawl-result/extraction/llm-strategies/>)
    * [Clustering Strategies](https://docs.crawl4ai.com/api/crawl-result/extraction/clustring-strategies/>)
    * [Chunking](https://docs.crawl4ai.com/api/crawl-result/extraction/chunking/>)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/api/crawl-result/<../async-webcrawler/>)
    * [arun()](https://docs.crawl4ai.com/api/crawl-result/<../arun/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/api/crawl-result/<../parameters/>)
    * CrawlResult
    * [Strategies](https://docs.crawl4ai.com/api/crawl-result/<../strategies/>)


  * [CrawlResult Reference](https://docs.crawl4ai.com/api/crawl-result/<#crawlresult-reference>)
  * [1. Basic Crawl Info](https://docs.crawl4ai.com/api/crawl-result/<#1-basic-crawl-info>)
  * [2. Raw / Cleaned Content](https://docs.crawl4ai.com/api/crawl-result/<#2-raw-cleaned-content>)
  * [3. Markdown Fields](https://docs.crawl4ai.com/api/crawl-result/<#3-markdown-fields>)
  * [4. Media & Links](https://docs.crawl4ai.com/api/crawl-result/<#4-media-links>)
  * [5. Additional Fields](https://docs.crawl4ai.com/api/crawl-result/<#5-additional-fields>)
  * [6. Example: Accessing Everything](https://docs.crawl4ai.com/api/crawl-result/<#6-example-accessing-everything>)
  * [7. Key Points & Future](https://docs.crawl4ai.com/api/crawl-result/<#7-key-points-future>)


# `CrawlResult` Reference
The **`CrawlResult`**class encapsulates everything returned after a single crawl operation. It provides the**raw or processed content** , details on links and media, plus optional metadata (like screenshots, PDFs, or extracted JSON).
**Location** : `crawl4ai/crawler/models.py` (for reference)
```
class CrawlResult(BaseModel):
  url: str
  html: str
  success: bool
  cleaned_html: Optional[str] = None
  media: Dict[str, List[Dict]] = {}
  links: Dict[str, List[Dict]] = {}
  downloaded_files: Optional[List[str]] = None
  screenshot: Optional[str] = None
  pdf : Optional[bytes] = None
  markdown: Optional[Union[str, MarkdownGenerationResult]] = None
  markdown_v2: Optional[MarkdownGenerationResult] = None
  fit_markdown: Optional[str] = None
  fit_html: Optional[str] = None
  extracted_content: Optional[str] = None
  metadata: Optional[dict] = None
  error_message: Optional[str] = None
  session_id: Optional[str] = None
  response_headers: Optional[dict] = None
  status_code: Optional[int] = None
  ssl_certificate: Optional[SSLCertificate] = None
  ...

```

Below is a **field-by-field** explanation and possible usage patterns.
## 1. Basic Crawl Info
### 1.1 **`url`**_(str)_
**What** : The final crawled URL (after any redirects). **Usage** : 
```
print(result.url) # e.g., "https://example.com/"

```

### 1.2 **`success`**_(bool)_
**What** : `True` if the crawl pipeline ended without major errors; `False` otherwise. **Usage** : 
```
if not result.success:
  print(f"Crawl failed: {result.error_message}")

```

### 1.3 **`status_code`**_(Optional[int])_
**What** : The page’s HTTP status code (e.g., 200, 404). **Usage** : 
```
if result.status_code == 404:
  print("Page not found!")

```

### 1.4 **`error_message`**_(Optional[str])_
**What** : If `success=False`, a textual description of the failure. **Usage** : 
```
if not result.success:
  print("Error:", result.error_message)

```

### 1.5 **`session_id`**_(Optional[str])_
**What** : The ID used for reusing a browser context across multiple calls. **Usage** : 
```
# If you used session_id="login_session" in CrawlerRunConfig, see it here:
print("Session:", result.session_id)

```

### 1.6 **`response_headers`**_(Optional[dict])_
**What** : Final HTTP response headers. **Usage** : 
```
if result.response_headers:
  print("Server:", result.response_headers.get("Server", "Unknown"))

```

### 1.7 **`ssl_certificate`**_(Optional[SSLCertificate])_
**What** : If `fetch_ssl_certificate=True` in your CrawlerRunConfig, **`result.ssl_certificate`**contains a[**`SSLCertificate`**](https://docs.crawl4ai.com/api/crawl-result/advanced/ssl-certificate/>)object describing the site’s certificate. You can export the cert in multiple formats (PEM/DER/JSON) or access its properties like`issuer`, `subject`, `valid_from`, `valid_until`, etc. **Usage** : 
```
if result.ssl_certificate:
  print("Issuer:", result.ssl_certificate.issuer)

```

## 2. Raw / Cleaned Content
### 2.1 **`html`**_(str)_
**What** : The **original** unmodified HTML from the final page load. **Usage** : 
```
# Possibly large
print(len(result.html))

```

### 2.2 **`cleaned_html`**_(Optional[str])_
**What** : A sanitized HTML version—scripts, styles, or excluded tags are removed based on your `CrawlerRunConfig`. **Usage** : 
```
print(result.cleaned_html[:500]) # Show a snippet

```

### 2.3 **`fit_html`**_(Optional[str])_
**What** : If a **content filter** or heuristic (e.g., Pruning/BM25) modifies the HTML, the “fit” or post-filter version. **When** : This is **only** present if your `markdown_generator` or `content_filter` produces it. **Usage** : 
```
if result.fit_html:
  print("High-value HTML content:", result.fit_html[:300])

```

## 3. Markdown Fields
### 3.1 The Markdown Generation Approach
Crawl4AI can convert HTML→Markdown, optionally including:
  * **Raw** markdown 
  * **Links as citations** (with a references section) 
  * **Fit** markdown if a **content filter** is used (like Pruning or BM25)


### 3.2 **`markdown_v2`**_(Optional[MarkdownGenerationResult])_
**What** : The **structured** object holding multiple markdown variants. Soon to be consolidated into `markdown`. 
**`MarkdownGenerationResult`**includes: -**`raw_markdown`**_(str)_ : The full HTML→Markdown conversion. - **`markdown_with_citations`**_(str)_ : Same markdown, but with link references as academic-style citations. - **`references_markdown`**_(str)_ : The reference list or footnotes at the end. - **`fit_markdown`**_(Optional[str])_ : If content filtering (Pruning/BM25) was applied, the filtered “fit” text. - **`fit_html`**_(Optional[str])_ : The HTML that led to `fit_markdown`.
**Usage** : 
```
if result.markdown_v2:
  md_res = result.markdown_v2
  print("Raw MD:", md_res.raw_markdown[:300])
  print("Citations MD:", md_res.markdown_with_citations[:300])
  print("References:", md_res.references_markdown)
  if md_res.fit_markdown:
    print("Pruned text:", md_res.fit_markdown[:300])

```

### 3.3 **`markdown`**_(Optional[Union[str, MarkdownGenerationResult]])_
**What** : In future versions, `markdown` will fully replace `markdown_v2`. Right now, it might be a `str` or a `MarkdownGenerationResult`. **Usage** : 
```
# Soon, you might see:
if isinstance(result.markdown, MarkdownGenerationResult):
  print(result.markdown.raw_markdown[:200])
else:
  print(result.markdown)

```

### 3.4 **`fit_markdown`**_(Optional[str])_
**What** : A direct reference to the final filtered markdown (legacy approach). **When** : This is set if a filter or content strategy explicitly writes there. Usually overshadowed by `markdown_v2.fit_markdown`. **Usage** : 
```
print(result.fit_markdown) # Legacy field, prefer result.markdown_v2.fit_markdown

```

**Important** : “Fit” content (in `fit_markdown`/`fit_html`) only exists if you used a **filter** (like **PruningContentFilter** or **BM25ContentFilter**) within a `MarkdownGenerationStrategy`.
## 4. Media & Links
### 4.1 **`media`**_(Dict[str, List[Dict]])_
**What** : Contains info about discovered images, videos, or audio. Typically keys: `"images"`, `"videos"`, `"audios"`. **Common Fields** in each item:
  * `src` _(str)_ : Media URL 
  * `alt` or `title` _(str)_ : Descriptive text 
  * `score` _(float)_ : Relevance score if the crawler’s heuristic found it “important” 
  * `desc` or `description` _(Optional[str])_ : Additional context extracted from surrounding text 


**Usage** : 
```
images = result.media.get("images", [])
for img in images:
  if img.get("score", 0) > 5:
    print("High-value image:", img["src"])

```

### 4.2 **`links`**_(Dict[str, List[Dict]])_
**What** : Holds internal and external link data. Usually two keys: `"internal"` and `"external"`. **Common Fields** :
  * `href` _(str)_ : The link target 
  * `text` _(str)_ : Link text 
  * `title` _(str)_ : Title attribute 
  * `context` _(str)_ : Surrounding text snippet 
  * `domain` _(str)_ : If external, the domain


**Usage** : 
```
for link in result.links["internal"]:
  print(f"Internal link to {link['href']} with text {link['text']}")

```

## 5. Additional Fields
### 5.1 **`extracted_content`**_(Optional[str])_
**What** : If you used **`extraction_strategy`**(CSS, LLM, etc.), the structured output (JSON).**Usage** : 
```
if result.extracted_content:
  data = json.loads(result.extracted_content)
  print(data)

```

### 5.2 **`downloaded_files`**_(Optional[List[str]])_
**What** : If `accept_downloads=True` in your `BrowserConfig` + `downloads_path`, lists local file paths for downloaded items. **Usage** : 
```
if result.downloaded_files:
  for file_path in result.downloaded_files:
    print("Downloaded:", file_path)

```

### 5.3 **`screenshot`**_(Optional[str])_
**What** : Base64-encoded screenshot if `screenshot=True` in `CrawlerRunConfig`. **Usage** : 
```
import base64
if result.screenshot:
  with open("page.png", "wb") as f:
    f.write(base64.b64decode(result.screenshot))

```

### 5.4 **`pdf`**_(Optional[bytes])_
**What** : Raw PDF bytes if `pdf=True` in `CrawlerRunConfig`. **Usage** : 
```
if result.pdf:
  with open("page.pdf", "wb") as f:
    f.write(result.pdf)

```

### 5.5 **`metadata`**_(Optional[dict])_
**What** : Page-level metadata if discovered (title, description, OG data, etc.). **Usage** : 
```
if result.metadata:
  print("Title:", result.metadata.get("title"))
  print("Author:", result.metadata.get("author"))

```

## 6. Example: Accessing Everything
```
async def handle_result(result: CrawlResult):
  if not result.success:
    print("Crawl error:", result.error_message)
    return
  # Basic info
  print("Crawled URL:", result.url)
  print("Status code:", result.status_code)
  # HTML
  print("Original HTML size:", len(result.html))
  print("Cleaned HTML size:", len(result.cleaned_html or ""))
  # Markdown output
  if result.markdown_v2:
    print("Raw Markdown:", result.markdown_v2.raw_markdown[:300])
    print("Citations Markdown:", result.markdown_v2.markdown_with_citations[:300])
    if result.markdown_v2.fit_markdown:
      print("Fit Markdown:", result.markdown_v2.fit_markdown[:200])
  else:
    print("Raw Markdown (legacy):", result.markdown[:200] if result.markdown else "N/A")
  # Media & Links
  if "images" in result.media:
    print("Image count:", len(result.media["images"]))
  if "internal" in result.links:
    print("Internal link count:", len(result.links["internal"]))
  # Extraction strategy result
  if result.extracted_content:
    print("Structured data:", result.extracted_content)
  # Screenshot/PDF
  if result.screenshot:
    print("Screenshot length:", len(result.screenshot))
  if result.pdf:
    print("PDF bytes length:", len(result.pdf))

```

## 7. Key Points & Future
1. **`markdown_v2`vs`markdown`** - Right now, `markdown_v2` is the more robust container (`MarkdownGenerationResult`), providing **raw_markdown** , **markdown_with_citations** , references, plus possible **fit_markdown**. - In future versions, everything will unify under **`markdown`**. If you rely on advanced features (citations, fit content), check`markdown_v2`.
2. **Fit Content** - **`fit_markdown`**and**`fit_html`**appear only if you used a content filter (like**PruningContentFilter** or **BM25ContentFilter**) inside your **MarkdownGenerationStrategy** or set them directly. - If no filter is used, they remain `None`.
3. **References & Citations** - If you enable link citations in your `DefaultMarkdownGenerator` (`options={"citations": True}`), you’ll see `markdown_with_citations` plus a **`references_markdown`**block. This helps large language models or academic-like referencing.
4. **Links & Media** - `links["internal"]` and `links["external"]` group discovered anchors by domain. - `media["images"]` / `["videos"]` / `["audios"]` store extracted media elements with optional scoring or context.
5. **Error Cases** - If `success=False`, check `error_message` (e.g., timeouts, invalid URLs). - `status_code` might be `None` if we failed before an HTTP response.
Use **`CrawlResult`**to glean all final outputs and feed them into your data pipelines, AI models, or archives. With the synergy of a properly configured**BrowserConfig** and **CrawlerRunConfig** , the crawler can produce robust, structured results here in **`CrawlResult`**.
Site built with [MkDocs](https://docs.crawl4ai.com/api/crawl-result/<http:/www.mkdocs.org>) and [Terminal for MkDocs](https://docs.crawl4ai.com/api/crawl-result/<https:/github.com/ntno/mkdocs-terminal>). 
##### Search
xClose
Type to start searching


==================================================

# URL: https://docs.crawl4ai.com/api/parameters/

[Crawl4AI Documentation](https://docs.crawl4ai.com/api/parameters/<https:/docs.crawl4ai.com/>)
  * [ Home ](https://docs.crawl4ai.com/api/parameters/<../..>)
  * [ Quick Start ](https://docs.crawl4ai.com/api/parameters/core/quickstart/>)
  * [ Search ](https://docs.crawl4ai.com/api/parameters/<#>)


  * [Home](https://docs.crawl4ai.com/api/parameters/<../..>)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/api/parameters/core/installation/>)
    * [Docker Deployment](https://docs.crawl4ai.com/api/parameters/core/docker-deploymeny/>)
  * [Quick Start](https://docs.crawl4ai.com/api/parameters/core/quickstart/>)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/api/parameters/blog/>)
    * [Changelog](https://docs.crawl4ai.com/api/parameters/<https:/github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md>)
  * Core
    * [Simple Crawling](https://docs.crawl4ai.com/api/parameters/core/simple-crawling/>)
    * [Crawler Result](https://docs.crawl4ai.com/api/parameters/core/crawler-result/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/api/parameters/core/browser-crawler-config/>)
    * [Markdown Generation](https://docs.crawl4ai.com/api/parameters/core/markdown-generation/>)
    * [Fit Markdown](https://docs.crawl4ai.com/api/parameters/core/fit-markdown/>)
    * [Page Interaction](https://docs.crawl4ai.com/api/parameters/core/page-interaction/>)
    * [Content Selection](https://docs.crawl4ai.com/api/parameters/core/content-selection/>)
    * [Cache Modes](https://docs.crawl4ai.com/api/parameters/core/cache-modes/>)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/api/parameters/core/local-files/>)
    * [Link & Media](https://docs.crawl4ai.com/api/parameters/core/link-media/>)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/api/parameters/advanced/advanced-features/>)
    * [File Downloading](https://docs.crawl4ai.com/api/parameters/advanced/file-downloading/>)
    * [Lazy Loading](https://docs.crawl4ai.com/api/parameters/advanced/lazy-loading/>)
    * [Hooks & Auth](https://docs.crawl4ai.com/api/parameters/advanced/hooks-auth/>)
    * [Proxy & Security](https://docs.crawl4ai.com/api/parameters/advanced/proxy-security/>)
    * [Session Management](https://docs.crawl4ai.com/api/parameters/advanced/session-management/>)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/api/parameters/advanced/multi-url-crawling/>)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/api/parameters/advanced/crawl-dispatcher/>)
    * [Identity Based Crawling](https://docs.crawl4ai.com/api/parameters/advanced/identity-based-crawling/>)
    * [SSL Certificate](https://docs.crawl4ai.com/api/parameters/advanced/ssl-certificate/>)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/api/parameters/extraction/no-llm-strategies/>)
    * [LLM Strategies](https://docs.crawl4ai.com/api/parameters/extraction/llm-strategies/>)
    * [Clustering Strategies](https://docs.crawl4ai.com/api/parameters/extraction/clustring-strategies/>)
    * [Chunking](https://docs.crawl4ai.com/api/parameters/extraction/chunking/>)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/api/parameters/<../async-webcrawler/>)
    * [arun()](https://docs.crawl4ai.com/api/parameters/<../arun/>)
    * Browser & Crawler Config
    * [CrawlResult](https://docs.crawl4ai.com/api/parameters/<../crawl-result/>)
    * [Strategies](https://docs.crawl4ai.com/api/parameters/<../strategies/>)


  * [1. BrowserConfig – Controlling the Browser](https://docs.crawl4ai.com/api/parameters/<#1-browserconfig-controlling-the-browser>)
  * [1.1 Parameter Highlights](https://docs.crawl4ai.com/api/parameters/<#11-parameter-highlights>)
  * [2. CrawlerRunConfig – Controlling Each Crawl](https://docs.crawl4ai.com/api/parameters/<#2-crawlerrunconfig-controlling-each-crawl>)
  * [2.1 Parameter Highlights](https://docs.crawl4ai.com/api/parameters/<#21-parameter-highlights>)
  * [2.2 Example Usage](https://docs.crawl4ai.com/api/parameters/<#22-example-usage>)
  * [3. Putting It All Together](https://docs.crawl4ai.com/api/parameters/<#3-putting-it-all-together>)


# 1. **BrowserConfig** – Controlling the Browser
`BrowserConfig` focuses on **how** the browser is launched and behaves. This includes headless mode, proxies, user agents, and other environment tweaks.
```
from crawl4ai import AsyncWebCrawler, BrowserConfig
browser_cfg = BrowserConfig(
  browser_type="chromium",
  headless=True,
  viewport_width=1280,
  viewport_height=720,
  proxy="http://user:pass@proxy:8080",
  user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/116.0.0.0 Safari/537.36",
)

```

## 1.1 Parameter Highlights
**Parameter** | **Type / Default** | **What It Does**  
---|---|---  
**`browser_type`**| `"chromium"` , `"firefox"`, `"webkit"`_(default:`"chromium"`)_ | Which browser engine to use. `"chromium"` is typical for many sites, `"firefox"` or `"webkit"` for specialized tests.  
**`headless`**| `bool` (default: `True`) | Headless means no visible UI. `False` is handy for debugging.  
**`viewport_width`**| `int` (default: `1080`) | Initial page width (in px). Useful for testing responsive layouts.  
**`viewport_height`**| `int` (default: `600`) | Initial page height (in px).  
**`proxy`**| `str` (default: `None`) | Single-proxy URL if you want all traffic to go through it, e.g. `"http://user:pass@proxy:8080"`.  
**`proxy_config`**| `dict` (default: `None`) | For advanced or multi-proxy needs, specify details like `{"server": "...", "username": "...", ...}`.  
**`use_persistent_context`**| `bool` (default: `False`) | If `True`, uses a **persistent** browser context (keep cookies, sessions across runs). Also sets `use_managed_browser=True`.  
**`user_data_dir`**| `str or None` (default: `None`) | Directory to store user data (profiles, cookies). Must be set if you want permanent sessions.  
**`ignore_https_errors`**| `bool` (default: `True`) | If `True`, continues despite invalid certificates (common in dev/staging).  
**`java_script_enabled`**| `bool` (default: `True`) | Disable if you want no JS overhead, or if only static content is needed.  
**`cookies`**| `list` (default: `[]`) | Pre-set cookies, each a dict like `{"name": "session", "value": "...", "url": "..."}`.  
**`headers`**| `dict` (default: `{}`) | Extra HTTP headers for every request, e.g. `{"Accept-Language": "en-US"}`.  
**`user_agent`**| `str` (default: Chrome-based UA) | Your custom or random user agent. `user_agent_mode="random"` can shuffle it.  
**`light_mode`**| `bool` (default: `False`) | Disables some background features for performance gains.  
**`text_mode`**| `bool` (default: `False`) | If `True`, tries to disable images/other heavy content for speed.  
**`use_managed_browser`**| `bool` (default: `False`) | For advanced “managed” interactions (debugging, CDP usage). Typically set automatically if persistent context is on.  
**`extra_args`**| `list` (default: `[]`) | Additional flags for the underlying browser process, e.g. `["--disable-extensions"]`.  
**Tips** : - Set `headless=False` to visually **debug** how pages load or how interactions proceed. - If you need **authentication** storage or repeated sessions, consider `use_persistent_context=True` and specify `user_data_dir`. - For large pages, you might need a bigger `viewport_width` and `viewport_height` to handle dynamic content.
# 2. **CrawlerRunConfig** – Controlling Each Crawl
While `BrowserConfig` sets up the **environment** , `CrawlerRunConfig` details **how** each **crawl operation** should behave: caching, content filtering, link or domain blocking, timeouts, JavaScript code, etc.
```
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
run_cfg = CrawlerRunConfig(
  wait_for="css:.main-content",
  word_count_threshold=15,
  excluded_tags=["nav", "footer"],
  exclude_external_links=True,
)

```

## 2.1 Parameter Highlights
We group them by category. 
### A) **Content Processing**
**Parameter** | **Type / Default** | **What It Does**  
---|---|---  
**`word_count_threshold`**| `int` (default: ~200) | Skips text blocks below X words. Helps ignore trivial sections.  
**`extraction_strategy`**| `ExtractionStrategy` (default: None) | If set, extracts structured data (CSS-based, LLM-based, etc.).  
**`markdown_generator`**| `MarkdownGenerationStrategy` (None) | If you want specialized markdown output (citations, filtering, chunking, etc.).  
**`content_filter`**| `RelevantContentFilter` (None) | Filters out irrelevant text blocks. E.g., `PruningContentFilter` or `BM25ContentFilter`.  
**`css_selector`**| `str` (None) | Retains only the part of the page matching this selector.  
**`excluded_tags`**| `list` (None) | Removes entire tags (e.g. `["script", "style"]`).  
**`excluded_selector`**| `str` (None) | Like `css_selector` but to exclude. E.g. `"#ads, .tracker"`.  
**`only_text`**| `bool` (False) | If `True`, tries to extract text-only content.  
**`prettiify`**| `bool` (False) | If `True`, beautifies final HTML (slower, purely cosmetic).  
**`keep_data_attributes`**| `bool` (False) | If `True`, preserve `data-*` attributes in cleaned HTML.  
**`remove_forms`**| `bool` (False) | If `True`, remove all `<form>` elements.  
### B) **Caching & Session**
**Parameter** | **Type / Default** | **What It Does**  
---|---|---  
**`cache_mode`**| `CacheMode or None` | Controls how caching is handled (`ENABLED`, `BYPASS`, `DISABLED`, etc.). If `None`, typically defaults to `ENABLED`.  
**`session_id`**| `str or None` | Assign a unique ID to reuse a single browser session across multiple `arun()` calls.  
**`bypass_cache`**| `bool` (False) | If `True`, acts like `CacheMode.BYPASS`.  
**`disable_cache`**| `bool` (False) | If `True`, acts like `CacheMode.DISABLED`.  
**`no_cache_read`**| `bool` (False) | If `True`, acts like `CacheMode.WRITE_ONLY` (writes cache but never reads).  
**`no_cache_write`**| `bool` (False) | If `True`, acts like `CacheMode.READ_ONLY` (reads cache but never writes).  
Use these for controlling whether you read or write from a local content cache. Handy for large batch crawls or repeated site visits.
### C) **Page Navigation & Timing**
**Parameter** | **Type / Default** | **What It Does**  
---|---|---  
**`wait_until`**| `str` (domcontentloaded) | Condition for navigation to “complete”. Often `"networkidle"` or `"domcontentloaded"`.  
**`page_timeout`**| `int` (60000 ms) | Timeout for page navigation or JS steps. Increase for slow sites.  
**`wait_for`**| `str or None` | Wait for a CSS (`"css:selector"`) or JS (`"js:() => bool"`) condition before content extraction.  
**`wait_for_images`**| `bool` (False) | Wait for images to load before finishing. Slows down if you only want text.  
**`delay_before_return_html`**| `float` (0.1) | Additional pause (seconds) before final HTML is captured. Good for last-second updates.  
**`mean_delay`**and**`max_range`**| `float` (0.1, 0.3) | If you call `arun_many()`, these define random delay intervals between crawls, helping avoid detection or rate limits.  
**`semaphore_count`**| `int` (5) | Max concurrency for `arun_many()`. Increase if you have resources for parallel crawls.  
### D) **Page Interaction**
**Parameter** | **Type / Default** | **What It Does**  
---|---|---  
**`js_code`**| `str or list[str]` (None) | JavaScript to run after load. E.g. `"document.querySelector('button')?.click();"`.  
**`js_only`**| `bool` (False) | If `True`, indicates we’re reusing an existing session and only applying JS. No full reload.  
**`ignore_body_visibility`**| `bool` (True) | Skip checking if `<body>` is visible. Usually best to keep `True`.  
**`scan_full_page`**| `bool` (False) | If `True`, auto-scroll the page to load dynamic content (infinite scroll).  
**`scroll_delay`**| `float` (0.2) | Delay between scroll steps if `scan_full_page=True`.  
**`process_iframes`**| `bool` (False) | Inlines iframe content for single-page extraction.  
**`remove_overlay_elements`**| `bool` (False) | Removes potential modals/popups blocking the main content.  
**`simulate_user`**| `bool` (False) | Simulate user interactions (mouse movements) to avoid bot detection.  
**`override_navigator`**| `bool` (False) | Override `navigator` properties in JS for stealth.  
**`magic`**| `bool` (False) | Automatic handling of popups/consent banners. Experimental.  
**`adjust_viewport_to_content`**| `bool` (False) | Resizes viewport to match page content height.  
If your page is a single-page app with repeated JS updates, set `js_only=True` in subsequent calls, plus a `session_id` for reusing the same tab.
### E) **Media Handling**
**Parameter** | **Type / Default** | **What It Does**  
---|---|---  
**`screenshot`**| `bool` (False) | Capture a screenshot (base64) in `result.screenshot`.  
**`screenshot_wait_for`**| `float or None` | Extra wait time before the screenshot.  
**`screenshot_height_threshold`**| `int` (~20000) | If the page is taller than this, alternate screenshot strategies are used.  
**`pdf`**| `bool` (False) | If `True`, returns a PDF in `result.pdf`.  
**`image_description_min_word_threshold`**| `int` (~50) | Minimum words for an image’s alt text or description to be considered valid.  
**`image_score_threshold`**| `int` (~3) | Filter out low-scoring images. The crawler scores images by relevance (size, context, etc.).  
**`exclude_external_images`**| `bool` (False) | Exclude images from other domains.  
### F) **Link/Domain Handling**
**Parameter** | **Type / Default** | **What It Does**  
---|---|---  
**`exclude_social_media_domains`**| `list` (e.g. Facebook/Twitter) | A default list can be extended. Any link to these domains is removed from final output.  
**`exclude_external_links`**| `bool` (False) | Removes all links pointing outside the current domain.  
**`exclude_social_media_links`**| `bool` (False) | Strips links specifically to social sites (like Facebook or Twitter).  
**`exclude_domains`**| `list` ([]) | Provide a custom list of domains to exclude (like `["ads.com", "trackers.io"]`).  
Use these for link-level content filtering (often to keep crawls “internal” or to remove spammy domains).
### G) **Debug & Logging**
**Parameter** | **Type / Default** | **What It Does**  
---|---|---  
**`verbose`**| `bool` (True) | Prints logs detailing each step of crawling, interactions, or errors.  
**`log_console`**| `bool` (False) | Logs the page’s JavaScript console output if you want deeper JS debugging.  
## 2.2 Example Usage
```
import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
async def main():
  # Configure the browser
  browser_cfg = BrowserConfig(
    headless=False,
    viewport_width=1280,
    viewport_height=720,
    proxy="http://user:pass@myproxy:8080",
    text_mode=True
  )
  # Configure the run
  run_cfg = CrawlerRunConfig(
    cache_mode=CacheMode.BYPASS,
    session_id="my_session",
    css_selector="main.article",
    excluded_tags=["script", "style"],
    exclude_external_links=True,
    wait_for="css:.article-loaded",
    screenshot=True
  )
  async with AsyncWebCrawler(config=browser_cfg) as crawler:
    result = await crawler.arun(
      url="https://example.com/news",
      config=run_cfg
    )
    if result.success:
      print("Final cleaned_html length:", len(result.cleaned_html))
      if result.screenshot:
        print("Screenshot captured (base64, length):", len(result.screenshot))
    else:
      print("Crawl failed:", result.error_message)
if __name__ == "__main__":
  asyncio.run(main())

```

**What’s Happening** : - **`text_mode=True`**avoids loading images and other heavy resources, speeding up the crawl. - We disable caching (`cache_mode=CacheMode.BYPASS`) to always fetch fresh content. - We only keep `main.article` content by specifying `css_selector="main.article"`. - We exclude external links (`exclude_external_links=True`). - We do a quick screenshot (`screenshot=True`) before finishing.
## 3. Putting It All Together
  * **Use** `BrowserConfig` for **global** browser settings: engine, headless, proxy, user agent. 
  * **Use** `CrawlerRunConfig` for each crawl’s **context** : how to filter content, handle caching, wait for dynamic elements, or run JS. 
  * **Pass** both configs to `AsyncWebCrawler` (the `BrowserConfig`) and then to `arun()` (the `CrawlerRunConfig`). 


Site built with [MkDocs](https://docs.crawl4ai.com/api/parameters/<http:/www.mkdocs.org>) and [Terminal for MkDocs](https://docs.crawl4ai.com/api/parameters/<https:/github.com/ntno/mkdocs-terminal>). 
##### Search
xClose
Type to start searching


==================================================

# URL: https://docs.crawl4ai.com/api/strategies/

[Crawl4AI Documentation](https://docs.crawl4ai.com/api/strategies/<https:/docs.crawl4ai.com/>)
  * [ Home ](https://docs.crawl4ai.com/api/strategies/<../..>)
  * [ Quick Start ](https://docs.crawl4ai.com/api/strategies/core/quickstart/>)
  * [ Search ](https://docs.crawl4ai.com/api/strategies/<#>)


  * [Home](https://docs.crawl4ai.com/api/strategies/<../..>)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/api/strategies/core/installation/>)
    * [Docker Deployment](https://docs.crawl4ai.com/api/strategies/core/docker-deploymeny/>)
  * [Quick Start](https://docs.crawl4ai.com/api/strategies/core/quickstart/>)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/api/strategies/blog/>)
    * [Changelog](https://docs.crawl4ai.com/api/strategies/<https:/github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md>)
  * Core
    * [Simple Crawling](https://docs.crawl4ai.com/api/strategies/core/simple-crawling/>)
    * [Crawler Result](https://docs.crawl4ai.com/api/strategies/core/crawler-result/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/api/strategies/core/browser-crawler-config/>)
    * [Markdown Generation](https://docs.crawl4ai.com/api/strategies/core/markdown-generation/>)
    * [Fit Markdown](https://docs.crawl4ai.com/api/strategies/core/fit-markdown/>)
    * [Page Interaction](https://docs.crawl4ai.com/api/strategies/core/page-interaction/>)
    * [Content Selection](https://docs.crawl4ai.com/api/strategies/core/content-selection/>)
    * [Cache Modes](https://docs.crawl4ai.com/api/strategies/core/cache-modes/>)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/api/strategies/core/local-files/>)
    * [Link & Media](https://docs.crawl4ai.com/api/strategies/core/link-media/>)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/api/strategies/advanced/advanced-features/>)
    * [File Downloading](https://docs.crawl4ai.com/api/strategies/advanced/file-downloading/>)
    * [Lazy Loading](https://docs.crawl4ai.com/api/strategies/advanced/lazy-loading/>)
    * [Hooks & Auth](https://docs.crawl4ai.com/api/strategies/advanced/hooks-auth/>)
    * [Proxy & Security](https://docs.crawl4ai.com/api/strategies/advanced/proxy-security/>)
    * [Session Management](https://docs.crawl4ai.com/api/strategies/advanced/session-management/>)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/api/strategies/advanced/multi-url-crawling/>)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/api/strategies/advanced/crawl-dispatcher/>)
    * [Identity Based Crawling](https://docs.crawl4ai.com/api/strategies/advanced/identity-based-crawling/>)
    * [SSL Certificate](https://docs.crawl4ai.com/api/strategies/advanced/ssl-certificate/>)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/api/strategies/extraction/no-llm-strategies/>)
    * [LLM Strategies](https://docs.crawl4ai.com/api/strategies/extraction/llm-strategies/>)
    * [Clustering Strategies](https://docs.crawl4ai.com/api/strategies/extraction/clustring-strategies/>)
    * [Chunking](https://docs.crawl4ai.com/api/strategies/extraction/chunking/>)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/api/strategies/<../async-webcrawler/>)
    * [arun()](https://docs.crawl4ai.com/api/strategies/<../arun/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/api/strategies/<../parameters/>)
    * [CrawlResult](https://docs.crawl4ai.com/api/strategies/<../crawl-result/>)
    * Strategies


  * [Extraction & Chunking Strategies API](https://docs.crawl4ai.com/api/strategies/<#extraction-chunking-strategies-api>)
  * [Extraction Strategies](https://docs.crawl4ai.com/api/strategies/<#extraction-strategies>)
  * [Chunking Strategies](https://docs.crawl4ai.com/api/strategies/<#chunking-strategies>)
  * [Usage Examples](https://docs.crawl4ai.com/api/strategies/<#usage-examples>)
  * [Best Practices](https://docs.crawl4ai.com/api/strategies/<#best-practices>)


# Extraction & Chunking Strategies API
This documentation covers the API reference for extraction and chunking strategies in Crawl4AI.
## Extraction Strategies
All extraction strategies inherit from the base `ExtractionStrategy` class and implement two key methods: - `extract(url: str, html: str) -> List[Dict[str, Any]]` - `run(url: str, sections: List[str]) -> List[Dict[str, Any]]`
### LLMExtractionStrategy
Used for extracting structured data using Language Models.
```
LLMExtractionStrategy(
  # Required Parameters
  provider: str = DEFAULT_PROVIDER,   # LLM provider (e.g., "ollama/llama2")
  api_token: Optional[str] = None,   # API token
  # Extraction Configuration
  instruction: str = None,       # Custom extraction instruction
  schema: Dict = None,         # Pydantic model schema for structured data
  extraction_type: str = "block",    # "block" or "schema"
  # Chunking Parameters
  chunk_token_threshold: int = 4000,  # Maximum tokens per chunk
  overlap_rate: float = 0.1,      # Overlap between chunks
  word_token_rate: float = 0.75,    # Word to token conversion rate
  apply_chunking: bool = True,     # Enable/disable chunking
  # API Configuration
  base_url: str = None,        # Base URL for API
  extra_args: Dict = {},        # Additional provider arguments
  verbose: bool = False        # Enable verbose logging
)

```

### CosineStrategy
Used for content similarity-based extraction and clustering.
```
CosineStrategy(
  # Content Filtering
  semantic_filter: str = None,    # Topic/keyword filter
  word_count_threshold: int = 10,   # Minimum words per cluster
  sim_threshold: float = 0.3,     # Similarity threshold
  # Clustering Parameters
  max_dist: float = 0.2,       # Maximum cluster distance
  linkage_method: str = 'ward',    # Clustering method
  top_k: int = 3,          # Top clusters to return
  # Model Configuration
  model_name: str = 'sentence-transformers/all-MiniLM-L6-v2', # Embedding model
  verbose: bool = False       # Enable verbose logging
)

```

### JsonCssExtractionStrategy
Used for CSS selector-based structured data extraction.
```
JsonCssExtractionStrategy(
  schema: Dict[str, Any],  # Extraction schema
  verbose: bool = False   # Enable verbose logging
)
# Schema Structure
schema = {
  "name": str,       # Schema name
  "baseSelector": str,   # Base CSS selector
  "fields": [        # List of fields to extract
    {
      "name": str,   # Field name
      "selector": str, # CSS selector
      "type": str,   # Field type: "text", "attribute", "html", "regex"
      "attribute": str, # For type="attribute"
      "pattern": str, # For type="regex"
      "transform": str, # Optional: "lowercase", "uppercase", "strip"
      "default": Any  # Default value if extraction fails
    }
  ]
}

```

## Chunking Strategies
All chunking strategies inherit from `ChunkingStrategy` and implement the `chunk(text: str) -> list` method.
### RegexChunking
Splits text based on regex patterns.
```
RegexChunking(
  patterns: List[str] = None # Regex patterns for splitting
                # Default: [r'\n\n']
)

```

### SlidingWindowChunking
Creates overlapping chunks with a sliding window approach.
```
SlidingWindowChunking(
  window_size: int = 100,  # Window size in words
  step: int = 50       # Step size between windows
)

```

### OverlappingWindowChunking
Creates chunks with specified overlap.
```
OverlappingWindowChunking(
  window_size: int = 1000,  # Chunk size in words
  overlap: int = 100     # Overlap size in words
)

```

## Usage Examples
### LLM Extraction
```
from pydantic import BaseModel
from crawl4ai.extraction_strategy import LLMExtractionStrategy
# Define schema
class Article(BaseModel):
  title: str
  content: str
  author: str
# Create strategy
strategy = LLMExtractionStrategy(
  provider="ollama/llama2",
  schema=Article.schema(),
  instruction="Extract article details"
)
# Use with crawler
result = await crawler.arun(
  url="https://example.com/article",
  extraction_strategy=strategy
)
# Access extracted data
data = json.loads(result.extracted_content)

```

### CSS Extraction
```
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
# Define schema
schema = {
  "name": "Product List",
  "baseSelector": ".product-card",
  "fields": [
    {
      "name": "title",
      "selector": "h2.title",
      "type": "text"
    },
    {
      "name": "price",
      "selector": ".price",
      "type": "text",
      "transform": "strip"
    },
    {
      "name": "image",
      "selector": "img",
      "type": "attribute",
      "attribute": "src"
    }
  ]
}
# Create and use strategy
strategy = JsonCssExtractionStrategy(schema)
result = await crawler.arun(
  url="https://example.com/products",
  extraction_strategy=strategy
)

```

### Content Chunking
```
from crawl4ai.chunking_strategy import OverlappingWindowChunking
# Create chunking strategy
chunker = OverlappingWindowChunking(
  window_size=500, # 500 words per chunk
  overlap=50    # 50 words overlap
)
# Use with extraction strategy
strategy = LLMExtractionStrategy(
  provider="ollama/llama2",
  chunking_strategy=chunker
)
result = await crawler.arun(
  url="https://example.com/long-article",
  extraction_strategy=strategy
)

```

## Best Practices
1. **Choose the Right Strategy** - Use `LLMExtractionStrategy` for complex, unstructured content - Use `JsonCssExtractionStrategy` for well-structured HTML - Use `CosineStrategy` for content similarity and clustering
2. **Optimize Chunking**
```
# For long documents
strategy = LLMExtractionStrategy(
  chunk_token_threshold=2000, # Smaller chunks
  overlap_rate=0.1      # 10% overlap
)

```

3. **Handle Errors**
```
try:
  result = await crawler.arun(
    url="https://example.com",
    extraction_strategy=strategy
  )
  if result.success:
    content = json.loads(result.extracted_content)
except Exception as e:
  print(f"Extraction failed: {e}")

```

4. **Monitor Performance**
```
strategy = CosineStrategy(
  verbose=True, # Enable logging
  word_count_threshold=20, # Filter short content
  top_k=5 # Limit results
)

```

Site built with [MkDocs](https://docs.crawl4ai.com/api/strategies/<http:/www.mkdocs.org>) and [Terminal for MkDocs](https://docs.crawl4ai.com/api/strategies/<https:/github.com/ntno/mkdocs-terminal>). 
##### Search
xClose
Type to start searching


==================================================

# URL: https://docs.crawl4ai.com/blog/

[Crawl4AI Documentation](https://docs.crawl4ai.com/blog/<https:/docs.crawl4ai.com/>)
  * [ Home ](https://docs.crawl4ai.com/blog/<..>)
  * [ Quick Start ](https://docs.crawl4ai.com/blog/<../core/quickstart/>)
  * [ Search ](https://docs.crawl4ai.com/blog/<#>)


  * [Home](https://docs.crawl4ai.com/blog/<..>)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/blog/<../core/installation/>)
    * [Docker Deployment](https://docs.crawl4ai.com/blog/<../core/docker-deploymeny/>)
  * [Quick Start](https://docs.crawl4ai.com/blog/<../core/quickstart/>)
  * Blog & Changelog
    * Blog Home
    * [Changelog](https://docs.crawl4ai.com/blog/<https:/github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md>)
  * Core
    * [Simple Crawling](https://docs.crawl4ai.com/blog/<../core/simple-crawling/>)
    * [Crawler Result](https://docs.crawl4ai.com/blog/<../core/crawler-result/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/blog/<../core/browser-crawler-config/>)
    * [Markdown Generation](https://docs.crawl4ai.com/blog/<../core/markdown-generation/>)
    * [Fit Markdown](https://docs.crawl4ai.com/blog/<../core/fit-markdown/>)
    * [Page Interaction](https://docs.crawl4ai.com/blog/<../core/page-interaction/>)
    * [Content Selection](https://docs.crawl4ai.com/blog/<../core/content-selection/>)
    * [Cache Modes](https://docs.crawl4ai.com/blog/<../core/cache-modes/>)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/blog/<../core/local-files/>)
    * [Link & Media](https://docs.crawl4ai.com/blog/<../core/link-media/>)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/blog/<../advanced/advanced-features/>)
    * [File Downloading](https://docs.crawl4ai.com/blog/<../advanced/file-downloading/>)
    * [Lazy Loading](https://docs.crawl4ai.com/blog/<../advanced/lazy-loading/>)
    * [Hooks & Auth](https://docs.crawl4ai.com/blog/<../advanced/hooks-auth/>)
    * [Proxy & Security](https://docs.crawl4ai.com/blog/<../advanced/proxy-security/>)
    * [Session Management](https://docs.crawl4ai.com/blog/<../advanced/session-management/>)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/blog/<../advanced/multi-url-crawling/>)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/blog/<../advanced/crawl-dispatcher/>)
    * [Identity Based Crawling](https://docs.crawl4ai.com/blog/<../advanced/identity-based-crawling/>)
    * [SSL Certificate](https://docs.crawl4ai.com/blog/<../advanced/ssl-certificate/>)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/blog/<../extraction/no-llm-strategies/>)
    * [LLM Strategies](https://docs.crawl4ai.com/blog/<../extraction/llm-strategies/>)
    * [Clustering Strategies](https://docs.crawl4ai.com/blog/<../extraction/clustring-strategies/>)
    * [Chunking](https://docs.crawl4ai.com/blog/<../extraction/chunking/>)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/blog/<../api/async-webcrawler/>)
    * [arun()](https://docs.crawl4ai.com/blog/<../api/arun/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/blog/<../api/parameters/>)
    * [CrawlResult](https://docs.crawl4ai.com/blog/<../api/crawl-result/>)
    * [Strategies](https://docs.crawl4ai.com/blog/<../api/strategies/>)


  * [Crawl4AI Blog](https://docs.crawl4ai.com/blog/<#crawl4ai-blog>)
  * [Latest Release](https://docs.crawl4ai.com/blog/<#latest-release>)
  * [Project History](https://docs.crawl4ai.com/blog/<#project-history>)
  * [Stay Updated](https://docs.crawl4ai.com/blog/<#stay-updated>)


# Crawl4AI Blog
Welcome to the Crawl4AI blog! Here you'll find detailed release notes, technical insights, and updates about the project. Whether you're looking for the latest improvements or want to dive deep into web crawling techniques, this is the place.
## Latest Release
### [0.4.2 - Configurable Crawlers, Session Management, and Smarter Screenshots](https://docs.crawl4ai.com/blog/<releases/0.4.2/>)
_December 12, 2024_
The 0.4.2 update brings massive improvements to configuration, making crawlers and browsers easier to manage with dedicated objects. You can now import/export local storage for seamless session management. Plus, long-page screenshots are faster and cleaner, and full-page PDF exports are now possible. Check out all the new features to make your crawling experience even smoother.
[Read full release notes →](https://docs.crawl4ai.com/blog/<releases/0.4.2/>)
### [0.4.1 - Smarter Crawling with Lazy-Load Handling, Text-Only Mode, and More](https://docs.crawl4ai.com/blog/<releases/0.4.1/>)
_December 8, 2024_
This release brings major improvements to handling lazy-loaded images, a blazing-fast Text-Only Mode, full-page scanning for infinite scrolls, dynamic viewport adjustments, and session reuse for efficient crawling. If you're looking to improve speed, reliability, or handle dynamic content with ease, this update has you covered.
[Read full release notes →](https://docs.crawl4ai.com/blog/<releases/0.4.1/>)
### [0.4.0 - Major Content Filtering Update](https://docs.crawl4ai.com/blog/<releases/0.4.0/>)
_December 1, 2024_
Introduced significant improvements to content filtering, multi-threaded environment handling, and user-agent generation. This release features the new PruningContentFilter, enhanced thread safety, and improved test coverage.
[Read full release notes →](https://docs.crawl4ai.com/blog/<releases/0.4.0/>)
## Project History
Curious about how Crawl4AI has evolved? Check out our [complete changelog](https://docs.crawl4ai.com/blog/<https:/github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md>) for a detailed history of all versions and updates.
## Stay Updated
  * Star us on [GitHub](https://docs.crawl4ai.com/blog/<https:/github.com/unclecode/crawl4ai>)
  * Follow [@unclecode](https://docs.crawl4ai.com/blog/<https:/twitter.com/unclecode>) on Twitter
  * Join our community discussions on GitHub


Site built with [MkDocs](https://docs.crawl4ai.com/blog/<http:/www.mkdocs.org>) and [Terminal for MkDocs](https://docs.crawl4ai.com/blog/<https:/github.com/ntno/mkdocs-terminal>). 
##### Search
xClose
Type to start searching


==================================================

# URL: https://docs.crawl4ai.com/blog/articles/dockerize_hooks/

[Crawl4AI Documentation](https://docs.crawl4ai.com/blog/articles/dockerize_hooks/<https:/docs.crawl4ai.com/>)
  * [ Home ](https://docs.crawl4ai.com/blog/articles/dockerize_hooks/..>)
  * [ Quick Start ](https://docs.crawl4ai.com/blog/articles/core/quickstart/>)
  * [ Search ](https://docs.crawl4ai.com/blog/articles/dockerize_hooks/<#>)


  * [Home](https://docs.crawl4ai.com/blog/articles/dockerize_hooks/..>)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/blog/articles/core/installation/>)
    * [Docker Deployment](https://docs.crawl4ai.com/blog/articles/core/docker-deploymeny/>)
  * [Quick Start](https://docs.crawl4ai.com/blog/articles/core/quickstart/>)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/blog/articles/dockerize_hooks/>)
    * [Changelog](https://docs.crawl4ai.com/blog/articles/dockerize_hooks/<https:/github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md>)
  * Core
    * [Simple Crawling](https://docs.crawl4ai.com/blog/articles/core/simple-crawling/>)
    * [Crawler Result](https://docs.crawl4ai.com/blog/articles/core/crawler-result/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/blog/articles/core/browser-crawler-config/>)
    * [Markdown Generation](https://docs.crawl4ai.com/blog/articles/core/markdown-generation/>)
    * [Fit Markdown](https://docs.crawl4ai.com/blog/articles/core/fit-markdown/>)
    * [Page Interaction](https://docs.crawl4ai.com/blog/articles/core/page-interaction/>)
    * [Content Selection](https://docs.crawl4ai.com/blog/articles/core/content-selection/>)
    * [Cache Modes](https://docs.crawl4ai.com/blog/articles/core/cache-modes/>)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/blog/articles/core/local-files/>)
    * [Link & Media](https://docs.crawl4ai.com/blog/articles/core/link-media/>)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/blog/articles/advanced/advanced-features/>)
    * [File Downloading](https://docs.crawl4ai.com/blog/articles/advanced/file-downloading/>)
    * [Lazy Loading](https://docs.crawl4ai.com/blog/articles/advanced/lazy-loading/>)
    * [Hooks & Auth](https://docs.crawl4ai.com/blog/articles/advanced/hooks-auth/>)
    * [Proxy & Security](https://docs.crawl4ai.com/blog/articles/advanced/proxy-security/>)
    * [Session Management](https://docs.crawl4ai.com/blog/articles/advanced/session-management/>)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/blog/articles/advanced/multi-url-crawling/>)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/blog/articles/advanced/crawl-dispatcher/>)
    * [Identity Based Crawling](https://docs.crawl4ai.com/blog/articles/advanced/identity-based-crawling/>)
    * [SSL Certificate](https://docs.crawl4ai.com/blog/articles/advanced/ssl-certificate/>)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/blog/articles/extraction/no-llm-strategies/>)
    * [LLM Strategies](https://docs.crawl4ai.com/blog/articles/extraction/llm-strategies/>)
    * [Clustering Strategies](https://docs.crawl4ai.com/blog/articles/extraction/clustring-strategies/>)
    * [Chunking](https://docs.crawl4ai.com/blog/articles/extraction/chunking/>)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/blog/articles/api/async-webcrawler/>)
    * [arun()](https://docs.crawl4ai.com/blog/articles/api/arun/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/blog/articles/api/parameters/>)
    * [CrawlResult](https://docs.crawl4ai.com/blog/articles/api/crawl-result/>)
    * [Strategies](https://docs.crawl4ai.com/blog/articles/api/strategies/>)


  * [Introducing Event Streams and Interactive Hooks in Crawl4AI](https://docs.crawl4ai.com/blog/articles/dockerize_hooks/<#introducing-event-streams-and-interactive-hooks-in-crawl4ai>)


## Introducing Event Streams and Interactive Hooks in Crawl4AI
![event-driven-crawl](https://res.cloudinary.com/kidocode/image/upload/t_400x400/v1734344008/15bb8bbb-83ac-43ac-962d-3feb3e0c3bbf_2_tjmr4n.webp)
In the near future, I’m planning to enhance Crawl4AI’s capabilities by introducing an event stream mechanism that will give clients deeper, real-time insights into the crawling process. Today, hooks are a powerful feature at the code level—they let developers define custom logic at key points in the crawl. However, when using Crawl4AI as a service (e.g., through a Dockerized API), there isn’t an easy way to interact with these hooks at runtime.
**What’s Changing?**
I’m working on a solution that will allow the crawler to emit a continuous stream of events, updating clients on the current crawling stage, encountered pages, and any decision points. This event stream could be exposed over a standardized protocol like Server-Sent Events (SSE) or WebSockets, enabling clients to “subscribe” and listen as the crawler works.
**Interactivity Through Process IDs**
A key part of this new design is the concept of a unique process ID for each crawl session. Imagine you’re listening to an event stream that informs you: - The crawler just hit a certain page - It triggered a hook and is now pausing for instructions 
With the event stream in place, you can send a follow-up request back to the server—referencing the unique process ID—to provide extra data, instructions, or parameters. This might include selecting which links to follow next, adjusting extraction strategies, or providing authentication tokens for a protected API. Once the crawler receives these instructions, it resumes execution with the updated context.
```
sequenceDiagram
  participant Client
  participant Server
  participant Crawler
  Client->>Server: Start crawl request
  Server->>Crawler: Initiate crawl with Process ID
  Crawler-->>Server: Event: Page hit
  Server-->>Client: Stream: Page hit event
  Client->>Server: Instruction for Process ID
  Server->>Crawler: Update crawl with new instructions
  Crawler-->>Server: Event: Crawl completed
  Server-->>Client: Stream: Crawl completed

```

**Benefits for Developers and Users**
1. **Fine-Grained Control** : Instead of predefining all logic upfront, you can dynamically guide the crawler in response to actual data and conditions encountered mid-crawl. 2. **Real-Time Insights** : Monitor progress, errors, or network bottlenecks as they happen, without waiting for the entire crawl to finish. 3. **Enhanced Collaboration** : Different team members or automated systems can watch the same crawl events and provide input, making the crawling process more adaptive and intelligent.
**Next Steps**
I’m currently exploring the best APIs, technologies, and patterns to make this vision a reality. My goal is to deliver a seamless developer experience—one that integrates with existing Crawl4AI workflows while offering new flexibility and power.
Stay tuned for more updates as I continue building this feature out. In the meantime, I’d love to hear any feedback or suggestions you might have to help shape this interactive, event-driven future of web crawling with Crawl4AI.
Site built with [MkDocs](https://docs.crawl4ai.com/blog/articles/dockerize_hooks/<http:/www.mkdocs.org>) and [Terminal for MkDocs](https://docs.crawl4ai.com/blog/articles/dockerize_hooks/<https:/github.com/ntno/mkdocs-terminal>). 
##### Search
xClose
Type to start searching


==================================================

# URL: https://docs.crawl4ai.com/blog/releases/0.4.0/

[Crawl4AI Documentation](https://docs.crawl4ai.com/blog/releases/0.4.0/<https:/docs.crawl4ai.com/>)
  * [ Home ](https://docs.crawl4ai.com/blog/releases/0.4.0/..>)
  * [ Quick Start ](https://docs.crawl4ai.com/blog/releases/core/quickstart/>)
  * [ Search ](https://docs.crawl4ai.com/blog/releases/0.4.0/<#>)


  * [Home](https://docs.crawl4ai.com/blog/releases/0.4.0/..>)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/blog/releases/core/installation/>)
    * [Docker Deployment](https://docs.crawl4ai.com/blog/releases/core/docker-deploymeny/>)
  * [Quick Start](https://docs.crawl4ai.com/blog/releases/core/quickstart/>)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/blog/releases/0.4.0/>)
    * [Changelog](https://docs.crawl4ai.com/blog/releases/0.4.0/<https:/github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md>)
  * Core
    * [Simple Crawling](https://docs.crawl4ai.com/blog/releases/core/simple-crawling/>)
    * [Crawler Result](https://docs.crawl4ai.com/blog/releases/core/crawler-result/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/blog/releases/core/browser-crawler-config/>)
    * [Markdown Generation](https://docs.crawl4ai.com/blog/releases/core/markdown-generation/>)
    * [Fit Markdown](https://docs.crawl4ai.com/blog/releases/core/fit-markdown/>)
    * [Page Interaction](https://docs.crawl4ai.com/blog/releases/core/page-interaction/>)
    * [Content Selection](https://docs.crawl4ai.com/blog/releases/core/content-selection/>)
    * [Cache Modes](https://docs.crawl4ai.com/blog/releases/core/cache-modes/>)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/blog/releases/core/local-files/>)
    * [Link & Media](https://docs.crawl4ai.com/blog/releases/core/link-media/>)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/blog/releases/advanced/advanced-features/>)
    * [File Downloading](https://docs.crawl4ai.com/blog/releases/advanced/file-downloading/>)
    * [Lazy Loading](https://docs.crawl4ai.com/blog/releases/advanced/lazy-loading/>)
    * [Hooks & Auth](https://docs.crawl4ai.com/blog/releases/advanced/hooks-auth/>)
    * [Proxy & Security](https://docs.crawl4ai.com/blog/releases/advanced/proxy-security/>)
    * [Session Management](https://docs.crawl4ai.com/blog/releases/advanced/session-management/>)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/blog/releases/advanced/multi-url-crawling/>)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/blog/releases/advanced/crawl-dispatcher/>)
    * [Identity Based Crawling](https://docs.crawl4ai.com/blog/releases/advanced/identity-based-crawling/>)
    * [SSL Certificate](https://docs.crawl4ai.com/blog/releases/advanced/ssl-certificate/>)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/blog/releases/extraction/no-llm-strategies/>)
    * [LLM Strategies](https://docs.crawl4ai.com/blog/releases/extraction/llm-strategies/>)
    * [Clustering Strategies](https://docs.crawl4ai.com/blog/releases/extraction/clustring-strategies/>)
    * [Chunking](https://docs.crawl4ai.com/blog/releases/extraction/chunking/>)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/blog/releases/api/async-webcrawler/>)
    * [arun()](https://docs.crawl4ai.com/blog/releases/api/arun/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/blog/releases/api/parameters/>)
    * [CrawlResult](https://docs.crawl4ai.com/blog/releases/api/crawl-result/>)
    * [Strategies](https://docs.crawl4ai.com/blog/releases/api/strategies/>)


  * [Release Summary for Version 0.4.0 (December 1, 2024)](https://docs.crawl4ai.com/blog/releases/0.4.0/<#release-summary-for-version-040-december-1-2024>)
  * [Overview](https://docs.crawl4ai.com/blog/releases/0.4.0/<#overview>)
  * [Major Features and Enhancements](https://docs.crawl4ai.com/blog/releases/0.4.0/<#major-features-and-enhancements>)
  * [Revised Change Logs for Version 0.4.0](https://docs.crawl4ai.com/blog/releases/0.4.0/<#revised-change-logs-for-version-040>)
  * [Experimental Features](https://docs.crawl4ai.com/blog/releases/0.4.0/<#experimental-features>)
  * [Conclusion](https://docs.crawl4ai.com/blog/releases/0.4.0/<#conclusion>)


# Release Summary for Version 0.4.0 (December 1, 2024)
## Overview
The 0.4.0 release introduces significant improvements to content filtering, multi-threaded environment handling, user-agent generation, and test coverage. Key highlights include the introduction of the PruningContentFilter, designed to automatically identify and extract the most valuable parts of an HTML document, as well as enhancements to the BM25ContentFilter to extend its versatility and effectiveness.
## Major Features and Enhancements
### 1. PruningContentFilter
  * Introduced a new unsupervised content filtering strategy that scores and prunes less relevant nodes in an HTML document based on metrics like text and link density.
  * Focuses on retaining the most valuable parts of the content, making it highly effective for extracting relevant information from complex web pages.
  * Fully documented with updated README and expanded user guides.


### 2. User-Agent Generator
  * Added a user-agent generator utility that resolves compatibility issues and supports customizable user-agent strings.
  * By default, the generator randomizes user agents for each request, adding diversity, but users can customize it for tailored scenarios.


### 3. Enhanced Thread Safety
  * Improved handling of multi-threaded environments by adding better thread locks for parallel processing, ensuring consistency and stability when running multiple threads.


### 4. Extended Content Filtering Strategies
  * Users now have access to both the PruningContentFilter for unsupervised extraction and the BM25ContentFilter for supervised filtering based on user queries.
  * Enhanced BM25ContentFilter with improved capabilities to process page titles, meta tags, and descriptions, allowing for more effective classification and clustering of text chunks.


### 5. Documentation Updates
  * Updated examples and tutorials to promote the use of the PruningContentFilter alongside the BM25ContentFilter, providing clear instructions for selecting the appropriate filter for each use case.


### 6. Unit Test Enhancements
  * Added unit tests for PruningContentFilter to ensure accuracy and reliability.
  * Enhanced BM25ContentFilter tests to cover additional edge cases and performance metrics, particularly for malformed HTML inputs.


## Revised Change Logs for Version 0.4.0
### PruningContentFilter (Dec 01, 2024)
  * Introduced the PruningContentFilter to optimize content extraction by pruning less relevant HTML nodes.
  * **Affected Files:**
    * **crawl4ai/content_filter_strategy.py** : Added a scoring-based pruning algorithm.
    * **README.md** : Updated to include PruningContentFilter usage.
    * **docs/md_v2/basic/content_filtering.md** : Expanded user documentation, detailing the use and benefits of PruningContentFilter.


### Unit Tests for PruningContentFilter (Dec 01, 2024)
  * Added comprehensive unit tests for PruningContentFilter to ensure correctness and efficiency.
  * **Affected Files:**
    * **tests/async/test_content_filter_prune.py** : Created tests covering different pruning scenarios to ensure stability and correctness.


### Enhanced BM25ContentFilter Tests (Dec 01, 2024)
  * Expanded tests to cover additional extraction scenarios and performance metrics, improving robustness.
  * **Affected Files:**
    * **tests/async/test_content_filter_bm25.py** : Added tests for edge cases, including malformed HTML inputs.


### Documentation and Example Updates (Dec 01, 2024)
  * Revised examples to illustrate the use of PruningContentFilter alongside existing content filtering methods.
  * **Affected Files:**
    * **docs/examples/quickstart_async.py** : Enhanced example clarity and usability for new users.


## Experimental Features
  * The PruningContentFilter is still under experimental development, and we continue to gather feedback for further refinements.


## Conclusion
This release significantly enhances the content extraction capabilities of Crawl4ai with the introduction of the PruningContentFilter, improved supervised filtering with BM25ContentFilter, and robust multi-threaded handling. Additionally, the user-agent generator provides much-needed versatility, resolving compatibility issues faced by many users.
Users are encouraged to experiment with the new content filtering methods to determine which best suits their needs.
Site built with [MkDocs](https://docs.crawl4ai.com/blog/releases/0.4.0/<http:/www.mkdocs.org>) and [Terminal for MkDocs](https://docs.crawl4ai.com/blog/releases/0.4.0/<https:/github.com/ntno/mkdocs-terminal>). 
##### Search
xClose
Type to start searching


==================================================

# URL: https://docs.crawl4ai.com/blog/releases/0.4.1/

[Crawl4AI Documentation](https://docs.crawl4ai.com/blog/releases/0.4.1/<https:/docs.crawl4ai.com/>)
  * [ Home ](https://docs.crawl4ai.com/blog/releases/0.4.1/..>)
  * [ Quick Start ](https://docs.crawl4ai.com/blog/releases/core/quickstart/>)
  * [ Search ](https://docs.crawl4ai.com/blog/releases/0.4.1/<#>)


  * [Home](https://docs.crawl4ai.com/blog/releases/0.4.1/..>)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/blog/releases/core/installation/>)
    * [Docker Deployment](https://docs.crawl4ai.com/blog/releases/core/docker-deploymeny/>)
  * [Quick Start](https://docs.crawl4ai.com/blog/releases/core/quickstart/>)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/blog/releases/0.4.1/>)
    * [Changelog](https://docs.crawl4ai.com/blog/releases/0.4.1/<https:/github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md>)
  * Core
    * [Simple Crawling](https://docs.crawl4ai.com/blog/releases/core/simple-crawling/>)
    * [Crawler Result](https://docs.crawl4ai.com/blog/releases/core/crawler-result/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/blog/releases/core/browser-crawler-config/>)
    * [Markdown Generation](https://docs.crawl4ai.com/blog/releases/core/markdown-generation/>)
    * [Fit Markdown](https://docs.crawl4ai.com/blog/releases/core/fit-markdown/>)
    * [Page Interaction](https://docs.crawl4ai.com/blog/releases/core/page-interaction/>)
    * [Content Selection](https://docs.crawl4ai.com/blog/releases/core/content-selection/>)
    * [Cache Modes](https://docs.crawl4ai.com/blog/releases/core/cache-modes/>)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/blog/releases/core/local-files/>)
    * [Link & Media](https://docs.crawl4ai.com/blog/releases/core/link-media/>)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/blog/releases/advanced/advanced-features/>)
    * [File Downloading](https://docs.crawl4ai.com/blog/releases/advanced/file-downloading/>)
    * [Lazy Loading](https://docs.crawl4ai.com/blog/releases/advanced/lazy-loading/>)
    * [Hooks & Auth](https://docs.crawl4ai.com/blog/releases/advanced/hooks-auth/>)
    * [Proxy & Security](https://docs.crawl4ai.com/blog/releases/advanced/proxy-security/>)
    * [Session Management](https://docs.crawl4ai.com/blog/releases/advanced/session-management/>)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/blog/releases/advanced/multi-url-crawling/>)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/blog/releases/advanced/crawl-dispatcher/>)
    * [Identity Based Crawling](https://docs.crawl4ai.com/blog/releases/advanced/identity-based-crawling/>)
    * [SSL Certificate](https://docs.crawl4ai.com/blog/releases/advanced/ssl-certificate/>)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/blog/releases/extraction/no-llm-strategies/>)
    * [LLM Strategies](https://docs.crawl4ai.com/blog/releases/extraction/llm-strategies/>)
    * [Clustering Strategies](https://docs.crawl4ai.com/blog/releases/extraction/clustring-strategies/>)
    * [Chunking](https://docs.crawl4ai.com/blog/releases/extraction/chunking/>)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/blog/releases/api/async-webcrawler/>)
    * [arun()](https://docs.crawl4ai.com/blog/releases/api/arun/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/blog/releases/api/parameters/>)
    * [CrawlResult](https://docs.crawl4ai.com/blog/releases/api/crawl-result/>)
    * [Strategies](https://docs.crawl4ai.com/blog/releases/api/strategies/>)


  * [Release Summary for Version 0.4.1 (December 8, 2024): Major Efficiency Boosts with New Features!](https://docs.crawl4ai.com/blog/releases/0.4.1/<#release-summary-for-version-041-december-8-2024-major-efficiency-boosts-with-new-features>)
  * [Handling Lazy Loading Better (Images Included)](https://docs.crawl4ai.com/blog/releases/0.4.1/<#handling-lazy-loading-better-images-included>)
  * [Text-Only Mode (Fast, Lightweight Crawling)](https://docs.crawl4ai.com/blog/releases/0.4.1/<#text-only-mode-fast-lightweight-crawling>)
  * [Adjusting the Viewport Dynamically](https://docs.crawl4ai.com/blog/releases/0.4.1/<#adjusting-the-viewport-dynamically>)
  * [Simulating Full-Page Scrolling](https://docs.crawl4ai.com/blog/releases/0.4.1/<#simulating-full-page-scrolling>)
  * [Reusing Browser Sessions (Save Time on Setup)](https://docs.crawl4ai.com/blog/releases/0.4.1/<#reusing-browser-sessions-save-time-on-setup>)
  * [Other Updates](https://docs.crawl4ai.com/blog/releases/0.4.1/<#other-updates>)
  * [How to Get the Update](https://docs.crawl4ai.com/blog/releases/0.4.1/<#how-to-get-the-update>)


# Release Summary for Version 0.4.1 (December 8, 2024): Major Efficiency Boosts with New Features!
_This post was generated with the help of ChatGPT, take everything with a grain of salt. 🧂_
Hi everyone,
I just finished putting together version 0.4.1 of Crawl4AI, and there are a few changes in here that I think you’ll find really helpful. I’ll explain what’s new, why it matters, and exactly how you can use these features (with the code to back it up). Let’s get into it.
### Handling Lazy Loading Better (Images Included)
One thing that always bugged me with crawlers is how often they miss lazy-loaded content, especially images. In this version, I made sure Crawl4AI **waits for all images to load** before moving forward. This is useful because many modern websites only load images when they’re in the viewport or after some JavaScript executes.
Here’s how to enable it:
```
await crawler.crawl(
  url="https://example.com",
  wait_for_images=True # Add this argument to ensure images are fully loaded
)

```

What this does is: 1. Waits for the page to reach a "network idle" state. 2. Ensures all images on the page have been completely loaded.
This single change handles the majority of lazy-loading cases you’re likely to encounter.
### Text-Only Mode (Fast, Lightweight Crawling)
Sometimes, you don’t need to download images or process JavaScript at all. For example, if you’re crawling to extract text data, you can enable **text-only mode** to speed things up. By disabling images, JavaScript, and other heavy resources, this mode makes crawling **3-4 times faster** in most cases.
Here’s how to turn it on:
```
crawler = AsyncPlaywrightCrawlerStrategy(
  text_mode=True # Set this to True to enable text-only crawling
)

```

When `text_mode=True`, the crawler automatically: - Disables GPU processing. - Blocks image and JavaScript resources. - Reduces the viewport size to 800x600 (you can override this with `viewport_width` and `viewport_height`).
If you need to crawl thousands of pages where you only care about text, this mode will save you a ton of time and resources.
### Adjusting the Viewport Dynamically
Another useful addition is the ability to **dynamically adjust the viewport size** to match the content on the page. This is particularly helpful when you’re working with responsive layouts or want to ensure all parts of the page load properly.
Here’s how it works: 1. The crawler calculates the page’s width and height after it loads. 2. It adjusts the viewport to fit the content dimensions. 3. (Optional) It uses Chrome DevTools Protocol (CDP) to simulate zooming out so everything fits in the viewport.
To enable this, use:
```
await crawler.crawl(
  url="https://example.com",
  adjust_viewport_to_content=True # Dynamically adjusts the viewport
)

```

This approach makes sure the entire page gets loaded into the viewport, especially for layouts that load content based on visibility.
### Simulating Full-Page Scrolling
Some websites load data dynamically as you scroll down the page. To handle these cases, I added support for **full-page scanning**. It simulates scrolling to the bottom of the page, checking for new content, and capturing it all.
Here’s an example:
```
await crawler.crawl(
  url="https://example.com",
  scan_full_page=True,  # Enables scrolling
  scroll_delay=0.2    # Waits 200ms between scrolls (optional)
)

```

What happens here: 1. The crawler scrolls down in increments, waiting for content to load after each scroll. 2. It stops when no new content appears (i.e., dynamic elements stop loading). 3. It scrolls back to the top before finishing (if necessary).
If you’ve ever had to deal with infinite scroll pages, this is going to save you a lot of headaches.
### Reusing Browser Sessions (Save Time on Setup)
By default, every time you crawl a page, a new browser context (or tab) is created. That’s fine for small crawls, but if you’re working on a large dataset, it’s more efficient to reuse the same session.
I added a method called `create_session` for this:
```
session_id = await crawler.create_session()
# Use the same session for multiple crawls
await crawler.crawl(
  url="https://example.com/page1",
  session_id=session_id # Reuse the session
)
await crawler.crawl(
  url="https://example.com/page2",
  session_id=session_id
)

```

This avoids creating a new tab for every page, speeding up the crawl and reducing memory usage.
### Other Updates
Here are a few smaller updates I’ve made: - **Light Mode** : Use `light_mode=True` to disable background processes, extensions, and other unnecessary features, making the browser more efficient. - **Logging** : Improved logs to make debugging easier. - **Defaults** : Added sensible defaults for things like `delay_before_return_html` (now set to 0.1 seconds).
### How to Get the Update
You can install or upgrade to version `0.4.1` like this:
```
pip install crawl4ai --upgrade

```

As always, I’d love to hear your thoughts. If there’s something you think could be improved or if you have suggestions for future versions, let me know!
Enjoy the new features, and happy crawling! 🕷️
Site built with [MkDocs](https://docs.crawl4ai.com/blog/releases/0.4.1/<http:/www.mkdocs.org>) and [Terminal for MkDocs](https://docs.crawl4ai.com/blog/releases/0.4.1/<https:/github.com/ntno/mkdocs-terminal>). 
##### Search
xClose
Type to start searching


==================================================

# URL: https://docs.crawl4ai.com/blog/releases/0.4.2/

[Crawl4AI Documentation](https://docs.crawl4ai.com/blog/releases/0.4.2/<https:/docs.crawl4ai.com/>)
  * [ Home ](https://docs.crawl4ai.com/blog/releases/0.4.2/..>)
  * [ Quick Start ](https://docs.crawl4ai.com/blog/releases/core/quickstart/>)
  * [ Search ](https://docs.crawl4ai.com/blog/releases/0.4.2/<#>)


  * [Home](https://docs.crawl4ai.com/blog/releases/0.4.2/..>)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/blog/releases/core/installation/>)
    * [Docker Deployment](https://docs.crawl4ai.com/blog/releases/core/docker-deploymeny/>)
  * [Quick Start](https://docs.crawl4ai.com/blog/releases/core/quickstart/>)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/blog/releases/0.4.2/>)
    * [Changelog](https://docs.crawl4ai.com/blog/releases/0.4.2/<https:/github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md>)
  * Core
    * [Simple Crawling](https://docs.crawl4ai.com/blog/releases/core/simple-crawling/>)
    * [Crawler Result](https://docs.crawl4ai.com/blog/releases/core/crawler-result/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/blog/releases/core/browser-crawler-config/>)
    * [Markdown Generation](https://docs.crawl4ai.com/blog/releases/core/markdown-generation/>)
    * [Fit Markdown](https://docs.crawl4ai.com/blog/releases/core/fit-markdown/>)
    * [Page Interaction](https://docs.crawl4ai.com/blog/releases/core/page-interaction/>)
    * [Content Selection](https://docs.crawl4ai.com/blog/releases/core/content-selection/>)
    * [Cache Modes](https://docs.crawl4ai.com/blog/releases/core/cache-modes/>)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/blog/releases/core/local-files/>)
    * [Link & Media](https://docs.crawl4ai.com/blog/releases/core/link-media/>)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/blog/releases/advanced/advanced-features/>)
    * [File Downloading](https://docs.crawl4ai.com/blog/releases/advanced/file-downloading/>)
    * [Lazy Loading](https://docs.crawl4ai.com/blog/releases/advanced/lazy-loading/>)
    * [Hooks & Auth](https://docs.crawl4ai.com/blog/releases/advanced/hooks-auth/>)
    * [Proxy & Security](https://docs.crawl4ai.com/blog/releases/advanced/proxy-security/>)
    * [Session Management](https://docs.crawl4ai.com/blog/releases/advanced/session-management/>)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/blog/releases/advanced/multi-url-crawling/>)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/blog/releases/advanced/crawl-dispatcher/>)
    * [Identity Based Crawling](https://docs.crawl4ai.com/blog/releases/advanced/identity-based-crawling/>)
    * [SSL Certificate](https://docs.crawl4ai.com/blog/releases/advanced/ssl-certificate/>)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/blog/releases/extraction/no-llm-strategies/>)
    * [LLM Strategies](https://docs.crawl4ai.com/blog/releases/extraction/llm-strategies/>)
    * [Clustering Strategies](https://docs.crawl4ai.com/blog/releases/extraction/clustring-strategies/>)
    * [Chunking](https://docs.crawl4ai.com/blog/releases/extraction/chunking/>)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/blog/releases/api/async-webcrawler/>)
    * [arun()](https://docs.crawl4ai.com/blog/releases/api/arun/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/blog/releases/api/parameters/>)
    * [CrawlResult](https://docs.crawl4ai.com/blog/releases/api/crawl-result/>)
    * [Strategies](https://docs.crawl4ai.com/blog/releases/api/strategies/>)


  * [🚀 Crawl4AI 0.4.2 Update: Smarter Crawling Just Got Easier (Dec 12, 2024)](https://docs.crawl4ai.com/blog/releases/0.4.2/<#crawl4ai-042-update-smarter-crawling-just-got-easier-dec-12-2024>)
  * [Hey Developers,](https://docs.crawl4ai.com/blog/releases/0.4.2/<#hey-developers>)
  * [🔧 Configurable Browser and Crawler Behavior](https://docs.crawl4ai.com/blog/releases/0.4.2/<#configurable-browser-and-crawler-behavior>)
  * [🔐 Streamlined Session Management](https://docs.crawl4ai.com/blog/releases/0.4.2/<#streamlined-session-management>)
  * [🔢 Handling Large Pages: Supercharged Screenshots and PDF Conversion](https://docs.crawl4ai.com/blog/releases/0.4.2/<#handling-large-pages-supercharged-screenshots-and-pdf-conversion>)
  * [🔧 Other Cool Stuff](https://docs.crawl4ai.com/blog/releases/0.4.2/<#other-cool-stuff>)
  * [📊 Performance Boosts and Dev-friendly Updates](https://docs.crawl4ai.com/blog/releases/0.4.2/<#performance-boosts-and-dev-friendly-updates>)
  * [🔠 Use Cases You’ll Love](https://docs.crawl4ai.com/blog/releases/0.4.2/<#use-cases-youll-love>)
  * [Let’s Get Crawling](https://docs.crawl4ai.com/blog/releases/0.4.2/<#lets-get-crawling>)


## 🚀 Crawl4AI 0.4.2 Update: Smarter Crawling Just Got Easier (Dec 12, 2024)
### Hey Developers,
I’m excited to share Crawl4AI 0.4.2—a major upgrade that makes crawling smarter, faster, and a whole lot more intuitive. I’ve packed in a bunch of new features to simplify your workflows and improve your experience. Let’s cut to the chase!
### 🔧 **Configurable Browser and Crawler Behavior**
You’ve asked for better control over how browsers and crawlers are configured, and now you’ve got it. With the new `BrowserConfig` and `CrawlerRunConfig` objects, you can set up your browser and crawling behavior exactly how you want. No more cluttering `arun` with a dozen arguments—just pass in your configs and go.
**Example:**
```
from crawl4ai import BrowserConfig, CrawlerRunConfig, AsyncWebCrawler
browser_config = BrowserConfig(headless=True, viewport_width=1920, viewport_height=1080)
crawler_config = CrawlerRunConfig(cache_mode="BYPASS")
async with AsyncWebCrawler(config=browser_config) as crawler:
  result = await crawler.arun(url="https://example.com", config=crawler_config)
  print(result.markdown[:500])

```

This setup is a game-changer for scalability, keeping your code clean and flexible as we add more parameters in the future.
Remember: If you like to use the old way, you can still pass arguments directly to `arun` as before, no worries!
### 🔐 **Streamlined Session Management**
Here’s the big one: You can now pass local storage and cookies directly. Whether it’s setting values programmatically or importing a saved JSON state, managing sessions has never been easier. This is a must-have for authenticated crawls—just export your storage state once and reuse it effortlessly across runs.
**Example:** 1. Open a browser, log in manually, and export the storage state. 2. Import the JSON file for seamless authenticated crawling:
```
result = await crawler.arun(
  url="https://example.com/protected",
  storage_state="my_storage_state.json"
)

```

### 🔢 **Handling Large Pages: Supercharged Screenshots and PDF Conversion**
Two big upgrades here:
  * **Blazing-fast long-page screenshots** : Turn extremely long web pages into clean, high-quality screenshots—without breaking a sweat. It’s optimized to handle large content without lag.
  * **Full-page PDF exports** : Now, you can also convert any page into a PDF with all the details intact. Perfect for archiving or sharing complex layouts.


### 🔧 **Other Cool Stuff**
  * **Anti-bot enhancements** : Magic mode now handles overlays, user simulation, and anti-detection features like a pro.
  * **JavaScript execution** : Execute custom JS snippets to handle dynamic content. No more wrestling with endless page interactions.


### 📊 **Performance Boosts and Dev-friendly Updates**
  * Faster rendering and viewport adjustments for better performance.
  * Improved cookie and local storage handling for seamless authentication.
  * Better debugging with detailed logs and actionable error messages.


### 🔠 **Use Cases You’ll Love**
1. **Authenticated Crawls** : Login once, export your storage state, and reuse it across multiple requests without the headache. 2. **Long-page Screenshots** : Perfect for blogs, e-commerce pages, or any endless-scroll website. 3. **PDF Export** : Create professional-looking page PDFs in seconds.
### Let’s Get Crawling
Crawl4AI 0.4.2 is ready for you to download and try. I’m always looking for ways to improve, so don’t hold back—share your thoughts and feedback.
Happy Crawling! 🚀
Site built with [MkDocs](https://docs.crawl4ai.com/blog/releases/0.4.2/<http:/www.mkdocs.org>) and [Terminal for MkDocs](https://docs.crawl4ai.com/blog/releases/0.4.2/<https:/github.com/ntno/mkdocs-terminal>). 
##### Search
xClose
Type to start searching


==================================================

# URL: https://docs.crawl4ai.com/core/browser-crawler-config/

[Crawl4AI Documentation](https://docs.crawl4ai.com/core/browser-crawler-config/<https:/docs.crawl4ai.com/>)
  * [ Home ](https://docs.crawl4ai.com/core/browser-crawler-config/<../..>)
  * [ Quick Start ](https://docs.crawl4ai.com/core/browser-crawler-config/<../quickstart/>)
  * [ Search ](https://docs.crawl4ai.com/core/browser-crawler-config/<#>)


  * [Home](https://docs.crawl4ai.com/core/browser-crawler-config/<../..>)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/core/browser-crawler-config/<../installation/>)
    * [Docker Deployment](https://docs.crawl4ai.com/core/browser-crawler-config/<../docker-deploymeny/>)
  * [Quick Start](https://docs.crawl4ai.com/core/browser-crawler-config/<../quickstart/>)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/core/browser-crawler-config/blog/>)
    * [Changelog](https://docs.crawl4ai.com/core/browser-crawler-config/<https:/github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md>)
  * Core
    * [Simple Crawling](https://docs.crawl4ai.com/core/browser-crawler-config/<../simple-crawling/>)
    * [Crawler Result](https://docs.crawl4ai.com/core/browser-crawler-config/<../crawler-result/>)
    * Browser & Crawler Config
    * [Markdown Generation](https://docs.crawl4ai.com/core/browser-crawler-config/<../markdown-generation/>)
    * [Fit Markdown](https://docs.crawl4ai.com/core/browser-crawler-config/<../fit-markdown/>)
    * [Page Interaction](https://docs.crawl4ai.com/core/browser-crawler-config/<../page-interaction/>)
    * [Content Selection](https://docs.crawl4ai.com/core/browser-crawler-config/<../content-selection/>)
    * [Cache Modes](https://docs.crawl4ai.com/core/browser-crawler-config/<../cache-modes/>)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/core/browser-crawler-config/<../local-files/>)
    * [Link & Media](https://docs.crawl4ai.com/core/browser-crawler-config/<../link-media/>)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/core/browser-crawler-config/advanced/advanced-features/>)
    * [File Downloading](https://docs.crawl4ai.com/core/browser-crawler-config/advanced/file-downloading/>)
    * [Lazy Loading](https://docs.crawl4ai.com/core/browser-crawler-config/advanced/lazy-loading/>)
    * [Hooks & Auth](https://docs.crawl4ai.com/core/browser-crawler-config/advanced/hooks-auth/>)
    * [Proxy & Security](https://docs.crawl4ai.com/core/browser-crawler-config/advanced/proxy-security/>)
    * [Session Management](https://docs.crawl4ai.com/core/browser-crawler-config/advanced/session-management/>)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/core/browser-crawler-config/advanced/multi-url-crawling/>)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/core/browser-crawler-config/advanced/crawl-dispatcher/>)
    * [Identity Based Crawling](https://docs.crawl4ai.com/core/browser-crawler-config/advanced/identity-based-crawling/>)
    * [SSL Certificate](https://docs.crawl4ai.com/core/browser-crawler-config/advanced/ssl-certificate/>)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/core/browser-crawler-config/extraction/no-llm-strategies/>)
    * [LLM Strategies](https://docs.crawl4ai.com/core/browser-crawler-config/extraction/llm-strategies/>)
    * [Clustering Strategies](https://docs.crawl4ai.com/core/browser-crawler-config/extraction/clustring-strategies/>)
    * [Chunking](https://docs.crawl4ai.com/core/browser-crawler-config/extraction/chunking/>)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/core/browser-crawler-config/api/async-webcrawler/>)
    * [arun()](https://docs.crawl4ai.com/core/browser-crawler-config/api/arun/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/core/browser-crawler-config/api/parameters/>)
    * [CrawlResult](https://docs.crawl4ai.com/core/browser-crawler-config/api/crawl-result/>)
    * [Strategies](https://docs.crawl4ai.com/core/browser-crawler-config/api/strategies/>)


  * [Browser & Crawler Configuration (Quick Overview)](https://docs.crawl4ai.com/core/browser-crawler-config/<#browser-crawler-configuration-quick-overview>)
  * [1. BrowserConfig Essentials](https://docs.crawl4ai.com/core/browser-crawler-config/<#1-browserconfig-essentials>)
  * [2. CrawlerRunConfig Essentials](https://docs.crawl4ai.com/core/browser-crawler-config/<#2-crawlerrunconfig-essentials>)
  * [3. Putting It All Together](https://docs.crawl4ai.com/core/browser-crawler-config/<#3-putting-it-all-together>)
  * [4. Next Steps](https://docs.crawl4ai.com/core/browser-crawler-config/<#4-next-steps>)
  * [5. Conclusion](https://docs.crawl4ai.com/core/browser-crawler-config/<#5-conclusion>)


# Browser & Crawler Configuration (Quick Overview)
Crawl4AI’s flexibility stems from two key classes:
1. **`BrowserConfig`**– Dictates**how** the browser is launched and behaves (e.g., headless or visible, proxy, user agent). 2. **`CrawlerRunConfig`**– Dictates**how** each **crawl** operates (e.g., caching, extraction, timeouts, JavaScript code to run, etc.).
In most examples, you create **one** `BrowserConfig` for the entire crawler session, then pass a **fresh** or re-used `CrawlerRunConfig` whenever you call `arun()`. This tutorial shows the most commonly used parameters. If you need advanced or rarely used fields, see the [Configuration Parameters](https://docs.crawl4ai.com/core/browser-crawler-config/api/parameters/>).
## 1. BrowserConfig Essentials
```
class BrowserConfig:
  def __init__(
    browser_type="chromium",
    headless=True,
    proxy_config=None,
    viewport_width=1080,
    viewport_height=600,
    verbose=True,
    use_persistent_context=False,
    user_data_dir=None,
    cookies=None,
    headers=None,
    user_agent=None,
    text_mode=False,
    light_mode=False,
    extra_args=None,
    # ... other advanced parameters omitted here
  ):
    ...

```

### Key Fields to Note
1. **`browser_type`**- Options:`"chromium"` , `"firefox"`, or `"webkit"`. - Defaults to `"chromium"`. - If you need a different engine, specify it here.
2. **`headless`**-`True` : Runs the browser in headless mode (invisible browser). - `False`: Runs the browser in visible mode, which helps with debugging.
3. **`proxy_config`**- A dictionary with fields like:
```
{
  "server": "http://proxy.example.com:8080", 
  "username": "...", 
  "password": "..."
}

```

- Leave as `None` if a proxy is not required. 
4. **`viewport_width` & `viewport_height`**: - The initial window size. - Some sites behave differently with smaller or bigger viewports.
5. **`verbose`**: - If`True` , prints extra logs. - Handy for debugging.
6. **`use_persistent_context`**: - If`True` , uses a **persistent** browser profile, storing cookies/local storage across runs. - Typically also set `user_data_dir` to point to a folder.
7. **`cookies`** & **`headers`**: - If you want to start with specific cookies or add universal HTTP headers, set them here. - E.g.`cookies=[{"name": "session", "value": "abc123", "domain": "example.com"}]`.
8. **`user_agent`**: - Custom User-Agent string. If`None` , a default is used. - You can also set `user_agent_mode="random"` for randomization (if you want to fight bot detection).
9. **`text_mode`** & **`light_mode`**: -`text_mode=True` disables images, possibly speeding up text-only crawls. - `light_mode=True` turns off certain background features for performance. 
10. **`extra_args`**: - Additional flags for the underlying browser. - E.g.`["--disable-extensions"]`.
**Minimal Example** :
```
from crawl4ai import AsyncWebCrawler, BrowserConfig
browser_conf = BrowserConfig(
  browser_type="firefox",
  headless=False,
  text_mode=True
)
async with AsyncWebCrawler(config=browser_conf) as crawler:
  result = await crawler.arun("https://example.com")
  print(result.markdown[:300])

```

## 2. CrawlerRunConfig Essentials
```
class CrawlerRunConfig:
  def __init__(
    word_count_threshold=200,
    extraction_strategy=None,
    markdown_generator=None,
    cache_mode=None,
    js_code=None,
    wait_for=None,
    screenshot=False,
    pdf=False,
    verbose=True,
    # ... other advanced parameters omitted
  ):
    ...

```

### Key Fields to Note
1. **`word_count_threshold`**: - The minimum word count before a block is considered. - If your site has lots of short paragraphs or items, you can lower it.
2. **`extraction_strategy`**: - Where you plug in JSON-based extraction (CSS, LLM, etc.). - If`None` , no structured extraction is done (only raw/cleaned HTML + markdown).
3. **`markdown_generator`**: - E.g.,`DefaultMarkdownGenerator(...)` , controlling how HTML→Markdown conversion is done. - If `None`, a default approach is used.
4. **`cache_mode`**: - Controls caching behavior (`ENABLED` , `BYPASS`, `DISABLED`, etc.). - If `None`, defaults to some level of caching or you can specify `CacheMode.ENABLED`.
5. **`js_code`**: - A string or list of JS strings to execute. - Great for “Load More” buttons or user interactions.
6. **`wait_for`**: - A CSS or JS expression to wait for before extracting content. - Common usage:`wait_for="css:.main-loaded"` or `wait_for="js:() => window.loaded === true"`.
7. **`screenshot`** & **`pdf`**: - If`True` , captures a screenshot or PDF after the page is fully loaded. - The results go to `result.screenshot` (base64) or `result.pdf` (bytes).
8. **`verbose`**: - Logs additional runtime details. - Overlaps with the browser’s verbosity if also set to`True` in `BrowserConfig`.
**Minimal Example** :
```
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
crawl_conf = CrawlerRunConfig(
  js_code="document.querySelector('button#loadMore')?.click()",
  wait_for="css:.loaded-content",
  screenshot=True
)
async with AsyncWebCrawler() as crawler:
  result = await crawler.arun(url="https://example.com", config=crawl_conf)
  print(result.screenshot[:100]) # Base64-encoded PNG snippet

```

## 3. Putting It All Together
In a typical scenario, you define **one** `BrowserConfig` for your crawler session, then create **one or more** `CrawlerRunConfig` depending on each call’s needs:
```
import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
async def main():
  # 1) Browser config: headless, bigger viewport, no proxy
  browser_conf = BrowserConfig(
    headless=True,
    viewport_width=1280,
    viewport_height=720
  )
  # 2) Example extraction strategy
  schema = {
    "name": "Articles",
    "baseSelector": "div.article",
    "fields": [
      {"name": "title", "selector": "h2", "type": "text"},
      {"name": "link", "selector": "a", "type": "attribute", "attribute": "href"}
    ]
  }
  extraction = JsonCssExtractionStrategy(schema)
  # 3) Crawler run config: skip cache, use extraction
  run_conf = CrawlerRunConfig(
    extraction_strategy=extraction,
    cache_mode=CacheMode.BYPASS
  )
  async with AsyncWebCrawler(config=browser_conf) as crawler:
    # 4) Execute the crawl
    result = await crawler.arun(url="https://example.com/news", config=run_conf)
    if result.success:
      print("Extracted content:", result.extracted_content)
    else:
      print("Error:", result.error_message)
if __name__ == "__main__":
  asyncio.run(main())

```

## 4. Next Steps
For a **detailed list** of available parameters (including advanced ones), see:
  * [BrowserConfig and CrawlerRunConfig Reference](https://docs.crawl4ai.com/core/browser-crawler-config/api/parameters/>)


You can explore topics like:
  * **Custom Hooks & Auth** (Inject JavaScript or handle login forms). 
  * **Session Management** (Re-use pages, preserve state across multiple calls). 
  * **Magic Mode** or **Identity-based Crawling** (Fight bot detection by simulating user behavior). 
  * **Advanced Caching** (Fine-tune read/write cache modes). 


## 5. Conclusion
**BrowserConfig** and **CrawlerRunConfig** give you straightforward ways to define:
  * **Which** browser to launch, how it should run, and any proxy or user agent needs. 
  * **How** each crawl should behave—caching, timeouts, JavaScript code, extraction strategies, etc.


Use them together for **clear, maintainable** code, and when you need more specialized behavior, check out the advanced parameters in the [reference docs](https://docs.crawl4ai.com/core/browser-crawler-config/api/parameters/>). Happy crawling!
Site built with [MkDocs](https://docs.crawl4ai.com/core/browser-crawler-config/<http:/www.mkdocs.org>) and [Terminal for MkDocs](https://docs.crawl4ai.com/core/browser-crawler-config/<https:/github.com/ntno/mkdocs-terminal>). 
##### Search
xClose
Type to start searching


==================================================

# URL: https://docs.crawl4ai.com/core/cache-modes/

[Crawl4AI Documentation](https://docs.crawl4ai.com/core/cache-modes/<https:/docs.crawl4ai.com/>)
  * [ Home ](https://docs.crawl4ai.com/core/cache-modes/<../..>)
  * [ Quick Start ](https://docs.crawl4ai.com/core/cache-modes/<../quickstart/>)
  * [ Search ](https://docs.crawl4ai.com/core/cache-modes/<#>)


  * [Home](https://docs.crawl4ai.com/core/cache-modes/<../..>)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/core/cache-modes/<../installation/>)
    * [Docker Deployment](https://docs.crawl4ai.com/core/cache-modes/<../docker-deploymeny/>)
  * [Quick Start](https://docs.crawl4ai.com/core/cache-modes/<../quickstart/>)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/core/cache-modes/blog/>)
    * [Changelog](https://docs.crawl4ai.com/core/cache-modes/<https:/github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md>)
  * Core
    * [Simple Crawling](https://docs.crawl4ai.com/core/cache-modes/<../simple-crawling/>)
    * [Crawler Result](https://docs.crawl4ai.com/core/cache-modes/<../crawler-result/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/core/cache-modes/<../browser-crawler-config/>)
    * [Markdown Generation](https://docs.crawl4ai.com/core/cache-modes/<../markdown-generation/>)
    * [Fit Markdown](https://docs.crawl4ai.com/core/cache-modes/<../fit-markdown/>)
    * [Page Interaction](https://docs.crawl4ai.com/core/cache-modes/<../page-interaction/>)
    * [Content Selection](https://docs.crawl4ai.com/core/cache-modes/<../content-selection/>)
    * Cache Modes
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/core/cache-modes/<../local-files/>)
    * [Link & Media](https://docs.crawl4ai.com/core/cache-modes/<../link-media/>)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/core/cache-modes/advanced/advanced-features/>)
    * [File Downloading](https://docs.crawl4ai.com/core/cache-modes/advanced/file-downloading/>)
    * [Lazy Loading](https://docs.crawl4ai.com/core/cache-modes/advanced/lazy-loading/>)
    * [Hooks & Auth](https://docs.crawl4ai.com/core/cache-modes/advanced/hooks-auth/>)
    * [Proxy & Security](https://docs.crawl4ai.com/core/cache-modes/advanced/proxy-security/>)
    * [Session Management](https://docs.crawl4ai.com/core/cache-modes/advanced/session-management/>)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/core/cache-modes/advanced/multi-url-crawling/>)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/core/cache-modes/advanced/crawl-dispatcher/>)
    * [Identity Based Crawling](https://docs.crawl4ai.com/core/cache-modes/advanced/identity-based-crawling/>)
    * [SSL Certificate](https://docs.crawl4ai.com/core/cache-modes/advanced/ssl-certificate/>)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/core/cache-modes/extraction/no-llm-strategies/>)
    * [LLM Strategies](https://docs.crawl4ai.com/core/cache-modes/extraction/llm-strategies/>)
    * [Clustering Strategies](https://docs.crawl4ai.com/core/cache-modes/extraction/clustring-strategies/>)
    * [Chunking](https://docs.crawl4ai.com/core/cache-modes/extraction/chunking/>)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/core/cache-modes/api/async-webcrawler/>)
    * [arun()](https://docs.crawl4ai.com/core/cache-modes/api/arun/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/core/cache-modes/api/parameters/>)
    * [CrawlResult](https://docs.crawl4ai.com/core/cache-modes/api/crawl-result/>)
    * [Strategies](https://docs.crawl4ai.com/core/cache-modes/api/strategies/>)


  * [Crawl4AI Cache System and Migration Guide](https://docs.crawl4ai.com/core/cache-modes/<#crawl4ai-cache-system-and-migration-guide>)
  * [Overview](https://docs.crawl4ai.com/core/cache-modes/<#overview>)
  * [Old vs New Approach](https://docs.crawl4ai.com/core/cache-modes/<#old-vs-new-approach>)
  * [Migration Example](https://docs.crawl4ai.com/core/cache-modes/<#migration-example>)
  * [Common Migration Patterns](https://docs.crawl4ai.com/core/cache-modes/<#common-migration-patterns>)


# Crawl4AI Cache System and Migration Guide
## Overview
Starting from version 0.5.0, Crawl4AI introduces a new caching system that replaces the old boolean flags with a more intuitive `CacheMode` enum. This change simplifies cache control and makes the behavior more predictable.
## Old vs New Approach
### Old Way (Deprecated)
The old system used multiple boolean flags: - `bypass_cache`: Skip cache entirely - `disable_cache`: Disable all caching - `no_cache_read`: Don't read from cache - `no_cache_write`: Don't write to cache
### New Way (Recommended)
The new system uses a single `CacheMode` enum: - `CacheMode.ENABLED`: Normal caching (read/write) - `CacheMode.DISABLED`: No caching at all - `CacheMode.READ_ONLY`: Only read from cache - `CacheMode.WRITE_ONLY`: Only write to cache - `CacheMode.BYPASS`: Skip cache for this operation
## Migration Example
### Old Code (Deprecated)
```
import asyncio
from crawl4ai import AsyncWebCrawler
async def use_proxy():
  async with AsyncWebCrawler(verbose=True) as crawler:
    result = await crawler.arun(
      url="https://www.nbcnews.com/business",
      bypass_cache=True # Old way
    )
    print(len(result.markdown))
async def main():
  await use_proxy()
if __name__ == "__main__":
  asyncio.run(main())

```

### New Code (Recommended)
```
import asyncio
from crawl4ai import AsyncWebCrawler, CacheMode
from crawl4ai.async_configs import CrawlerRunConfig
async def use_proxy():
  # Use CacheMode in CrawlerRunConfig
  config = CrawlerRunConfig(cache_mode=CacheMode.BYPASS) 
  async with AsyncWebCrawler(verbose=True) as crawler:
    result = await crawler.arun(
      url="https://www.nbcnews.com/business",
      config=config # Pass the configuration object
    )
    print(len(result.markdown))
async def main():
  await use_proxy()
if __name__ == "__main__":
  asyncio.run(main())

```

## Common Migration Patterns
Old Flag | New Mode  
---|---  
`bypass_cache=True` | `cache_mode=CacheMode.BYPASS`  
`disable_cache=True` | `cache_mode=CacheMode.DISABLED`  
`no_cache_read=True` | `cache_mode=CacheMode.WRITE_ONLY`  
`no_cache_write=True` | `cache_mode=CacheMode.READ_ONLY`  
Site built with [MkDocs](https://docs.crawl4ai.com/core/cache-modes/<http:/www.mkdocs.org>) and [Terminal for MkDocs](https://docs.crawl4ai.com/core/cache-modes/<https:/github.com/ntno/mkdocs-terminal>). 
##### Search
xClose
Type to start searching


==================================================

# URL: https://docs.crawl4ai.com/core/content-selection/

[Crawl4AI Documentation](https://docs.crawl4ai.com/core/content-selection/<https:/docs.crawl4ai.com/>)
  * [ Home ](https://docs.crawl4ai.com/core/content-selection/<../..>)
  * [ Quick Start ](https://docs.crawl4ai.com/core/content-selection/<../quickstart/>)
  * [ Search ](https://docs.crawl4ai.com/core/content-selection/<#>)


  * [Home](https://docs.crawl4ai.com/core/content-selection/<../..>)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/core/content-selection/<../installation/>)
    * [Docker Deployment](https://docs.crawl4ai.com/core/content-selection/<../docker-deploymeny/>)
  * [Quick Start](https://docs.crawl4ai.com/core/content-selection/<../quickstart/>)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/core/content-selection/blog/>)
    * [Changelog](https://docs.crawl4ai.com/core/content-selection/<https:/github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md>)
  * Core
    * [Simple Crawling](https://docs.crawl4ai.com/core/content-selection/<../simple-crawling/>)
    * [Crawler Result](https://docs.crawl4ai.com/core/content-selection/<../crawler-result/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/core/content-selection/<../browser-crawler-config/>)
    * [Markdown Generation](https://docs.crawl4ai.com/core/content-selection/<../markdown-generation/>)
    * [Fit Markdown](https://docs.crawl4ai.com/core/content-selection/<../fit-markdown/>)
    * [Page Interaction](https://docs.crawl4ai.com/core/content-selection/<../page-interaction/>)
    * Content Selection
    * [Cache Modes](https://docs.crawl4ai.com/core/content-selection/<../cache-modes/>)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/core/content-selection/<../local-files/>)
    * [Link & Media](https://docs.crawl4ai.com/core/content-selection/<../link-media/>)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/core/content-selection/advanced/advanced-features/>)
    * [File Downloading](https://docs.crawl4ai.com/core/content-selection/advanced/file-downloading/>)
    * [Lazy Loading](https://docs.crawl4ai.com/core/content-selection/advanced/lazy-loading/>)
    * [Hooks & Auth](https://docs.crawl4ai.com/core/content-selection/advanced/hooks-auth/>)
    * [Proxy & Security](https://docs.crawl4ai.com/core/content-selection/advanced/proxy-security/>)
    * [Session Management](https://docs.crawl4ai.com/core/content-selection/advanced/session-management/>)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/core/content-selection/advanced/multi-url-crawling/>)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/core/content-selection/advanced/crawl-dispatcher/>)
    * [Identity Based Crawling](https://docs.crawl4ai.com/core/content-selection/advanced/identity-based-crawling/>)
    * [SSL Certificate](https://docs.crawl4ai.com/core/content-selection/advanced/ssl-certificate/>)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/core/content-selection/extraction/no-llm-strategies/>)
    * [LLM Strategies](https://docs.crawl4ai.com/core/content-selection/extraction/llm-strategies/>)
    * [Clustering Strategies](https://docs.crawl4ai.com/core/content-selection/extraction/clustring-strategies/>)
    * [Chunking](https://docs.crawl4ai.com/core/content-selection/extraction/chunking/>)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/core/content-selection/api/async-webcrawler/>)
    * [arun()](https://docs.crawl4ai.com/core/content-selection/api/arun/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/core/content-selection/api/parameters/>)
    * [CrawlResult](https://docs.crawl4ai.com/core/content-selection/api/crawl-result/>)
    * [Strategies](https://docs.crawl4ai.com/core/content-selection/api/strategies/>)


  * [Content Selection](https://docs.crawl4ai.com/core/content-selection/<#content-selection>)
  * [1. CSS-Based Selection](https://docs.crawl4ai.com/core/content-selection/<#1-css-based-selection>)
  * [2. Content Filtering & Exclusions](https://docs.crawl4ai.com/core/content-selection/<#2-content-filtering-exclusions>)
  * [3. Handling Iframes](https://docs.crawl4ai.com/core/content-selection/<#3-handling-iframes>)
  * [4. Structured Extraction Examples](https://docs.crawl4ai.com/core/content-selection/<#4-structured-extraction-examples>)
  * [5. Comprehensive Example](https://docs.crawl4ai.com/core/content-selection/<#5-comprehensive-example>)
  * [6. Conclusion](https://docs.crawl4ai.com/core/content-selection/<#6-conclusion>)


# Content Selection
Crawl4AI provides multiple ways to **select** , **filter** , and **refine** the content from your crawls. Whether you need to target a specific CSS region, exclude entire tags, filter out external links, or remove certain domains and images, **`CrawlerRunConfig`**offers a wide range of parameters.
Below, we show how to configure these parameters and combine them for precise control.
## 1. CSS-Based Selection
A straightforward way to **limit** your crawl results to a certain region of the page is **`css_selector`**in**`CrawlerRunConfig`**:
```
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
async def main():
  config = CrawlerRunConfig(
    # e.g., first 30 items from Hacker News
    css_selector=".athing:nth-child(-n+30)" 
  )
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(
      url="https://news.ycombinator.com/newest", 
      config=config
    )
    print("Partial HTML length:", len(result.cleaned_html))
if __name__ == "__main__":
  asyncio.run(main())

```

**Result** : Only elements matching that selector remain in `result.cleaned_html`.
## 2. Content Filtering & Exclusions
### 2.1 Basic Overview
```
config = CrawlerRunConfig(
  # Content thresholds
  word_count_threshold=10,    # Minimum words per block
  # Tag exclusions
  excluded_tags=['form', 'header', 'footer', 'nav'],
  # Link filtering
  exclude_external_links=True,  
  exclude_social_media_links=True,
  # Block entire domains
  exclude_domains=["adtrackers.com", "spammynews.org"],  
  exclude_social_media_domains=["facebook.com", "twitter.com"],
  # Media filtering
  exclude_external_images=True
)

```

**Explanation** :
  * **`word_count_threshold`**: Ignores text blocks under X words. Helps skip trivial blocks like short nav or disclaimers.
  * **`excluded_tags`**: Removes entire tags (`<form>` , `<header>`, `<footer>`, etc.). 
  * **Link Filtering** : 
  * `exclude_external_links`: Strips out external links and may remove them from `result.links`. 
  * `exclude_social_media_links`: Removes links pointing to known social media domains. 
  * `exclude_domains`: A custom list of domains to block if discovered in links. 
  * `exclude_social_media_domains`: A curated list (override or add to it) for social media sites. 
  * **Media Filtering** : 
  * `exclude_external_images`: Discards images not hosted on the same domain as the main page (or its subdomains).


By default in case you set `exclude_social_media_links=True`, the following social media domains are excluded: 
```
[
  'facebook.com',
  'twitter.com',
  'x.com',
  'linkedin.com',
  'instagram.com',
  'pinterest.com',
  'tiktok.com',
  'snapchat.com',
  'reddit.com',
]

```

### 2.2 Example Usage
```
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
async def main():
  config = CrawlerRunConfig(
    css_selector="main.content", 
    word_count_threshold=10,
    excluded_tags=["nav", "footer"],
    exclude_external_links=True,
    exclude_social_media_links=True,
    exclude_domains=["ads.com", "spammytrackers.net"],
    exclude_external_images=True,
    cache_mode=CacheMode.BYPASS
  )
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(url="https://news.ycombinator.com", config=config)
    print("Cleaned HTML length:", len(result.cleaned_html))
if __name__ == "__main__":
  asyncio.run(main())

```

**Note** : If these parameters remove too much, reduce or disable them accordingly.
## 3. Handling Iframes
Some sites embed content in `<iframe>` tags. If you want that inline: 
```
config = CrawlerRunConfig(
  # Merge iframe content into the final output
  process_iframes=True,  
  remove_overlay_elements=True
)

```

**Usage** : 
```
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
async def main():
  config = CrawlerRunConfig(
    process_iframes=True,
    remove_overlay_elements=True
  )
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(
      url="https://example.org/iframe-demo", 
      config=config
    )
    print("Iframe-merged length:", len(result.cleaned_html))
if __name__ == "__main__":
  asyncio.run(main())

```

## 4. Structured Extraction Examples
You can combine content selection with a more advanced extraction strategy. For instance, a **CSS-based** or **LLM-based** extraction strategy can run on the filtered HTML.
### 4.1 Pattern-Based with `JsonCssExtractionStrategy`
```
import asyncio
import json
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
async def main():
  # Minimal schema for repeated items
  schema = {
    "name": "News Items",
    "baseSelector": "tr.athing",
    "fields": [
      {"name": "title", "selector": "a.storylink", "type": "text"},
      {
        "name": "link", 
        "selector": "a.storylink", 
        "type": "attribute", 
        "attribute": "href"
      }
    ]
  }
  config = CrawlerRunConfig(
    # Content filtering
    excluded_tags=["form", "header"],
    exclude_domains=["adsite.com"],
    # CSS selection or entire page
    css_selector="table.itemlist",
    # No caching for demonstration
    cache_mode=CacheMode.BYPASS,
    # Extraction strategy
    extraction_strategy=JsonCssExtractionStrategy(schema)
  )
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(
      url="https://news.ycombinator.com/newest", 
      config=config
    )
    data = json.loads(result.extracted_content)
    print("Sample extracted item:", data[:1]) # Show first item
if __name__ == "__main__":
  asyncio.run(main())

```

### 4.2 LLM-Based Extraction
```
import asyncio
import json
from pydantic import BaseModel, Field
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.extraction_strategy import LLMExtractionStrategy
class ArticleData(BaseModel):
  headline: str
  summary: str
async def main():
  llm_strategy = LLMExtractionStrategy(
    provider="openai/gpt-4",
    api_token="sk-YOUR_API_KEY",
    schema=ArticleData.schema(),
    extraction_type="schema",
    instruction="Extract 'headline' and a short 'summary' from the content."
  )
  config = CrawlerRunConfig(
    exclude_external_links=True,
    word_count_threshold=20,
    extraction_strategy=llm_strategy
  )
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(url="https://news.ycombinator.com", config=config)
    article = json.loads(result.extracted_content)
    print(article)
if __name__ == "__main__":
  asyncio.run(main())

```

Here, the crawler:
  * Filters out external links (`exclude_external_links=True`). 
  * Ignores very short text blocks (`word_count_threshold=20`). 
  * Passes the final HTML to your LLM strategy for an AI-driven parse.


## 5. Comprehensive Example
Below is a short function that unifies **CSS selection** , **exclusion** logic, and a pattern-based extraction, demonstrating how you can fine-tune your final data:
```
import asyncio
import json
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
async def extract_main_articles(url: str):
  schema = {
    "name": "ArticleBlock",
    "baseSelector": "div.article-block",
    "fields": [
      {"name": "headline", "selector": "h2", "type": "text"},
      {"name": "summary", "selector": ".summary", "type": "text"},
      {
        "name": "metadata",
        "type": "nested",
        "fields": [
          {"name": "author", "selector": ".author", "type": "text"},
          {"name": "date", "selector": ".date", "type": "text"}
        ]
      }
    ]
  }
  config = CrawlerRunConfig(
    # Keep only #main-content
    css_selector="#main-content",
    # Filtering
    word_count_threshold=10,
    excluded_tags=["nav", "footer"], 
    exclude_external_links=True,
    exclude_domains=["somebadsite.com"],
    exclude_external_images=True,
    # Extraction
    extraction_strategy=JsonCssExtractionStrategy(schema),
    cache_mode=CacheMode.BYPASS
  )
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(url=url, config=config)
    if not result.success:
      print(f"Error: {result.error_message}")
      return None
    return json.loads(result.extracted_content)
async def main():
  articles = await extract_main_articles("https://news.ycombinator.com/newest")
  if articles:
    print("Extracted Articles:", articles[:2]) # Show first 2
if __name__ == "__main__":
  asyncio.run(main())

```

**Why This Works** : - **CSS** scoping with `#main-content`. - Multiple **exclude_** parameters to remove domains, external images, etc. - A **JsonCssExtractionStrategy** to parse repeated article blocks.
## 6. Conclusion
By mixing **css_selector** scoping, **content filtering** parameters, and advanced **extraction strategies** , you can precisely **choose** which data to keep. Key parameters in **`CrawlerRunConfig`**for content selection include:
1. **`css_selector`**– Basic scoping to an element or region. 2.**`word_count_threshold`**– Skip short blocks. 3.**`excluded_tags`**– Remove entire HTML tags. 4.**`exclude_external_links`**,**`exclude_social_media_links`**,**`exclude_domains`**– Filter out unwanted links or domains. 5.**`exclude_external_images`**– Remove images from external sources. 6.**`process_iframes`**– Merge iframe content if needed.
Combine these with structured extraction (CSS, LLM-based, or others) to build powerful crawls that yield exactly the content you want, from raw or cleaned HTML up to sophisticated JSON structures. For more detail, see [Configuration Reference](https://docs.crawl4ai.com/core/content-selection/api/parameters/>). Enjoy curating your data to the max!
Site built with [MkDocs](https://docs.crawl4ai.com/core/content-selection/<http:/www.mkdocs.org>) and [Terminal for MkDocs](https://docs.crawl4ai.com/core/content-selection/<https:/github.com/ntno/mkdocs-terminal>). 
##### Search
xClose
Type to start searching


==================================================

# URL: https://docs.crawl4ai.com/core/crawler-result/

[Crawl4AI Documentation](https://docs.crawl4ai.com/core/crawler-result/<https:/docs.crawl4ai.com/>)
  * [ Home ](https://docs.crawl4ai.com/core/crawler-result/<../..>)
  * [ Quick Start ](https://docs.crawl4ai.com/core/crawler-result/<../quickstart/>)
  * [ Search ](https://docs.crawl4ai.com/core/crawler-result/<#>)


  * [Home](https://docs.crawl4ai.com/core/crawler-result/<../..>)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/core/crawler-result/<../installation/>)
    * [Docker Deployment](https://docs.crawl4ai.com/core/crawler-result/<../docker-deploymeny/>)
  * [Quick Start](https://docs.crawl4ai.com/core/crawler-result/<../quickstart/>)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/core/crawler-result/blog/>)
    * [Changelog](https://docs.crawl4ai.com/core/crawler-result/<https:/github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md>)
  * Core
    * [Simple Crawling](https://docs.crawl4ai.com/core/crawler-result/<../simple-crawling/>)
    * Crawler Result
    * [Browser & Crawler Config](https://docs.crawl4ai.com/core/crawler-result/<../browser-crawler-config/>)
    * [Markdown Generation](https://docs.crawl4ai.com/core/crawler-result/<../markdown-generation/>)
    * [Fit Markdown](https://docs.crawl4ai.com/core/crawler-result/<../fit-markdown/>)
    * [Page Interaction](https://docs.crawl4ai.com/core/crawler-result/<../page-interaction/>)
    * [Content Selection](https://docs.crawl4ai.com/core/crawler-result/<../content-selection/>)
    * [Cache Modes](https://docs.crawl4ai.com/core/crawler-result/<../cache-modes/>)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/core/crawler-result/<../local-files/>)
    * [Link & Media](https://docs.crawl4ai.com/core/crawler-result/<../link-media/>)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/core/crawler-result/advanced/advanced-features/>)
    * [File Downloading](https://docs.crawl4ai.com/core/crawler-result/advanced/file-downloading/>)
    * [Lazy Loading](https://docs.crawl4ai.com/core/crawler-result/advanced/lazy-loading/>)
    * [Hooks & Auth](https://docs.crawl4ai.com/core/crawler-result/advanced/hooks-auth/>)
    * [Proxy & Security](https://docs.crawl4ai.com/core/crawler-result/advanced/proxy-security/>)
    * [Session Management](https://docs.crawl4ai.com/core/crawler-result/advanced/session-management/>)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/core/crawler-result/advanced/multi-url-crawling/>)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/core/crawler-result/advanced/crawl-dispatcher/>)
    * [Identity Based Crawling](https://docs.crawl4ai.com/core/crawler-result/advanced/identity-based-crawling/>)
    * [SSL Certificate](https://docs.crawl4ai.com/core/crawler-result/advanced/ssl-certificate/>)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/core/crawler-result/extraction/no-llm-strategies/>)
    * [LLM Strategies](https://docs.crawl4ai.com/core/crawler-result/extraction/llm-strategies/>)
    * [Clustering Strategies](https://docs.crawl4ai.com/core/crawler-result/extraction/clustring-strategies/>)
    * [Chunking](https://docs.crawl4ai.com/core/crawler-result/extraction/chunking/>)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/core/crawler-result/api/async-webcrawler/>)
    * [arun()](https://docs.crawl4ai.com/core/crawler-result/api/arun/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/core/crawler-result/api/parameters/>)
    * [CrawlResult](https://docs.crawl4ai.com/core/crawler-result/api/crawl-result/>)
    * [Strategies](https://docs.crawl4ai.com/core/crawler-result/api/strategies/>)


  * [Crawl Result and Output](https://docs.crawl4ai.com/core/crawler-result/<#crawl-result-and-output>)
  * [1. The CrawlResult Model](https://docs.crawl4ai.com/core/crawler-result/<#1-the-crawlresult-model>)
  * [2. HTML Variants](https://docs.crawl4ai.com/core/crawler-result/<#2-html-variants>)
  * [3. Markdown Generation](https://docs.crawl4ai.com/core/crawler-result/<#3-markdown-generation>)
  * [4. Structured Extraction: extracted_content](https://docs.crawl4ai.com/core/crawler-result/<#4-structured-extraction-extracted_content>)
  * [5. More Fields: Links, Media, and More](https://docs.crawl4ai.com/core/crawler-result/<#5-more-fields-links-media-and-more>)
  * [6. Accessing These Fields](https://docs.crawl4ai.com/core/crawler-result/<#6-accessing-these-fields>)
  * [7. Next Steps](https://docs.crawl4ai.com/core/crawler-result/<#7-next-steps>)


# Crawl Result and Output
When you call `arun()` on a page, Crawl4AI returns a **`CrawlResult`**object containing everything you might need—raw HTML, a cleaned version, optional screenshots or PDFs, structured extraction results, and more. This document explains those fields and how they map to different output types.
## 1. The `CrawlResult` Model
Below is the core schema. Each field captures a different aspect of the crawl’s result:
```
class MarkdownGenerationResult(BaseModel):
  raw_markdown: str
  markdown_with_citations: str
  references_markdown: str
  fit_markdown: Optional[str] = None
  fit_html: Optional[str] = None
class CrawlResult(BaseModel):
  url: str
  html: str
  success: bool
  cleaned_html: Optional[str] = None
  media: Dict[str, List[Dict]] = {}
  links: Dict[str, List[Dict]] = {}
  downloaded_files: Optional[List[str]] = None
  screenshot: Optional[str] = None
  pdf : Optional[bytes] = None
  markdown: Optional[Union[str, MarkdownGenerationResult]] = None
  markdown_v2: Optional[MarkdownGenerationResult] = None
  extracted_content: Optional[str] = None
  metadata: Optional[dict] = None
  error_message: Optional[str] = None
  session_id: Optional[str] = None
  response_headers: Optional[dict] = None
  status_code: Optional[int] = None
  ssl_certificate: Optional[SSLCertificate] = None
  class Config:
    arbitrary_types_allowed = True

```

### Table: Key Fields in `CrawlResult`
Field (Name & Type) | Description  
---|---  
**url (`str`)** | The final or actual URL crawled (in case of redirects).  
**html (`str`)** | Original, unmodified page HTML. Good for debugging or custom processing.  
**success (`bool`)** | `True` if the crawl completed without major errors, else `False`.  
**cleaned_html (`Optional[str]`)** | Sanitized HTML with scripts/styles removed; can exclude tags if configured via `excluded_tags` etc.  
**media (`Dict[str, List[Dict]]`)** | Extracted media info (images, audio, etc.), each with attributes like `src`, `alt`, `score`, etc.  
**links (`Dict[str, List[Dict]]`)** | Extracted link data, split by `internal` and `external`. Each link usually has `href`, `text`, etc.  
**downloaded_files (`Optional[List[str]]`)** | If `accept_downloads=True` in `BrowserConfig`, this lists the filepaths of saved downloads.  
**screenshot (`Optional[str]`)** | Screenshot of the page (base64-encoded) if `screenshot=True`.  
**pdf (`Optional[bytes]`)** | PDF of the page if `pdf=True`.  
**markdown (`Optional[str or MarkdownGenerationResult]`)** | For now, `markdown_v2` holds a `MarkdownGenerationResult`. Over time, this will be consolidated into `markdown`. The generator can provide raw markdown, citations, references, and optionally `fit_markdown`.  
**markdown_v2 (`Optional[MarkdownGenerationResult]`)** | Legacy field for detailed markdown output. This will be replaced by `markdown` soon.  
**extracted_content (`Optional[str]`)** | The output of a structured extraction (CSS/LLM-based) stored as JSON string or other text.  
**metadata (`Optional[dict]`)** | Additional info about the crawl or extracted data.  
**error_message (`Optional[str]`)** | If `success=False`, contains a short description of what went wrong.  
**session_id (`Optional[str]`)** | The ID of the session used for multi-page or persistent crawling.  
**response_headers (`Optional[dict]`)** | HTTP response headers, if captured.  
**status_code (`Optional[int]`)** | HTTP status code (e.g., 200 for OK).  
**ssl_certificate (`Optional[SSLCertificate]`)** | SSL certificate info if `fetch_ssl_certificate=True`.  
## 2. HTML Variants
### `html`: Raw HTML
Crawl4AI preserves the exact HTML as `result.html`. Useful for:
  * Debugging page issues or checking the original content.
  * Performing your own specialized parse if needed.


### `cleaned_html`: Sanitized
If you specify any cleanup or exclusion parameters in `CrawlerRunConfig` (like `excluded_tags`, `remove_forms`, etc.), you’ll see the result here:
```
config = CrawlerRunConfig(
  excluded_tags=["form", "header", "footer"],
  keep_data_attributes=False
)
result = await crawler.arun("https://example.com", config=config)
print(result.cleaned_html) # Freed of forms, header, footer, data-* attributes

```

## 3. Markdown Generation
### 3.1 `markdown_v2` (Legacy) vs `markdown`
  * **`markdown_v2`**: The current location for detailed markdown output, returning a**`MarkdownGenerationResult`**object.
  * **`markdown`**: Eventually, we’re merging these fields. For now, you might see`result.markdown_v2` used widely in code examples.


**`MarkdownGenerationResult`**Fields:
Field | Description  
---|---  
**raw_markdown** | The basic HTML→Markdown conversion.  
**markdown_with_citations** | Markdown including inline citations that reference links at the end.  
**references_markdown** | The references/citations themselves (if `citations=True`).  
**fit_markdown** | The filtered/“fit” markdown if a content filter was used.  
**fit_html** | The filtered HTML that generated `fit_markdown`.  
### 3.2 Basic Example with a Markdown Generator
```
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
config = CrawlerRunConfig(
  markdown_generator=DefaultMarkdownGenerator(
    options={"citations": True, "body_width": 80} # e.g. pass html2text style options
  )
)
result = await crawler.arun(url="https://example.com", config=config)
md_res = result.markdown_v2 # or eventually 'result.markdown'
print(md_res.raw_markdown[:500])
print(md_res.markdown_with_citations)
print(md_res.references_markdown)

```

**Note** : If you use a filter like `PruningContentFilter`, you’ll get `fit_markdown` and `fit_html` as well.
## 4. Structured Extraction: `extracted_content`
If you run a JSON-based extraction strategy (CSS, XPath, LLM, etc.), the structured data is **not** stored in `markdown`—it’s placed in **`result.extracted_content`**as a JSON string (or sometimes plain text).
### Example: CSS Extraction with `raw://` HTML
```
import asyncio
import json
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
async def main():
  schema = {
    "name": "Example Items",
    "baseSelector": "div.item",
    "fields": [
      {"name": "title", "selector": "h2", "type": "text"},
      {"name": "link", "selector": "a", "type": "attribute", "attribute": "href"}
    ]
  }
  raw_html = "<div class='item'><h2>Item 1</h2><a href='https://example.com/item1'>Link 1</a></div>"
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(
      url="raw://" + raw_html,
      config=CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        extraction_strategy=JsonCssExtractionStrategy(schema)
      )
    )
    data = json.loads(result.extracted_content)
    print(data)
if __name__ == "__main__":
  asyncio.run(main())

```

Here: - `url="raw://..."` passes the HTML content directly, no network requests. - The **CSS** extraction strategy populates `result.extracted_content` with the JSON array `[{"title": "...", "link": "..."}]`.
## 5. More Fields: Links, Media, and More
### 5.1 `links`
A dictionary, typically with `"internal"` and `"external"` lists. Each entry might have `href`, `text`, `title`, etc. This is automatically captured if you haven’t disabled link extraction.
```
print(result.links["internal"][:3]) # Show first 3 internal links

```

### 5.2 `media`
Similarly, a dictionary with `"images"`, `"audio"`, `"video"`, etc. Each item could include `src`, `alt`, `score`, and more, if your crawler is set to gather them.
```
images = result.media.get("images", [])
for img in images:
  print("Image URL:", img["src"], "Alt:", img.get("alt"))

```

### 5.3 `screenshot` and `pdf`
If you set `screenshot=True` or `pdf=True` in **`CrawlerRunConfig`**, then:
  * `result.screenshot` contains a base64-encoded PNG string. 
  * `result.pdf` contains raw PDF bytes (you can write them to a file).


```
with open("page.pdf", "wb") as f:
  f.write(result.pdf)

```

### 5.4 `ssl_certificate`
If `fetch_ssl_certificate=True`, `result.ssl_certificate` holds details about the site’s SSL cert, such as issuer, validity dates, etc.
## 6. Accessing These Fields
After you run:
```
result = await crawler.arun(url="https://example.com", config=some_config)

```

Check any field:
```
if result.success:
  print(result.status_code, result.response_headers)
  print("Links found:", len(result.links.get("internal", [])))
  if result.markdown_v2:
    print("Markdown snippet:", result.markdown_v2.raw_markdown[:200])
  if result.extracted_content:
    print("Structured JSON:", result.extracted_content)
else:
  print("Error:", result.error_message)

```

**Remember** : Use `result.markdown_v2` for now. It will eventually become `result.markdown`.
## 7. Next Steps
  * **Markdown Generation** : Dive deeper into how to configure `DefaultMarkdownGenerator` and various filters. 
  * **Content Filtering** : Learn how to use `BM25ContentFilter` and `PruningContentFilter`.
  * **Session & Hooks**: If you want to manipulate the page or preserve state across multiple `arun()` calls, see the hooking or session docs. 
  * **LLM Extraction** : For complex or unstructured content requiring AI-driven parsing, check the LLM-based strategies doc.


**Enjoy** exploring all that `CrawlResult` offers—whether you need raw HTML, sanitized output, markdown, or fully structured data, Crawl4AI has you covered!
Site built with [MkDocs](https://docs.crawl4ai.com/core/crawler-result/<http:/www.mkdocs.org>) and [Terminal for MkDocs](https://docs.crawl4ai.com/core/crawler-result/<https:/github.com/ntno/mkdocs-terminal>). 
##### Search
xClose
Type to start searching


==================================================

# URL: https://docs.crawl4ai.com/core/docker-deploymeny/

[Crawl4AI Documentation](https://docs.crawl4ai.com/core/docker-deploymeny/<https:/docs.crawl4ai.com/>)
  * [ Home ](https://docs.crawl4ai.com/core/docker-deploymeny/<../..>)
  * [ Quick Start ](https://docs.crawl4ai.com/core/docker-deploymeny/<../quickstart/>)
  * [ Search ](https://docs.crawl4ai.com/core/docker-deploymeny/<#>)


  * [Home](https://docs.crawl4ai.com/core/docker-deploymeny/<../..>)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/core/docker-deploymeny/<../installation/>)
    * Docker Deployment
  * [Quick Start](https://docs.crawl4ai.com/core/docker-deploymeny/<../quickstart/>)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/core/docker-deploymeny/blog/>)
    * [Changelog](https://docs.crawl4ai.com/core/docker-deploymeny/<https:/github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md>)
  * Core
    * [Simple Crawling](https://docs.crawl4ai.com/core/docker-deploymeny/<../simple-crawling/>)
    * [Crawler Result](https://docs.crawl4ai.com/core/docker-deploymeny/<../crawler-result/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/core/docker-deploymeny/<../browser-crawler-config/>)
    * [Markdown Generation](https://docs.crawl4ai.com/core/docker-deploymeny/<../markdown-generation/>)
    * [Fit Markdown](https://docs.crawl4ai.com/core/docker-deploymeny/<../fit-markdown/>)
    * [Page Interaction](https://docs.crawl4ai.com/core/docker-deploymeny/<../page-interaction/>)
    * [Content Selection](https://docs.crawl4ai.com/core/docker-deploymeny/<../content-selection/>)
    * [Cache Modes](https://docs.crawl4ai.com/core/docker-deploymeny/<../cache-modes/>)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/core/docker-deploymeny/<../local-files/>)
    * [Link & Media](https://docs.crawl4ai.com/core/docker-deploymeny/<../link-media/>)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/core/docker-deploymeny/advanced/advanced-features/>)
    * [File Downloading](https://docs.crawl4ai.com/core/docker-deploymeny/advanced/file-downloading/>)
    * [Lazy Loading](https://docs.crawl4ai.com/core/docker-deploymeny/advanced/lazy-loading/>)
    * [Hooks & Auth](https://docs.crawl4ai.com/core/docker-deploymeny/advanced/hooks-auth/>)
    * [Proxy & Security](https://docs.crawl4ai.com/core/docker-deploymeny/advanced/proxy-security/>)
    * [Session Management](https://docs.crawl4ai.com/core/docker-deploymeny/advanced/session-management/>)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/core/docker-deploymeny/advanced/multi-url-crawling/>)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/core/docker-deploymeny/advanced/crawl-dispatcher/>)
    * [Identity Based Crawling](https://docs.crawl4ai.com/core/docker-deploymeny/advanced/identity-based-crawling/>)
    * [SSL Certificate](https://docs.crawl4ai.com/core/docker-deploymeny/advanced/ssl-certificate/>)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/core/docker-deploymeny/extraction/no-llm-strategies/>)
    * [LLM Strategies](https://docs.crawl4ai.com/core/docker-deploymeny/extraction/llm-strategies/>)
    * [Clustering Strategies](https://docs.crawl4ai.com/core/docker-deploymeny/extraction/clustring-strategies/>)
    * [Chunking](https://docs.crawl4ai.com/core/docker-deploymeny/extraction/chunking/>)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/core/docker-deploymeny/api/async-webcrawler/>)
    * [arun()](https://docs.crawl4ai.com/core/docker-deploymeny/api/arun/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/core/docker-deploymeny/api/parameters/>)
    * [CrawlResult](https://docs.crawl4ai.com/core/docker-deploymeny/api/crawl-result/>)
    * [Strategies](https://docs.crawl4ai.com/core/docker-deploymeny/api/strategies/>)


  * [Docker Deployment](https://docs.crawl4ai.com/core/docker-deploymeny/<#docker-deployment>)
  * [Quick Start 🚀](https://docs.crawl4ai.com/core/docker-deploymeny/<#quick-start>)
  * [Running with Docker Compose 🐳](https://docs.crawl4ai.com/core/docker-deploymeny/<#running-with-docker-compose>)
  * [API Security 🔒](https://docs.crawl4ai.com/core/docker-deploymeny/<#api-security>)
  * [Configuration Options 🔧](https://docs.crawl4ai.com/core/docker-deploymeny/<#configuration-options>)
  * [Usage Examples 📝](https://docs.crawl4ai.com/core/docker-deploymeny/<#usage-examples>)
  * [Platform-Specific Instructions 💻](https://docs.crawl4ai.com/core/docker-deploymeny/<#platform-specific-instructions>)
  * [Testing 🧪](https://docs.crawl4ai.com/core/docker-deploymeny/<#testing>)
  * [Advanced Configuration ⚙️](https://docs.crawl4ai.com/core/docker-deploymeny/<#advanced-configuration>)
  * [Troubleshooting 🔍](https://docs.crawl4ai.com/core/docker-deploymeny/<#troubleshooting>)
  * [Best Practices 🌟](https://docs.crawl4ai.com/core/docker-deploymeny/<#best-practices>)
  * [API Reference 📚](https://docs.crawl4ai.com/core/docker-deploymeny/<#api-reference>)


# Docker Deployment
Crawl4AI provides official Docker images for easy deployment and scalability. This guide covers installation, configuration, and usage of Crawl4AI in Docker environments.
## Quick Start 🚀
Pull and run the basic version:
```
# Basic run without security
docker pull unclecode/crawl4ai:basic
docker run -p 11235:11235 unclecode/crawl4ai:basic
# Run with API security enabled
docker run -p 11235:11235 -e CRAWL4AI_API_TOKEN=your_secret_token unclecode/crawl4ai:basic

```

## Running with Docker Compose 🐳
### Use Docker Compose (From Local Dockerfile or Docker Hub)
Crawl4AI provides flexibility to use Docker Compose for managing your containerized services. You can either build the image locally from the provided `Dockerfile` or use the pre-built image from Docker Hub.
### **Option 1: Using Docker Compose to Build Locally**
If you want to build the image locally, use the provided `docker-compose.local.yml` file.
```
docker-compose -f docker-compose.local.yml up -d

```

This will: 1. Build the Docker image from the provided `Dockerfile`. 2. Start the container and expose it on `http://localhost:11235`.
### **Option 2: Using Docker Compose with Pre-Built Image from Hub**
If you prefer using the pre-built image on Docker Hub, use the `docker-compose.hub.yml` file.
```
docker-compose -f docker-compose.hub.yml up -d

```

This will: 1. Pull the pre-built image `unclecode/crawl4ai:basic` (or `all`, depending on your configuration). 2. Start the container and expose it on `http://localhost:11235`.
### **Stopping the Running Services**
To stop the services started via Docker Compose, you can use:
```
docker-compose -f docker-compose.local.yml down
# OR
docker-compose -f docker-compose.hub.yml down

```

If the containers don’t stop and the application is still running, check the running containers:
```
docker ps

```

Find the `CONTAINER ID` of the running service and stop it forcefully:
```
docker stop <CONTAINER_ID>

```

### **Debugging with Docker Compose**
  * **Check Logs** : To view the container logs: 
```
docker-compose -f docker-compose.local.yml logs -f

```

  * **Remove Orphaned Containers** : If the service is still running unexpectedly: 
```
docker-compose -f docker-compose.local.yml down --remove-orphans

```

  * **Manually Remove Network** : If the network is still in use: 
```
docker network ls
docker network rm crawl4ai_default

```



### Why Use Docker Compose?
Docker Compose is the recommended way to deploy Crawl4AI because: 1. It simplifies multi-container setups. 2. Allows you to define environment variables, resources, and ports in a single file. 3. Makes it easier to switch between local development and production-ready images.
For example, your `docker-compose.yml` could include API keys, token settings, and memory limits, making deployment quick and consistent.
## API Security 🔒
### Understanding CRAWL4AI_API_TOKEN
The `CRAWL4AI_API_TOKEN` provides optional security for your Crawl4AI instance:
  * If `CRAWL4AI_API_TOKEN` is set: All API endpoints (except `/health`) require authentication
  * If `CRAWL4AI_API_TOKEN` is not set: The API is publicly accessible


```
# Secured Instance
docker run -p 11235:11235 -e CRAWL4AI_API_TOKEN=your_secret_token unclecode/crawl4ai:all
# Unsecured Instance
docker run -p 11235:11235 unclecode/crawl4ai:all

```

### Making API Calls
For secured instances, include the token in all requests:
```
import requests
# Setup headers if token is being used
api_token = "your_secret_token" # Same token set in CRAWL4AI_API_TOKEN
headers = {"Authorization": f"Bearer {api_token}"} if api_token else {}
# Making authenticated requests
response = requests.post(
  "http://localhost:11235/crawl",
  headers=headers,
  json={
    "urls": "https://example.com",
    "priority": 10
  }
)
# Checking task status
task_id = response.json()["task_id"]
status = requests.get(
  f"http://localhost:11235/task/{task_id}",
  headers=headers
)

```

### Using with Docker Compose
In your `docker-compose.yml`: 
```
services:
 crawl4ai:
  image: unclecode/crawl4ai:all
  environment:
   - CRAWL4AI_API_TOKEN=${CRAWL4AI_API_TOKEN:-} # Optional
  # ... other configuration

```

Then either: 1. Set in `.env` file: 
```
CRAWL4AI_API_TOKEN=your_secret_token

```

  1. Or set via command line: 
```
CRAWL4AI_API_TOKEN=your_secret_token docker-compose up

```



> **Security Note** : If you enable the API token, make sure to keep it secure and never commit it to version control. The token will be required for all API endpoints except the health check endpoint (`/health`).
## Configuration Options 🔧
### Environment Variables
You can configure the service using environment variables:
```
# Basic configuration
docker run -p 11235:11235 \
  -e MAX_CONCURRENT_TASKS=5 \
  unclecode/crawl4ai:all
# With security and LLM support
docker run -p 11235:11235 \
  -e CRAWL4AI_API_TOKEN=your_secret_token \
  -e OPENAI_API_KEY=sk-... \
  -e ANTHROPIC_API_KEY=sk-ant-... \
  unclecode/crawl4ai:all

```

### Using Docker Compose (Recommended) 🐳
Create a `docker-compose.yml`:
```
version: '3.8'
services:
 crawl4ai:
  image: unclecode/crawl4ai:all
  ports:
   - "11235:11235"
  environment:
   - CRAWL4AI_API_TOKEN=${CRAWL4AI_API_TOKEN:-} # Optional API security
   - MAX_CONCURRENT_TASKS=5
   # LLM Provider Keys
   - OPENAI_API_KEY=${OPENAI_API_KEY:-}
   - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY:-}
  volumes:
   - /dev/shm:/dev/shm
  deploy:
   resources:
    limits:
     memory: 4G
    reservations:
     memory: 1G

```

You can run it in two ways:
  1. Using environment variables directly: 
```
CRAWL4AI_API_TOKEN=secret123 OPENAI_API_KEY=sk-... docker-compose up

```

  2. Using a `.env` file (recommended): Create a `.env` file in the same directory: 
```
# API Security (optional)
CRAWL4AI_API_TOKEN=your_secret_token
# LLM Provider Keys
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
# Other Configuration
MAX_CONCURRENT_TASKS=5

```



Then simply run: 
```
docker-compose up

```

### Testing the Deployment 🧪
```
import requests
# For unsecured instances
def test_unsecured():
  # Health check
  health = requests.get("http://localhost:11235/health")
  print("Health check:", health.json())
  # Basic crawl
  response = requests.post(
    "http://localhost:11235/crawl",
    json={
      "urls": "https://www.nbcnews.com/business",
      "priority": 10
    }
  )
  task_id = response.json()["task_id"]
  print("Task ID:", task_id)
# For secured instances
def test_secured(api_token):
  headers = {"Authorization": f"Bearer {api_token}"}
  # Basic crawl with authentication
  response = requests.post(
    "http://localhost:11235/crawl",
    headers=headers,
    json={
      "urls": "https://www.nbcnews.com/business",
      "priority": 10
    }
  )
  task_id = response.json()["task_id"]
  print("Task ID:", task_id)

```

### LLM Extraction Example 🤖
When you've configured your LLM provider keys (via environment variables or `.env`), you can use LLM extraction:
```
request = {
  "urls": "https://example.com",
  "extraction_config": {
    "type": "llm",
    "params": {
      "provider": "openai/gpt-4",
      "instruction": "Extract main topics from the page"
    }
  }
}
# Make the request (add headers if using API security)
response = requests.post("http://localhost:11235/crawl", json=request)

```

> **Note** : Remember to add `.env` to your `.gitignore` to keep your API keys secure!
## Usage Examples 📝
### Basic Crawling
```
request = {
  "urls": "https://www.nbcnews.com/business",
  "priority": 10
}
response = requests.post("http://localhost:11235/crawl", json=request)
task_id = response.json()["task_id"]
# Get results
result = requests.get(f"http://localhost:11235/task/{task_id}")

```

### Structured Data Extraction
```
schema = {
  "name": "Crypto Prices",
  "baseSelector": ".cds-tableRow-t45thuk",
  "fields": [
    {
      "name": "crypto",
      "selector": "td:nth-child(1) h2",
      "type": "text",
    },
    {
      "name": "price",
      "selector": "td:nth-child(2)",
      "type": "text",
    }
  ],
}
request = {
  "urls": "https://www.coinbase.com/explore",
  "extraction_config": {
    "type": "json_css",
    "params": {"schema": schema}
  }
}

```

### Dynamic Content Handling
```
request = {
  "urls": "https://www.nbcnews.com/business",
  "js_code": [
    "const loadMoreButton = Array.from(document.querySelectorAll('button')).find(button => button.textContent.includes('Load More')); loadMoreButton && loadMoreButton.click();"
  ],
  "wait_for": "article.tease-card:nth-child(10)"
}

```

### AI-Powered Extraction (Full Version)
```
request = {
  "urls": "https://www.nbcnews.com/business",
  "extraction_config": {
    "type": "cosine",
    "params": {
      "semantic_filter": "business finance economy",
      "word_count_threshold": 10,
      "max_dist": 0.2,
      "top_k": 3
    }
  }
}

```

## Platform-Specific Instructions 💻
### macOS
```
docker pull unclecode/crawl4ai:basic
docker run -p 11235:11235 unclecode/crawl4ai:basic

```

### Ubuntu
```
# Basic version
docker pull unclecode/crawl4ai:basic
docker run -p 11235:11235 unclecode/crawl4ai:basic
# With GPU support
docker pull unclecode/crawl4ai:gpu
docker run --gpus all -p 11235:11235 unclecode/crawl4ai:gpu

```

### Windows (PowerShell)
```
docker pull unclecode/crawl4ai:basic
docker run -p 11235:11235 unclecode/crawl4ai:basic

```

## Testing 🧪
Save this as `test_docker.py`:
```
import requests
import json
import time
import sys
class Crawl4AiTester:
  def __init__(self, base_url: str = "http://localhost:11235"):
    self.base_url = base_url
  def submit_and_wait(self, request_data: dict, timeout: int = 300) -> dict:
    # Submit crawl job
    response = requests.post(f"{self.base_url}/crawl", json=request_data)
    task_id = response.json()["task_id"]
    print(f"Task ID: {task_id}")
    # Poll for result
    start_time = time.time()
    while True:
      if time.time() - start_time > timeout:
        raise TimeoutError(f"Task {task_id} timeout")
      result = requests.get(f"{self.base_url}/task/{task_id}")
      status = result.json()
      if status["status"] == "completed":
        return status
      time.sleep(2)
def test_deployment():
  tester = Crawl4AiTester()
  # Test basic crawl
  request = {
    "urls": "https://www.nbcnews.com/business",
    "priority": 10
  }
  result = tester.submit_and_wait(request)
  print("Basic crawl successful!")
  print(f"Content length: {len(result['result']['markdown'])}")
if __name__ == "__main__":
  test_deployment()

```

## Advanced Configuration ⚙️
### Crawler Parameters
The `crawler_params` field allows you to configure the browser instance and crawling behavior. Here are key parameters you can use:
```
request = {
  "urls": "https://example.com",
  "crawler_params": {
    # Browser Configuration
    "headless": True,          # Run in headless mode
    "browser_type": "chromium",     # chromium/firefox/webkit
    "user_agent": "custom-agent",    # Custom user agent
    "proxy": "http://proxy:8080",    # Proxy configuration
    # Performance & Behavior
    "page_timeout": 30000,        # Page load timeout (ms)
    "verbose": True,           # Enable detailed logging
    "semaphore_count": 5,        # Concurrent request limit
    # Anti-Detection Features
    "simulate_user": True,        # Simulate human behavior
    "magic": True,            # Advanced anti-detection
    "override_navigator": True,     # Override navigator properties
    # Session Management
    "user_data_dir": "./browser-data",  # Browser profile location
    "use_managed_browser": True,     # Use persistent browser
  }
}

```

### Extra Parameters
The `extra` field allows passing additional parameters directly to the crawler's `arun` function:
```
request = {
  "urls": "https://example.com",
  "extra": {
    "word_count_threshold": 10,     # Min words per block
    "only_text": True,          # Extract only text
    "bypass_cache": True,        # Force fresh crawl
    "process_iframes": True,       # Include iframe content
  }
}

```

### Complete Examples
1. **Advanced News Crawling**
```
request = {
  "urls": "https://www.nbcnews.com/business",
  "crawler_params": {
    "headless": True,
    "page_timeout": 30000,
    "remove_overlay_elements": True   # Remove popups
  },
  "extra": {
    "word_count_threshold": 50,     # Longer content blocks
    "bypass_cache": True         # Fresh content
  },
  "css_selector": ".article-body"
}

```

2. **Anti-Detection Configuration**
```
request = {
  "urls": "https://example.com",
  "crawler_params": {
    "simulate_user": True,
    "magic": True,
    "override_navigator": True,
    "user_agent": "Mozilla/5.0 ...",
    "headers": {
      "Accept-Language": "en-US,en;q=0.9"
    }
  }
}

```

3. **LLM Extraction with Custom Parameters**
```
request = {
  "urls": "https://openai.com/pricing",
  "extraction_config": {
    "type": "llm",
    "params": {
      "provider": "openai/gpt-4",
      "schema": pricing_schema
    }
  },
  "crawler_params": {
    "verbose": True,
    "page_timeout": 60000
  },
  "extra": {
    "word_count_threshold": 1,
    "only_text": True
  }
}

```

4. **Session-Based Dynamic Content**
```
request = {
  "urls": "https://example.com",
  "crawler_params": {
    "session_id": "dynamic_session",
    "headless": False,
    "page_timeout": 60000
  },
  "js_code": ["window.scrollTo(0, document.body.scrollHeight);"],
  "wait_for": "js:() => document.querySelectorAll('.item').length > 10",
  "extra": {
    "delay_before_return_html": 2.0
  }
}

```

5. **Screenshot with Custom Timing**
```
request = {
  "urls": "https://example.com",
  "screenshot": True,
  "crawler_params": {
    "headless": True,
    "screenshot_wait_for": ".main-content"
  },
  "extra": {
    "delay_before_return_html": 3.0
  }
}

```

### Parameter Reference Table
Category | Parameter | Type | Description  
---|---|---|---  
Browser | headless | bool | Run browser in headless mode  
Browser | browser_type | str | Browser engine selection  
Browser | user_agent | str | Custom user agent string  
Network | proxy | str | Proxy server URL  
Network | headers | dict | Custom HTTP headers  
Timing | page_timeout | int | Page load timeout (ms)  
Timing | delay_before_return_html | float | Wait before capture  
Anti-Detection | simulate_user | bool | Human behavior simulation  
Anti-Detection | magic | bool | Advanced protection  
Session | session_id | str | Browser session ID  
Session | user_data_dir | str | Profile directory  
Content | word_count_threshold | int | Minimum words per block  
Content | only_text | bool | Text-only extraction  
Content | process_iframes | bool | Include iframe content  
Debug | verbose | bool | Detailed logging  
Debug | log_console | bool | Browser console logs  
## Troubleshooting 🔍
### Common Issues
1. **Connection Refused**
```
Error: Connection refused at localhost:11235

```

Solution: Ensure the container is running and ports are properly mapped. 
2. **Resource Limits**
```
Error: No available slots

```

Solution: Increase MAX_CONCURRENT_TASKS or container resources. 
3. **GPU Access**
```
Error: GPU not found

```

Solution: Ensure proper NVIDIA drivers and use `--gpus all` flag. 
### Debug Mode
Access container for debugging: 
```
docker run -it --entrypoint /bin/bash unclecode/crawl4ai:all

```

View container logs: 
```
docker logs [container_id]

```

## Best Practices 🌟
1. **Resource Management** - Set appropriate memory and CPU limits - Monitor resource usage via health endpoint - Use basic version for simple crawling tasks
2. **Scaling** - Use multiple containers for high load - Implement proper load balancing - Monitor performance metrics
3. **Security** - Use environment variables for sensitive data - Implement proper network isolation - Regular security updates
## API Reference 📚
### Health Check
```
GET /health

```

### Submit Crawl Task
```
POST /crawl
Content-Type: application/json
{
  "urls": "string or array",
  "extraction_config": {
    "type": "basic|llm|cosine|json_css",
    "params": {}
  },
  "priority": 1-10,
  "ttl": 3600
}

```

### Get Task Status
```
GET /task/{task_id}

```

For more details, visit the [official documentation](https://docs.crawl4ai.com/core/docker-deploymeny/<https:/docs.crawl4ai.com/>).
Site built with [MkDocs](https://docs.crawl4ai.com/core/docker-deploymeny/<http:/www.mkdocs.org>) and [Terminal for MkDocs](https://docs.crawl4ai.com/core/docker-deploymeny/<https:/github.com/ntno/mkdocs-terminal>). 
##### Search
xClose
Type to start searching


==================================================

# URL: https://docs.crawl4ai.com/core/fit-markdown/

[Crawl4AI Documentation](https://docs.crawl4ai.com/core/fit-markdown/<https:/docs.crawl4ai.com/>)
  * [ Home ](https://docs.crawl4ai.com/core/fit-markdown/<../..>)
  * [ Quick Start ](https://docs.crawl4ai.com/core/fit-markdown/<../quickstart/>)
  * [ Search ](https://docs.crawl4ai.com/core/fit-markdown/<#>)


  * [Home](https://docs.crawl4ai.com/core/fit-markdown/<../..>)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/core/fit-markdown/<../installation/>)
    * [Docker Deployment](https://docs.crawl4ai.com/core/fit-markdown/<../docker-deploymeny/>)
  * [Quick Start](https://docs.crawl4ai.com/core/fit-markdown/<../quickstart/>)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/core/fit-markdown/blog/>)
    * [Changelog](https://docs.crawl4ai.com/core/fit-markdown/<https:/github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md>)
  * Core
    * [Simple Crawling](https://docs.crawl4ai.com/core/fit-markdown/<../simple-crawling/>)
    * [Crawler Result](https://docs.crawl4ai.com/core/fit-markdown/<../crawler-result/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/core/fit-markdown/<../browser-crawler-config/>)
    * [Markdown Generation](https://docs.crawl4ai.com/core/fit-markdown/<../markdown-generation/>)
    * Fit Markdown
    * [Page Interaction](https://docs.crawl4ai.com/core/fit-markdown/<../page-interaction/>)
    * [Content Selection](https://docs.crawl4ai.com/core/fit-markdown/<../content-selection/>)
    * [Cache Modes](https://docs.crawl4ai.com/core/fit-markdown/<../cache-modes/>)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/core/fit-markdown/<../local-files/>)
    * [Link & Media](https://docs.crawl4ai.com/core/fit-markdown/<../link-media/>)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/core/fit-markdown/advanced/advanced-features/>)
    * [File Downloading](https://docs.crawl4ai.com/core/fit-markdown/advanced/file-downloading/>)
    * [Lazy Loading](https://docs.crawl4ai.com/core/fit-markdown/advanced/lazy-loading/>)
    * [Hooks & Auth](https://docs.crawl4ai.com/core/fit-markdown/advanced/hooks-auth/>)
    * [Proxy & Security](https://docs.crawl4ai.com/core/fit-markdown/advanced/proxy-security/>)
    * [Session Management](https://docs.crawl4ai.com/core/fit-markdown/advanced/session-management/>)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/core/fit-markdown/advanced/multi-url-crawling/>)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/core/fit-markdown/advanced/crawl-dispatcher/>)
    * [Identity Based Crawling](https://docs.crawl4ai.com/core/fit-markdown/advanced/identity-based-crawling/>)
    * [SSL Certificate](https://docs.crawl4ai.com/core/fit-markdown/advanced/ssl-certificate/>)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/core/fit-markdown/extraction/no-llm-strategies/>)
    * [LLM Strategies](https://docs.crawl4ai.com/core/fit-markdown/extraction/llm-strategies/>)
    * [Clustering Strategies](https://docs.crawl4ai.com/core/fit-markdown/extraction/clustring-strategies/>)
    * [Chunking](https://docs.crawl4ai.com/core/fit-markdown/extraction/chunking/>)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/core/fit-markdown/api/async-webcrawler/>)
    * [arun()](https://docs.crawl4ai.com/core/fit-markdown/api/arun/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/core/fit-markdown/api/parameters/>)
    * [CrawlResult](https://docs.crawl4ai.com/core/fit-markdown/api/crawl-result/>)
    * [Strategies](https://docs.crawl4ai.com/core/fit-markdown/api/strategies/>)


  * [Fit Markdown with Pruning & BM25](https://docs.crawl4ai.com/core/fit-markdown/<#fit-markdown-with-pruning-bm25>)
  * [1. How “Fit Markdown” Works](https://docs.crawl4ai.com/core/fit-markdown/<#1-how-fit-markdown-works>)
  * [2. PruningContentFilter](https://docs.crawl4ai.com/core/fit-markdown/<#2-pruningcontentfilter>)
  * [3. BM25ContentFilter](https://docs.crawl4ai.com/core/fit-markdown/<#3-bm25contentfilter>)
  * [4. Accessing the “Fit” Output](https://docs.crawl4ai.com/core/fit-markdown/<#4-accessing-the-fit-output>)
  * [5. Code Patterns Recap](https://docs.crawl4ai.com/core/fit-markdown/<#5-code-patterns-recap>)
  * [6. Combining with “word_count_threshold” & Exclusions](https://docs.crawl4ai.com/core/fit-markdown/<#6-combining-with-word_count_threshold-exclusions>)
  * [7. Custom Filters](https://docs.crawl4ai.com/core/fit-markdown/<#7-custom-filters>)
  * [8. Final Thoughts](https://docs.crawl4ai.com/core/fit-markdown/<#8-final-thoughts>)


# Fit Markdown with Pruning & BM25
**Fit Markdown** is a specialized **filtered** version of your page’s markdown, focusing on the most relevant content. By default, Crawl4AI converts the entire HTML into a broad **raw_markdown**. With fit markdown, we apply a **content filter** algorithm (e.g., **Pruning** or **BM25**) to remove or rank low-value sections—such as repetitive sidebars, shallow text blocks, or irrelevancies—leaving a concise textual “core.”
## 1. How “Fit Markdown” Works
### 1.1 The `content_filter`
In **`CrawlerRunConfig`**, you can specify a**`content_filter`**to shape how content is pruned or ranked before final markdown generation. A filter’s logic is applied**before** or **during** the HTML→Markdown process, producing:
  * **`result.markdown_v2.raw_markdown`**(unfiltered)
  * **`result.markdown_v2.fit_markdown`**(filtered or “fit” version)
  * **`result.markdown_v2.fit_html`**(the corresponding HTML snippet that produced`fit_markdown`)


> **Note** : We’re currently storing the result in `markdown_v2`, but eventually we’ll unify it as `result.markdown`.
### 1.2 Common Filters
1. **PruningContentFilter** – Scores each node by text density, link density, and tag importance, discarding those below a threshold. 2. **BM25ContentFilter** – Focuses on textual relevance using BM25 ranking, especially useful if you have a specific user query (e.g., “machine learning” or “food nutrition”).
## 2. PruningContentFilter
**Pruning** discards less relevant nodes based on **text density, link density, and tag importance**. It’s a heuristic-based approach—if certain sections appear too “thin” or too “spammy,” they’re pruned.
### 2.1 Usage Example
```
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.content_filter_strategy import PruningContentFilter
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
async def main():
  # Step 1: Create a pruning filter
  prune_filter = PruningContentFilter(
    # Lower → more content retained, higher → more content pruned
    threshold=0.45,      
    # "fixed" or "dynamic"
    threshold_type="dynamic", 
    # Ignore nodes with <5 words
    min_word_threshold=5   
  )
  # Step 2: Insert it into a Markdown Generator
  md_generator = DefaultMarkdownGenerator(content_filter=prune_filter)
  # Step 3: Pass it to CrawlerRunConfig
  config = CrawlerRunConfig(
    markdown_generator=md_generator
  )
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(
      url="https://news.ycombinator.com", 
      config=config
    )
    if result.success:
      # 'fit_markdown' is your pruned content, focusing on "denser" text
      print("Raw Markdown length:", len(result.markdown_v2.raw_markdown))
      print("Fit Markdown length:", len(result.markdown_v2.fit_markdown))
    else:
      print("Error:", result.error_message)
if __name__ == "__main__":
  asyncio.run(main())

```

### 2.2 Key Parameters
  * **`min_word_threshold`**(int): If a block has fewer words than this, it’s pruned.
  * **`threshold_type`**(str):
  * `"fixed"` → each node must exceed `threshold` (0–1). 
  * `"dynamic"` → node scoring adjusts according to tag type, text/link density, etc. 
  * **`threshold`**(float, default ~0.48): The base or “anchor” cutoff.


**Algorithmic Factors** :
  * **Text density** – Encourages blocks that have a higher ratio of text to overall content. 
  * **Link density** – Penalizes sections that are mostly links. 
  * **Tag importance** – e.g., an `<article>` or `<p>` might be more important than a `<div>`. 
  * **Structural context** – If a node is deeply nested or in a suspected sidebar, it might be deprioritized.


## 3. BM25ContentFilter
**BM25** is a classical text ranking algorithm often used in search engines. If you have a **user query** or rely on page metadata to derive a query, BM25 can identify which text chunks best match that query.
### 3.1 Usage Example
```
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.content_filter_strategy import BM25ContentFilter
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
async def main():
  # 1) A BM25 filter with a user query
  bm25_filter = BM25ContentFilter(
    user_query="startup fundraising tips",
    # Adjust for stricter or looser results
    bm25_threshold=1.2 
  )
  # 2) Insert into a Markdown Generator
  md_generator = DefaultMarkdownGenerator(content_filter=bm25_filter)
  # 3) Pass to crawler config
  config = CrawlerRunConfig(
    markdown_generator=md_generator
  )
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(
      url="https://news.ycombinator.com", 
      config=config
    )
    if result.success:
      print("Fit Markdown (BM25 query-based):")
      print(result.markdown_v2.fit_markdown)
    else:
      print("Error:", result.error_message)
if __name__ == "__main__":
  asyncio.run(main())

```

### 3.2 Parameters
  * **`user_query`**(str, optional): E.g.`"machine learning"`. If blank, the filter tries to glean a query from page metadata. 
  * **`bm25_threshold`**(float, default 1.0):
  * Higher → fewer chunks but more relevant. 
  * Lower → more inclusive. 


> In more advanced scenarios, you might see parameters like `use_stemming`, `case_sensitive`, or `priority_tags` to refine how text is tokenized or weighted.
## 4. Accessing the “Fit” Output
After the crawl, your “fit” content is found in **`result.markdown_v2.fit_markdown`**. In future versions, it will be**`result.markdown.fit_markdown`**. Meanwhile:
```
fit_md = result.markdown_v2.fit_markdown
fit_html = result.markdown_v2.fit_html

```

If the content filter is **BM25** , you might see additional logic or references in `fit_markdown` that highlight relevant segments. If it’s **Pruning** , the text is typically well-cleaned but not necessarily matched to a query.
## 5. Code Patterns Recap
### 5.1 Pruning
```
prune_filter = PruningContentFilter(
  threshold=0.5,
  threshold_type="fixed",
  min_word_threshold=10
)
md_generator = DefaultMarkdownGenerator(content_filter=prune_filter)
config = CrawlerRunConfig(markdown_generator=md_generator)
# => result.markdown_v2.fit_markdown

```

### 5.2 BM25
```
bm25_filter = BM25ContentFilter(
  user_query="health benefits fruit",
  bm25_threshold=1.2
)
md_generator = DefaultMarkdownGenerator(content_filter=bm25_filter)
config = CrawlerRunConfig(markdown_generator=md_generator)
# => result.markdown_v2.fit_markdown

```

## 6. Combining with “word_count_threshold” & Exclusions
Remember you can also specify:
```
config = CrawlerRunConfig(
  word_count_threshold=10,
  excluded_tags=["nav", "footer", "header"],
  exclude_external_links=True,
  markdown_generator=DefaultMarkdownGenerator(
    content_filter=PruningContentFilter(threshold=0.5)
  )
)

```

Thus, **multi-level** filtering occurs:
  1. The crawler’s `excluded_tags` are removed from the HTML first. 
  2. The content filter (Pruning, BM25, or custom) prunes or ranks the remaining text blocks. 
  3. The final “fit” content is generated in `result.markdown_v2.fit_markdown`.


## 7. Custom Filters
If you need a different approach (like a specialized ML model or site-specific heuristics), you can create a new class inheriting from `RelevantContentFilter` and implement `filter_content(html)`. Then inject it into your **markdown generator** :
```
from crawl4ai.content_filter_strategy import RelevantContentFilter
class MyCustomFilter(RelevantContentFilter):
  def filter_content(self, html, min_word_threshold=None):
    # parse HTML, implement custom logic
    return [block for block in ... if ... some condition...]

```

**Steps** :
  1. Subclass `RelevantContentFilter`. 
  2. Implement `filter_content(...)`. 
  3. Use it in your `DefaultMarkdownGenerator(content_filter=MyCustomFilter(...))`.


## 8. Final Thoughts
**Fit Markdown** is a crucial feature for:
  * **Summaries** : Quickly get the important text from a cluttered page. 
  * **Search** : Combine with **BM25** to produce content relevant to a query. 
  * **AI Pipelines** : Filter out boilerplate so LLM-based extraction or summarization runs on denser text.


**Key Points** : - **PruningContentFilter** : Great if you just want the “meatiest” text without a user query. - **BM25ContentFilter** : Perfect for query-based extraction or searching. - Combine with **`excluded_tags`,`exclude_external_links` , `word_count_threshold`** to refine your final “fit” text. - Fit markdown ends up in **`result.markdown_v2.fit_markdown`**; eventually**`result.markdown.fit_markdown`**in future versions.
With these tools, you can **zero in** on the text that truly matters, ignoring spammy or boilerplate content, and produce a concise, relevant “fit markdown” for your AI or data pipelines. Happy pruning and searching!
  * Last Updated: 2025-01-01


Site built with [MkDocs](https://docs.crawl4ai.com/core/fit-markdown/<http:/www.mkdocs.org>) and [Terminal for MkDocs](https://docs.crawl4ai.com/core/fit-markdown/<https:/github.com/ntno/mkdocs-terminal>). 
##### Search
xClose
Type to start searching


==================================================

# URL: https://docs.crawl4ai.com/core/installation/

[Crawl4AI Documentation](https://docs.crawl4ai.com/core/installation/<https:/docs.crawl4ai.com/>)
  * [ Home ](https://docs.crawl4ai.com/core/installation/<../..>)
  * [ Quick Start ](https://docs.crawl4ai.com/core/installation/<../quickstart/>)
  * [ Search ](https://docs.crawl4ai.com/core/installation/<#>)


  * [Home](https://docs.crawl4ai.com/core/installation/<../..>)
  * Setup & Installation
    * Installation
    * [Docker Deployment](https://docs.crawl4ai.com/core/installation/<../docker-deploymeny/>)
  * [Quick Start](https://docs.crawl4ai.com/core/installation/<../quickstart/>)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/core/installation/blog/>)
    * [Changelog](https://docs.crawl4ai.com/core/installation/<https:/github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md>)
  * Core
    * [Simple Crawling](https://docs.crawl4ai.com/core/installation/<../simple-crawling/>)
    * [Crawler Result](https://docs.crawl4ai.com/core/installation/<../crawler-result/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/core/installation/<../browser-crawler-config/>)
    * [Markdown Generation](https://docs.crawl4ai.com/core/installation/<../markdown-generation/>)
    * [Fit Markdown](https://docs.crawl4ai.com/core/installation/<../fit-markdown/>)
    * [Page Interaction](https://docs.crawl4ai.com/core/installation/<../page-interaction/>)
    * [Content Selection](https://docs.crawl4ai.com/core/installation/<../content-selection/>)
    * [Cache Modes](https://docs.crawl4ai.com/core/installation/<../cache-modes/>)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/core/installation/<../local-files/>)
    * [Link & Media](https://docs.crawl4ai.com/core/installation/<../link-media/>)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/core/installation/advanced/advanced-features/>)
    * [File Downloading](https://docs.crawl4ai.com/core/installation/advanced/file-downloading/>)
    * [Lazy Loading](https://docs.crawl4ai.com/core/installation/advanced/lazy-loading/>)
    * [Hooks & Auth](https://docs.crawl4ai.com/core/installation/advanced/hooks-auth/>)
    * [Proxy & Security](https://docs.crawl4ai.com/core/installation/advanced/proxy-security/>)
    * [Session Management](https://docs.crawl4ai.com/core/installation/advanced/session-management/>)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/core/installation/advanced/multi-url-crawling/>)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/core/installation/advanced/crawl-dispatcher/>)
    * [Identity Based Crawling](https://docs.crawl4ai.com/core/installation/advanced/identity-based-crawling/>)
    * [SSL Certificate](https://docs.crawl4ai.com/core/installation/advanced/ssl-certificate/>)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/core/installation/extraction/no-llm-strategies/>)
    * [LLM Strategies](https://docs.crawl4ai.com/core/installation/extraction/llm-strategies/>)
    * [Clustering Strategies](https://docs.crawl4ai.com/core/installation/extraction/clustring-strategies/>)
    * [Chunking](https://docs.crawl4ai.com/core/installation/extraction/chunking/>)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/core/installation/api/async-webcrawler/>)
    * [arun()](https://docs.crawl4ai.com/core/installation/api/arun/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/core/installation/api/parameters/>)
    * [CrawlResult](https://docs.crawl4ai.com/core/installation/api/crawl-result/>)
    * [Strategies](https://docs.crawl4ai.com/core/installation/api/strategies/>)


  * [Installation & Setup (2023 Edition)](https://docs.crawl4ai.com/core/installation/<#installation-setup-2023-edition>)
  * [1. Basic Installation](https://docs.crawl4ai.com/core/installation/<#1-basic-installation>)
  * [2. Initial Setup & Diagnostics](https://docs.crawl4ai.com/core/installation/<#2-initial-setup-diagnostics>)
  * [3. Verifying Installation: A Simple Crawl (Skip this step if you already run crawl4ai-doctor)](https://docs.crawl4ai.com/core/installation/<#3-verifying-installation-a-simple-crawl-skip-this-step-if-you-already-run-crawl4ai-doctor>)
  * [4. Advanced Installation (Optional)](https://docs.crawl4ai.com/core/installation/<#4-advanced-installation-optional>)
  * [5. Docker (Experimental)](https://docs.crawl4ai.com/core/installation/<#5-docker-experimental>)
  * [6. Local Server Mode (Legacy)](https://docs.crawl4ai.com/core/installation/<#6-local-server-mode-legacy>)
  * [Summary](https://docs.crawl4ai.com/core/installation/<#summary>)


# Installation & Setup (2023 Edition)
## 1. Basic Installation
```
pip install crawl4ai

```

This installs the **core** Crawl4AI library along with essential dependencies. **No** advanced features (like transformers or PyTorch) are included yet.
## 2. Initial Setup & Diagnostics
### 2.1 Run the Setup Command
After installing, call:
```
crawl4ai-setup

```

**What does it do?** - Installs or updates required Playwright browsers (Chromium, Firefox, etc.) - Performs OS-level checks (e.g., missing libs on Linux) - Confirms your environment is ready to crawl
### 2.2 Diagnostics
Optionally, you can run **diagnostics** to confirm everything is functioning:
```
crawl4ai-doctor

```

This command attempts to: - Check Python version compatibility - Verify Playwright installation - Inspect environment variables or library conflicts
If any issues arise, follow its suggestions (e.g., installing additional system packages) and re-run `crawl4ai-setup`.
## 3. Verifying Installation: A Simple Crawl (Skip this step if you already run `crawl4ai-doctor`)
Below is a minimal Python script demonstrating a **basic** crawl. It uses our new **`BrowserConfig`**and**`CrawlerRunConfig`**for clarity, though no custom settings are passed in this example:
```
import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig
async def main():
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(
      url="https://www.example.com",
    )
    print(result.markdown[:300]) # Show the first 300 characters of extracted text
if __name__ == "__main__":
  asyncio.run(main())

```

**Expected** outcome: - A headless browser session loads `example.com` - Crawl4AI returns ~300 characters of markdown. If errors occur, rerun `crawl4ai-doctor` or manually ensure Playwright is installed correctly.
## 4. Advanced Installation (Optional)
**Warning** : Only install these **if you truly need them**. They bring in larger dependencies, including big models, which can increase disk usage and memory load significantly.
### 4.1 Torch, Transformers, or All
  * **Text Clustering (Torch)**
```
pip install crawl4ai[torch]
crawl4ai-setup

```

Installs PyTorch-based features (e.g., cosine similarity or advanced semantic chunking). 
  * **Transformers**
```
pip install crawl4ai[transformer]
crawl4ai-setup

```

Adds Hugging Face-based summarization or generation strategies. 
  * **All Features**
```
pip install crawl4ai[all]
crawl4ai-setup

```



#### (Optional) Pre-Fetching Models
```
crawl4ai-download-models

```

This step caches large models locally (if needed). **Only do this** if your workflow requires them. 
## 5. Docker (Experimental)
We provide a **temporary** Docker approach for testing. **It’s not stable and may break** with future releases. We plan a major Docker revamp in a future stable version, 2025 Q1. If you still want to try:
```
docker pull unclecode/crawl4ai:basic
docker run -p 11235:11235 unclecode/crawl4ai:basic

```

You can then make POST requests to `http://localhost:11235/crawl` to perform crawls. **Production usage** is discouraged until our new Docker approach is ready (planned in Jan or Feb 2025).
## 6. Local Server Mode (Legacy)
Some older docs mention running Crawl4AI as a local server. This approach has been **partially replaced** by the new Docker-based prototype and upcoming stable server release. You can experiment, but expect major changes. Official local server instructions will arrive once the new Docker architecture is finalized.
## Summary
1. **Install** with `pip install crawl4ai` and run `crawl4ai-setup`. 2. **Diagnose** with `crawl4ai-doctor` if you see errors. 3. **Verify** by crawling `example.com` with minimal `BrowserConfig` + `CrawlerRunConfig`. 4. **Advanced** features (Torch, Transformers) are **optional** —avoid them if you don’t need them (they significantly increase resource usage). 5. **Docker** is **experimental** —use at your own risk until the stable version is released. 6. **Local server** references in older docs are largely deprecated; a new solution is in progress.
**Got questions?** Check [GitHub issues](https://docs.crawl4ai.com/core/installation/<https:/github.com/unclecode/crawl4ai/issues>) for updates or ask the community!
Site built with [MkDocs](https://docs.crawl4ai.com/core/installation/<http:/www.mkdocs.org>) and [Terminal for MkDocs](https://docs.crawl4ai.com/core/installation/<https:/github.com/ntno/mkdocs-terminal>). 
##### Search
xClose
Type to start searching


==================================================

# URL: https://docs.crawl4ai.com/core/link-media/

[Crawl4AI Documentation](https://docs.crawl4ai.com/core/link-media/<https:/docs.crawl4ai.com/>)
  * [ Home ](https://docs.crawl4ai.com/core/link-media/<../..>)
  * [ Quick Start ](https://docs.crawl4ai.com/core/link-media/<../quickstart/>)
  * [ Search ](https://docs.crawl4ai.com/core/link-media/<#>)


  * [Home](https://docs.crawl4ai.com/core/link-media/<../..>)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/core/link-media/<../installation/>)
    * [Docker Deployment](https://docs.crawl4ai.com/core/link-media/<../docker-deploymeny/>)
  * [Quick Start](https://docs.crawl4ai.com/core/link-media/<../quickstart/>)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/core/link-media/blog/>)
    * [Changelog](https://docs.crawl4ai.com/core/link-media/<https:/github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md>)
  * Core
    * [Simple Crawling](https://docs.crawl4ai.com/core/link-media/<../simple-crawling/>)
    * [Crawler Result](https://docs.crawl4ai.com/core/link-media/<../crawler-result/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/core/link-media/<../browser-crawler-config/>)
    * [Markdown Generation](https://docs.crawl4ai.com/core/link-media/<../markdown-generation/>)
    * [Fit Markdown](https://docs.crawl4ai.com/core/link-media/<../fit-markdown/>)
    * [Page Interaction](https://docs.crawl4ai.com/core/link-media/<../page-interaction/>)
    * [Content Selection](https://docs.crawl4ai.com/core/link-media/<../content-selection/>)
    * [Cache Modes](https://docs.crawl4ai.com/core/link-media/<../cache-modes/>)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/core/link-media/<../local-files/>)
    * Link & Media
  * Advanced
    * [Overview](https://docs.crawl4ai.com/core/link-media/advanced/advanced-features/>)
    * [File Downloading](https://docs.crawl4ai.com/core/link-media/advanced/file-downloading/>)
    * [Lazy Loading](https://docs.crawl4ai.com/core/link-media/advanced/lazy-loading/>)
    * [Hooks & Auth](https://docs.crawl4ai.com/core/link-media/advanced/hooks-auth/>)
    * [Proxy & Security](https://docs.crawl4ai.com/core/link-media/advanced/proxy-security/>)
    * [Session Management](https://docs.crawl4ai.com/core/link-media/advanced/session-management/>)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/core/link-media/advanced/multi-url-crawling/>)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/core/link-media/advanced/crawl-dispatcher/>)
    * [Identity Based Crawling](https://docs.crawl4ai.com/core/link-media/advanced/identity-based-crawling/>)
    * [SSL Certificate](https://docs.crawl4ai.com/core/link-media/advanced/ssl-certificate/>)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/core/link-media/extraction/no-llm-strategies/>)
    * [LLM Strategies](https://docs.crawl4ai.com/core/link-media/extraction/llm-strategies/>)
    * [Clustering Strategies](https://docs.crawl4ai.com/core/link-media/extraction/clustring-strategies/>)
    * [Chunking](https://docs.crawl4ai.com/core/link-media/extraction/chunking/>)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/core/link-media/api/async-webcrawler/>)
    * [arun()](https://docs.crawl4ai.com/core/link-media/api/arun/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/core/link-media/api/parameters/>)
    * [CrawlResult](https://docs.crawl4ai.com/core/link-media/api/crawl-result/>)
    * [Strategies](https://docs.crawl4ai.com/core/link-media/api/strategies/>)


  * [Link & Media](https://docs.crawl4ai.com/core/link-media/<#link-media>)
  * [1. Link Extraction](https://docs.crawl4ai.com/core/link-media/<#1-link-extraction>)
  * [2. Domain Filtering](https://docs.crawl4ai.com/core/link-media/<#2-domain-filtering>)
  * [3. Media Extraction](https://docs.crawl4ai.com/core/link-media/<#3-media-extraction>)
  * [4. Putting It All Together: Link & Media Filtering](https://docs.crawl4ai.com/core/link-media/<#4-putting-it-all-together-link-media-filtering>)
  * [5. Common Pitfalls & Tips](https://docs.crawl4ai.com/core/link-media/<#5-common-pitfalls-tips>)


# Link & Media
In this tutorial, you’ll learn how to:
  1. Extract links (internal, external) from crawled pages 
  2. Filter or exclude specific domains (e.g., social media or custom domains) 
  3. Access and manage media data (especially images) in the crawl result 
  4. Configure your crawler to exclude or prioritize certain images


> **Prerequisites** - You have completed or are familiar with the [AsyncWebCrawler Basics](https://docs.crawl4ai.com/core/link-media/<../simple-crawling/>) tutorial. - You can run Crawl4AI in your environment (Playwright, Python, etc.).
Below is a revised version of the **Link Extraction** and **Media Extraction** sections that includes example data structures showing how links and media items are stored in `CrawlResult`. Feel free to adjust any field names or descriptions to match your actual output.
## 1. Link Extraction
### 1.1 `result.links`
When you call `arun()` or `arun_many()` on a URL, Crawl4AI automatically extracts links and stores them in the `links` field of `CrawlResult`. By default, the crawler tries to distinguish **internal** links (same domain) from **external** links (different domains).
**Basic Example** :
```
from crawl4ai import AsyncWebCrawler
async with AsyncWebCrawler() as crawler:
  result = await crawler.arun("https://www.example.com")
  if result.success:
    internal_links = result.links.get("internal", [])
    external_links = result.links.get("external", [])
    print(f"Found {len(internal_links)} internal links.")
    print(f"Found {len(internal_links)} external links.")
    print(f"Found {len(result.media)} media items.")
    # Each link is typically a dictionary with fields like:
    # { "href": "...", "text": "...", "title": "...", "base_domain": "..." }
    if internal_links:
      print("Sample Internal Link:", internal_links[0])
  else:
    print("Crawl failed:", result.error_message)

```

**Structure Example** :
```
result.links = {
 "internal": [
  {
   "href": "https://kidocode.com/",
   "text": "",
   "title": "",
   "base_domain": "kidocode.com"
  },
  {
   "href": "https://kidocode.com/degrees/technology",
   "text": "Technology Degree",
   "title": "KidoCode Tech Program",
   "base_domain": "kidocode.com"
  },
  # ...
 ],
 "external": [
  # possibly other links leading to third-party sites
 ]
}

```

  * **`href`**: The raw hyperlink URL.
  * **`text`**: The link text (if any) within the`<a>` tag. 
  * **`title`**: The`title` attribute of the link (if present). 
  * **`base_domain`**: The domain extracted from`href`. Helpful for filtering or grouping by domain.


## 2. Domain Filtering
Some websites contain hundreds of third-party or affiliate links. You can filter out certain domains at **crawl time** by configuring the crawler. The most relevant parameters in `CrawlerRunConfig` are:
  * **`exclude_external_links`**: If`True` , discard any link pointing outside the root domain. 
  * **`exclude_social_media_domains`**: Provide a list of social media platforms (e.g.,`["facebook.com", "twitter.com"]`) to exclude from your crawl. 
  * **`exclude_social_media_links`**: If`True` , automatically skip known social platforms. 
  * **`exclude_domains`**: Provide a list of custom domains you want to exclude (e.g.,`["spammyads.com", "tracker.net"]`).


### 2.1 Example: Excluding External & Social Media Links
```
import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig
async def main():
  crawler_cfg = CrawlerRunConfig(
    exclude_external_links=True,     # No links outside primary domain
    exclude_social_media_links=True    # Skip recognized social media domains
  )
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(
      "https://www.example.com",
      config=crawler_cfg
    )
    if result.success:
      print("[OK] Crawled:", result.url)
      print("Internal links count:", len(result.links.get("internal", [])))
      print("External links count:", len(result.links.get("external", []))) 
      # Likely zero external links in this scenario
    else:
      print("[ERROR]", result.error_message)
if __name__ == "__main__":
  asyncio.run(main())

```

### 2.2 Example: Excluding Specific Domains
If you want to let external links in, but specifically exclude a domain (e.g., `suspiciousads.com`), do this:
```
crawler_cfg = CrawlerRunConfig(
  exclude_domains=["suspiciousads.com"]
)

```

This approach is handy when you still want external links but need to block certain sites you consider spammy.
## 3. Media Extraction
### 3.1 Accessing `result.media`
By default, Crawl4AI collects images, audio, and video URLs it finds on the page. These are stored in `result.media`, a dictionary keyed by media type (e.g., `images`, `videos`, `audio`).
**Basic Example** :
```
if result.success:
  images_info = result.media.get("images", [])
  print(f"Found {len(images_info)} images in total.")
  for i, img in enumerate(images_info[:5]): # Inspect just the first 5
    print(f"[Image {i}] URL: {img['src']}")
    print(f"      Alt text: {img.get('alt', '')}")
    print(f"      Score: {img.get('score')}")
    print(f"      Description: {img.get('desc', '')}\n")

```

**Structure Example** :
```
result.media = {
 "images": [
  {
   "src": "https://cdn.prod.website-files.com/.../Group%2089.svg",
   "alt": "coding school for kids",
   "desc": "Trial Class Degrees degrees All Degrees AI Degree Technology ...",
   "score": 3,
   "type": "image",
   "group_id": 0,
   "format": None,
   "width": None,
   "height": None
  },
  # ...
 ],
 "videos": [
  # Similar structure but with video-specific fields
 ],
 "audio": [
  # Similar structure but with audio-specific fields
 ]
}

```

Depending on your Crawl4AI version or scraping strategy, these dictionaries can include fields like:
  * **`src`**: The media URL (e.g., image source)
  * **`alt`**: The alt text for images (if present)
  * **`desc`**: A snippet of nearby text or a short description (optional)
  * **`score`**: A heuristic relevance score if you’re using content-scoring features
  * **`width`**,**`height`**: If the crawler detects dimensions for the image/video
  * **`type`**: Usually`"image"` , `"video"`, or `"audio"`
  * **`group_id`**: If you’re grouping related media items, the crawler might assign an ID


With these details, you can easily filter out or focus on certain images (for instance, ignoring images with very low scores or a different domain), or gather metadata for analytics.
### 3.2 Excluding External Images
If you’re dealing with heavy pages or want to skip third-party images (advertisements, for example), you can turn on:
```
crawler_cfg = CrawlerRunConfig(
  exclude_external_images=True
)

```

This setting attempts to discard images from outside the primary domain, keeping only those from the site you’re crawling.
### 3.3 Additional Media Config
  * **`screenshot`**: Set to`True` if you want a full-page screenshot stored as `base64` in `result.screenshot`. 
  * **`pdf`**: Set to`True` if you want a PDF version of the page in `result.pdf`. 
  * **`wait_for_images`**: If`True` , attempts to wait until images are fully loaded before final extraction.


## 4. Putting It All Together: Link & Media Filtering
Here’s a combined example demonstrating how to filter out external links, skip certain domains, and exclude external images:
```
import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig
async def main():
  # Suppose we want to keep only internal links, remove certain domains, 
  # and discard external images from the final crawl data.
  crawler_cfg = CrawlerRunConfig(
    exclude_external_links=True,
    exclude_domains=["spammyads.com"],
    exclude_social_media_links=True,  # skip Twitter, Facebook, etc.
    exclude_external_images=True,   # keep only images from main domain
    wait_for_images=True,       # ensure images are loaded
    verbose=True
  )
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun("https://www.example.com", config=crawler_cfg)
    if result.success:
      print("[OK] Crawled:", result.url)
      # 1. Links
      in_links = result.links.get("internal", [])
      ext_links = result.links.get("external", [])
      print("Internal link count:", len(in_links))
      print("External link count:", len(ext_links)) # should be zero with exclude_external_links=True
      # 2. Images
      images = result.media.get("images", [])
      print("Images found:", len(images))
      # Let's see a snippet of these images
      for i, img in enumerate(images[:3]):
        print(f" - {img['src']} (alt={img.get('alt','')}, score={img.get('score','N/A')})")
    else:
      print("[ERROR] Failed to crawl. Reason:", result.error_message)
if __name__ == "__main__":
  asyncio.run(main())

```

## 5. Common Pitfalls & Tips
1. **Conflicting Flags** : - `exclude_external_links=True` but then also specifying `exclude_social_media_links=True` is typically fine, but understand that the first setting already discards _all_ external links. The second becomes somewhat redundant. - `exclude_external_images=True` but want to keep some external images? Currently no partial domain-based setting for images, so you might need a custom approach or hook logic.
2. **Relevancy Scores** : - If your version of Crawl4AI or your scraping strategy includes an `img["score"]`, it’s typically a heuristic based on size, position, or content analysis. Evaluate carefully if you rely on it.
3. **Performance** : - Excluding certain domains or external images can speed up your crawl, especially for large, media-heavy pages. - If you want a “full” link map, do _not_ exclude them. Instead, you can post-filter in your own code.
4. **Social Media Lists** : - `exclude_social_media_links=True` typically references an internal list of known social domains like Facebook, Twitter, LinkedIn, etc. If you need to add or remove from that list, look for library settings or a local config file (depending on your version).
**That’s it for Link & Media Analysis!** You’re now equipped to filter out unwanted sites and zero in on the images and videos that matter for your project.
Site built with [MkDocs](https://docs.crawl4ai.com/core/link-media/<http:/www.mkdocs.org>) and [Terminal for MkDocs](https://docs.crawl4ai.com/core/link-media/<https:/github.com/ntno/mkdocs-terminal>). 
##### Search
xClose
Type to start searching


==================================================

# URL: https://docs.crawl4ai.com/core/local-files/

[Crawl4AI Documentation](https://docs.crawl4ai.com/core/local-files/<https:/docs.crawl4ai.com/>)
  * [ Home ](https://docs.crawl4ai.com/core/local-files/<../..>)
  * [ Quick Start ](https://docs.crawl4ai.com/core/local-files/<../quickstart/>)
  * [ Search ](https://docs.crawl4ai.com/core/local-files/<#>)


  * [Home](https://docs.crawl4ai.com/core/local-files/<../..>)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/core/local-files/<../installation/>)
    * [Docker Deployment](https://docs.crawl4ai.com/core/local-files/<../docker-deploymeny/>)
  * [Quick Start](https://docs.crawl4ai.com/core/local-files/<../quickstart/>)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/core/local-files/blog/>)
    * [Changelog](https://docs.crawl4ai.com/core/local-files/<https:/github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md>)
  * Core
    * [Simple Crawling](https://docs.crawl4ai.com/core/local-files/<../simple-crawling/>)
    * [Crawler Result](https://docs.crawl4ai.com/core/local-files/<../crawler-result/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/core/local-files/<../browser-crawler-config/>)
    * [Markdown Generation](https://docs.crawl4ai.com/core/local-files/<../markdown-generation/>)
    * [Fit Markdown](https://docs.crawl4ai.com/core/local-files/<../fit-markdown/>)
    * [Page Interaction](https://docs.crawl4ai.com/core/local-files/<../page-interaction/>)
    * [Content Selection](https://docs.crawl4ai.com/core/local-files/<../content-selection/>)
    * [Cache Modes](https://docs.crawl4ai.com/core/local-files/<../cache-modes/>)
    * Local Files & Raw HTML
    * [Link & Media](https://docs.crawl4ai.com/core/local-files/<../link-media/>)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/core/local-files/advanced/advanced-features/>)
    * [File Downloading](https://docs.crawl4ai.com/core/local-files/advanced/file-downloading/>)
    * [Lazy Loading](https://docs.crawl4ai.com/core/local-files/advanced/lazy-loading/>)
    * [Hooks & Auth](https://docs.crawl4ai.com/core/local-files/advanced/hooks-auth/>)
    * [Proxy & Security](https://docs.crawl4ai.com/core/local-files/advanced/proxy-security/>)
    * [Session Management](https://docs.crawl4ai.com/core/local-files/advanced/session-management/>)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/core/local-files/advanced/multi-url-crawling/>)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/core/local-files/advanced/crawl-dispatcher/>)
    * [Identity Based Crawling](https://docs.crawl4ai.com/core/local-files/advanced/identity-based-crawling/>)
    * [SSL Certificate](https://docs.crawl4ai.com/core/local-files/advanced/ssl-certificate/>)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/core/local-files/extraction/no-llm-strategies/>)
    * [LLM Strategies](https://docs.crawl4ai.com/core/local-files/extraction/llm-strategies/>)
    * [Clustering Strategies](https://docs.crawl4ai.com/core/local-files/extraction/clustring-strategies/>)
    * [Chunking](https://docs.crawl4ai.com/core/local-files/extraction/chunking/>)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/core/local-files/api/async-webcrawler/>)
    * [arun()](https://docs.crawl4ai.com/core/local-files/api/arun/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/core/local-files/api/parameters/>)
    * [CrawlResult](https://docs.crawl4ai.com/core/local-files/api/crawl-result/>)
    * [Strategies](https://docs.crawl4ai.com/core/local-files/api/strategies/>)


  * [Prefix-Based Input Handling in Crawl4AI](https://docs.crawl4ai.com/core/local-files/<#prefix-based-input-handling-in-crawl4ai>)
  * [Crawling a Web URL](https://docs.crawl4ai.com/core/local-files/<#crawling-a-web-url>)
  * [Crawling a Local HTML File](https://docs.crawl4ai.com/core/local-files/<#crawling-a-local-html-file>)
  * [Crawling Raw HTML Content](https://docs.crawl4ai.com/core/local-files/<#crawling-raw-html-content>)
  * [Complete Example](https://docs.crawl4ai.com/core/local-files/<#complete-example>)
  * [Conclusion](https://docs.crawl4ai.com/core/local-files/<#conclusion>)


# Prefix-Based Input Handling in Crawl4AI
This guide will walk you through using the Crawl4AI library to crawl web pages, local HTML files, and raw HTML strings. We'll demonstrate these capabilities using a Wikipedia page as an example.
## Crawling a Web URL
To crawl a live web page, provide the URL starting with `http://` or `https://`, using a `CrawlerRunConfig` object:
```
import asyncio
from crawl4ai import AsyncWebCrawler
from crawl4ai.async_configs import CrawlerRunConfig
async def crawl_web():
  config = CrawlerRunConfig(bypass_cache=True)
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(
      url="https://en.wikipedia.org/wiki/apple", 
      config=config
    )
    if result.success:
      print("Markdown Content:")
      print(result.markdown)
    else:
      print(f"Failed to crawl: {result.error_message}")
asyncio.run(crawl_web())

```

## Crawling a Local HTML File
To crawl a local HTML file, prefix the file path with `file://`.
```
import asyncio
from crawl4ai import AsyncWebCrawler
from crawl4ai.async_configs import CrawlerRunConfig
async def crawl_local_file():
  local_file_path = "/path/to/apple.html" # Replace with your file path
  file_url = f"file://{local_file_path}"
  config = CrawlerRunConfig(bypass_cache=True)
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(url=file_url, config=config)
    if result.success:
      print("Markdown Content from Local File:")
      print(result.markdown)
    else:
      print(f"Failed to crawl local file: {result.error_message}")
asyncio.run(crawl_local_file())

```

## Crawling Raw HTML Content
To crawl raw HTML content, prefix the HTML string with `raw:`.
```
import asyncio
from crawl4ai import AsyncWebCrawler
from crawl4ai.async_configs import CrawlerRunConfig
async def crawl_raw_html():
  raw_html = "<html><body><h1>Hello, World!</h1></body></html>"
  raw_html_url = f"raw:{raw_html}"
  config = CrawlerRunConfig(bypass_cache=True)
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(url=raw_html_url, config=config)
    if result.success:
      print("Markdown Content from Raw HTML:")
      print(result.markdown)
    else:
      print(f"Failed to crawl raw HTML: {result.error_message}")
asyncio.run(crawl_raw_html())

```

# Complete Example
Below is a comprehensive script that:
  1. Crawls the Wikipedia page for "Apple."
  2. Saves the HTML content to a local file (`apple.html`).
  3. Crawls the local HTML file and verifies the markdown length matches the original crawl.
  4. Crawls the raw HTML content from the saved file and verifies consistency.


```
import os
import sys
import asyncio
from pathlib import Path
from crawl4ai import AsyncWebCrawler
from crawl4ai.async_configs import CrawlerRunConfig
async def main():
  wikipedia_url = "https://en.wikipedia.org/wiki/apple"
  script_dir = Path(__file__).parent
  html_file_path = script_dir / "apple.html"
  async with AsyncWebCrawler() as crawler:
    # Step 1: Crawl the Web URL
    print("\n=== Step 1: Crawling the Wikipedia URL ===")
    web_config = CrawlerRunConfig(bypass_cache=True)
    result = await crawler.arun(url=wikipedia_url, config=web_config)
    if not result.success:
      print(f"Failed to crawl {wikipedia_url}: {result.error_message}")
      return
    with open(html_file_path, 'w', encoding='utf-8') as f:
      f.write(result.html)
    web_crawl_length = len(result.markdown)
    print(f"Length of markdown from web crawl: {web_crawl_length}\n")
    # Step 2: Crawl from the Local HTML File
    print("=== Step 2: Crawling from the Local HTML File ===")
    file_url = f"file://{html_file_path.resolve()}"
    file_config = CrawlerRunConfig(bypass_cache=True)
    local_result = await crawler.arun(url=file_url, config=file_config)
    if not local_result.success:
      print(f"Failed to crawl local file {file_url}: {local_result.error_message}")
      return
    local_crawl_length = len(local_result.markdown)
    assert web_crawl_length == local_crawl_length, "Markdown length mismatch"
    print("✅ Markdown length matches between web and local file crawl.\n")
    # Step 3: Crawl Using Raw HTML Content
    print("=== Step 3: Crawling Using Raw HTML Content ===")
    with open(html_file_path, 'r', encoding='utf-8') as f:
      raw_html_content = f.read()
    raw_html_url = f"raw:{raw_html_content}"
    raw_config = CrawlerRunConfig(bypass_cache=True)
    raw_result = await crawler.arun(url=raw_html_url, config=raw_config)
    if not raw_result.success:
      print(f"Failed to crawl raw HTML content: {raw_result.error_message}")
      return
    raw_crawl_length = len(raw_result.markdown)
    assert web_crawl_length == raw_crawl_length, "Markdown length mismatch"
    print("✅ Markdown length matches between web and raw HTML crawl.\n")
    print("All tests passed successfully!")
  if html_file_path.exists():
    os.remove(html_file_path)
if __name__ == "__main__":
  asyncio.run(main())

```

# Conclusion
With the unified `url` parameter and prefix-based handling in **Crawl4AI** , you can seamlessly handle web URLs, local HTML files, and raw HTML content. Use `CrawlerRunConfig` for flexible and consistent configuration in all scenarios.
Site built with [MkDocs](https://docs.crawl4ai.com/core/local-files/<http:/www.mkdocs.org>) and [Terminal for MkDocs](https://docs.crawl4ai.com/core/local-files/<https:/github.com/ntno/mkdocs-terminal>). 
##### Search
xClose
Type to start searching


==================================================

# URL: https://docs.crawl4ai.com/core/markdown-generation/

[Crawl4AI Documentation](https://docs.crawl4ai.com/core/markdown-generation/<https:/docs.crawl4ai.com/>)
  * [ Home ](https://docs.crawl4ai.com/core/markdown-generation/<../..>)
  * [ Quick Start ](https://docs.crawl4ai.com/core/markdown-generation/<../quickstart/>)
  * [ Search ](https://docs.crawl4ai.com/core/markdown-generation/<#>)


  * [Home](https://docs.crawl4ai.com/core/markdown-generation/<../..>)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/core/markdown-generation/<../installation/>)
    * [Docker Deployment](https://docs.crawl4ai.com/core/markdown-generation/<../docker-deploymeny/>)
  * [Quick Start](https://docs.crawl4ai.com/core/markdown-generation/<../quickstart/>)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/core/markdown-generation/blog/>)
    * [Changelog](https://docs.crawl4ai.com/core/markdown-generation/<https:/github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md>)
  * Core
    * [Simple Crawling](https://docs.crawl4ai.com/core/markdown-generation/<../simple-crawling/>)
    * [Crawler Result](https://docs.crawl4ai.com/core/markdown-generation/<../crawler-result/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/core/markdown-generation/<../browser-crawler-config/>)
    * Markdown Generation
    * [Fit Markdown](https://docs.crawl4ai.com/core/markdown-generation/<../fit-markdown/>)
    * [Page Interaction](https://docs.crawl4ai.com/core/markdown-generation/<../page-interaction/>)
    * [Content Selection](https://docs.crawl4ai.com/core/markdown-generation/<../content-selection/>)
    * [Cache Modes](https://docs.crawl4ai.com/core/markdown-generation/<../cache-modes/>)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/core/markdown-generation/<../local-files/>)
    * [Link & Media](https://docs.crawl4ai.com/core/markdown-generation/<../link-media/>)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/core/markdown-generation/advanced/advanced-features/>)
    * [File Downloading](https://docs.crawl4ai.com/core/markdown-generation/advanced/file-downloading/>)
    * [Lazy Loading](https://docs.crawl4ai.com/core/markdown-generation/advanced/lazy-loading/>)
    * [Hooks & Auth](https://docs.crawl4ai.com/core/markdown-generation/advanced/hooks-auth/>)
    * [Proxy & Security](https://docs.crawl4ai.com/core/markdown-generation/advanced/proxy-security/>)
    * [Session Management](https://docs.crawl4ai.com/core/markdown-generation/advanced/session-management/>)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/core/markdown-generation/advanced/multi-url-crawling/>)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/core/markdown-generation/advanced/crawl-dispatcher/>)
    * [Identity Based Crawling](https://docs.crawl4ai.com/core/markdown-generation/advanced/identity-based-crawling/>)
    * [SSL Certificate](https://docs.crawl4ai.com/core/markdown-generation/advanced/ssl-certificate/>)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/core/markdown-generation/extraction/no-llm-strategies/>)
    * [LLM Strategies](https://docs.crawl4ai.com/core/markdown-generation/extraction/llm-strategies/>)
    * [Clustering Strategies](https://docs.crawl4ai.com/core/markdown-generation/extraction/clustring-strategies/>)
    * [Chunking](https://docs.crawl4ai.com/core/markdown-generation/extraction/chunking/>)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/core/markdown-generation/api/async-webcrawler/>)
    * [arun()](https://docs.crawl4ai.com/core/markdown-generation/api/arun/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/core/markdown-generation/api/parameters/>)
    * [CrawlResult](https://docs.crawl4ai.com/core/markdown-generation/api/crawl-result/>)
    * [Strategies](https://docs.crawl4ai.com/core/markdown-generation/api/strategies/>)


  * [Markdown Generation Basics](https://docs.crawl4ai.com/core/markdown-generation/<#markdown-generation-basics>)
  * [1. Quick Example](https://docs.crawl4ai.com/core/markdown-generation/<#1-quick-example>)
  * [2. How Markdown Generation Works](https://docs.crawl4ai.com/core/markdown-generation/<#2-how-markdown-generation-works>)
  * [3. Configuring the Default Markdown Generator](https://docs.crawl4ai.com/core/markdown-generation/<#3-configuring-the-default-markdown-generator>)
  * [4. Content Filters](https://docs.crawl4ai.com/core/markdown-generation/<#4-content-filters>)
  * [5. Using Fit Markdown](https://docs.crawl4ai.com/core/markdown-generation/<#5-using-fit-markdown>)
  * [6. The MarkdownGenerationResult Object](https://docs.crawl4ai.com/core/markdown-generation/<#6-the-markdowngenerationresult-object>)
  * [7. Combining Filters (BM25 + Pruning) in Two Passes](https://docs.crawl4ai.com/core/markdown-generation/<#7-combining-filters-bm25-pruning-in-two-passes>)
  * [8. Common Pitfalls & Tips](https://docs.crawl4ai.com/core/markdown-generation/<#8-common-pitfalls-tips>)
  * [9. Summary & Next Steps](https://docs.crawl4ai.com/core/markdown-generation/<#9-summary-next-steps>)


# Markdown Generation Basics
One of Crawl4AI’s core features is generating **clean, structured markdown** from web pages. Originally built to solve the problem of extracting only the “actual” content and discarding boilerplate or noise, Crawl4AI’s markdown system remains one of its biggest draws for AI workflows.
In this tutorial, you’ll learn:
  1. How to configure the **Default Markdown Generator**
  2. How **content filters** (BM25 or Pruning) help you refine markdown and discard junk 
  3. The difference between raw markdown (`result.markdown`) and filtered markdown (`fit_markdown`) 


> **Prerequisites** - You’ve completed or read [AsyncWebCrawler Basics](https://docs.crawl4ai.com/core/markdown-generation/<../simple-crawling/>) to understand how to run a simple crawl. - You know how to configure `CrawlerRunConfig`.
## 1. Quick Example
Here’s a minimal code snippet that uses the **DefaultMarkdownGenerator** with no additional filtering:
```
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
async def main():
  config = CrawlerRunConfig(
    markdown_generator=DefaultMarkdownGenerator()
  )
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun("https://example.com", config=config)
    if result.success:
      print("Raw Markdown Output:\n")
      print(result.markdown) # The unfiltered markdown from the page
    else:
      print("Crawl failed:", result.error_message)
if __name__ == "__main__":
  asyncio.run(main())

```

**What’s happening?** - `CrawlerRunConfig( markdown_generator = DefaultMarkdownGenerator() )` instructs Crawl4AI to convert the final HTML into markdown at the end of each crawl. - The resulting markdown is accessible via `result.markdown`.
## 2. How Markdown Generation Works
### 2.1 HTML-to-Text Conversion (Forked & Modified)
Under the hood, **DefaultMarkdownGenerator** uses a specialized HTML-to-text approach that:
  * Preserves headings, code blocks, bullet points, etc. 
  * Removes extraneous tags (scripts, styles) that don’t add meaningful content. 
  * Can optionally generate references for links or skip them altogether.


A set of **options** (passed as a dict) allows you to customize precisely how HTML converts to markdown. These map to standard html2text-like configuration plus your own enhancements (e.g., ignoring internal links, preserving certain tags verbatim, or adjusting line widths).
### 2.2 Link Citations & References
By default, the generator can convert `<a href="...">` elements into `[text][1]` citations, then place the actual links at the bottom of the document. This is handy for research workflows that demand references in a structured manner.
### 2.3 Optional Content Filters
Before or after the HTML-to-Markdown step, you can apply a **content filter** (like BM25 or Pruning) to reduce noise and produce a “fit_markdown”—a heavily pruned version focusing on the page’s main text. We’ll cover these filters shortly.
## 3. Configuring the Default Markdown Generator
You can tweak the output by passing an `options` dict to `DefaultMarkdownGenerator`. For example:
```
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
async def main():
  # Example: ignore all links, don't escape HTML, and wrap text at 80 characters
  md_generator = DefaultMarkdownGenerator(
    options={
      "ignore_links": True,
      "escape_html": False,
      "body_width": 80
    }
  )
  config = CrawlerRunConfig(
    markdown_generator=md_generator
  )
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun("https://example.com/docs", config=config)
    if result.success:
      print("Markdown:\n", result.markdown[:500]) # Just a snippet
    else:
      print("Crawl failed:", result.error_message)
if __name__ == "__main__":
  import asyncio
  asyncio.run(main())

```

Some commonly used `options`:
  * **`ignore_links`**(bool): Whether to remove all hyperlinks in the final markdown.
  * **`ignore_images`**(bool): Remove all`![image]()` references. 
  * **`escape_html`**(bool): Turn HTML entities into text (default is often`True`). 
  * **`body_width`**(int): Wrap text at N characters.`0` or `None` means no wrapping. 
  * **`skip_internal_links`**(bool): If`True` , omit `#localAnchors` or internal links referencing the same page. 
  * **`include_sup_sub`**(bool): Attempt to handle`<sup>` / `<sub>` in a more readable way.


## 4. Content Filters
**Content filters** selectively remove or rank sections of text before turning them into Markdown. This is especially helpful if your page has ads, nav bars, or other clutter you don’t want.
### 4.1 BM25ContentFilter
If you have a **search query** , BM25 is a good choice:
```
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
from crawl4ai.content_filter_strategy import BM25ContentFilter
from crawl4ai import CrawlerRunConfig
bm25_filter = BM25ContentFilter(
  user_query="machine learning",
  bm25_threshold=1.2,
  use_stemming=True
)
md_generator = DefaultMarkdownGenerator(
  content_filter=bm25_filter,
  options={"ignore_links": True}
)
config = CrawlerRunConfig(markdown_generator=md_generator)

```

  * **`user_query`**: The term you want to focus on. BM25 tries to keep only content blocks relevant to that query.
  * **`bm25_threshold`**: Raise it to keep fewer blocks; lower it to keep more.
  * **`use_stemming`**: If`True` , variations of words match (e.g., “learn,” “learning,” “learnt”).


**No query provided?** BM25 tries to glean a context from page metadata, or you can simply treat it as a scorched-earth approach that discards text with low generic score. Realistically, you want to supply a query for best results.
### 4.2 PruningContentFilter
If you **don’t** have a specific query, or if you just want a robust “junk remover,” use `PruningContentFilter`. It analyzes text density, link density, HTML structure, and known patterns (like “nav,” “footer”) to systematically prune extraneous or repetitive sections.
```
from crawl4ai.content_filter_strategy import PruningContentFilter
prune_filter = PruningContentFilter(
  threshold=0.5,
  threshold_type="fixed", # or "dynamic"
  min_word_threshold=50
)

```

  * **`threshold`**: Score boundary. Blocks below this score get removed.
  * **`threshold_type`**:
    * `"fixed"`: Straight comparison (`score >= threshold` keeps the block). 
    * `"dynamic"`: The filter adjusts threshold in a data-driven manner. 
  * **`min_word_threshold`**: Discard blocks under N words as likely too short or unhelpful.


**When to Use PruningContentFilter** - You want a broad cleanup without a user query. - The page has lots of repeated sidebars, footers, or disclaimers that hamper text extraction.
## 5. Using Fit Markdown
When a content filter is active, the library produces two forms of markdown inside `result.markdown_v2` or (if using the simplified field) `result.markdown`:
1. **`raw_markdown`**: The full unfiltered markdown. 2.**`fit_markdown`**: A “fit” version where the filter has removed or trimmed noisy segments.
**Note** : 
> In earlier examples, you may see references to `result.markdown_v2`. Depending on your library version, you might access `result.markdown`, `result.markdown_v2`, or an object named `MarkdownGenerationResult`. The idea is the same: you’ll have a raw version and a filtered (“fit”) version if a filter is used.
```
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
from crawl4ai.content_filter_strategy import PruningContentFilter
async def main():
  config = CrawlerRunConfig(
    markdown_generator=DefaultMarkdownGenerator(
      content_filter=PruningContentFilter(threshold=0.6),
      options={"ignore_links": True}
    )
  )
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun("https://news.example.com/tech", config=config)
    if result.success:
      print("Raw markdown:\n", result.markdown)
      # If a filter is used, we also have .fit_markdown:
      md_object = result.markdown_v2 # or your equivalent
      print("Filtered markdown:\n", md_object.fit_markdown)
    else:
      print("Crawl failed:", result.error_message)
if __name__ == "__main__":
  asyncio.run(main())

```

## 6. The `MarkdownGenerationResult` Object
If your library stores detailed markdown output in an object like `MarkdownGenerationResult`, you’ll see fields such as:
  * **`raw_markdown`**: The direct HTML-to-markdown transformation (no filtering).
  * **`markdown_with_citations`**: A version that moves links to reference-style footnotes.
  * **`references_markdown`**: A separate string or section containing the gathered references.
  * **`fit_markdown`**: The filtered markdown if you used a content filter.
  * **`fit_html`**: The corresponding HTML snippet used to generate`fit_markdown` (helpful for debugging or advanced usage).


**Example** :
```
md_obj = result.markdown_v2 # your library’s naming may vary
print("RAW:\n", md_obj.raw_markdown)
print("CITED:\n", md_obj.markdown_with_citations)
print("REFERENCES:\n", md_obj.references_markdown)
print("FIT:\n", md_obj.fit_markdown)

```

**Why Does This Matter?** - You can supply `raw_markdown` to an LLM if you want the entire text. - Or feed `fit_markdown` into a vector database to reduce token usage. - `references_markdown` can help you keep track of link provenance.
Below is a **revised section** under “Combining Filters (BM25 + Pruning)” that demonstrates how you can run **two** passes of content filtering without re-crawling, by taking the HTML (or text) from a first pass and feeding it into the second filter. It uses real code patterns from the snippet you provided for **BM25ContentFilter** , which directly accepts **HTML** strings (and can also handle plain text with minimal adaptation).
## 7. Combining Filters (BM25 + Pruning) in Two Passes
You might want to **prune out** noisy boilerplate first (with `PruningContentFilter`), and then **rank what’s left** against a user query (with `BM25ContentFilter`). You don’t have to crawl the page twice. Instead:
1. **First pass** : Apply `PruningContentFilter` directly to the raw HTML from `result.html` (the crawler’s downloaded HTML). 2. **Second pass** : Take the pruned HTML (or text) from step 1, and feed it into `BM25ContentFilter`, focusing on a user query.
### Two-Pass Example
```
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.content_filter_strategy import PruningContentFilter, BM25ContentFilter
from bs4 import BeautifulSoup
async def main():
  # 1. Crawl with minimal or no markdown generator, just get raw HTML
  config = CrawlerRunConfig(
    # If you only want raw HTML, you can skip passing a markdown_generator
    # or provide one but focus on .html in this example
  )
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun("https://example.com/tech-article", config=config)
    if not result.success or not result.html:
      print("Crawl failed or no HTML content.")
      return
    raw_html = result.html
    # 2. First pass: PruningContentFilter on raw HTML
    pruning_filter = PruningContentFilter(threshold=0.5, min_word_threshold=50)
    # filter_content returns a list of "text chunks" or cleaned HTML sections
    pruned_chunks = pruning_filter.filter_content(raw_html)
    # This list is basically pruned content blocks, presumably in HTML or text form
    # For demonstration, let's combine these chunks back into a single HTML-like string
    # or you could do further processing. It's up to your pipeline design.
    pruned_html = "\n".join(pruned_chunks)
    # 3. Second pass: BM25ContentFilter with a user query
    bm25_filter = BM25ContentFilter(
      user_query="machine learning",
      bm25_threshold=1.2,
      language="english"
    )
    # returns a list of text chunks
    bm25_chunks = bm25_filter.filter_content(pruned_html) 
    if not bm25_chunks:
      print("Nothing matched the BM25 query after pruning.")
      return
    # 4. Combine or display final results
    final_text = "\n---\n".join(bm25_chunks)
    print("==== PRUNED OUTPUT (first pass) ====")
    print(pruned_html[:500], "... (truncated)") # preview
    print("\n==== BM25 OUTPUT (second pass) ====")
    print(final_text[:500], "... (truncated)")
if __name__ == "__main__":
  asyncio.run(main())

```

### What’s Happening?
1. **Raw HTML** : We crawl once and store the raw HTML in `result.html`. 2. **PruningContentFilter** : Takes HTML + optional parameters. It extracts blocks of text or partial HTML, removing headings/sections deemed “noise.” It returns a **list of text chunks**. 3. **Combine or Transform** : We join these pruned chunks back into a single HTML-like string. (Alternatively, you could store them in a list for further logic—whatever suits your pipeline.) 4. **BM25ContentFilter** : We feed the pruned string into `BM25ContentFilter` with a user query. This second pass further narrows the content to chunks relevant to “machine learning.”
**No Re-Crawling** : We used `raw_html` from the first pass, so there’s no need to run `arun()` again—**no second network request**.
### Tips & Variations
  * **Plain Text vs. HTML** : If your pruned output is mostly text, BM25 can still handle it; just keep in mind it expects a valid string input. If you supply partial HTML (like `"<p>some text</p>"`), it will parse it as HTML. 
  * **Chaining in a Single Pipeline** : If your code supports it, you can chain multiple filters automatically. Otherwise, manual two-pass filtering (as shown) is straightforward. 
  * **Adjust Thresholds** : If you see too much or too little text in step one, tweak `threshold=0.5` or `min_word_threshold=50`. Similarly, `bm25_threshold=1.2` can be raised/lowered for more or fewer chunks in step two.


### One-Pass Combination?
If your codebase or pipeline design allows applying multiple filters in one pass, you could do so. But often it’s simpler—and more transparent—to run them sequentially, analyzing each step’s result.
**Bottom Line** : By **manually chaining** your filtering logic in two passes, you get powerful incremental control over the final content. First, remove “global” clutter with Pruning, then refine further with BM25-based query relevance—without incurring a second network crawl.
## 8. Common Pitfalls & Tips
1. **No Markdown Output?** - Make sure the crawler actually retrieved HTML. If the site is heavily JS-based, you may need to enable dynamic rendering or wait for elements. - Check if your content filter is too aggressive. Lower thresholds or disable the filter to see if content reappears.
2. **Performance Considerations** - Very large pages with multiple filters can be slower. Consider `cache_mode` to avoid re-downloading. - If your final use case is LLM ingestion, consider summarizing further or chunking big texts.
3. **Take Advantage of`fit_markdown`** - Great for RAG pipelines, semantic search, or any scenario where extraneous boilerplate is unwanted. - Still verify the textual quality—some sites have crucial data in footers or sidebars.
4. **Adjusting`html2text` Options** - If you see lots of raw HTML slipping into the text, turn on `escape_html`. - If code blocks look messy, experiment with `mark_code` or `handle_code_in_pre`.
## 9. Summary & Next Steps
In this **Markdown Generation Basics** tutorial, you learned to:
  * Configure the **DefaultMarkdownGenerator** with HTML-to-text options. 
  * Use **BM25ContentFilter** for query-specific extraction or **PruningContentFilter** for general noise removal. 
  * Distinguish between raw and filtered markdown (`fit_markdown`). 
  * Leverage the `MarkdownGenerationResult` object to handle different forms of output (citations, references, etc.).


Now you can produce high-quality Markdown from any website, focusing on exactly the content you need—an essential step for powering AI models, summarization pipelines, or knowledge-base queries.
**Last Updated** : 2025-01-01
Site built with [MkDocs](https://docs.crawl4ai.com/core/markdown-generation/<http:/www.mkdocs.org>) and [Terminal for MkDocs](https://docs.crawl4ai.com/core/markdown-generation/<https:/github.com/ntno/mkdocs-terminal>). 
##### Search
xClose
Type to start searching


==================================================

# URL: https://docs.crawl4ai.com/core/page-interaction/

[Crawl4AI Documentation](https://docs.crawl4ai.com/core/page-interaction/<https:/docs.crawl4ai.com/>)
  * [ Home ](https://docs.crawl4ai.com/core/page-interaction/<../..>)
  * [ Quick Start ](https://docs.crawl4ai.com/core/page-interaction/<../quickstart/>)
  * [ Search ](https://docs.crawl4ai.com/core/page-interaction/<#>)


  * [Home](https://docs.crawl4ai.com/core/page-interaction/<../..>)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/core/page-interaction/<../installation/>)
    * [Docker Deployment](https://docs.crawl4ai.com/core/page-interaction/<../docker-deploymeny/>)
  * [Quick Start](https://docs.crawl4ai.com/core/page-interaction/<../quickstart/>)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/core/page-interaction/blog/>)
    * [Changelog](https://docs.crawl4ai.com/core/page-interaction/<https:/github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md>)
  * Core
    * [Simple Crawling](https://docs.crawl4ai.com/core/page-interaction/<../simple-crawling/>)
    * [Crawler Result](https://docs.crawl4ai.com/core/page-interaction/<../crawler-result/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/core/page-interaction/<../browser-crawler-config/>)
    * [Markdown Generation](https://docs.crawl4ai.com/core/page-interaction/<../markdown-generation/>)
    * [Fit Markdown](https://docs.crawl4ai.com/core/page-interaction/<../fit-markdown/>)
    * Page Interaction
    * [Content Selection](https://docs.crawl4ai.com/core/page-interaction/<../content-selection/>)
    * [Cache Modes](https://docs.crawl4ai.com/core/page-interaction/<../cache-modes/>)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/core/page-interaction/<../local-files/>)
    * [Link & Media](https://docs.crawl4ai.com/core/page-interaction/<../link-media/>)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/core/page-interaction/advanced/advanced-features/>)
    * [File Downloading](https://docs.crawl4ai.com/core/page-interaction/advanced/file-downloading/>)
    * [Lazy Loading](https://docs.crawl4ai.com/core/page-interaction/advanced/lazy-loading/>)
    * [Hooks & Auth](https://docs.crawl4ai.com/core/page-interaction/advanced/hooks-auth/>)
    * [Proxy & Security](https://docs.crawl4ai.com/core/page-interaction/advanced/proxy-security/>)
    * [Session Management](https://docs.crawl4ai.com/core/page-interaction/advanced/session-management/>)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/core/page-interaction/advanced/multi-url-crawling/>)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/core/page-interaction/advanced/crawl-dispatcher/>)
    * [Identity Based Crawling](https://docs.crawl4ai.com/core/page-interaction/advanced/identity-based-crawling/>)
    * [SSL Certificate](https://docs.crawl4ai.com/core/page-interaction/advanced/ssl-certificate/>)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/core/page-interaction/extraction/no-llm-strategies/>)
    * [LLM Strategies](https://docs.crawl4ai.com/core/page-interaction/extraction/llm-strategies/>)
    * [Clustering Strategies](https://docs.crawl4ai.com/core/page-interaction/extraction/clustring-strategies/>)
    * [Chunking](https://docs.crawl4ai.com/core/page-interaction/extraction/chunking/>)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/core/page-interaction/api/async-webcrawler/>)
    * [arun()](https://docs.crawl4ai.com/core/page-interaction/api/arun/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/core/page-interaction/api/parameters/>)
    * [CrawlResult](https://docs.crawl4ai.com/core/page-interaction/api/crawl-result/>)
    * [Strategies](https://docs.crawl4ai.com/core/page-interaction/api/strategies/>)


  * [Page Interaction](https://docs.crawl4ai.com/core/page-interaction/<#page-interaction>)
  * [1. JavaScript Execution](https://docs.crawl4ai.com/core/page-interaction/<#1-javascript-execution>)
  * [2. Wait Conditions](https://docs.crawl4ai.com/core/page-interaction/<#2-wait-conditions>)
  * [3. Handling Dynamic Content](https://docs.crawl4ai.com/core/page-interaction/<#3-handling-dynamic-content>)
  * [4. Timing Control](https://docs.crawl4ai.com/core/page-interaction/<#4-timing-control>)
  * [5. Multi-Step Interaction Example](https://docs.crawl4ai.com/core/page-interaction/<#5-multi-step-interaction-example>)
  * [6. Combine Interaction with Extraction](https://docs.crawl4ai.com/core/page-interaction/<#6-combine-interaction-with-extraction>)
  * [7. Relevant CrawlerRunConfig Parameters](https://docs.crawl4ai.com/core/page-interaction/<#7-relevant-crawlerrunconfig-parameters>)
  * [8. Conclusion](https://docs.crawl4ai.com/core/page-interaction/<#8-conclusion>)


# Page Interaction
Crawl4AI provides powerful features for interacting with **dynamic** webpages, handling JavaScript execution, waiting for conditions, and managing multi-step flows. By combining **js_code** , **wait_for** , and certain **CrawlerRunConfig** parameters, you can:
  1. Click “Load More” buttons 
  2. Fill forms and submit them 
  3. Wait for elements or data to appear 
  4. Reuse sessions across multiple steps 


Below is a quick overview of how to do it.
## 1. JavaScript Execution
### Basic Execution
**`js_code`**in**`CrawlerRunConfig`**accepts either a single JS string or a list of JS snippets.**Example** : We’ll scroll to the bottom of the page, then optionally click a “Load More” button.
```
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
async def main():
  # Single JS command
  config = CrawlerRunConfig(
    js_code="window.scrollTo(0, document.body.scrollHeight);"
  )
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(
      url="https://news.ycombinator.com", # Example site
      config=config
    )
    print("Crawled length:", len(result.cleaned_html))
  # Multiple commands
  js_commands = [
    "window.scrollTo(0, document.body.scrollHeight);",
    # 'More' link on Hacker News
    "document.querySelector('a.morelink')?.click();", 
  ]
  config = CrawlerRunConfig(js_code=js_commands)
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(
      url="https://news.ycombinator.com", # Another pass
      config=config
    )
    print("After scroll+click, length:", len(result.cleaned_html))
if __name__ == "__main__":
  asyncio.run(main())

```

**Relevant`CrawlerRunConfig` params**: - **`js_code`**: A string or list of strings with JavaScript to run after the page loads. -**`js_only`**: If set to`True` on subsequent calls, indicates we’re continuing an existing session without a new full navigation. - **`session_id`**: If you want to keep the same page across multiple calls, specify an ID.
## 2. Wait Conditions
### 2.1 CSS-Based Waiting
Sometimes, you just want to wait for a specific element to appear. For example:
```
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
async def main():
  config = CrawlerRunConfig(
    # Wait for at least 30 items on Hacker News
    wait_for="css:.athing:nth-child(30)" 
  )
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(
      url="https://news.ycombinator.com",
      config=config
    )
    print("We have at least 30 items loaded!")
    # Rough check
    print("Total items in HTML:", result.cleaned_html.count("athing")) 
if __name__ == "__main__":
  asyncio.run(main())

```

**Key param** : - **`wait_for="css:..."`**: Tells the crawler to wait until that CSS selector is present.
### 2.2 JavaScript-Based Waiting
For more complex conditions (e.g., waiting for content length to exceed a threshold), prefix `js:`:
```
wait_condition = """() => {
  const items = document.querySelectorAll('.athing');
  return items.length > 50; // Wait for at least 51 items
}"""
config = CrawlerRunConfig(wait_for=f"js:{wait_condition}")

```

**Behind the Scenes** : Crawl4AI keeps polling the JS function until it returns `true` or a timeout occurs.
## 3. Handling Dynamic Content
Many modern sites require **multiple steps** : scrolling, clicking “Load More,” or updating via JavaScript. Below are typical patterns.
### 3.1 Load More Example (Hacker News “More” Link)
```
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
async def main():
  # Step 1: Load initial Hacker News page
  config = CrawlerRunConfig(
    wait_for="css:.athing:nth-child(30)" # Wait for 30 items
  )
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(
      url="https://news.ycombinator.com",
      config=config
    )
    print("Initial items loaded.")
    # Step 2: Let's scroll and click the "More" link
    load_more_js = [
      "window.scrollTo(0, document.body.scrollHeight);",
      # The "More" link at page bottom
      "document.querySelector('a.morelink')?.click();" 
    ]
    next_page_conf = CrawlerRunConfig(
      js_code=load_more_js,
      wait_for="""js:() => {
        return document.querySelectorAll('.athing').length > 30;
      }""",
      # Mark that we do not re-navigate, but run JS in the same session:
      js_only=True,
      session_id="hn_session"
    )
    # Re-use the same crawler session
    result2 = await crawler.arun(
      url="https://news.ycombinator.com", # same URL but continuing session
      config=next_page_conf
    )
    total_items = result2.cleaned_html.count("athing")
    print("Items after load-more:", total_items)
if __name__ == "__main__":
  asyncio.run(main())

```

**Key params** : - **`session_id="hn_session"`**: Keep the same page across multiple calls to`arun()`. - **`js_only=True`**: We’re not performing a full reload, just applying JS in the existing page. -**`wait_for`**with`js:` : Wait for item count to grow beyond 30.
### 3.2 Form Interaction
If the site has a search or login form, you can fill fields and submit them with **`js_code`**. For instance, if GitHub had a local search form:
```
js_form_interaction = """
document.querySelector('#your-search').value = 'TypeScript commits';
document.querySelector('form').submit();
"""
config = CrawlerRunConfig(
  js_code=js_form_interaction,
  wait_for="css:.commit"
)
result = await crawler.arun(url="https://github.com/search", config=config)

```

**In reality** : Replace IDs or classes with the real site’s form selectors.
## 4. Timing Control
1. **`page_timeout`**(ms): Overall page load or script execution time limit. 2.**`delay_before_return_html`**(seconds): Wait an extra moment before capturing the final HTML. 3.**`mean_delay`** & **`max_range`**: If you call`arun_many()` with multiple URLs, these add a random pause between each request.
**Example** :
```
config = CrawlerRunConfig(
  page_timeout=60000, # 60s limit
  delay_before_return_html=2.5
)

```

## 5. Multi-Step Interaction Example
Below is a simplified script that does multiple “Load More” clicks on GitHub’s TypeScript commits page. It **re-uses** the same session to accumulate new commits each time. The code includes the relevant **`CrawlerRunConfig`**parameters you’d rely on.
```
import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
async def multi_page_commits():
  browser_cfg = BrowserConfig(
    headless=False, # Visible for demonstration
    verbose=True
  )
  session_id = "github_ts_commits"
  base_wait = """js:() => {
    const commits = document.querySelectorAll('li.Box-sc-g0xbh4-0 h4');
    return commits.length > 0;
  }"""
  # Step 1: Load initial commits
  config1 = CrawlerRunConfig(
    wait_for=base_wait,
    session_id=session_id,
    cache_mode=CacheMode.BYPASS,
    # Not using js_only yet since it's our first load
  )
  async with AsyncWebCrawler(config=browser_cfg) as crawler:
    result = await crawler.arun(
      url="https://github.com/microsoft/TypeScript/commits/main",
      config=config1
    )
    print("Initial commits loaded. Count:", result.cleaned_html.count("commit"))
    # Step 2: For subsequent pages, we run JS to click 'Next Page' if it exists
    js_next_page = """
    const selector = 'a[data-testid="pagination-next-button"]';
    const button = document.querySelector(selector);
    if (button) button.click();
    """
    # Wait until new commits appear
    wait_for_more = """js:() => {
      const commits = document.querySelectorAll('li.Box-sc-g0xbh4-0 h4');
      if (!window.firstCommit && commits.length>0) {
        window.firstCommit = commits[0].textContent;
        return false;
      }
      // If top commit changes, we have new commits
      const topNow = commits[0]?.textContent.trim();
      return topNow && topNow !== window.firstCommit;
    }"""
    for page in range(2): # let's do 2 more "Next" pages
      config_next = CrawlerRunConfig(
        session_id=session_id,
        js_code=js_next_page,
        wait_for=wait_for_more,
        js_only=True,    # We're continuing from the open tab
        cache_mode=CacheMode.BYPASS
      )
      result2 = await crawler.arun(
        url="https://github.com/microsoft/TypeScript/commits/main",
        config=config_next
      )
      print(f"Page {page+2} commits count:", result2.cleaned_html.count("commit"))
    # Optionally kill session
    await crawler.crawler_strategy.kill_session(session_id)
async def main():
  await multi_page_commits()
if __name__ == "__main__":
  asyncio.run(main())

```

**Key Points** :
  * **`session_id`**: Keep the same page open.
  * **`js_code`**+**`wait_for`**+**`js_only=True`**: We do partial refreshes, waiting for new commits to appear.
  * **`cache_mode=CacheMode.BYPASS`**ensures we always see fresh data each step.


## 6. Combine Interaction with Extraction
Once dynamic content is loaded, you can attach an **`extraction_strategy`**(like`JsonCssExtractionStrategy` or `LLMExtractionStrategy`). For example:
```
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
schema = {
  "name": "Commits",
  "baseSelector": "li.Box-sc-g0xbh4-0",
  "fields": [
    {"name": "title", "selector": "h4.markdown-title", "type": "text"}
  ]
}
config = CrawlerRunConfig(
  session_id="ts_commits_session",
  js_code=js_next_page,
  wait_for=wait_for_more,
  extraction_strategy=JsonCssExtractionStrategy(schema)
)

```

When done, check `result.extracted_content` for the JSON.
## 7. Relevant `CrawlerRunConfig` Parameters
Below are the key interaction-related parameters in `CrawlerRunConfig`. For a full list, see [Configuration Parameters](https://docs.crawl4ai.com/core/page-interaction/api/parameters/>).
  * **`js_code`**: JavaScript to run after initial load.
  * **`js_only`**: If`True` , no new page navigation—only JS in the existing session. 
  * **`wait_for`**: CSS (`"css:..."`) or JS (`"js:..."`) expression to wait for. 
  * **`session_id`**: Reuse the same page across calls.
  * **`cache_mode`**: Whether to read/write from the cache or bypass.
  * **`remove_overlay_elements`**: Remove certain popups automatically.
  * **`simulate_user`,`override_navigator` , `magic`**: Anti-bot or “human-like” interactions.


## 8. Conclusion
Crawl4AI’s **page interaction** features let you:
1. **Execute JavaScript** for scrolling, clicks, or form filling. 2. **Wait** for CSS or custom JS conditions before capturing data. 3. **Handle** multi-step flows (like “Load More”) with partial reloads or persistent sessions. 4. Combine with **structured extraction** for dynamic sites.
With these tools, you can scrape modern, interactive webpages confidently. For advanced hooking, user simulation, or in-depth config, check the [API reference](https://docs.crawl4ai.com/core/page-interaction/api/parameters/>) or related advanced docs. Happy scripting!
Site built with [MkDocs](https://docs.crawl4ai.com/core/page-interaction/<http:/www.mkdocs.org>) and [Terminal for MkDocs](https://docs.crawl4ai.com/core/page-interaction/<https:/github.com/ntno/mkdocs-terminal>). 
##### Search
xClose
Type to start searching


==================================================

# URL: https://docs.crawl4ai.com/core/quickstart/

[Crawl4AI Documentation](https://docs.crawl4ai.com/core/quickstart/<https:/docs.crawl4ai.com/>)
  * [ Home ](https://docs.crawl4ai.com/core/quickstart/<../..>)
  * [ Quick Start ](https://docs.crawl4ai.com/core/quickstart/<./>)
  * [ Search ](https://docs.crawl4ai.com/core/quickstart/<#>)


  * [Home](https://docs.crawl4ai.com/core/quickstart/<../..>)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/core/quickstart/<../installation/>)
    * [Docker Deployment](https://docs.crawl4ai.com/core/quickstart/<../docker-deploymeny/>)
  * Quick Start
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/core/quickstart/blog/>)
    * [Changelog](https://docs.crawl4ai.com/core/quickstart/<https:/github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md>)
  * Core
    * [Simple Crawling](https://docs.crawl4ai.com/core/quickstart/<../simple-crawling/>)
    * [Crawler Result](https://docs.crawl4ai.com/core/quickstart/<../crawler-result/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/core/quickstart/<../browser-crawler-config/>)
    * [Markdown Generation](https://docs.crawl4ai.com/core/quickstart/<../markdown-generation/>)
    * [Fit Markdown](https://docs.crawl4ai.com/core/quickstart/<../fit-markdown/>)
    * [Page Interaction](https://docs.crawl4ai.com/core/quickstart/<../page-interaction/>)
    * [Content Selection](https://docs.crawl4ai.com/core/quickstart/<../content-selection/>)
    * [Cache Modes](https://docs.crawl4ai.com/core/quickstart/<../cache-modes/>)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/core/quickstart/<../local-files/>)
    * [Link & Media](https://docs.crawl4ai.com/core/quickstart/<../link-media/>)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/core/quickstart/advanced/advanced-features/>)
    * [File Downloading](https://docs.crawl4ai.com/core/quickstart/advanced/file-downloading/>)
    * [Lazy Loading](https://docs.crawl4ai.com/core/quickstart/advanced/lazy-loading/>)
    * [Hooks & Auth](https://docs.crawl4ai.com/core/quickstart/advanced/hooks-auth/>)
    * [Proxy & Security](https://docs.crawl4ai.com/core/quickstart/advanced/proxy-security/>)
    * [Session Management](https://docs.crawl4ai.com/core/quickstart/advanced/session-management/>)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/core/quickstart/advanced/multi-url-crawling/>)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/core/quickstart/advanced/crawl-dispatcher/>)
    * [Identity Based Crawling](https://docs.crawl4ai.com/core/quickstart/advanced/identity-based-crawling/>)
    * [SSL Certificate](https://docs.crawl4ai.com/core/quickstart/advanced/ssl-certificate/>)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/core/quickstart/extraction/no-llm-strategies/>)
    * [LLM Strategies](https://docs.crawl4ai.com/core/quickstart/extraction/llm-strategies/>)
    * [Clustering Strategies](https://docs.crawl4ai.com/core/quickstart/extraction/clustring-strategies/>)
    * [Chunking](https://docs.crawl4ai.com/core/quickstart/extraction/chunking/>)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/core/quickstart/api/async-webcrawler/>)
    * [arun()](https://docs.crawl4ai.com/core/quickstart/api/arun/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/core/quickstart/api/parameters/>)
    * [CrawlResult](https://docs.crawl4ai.com/core/quickstart/api/crawl-result/>)
    * [Strategies](https://docs.crawl4ai.com/core/quickstart/api/strategies/>)


  * [Getting Started with Crawl4AI](https://docs.crawl4ai.com/core/quickstart/<#getting-started-with-crawl4ai>)
  * [1. Introduction](https://docs.crawl4ai.com/core/quickstart/<#1-introduction>)
  * [2. Your First Crawl](https://docs.crawl4ai.com/core/quickstart/<#2-your-first-crawl>)
  * [3. Basic Configuration (Light Introduction)](https://docs.crawl4ai.com/core/quickstart/<#3-basic-configuration-light-introduction>)
  * [4. Generating Markdown Output](https://docs.crawl4ai.com/core/quickstart/<#4-generating-markdown-output>)
  * [5. Simple Data Extraction (CSS-based)](https://docs.crawl4ai.com/core/quickstart/<#5-simple-data-extraction-css-based>)
  * [6. Simple Data Extraction (LLM-based)](https://docs.crawl4ai.com/core/quickstart/<#6-simple-data-extraction-llm-based>)
  * [7. Dynamic Content Example](https://docs.crawl4ai.com/core/quickstart/<#7-dynamic-content-example>)
  * [8. Next Steps](https://docs.crawl4ai.com/core/quickstart/<#8-next-steps>)


# Getting Started with Crawl4AI
Welcome to **Crawl4AI** , an open-source LLM-friendly Web Crawler & Scraper. In this tutorial, you’ll:
  1. Run your **first crawl** using minimal configuration. 
  2. Generate **Markdown** output (and learn how it’s influenced by content filters). 
  3. Experiment with a simple **CSS-based extraction** strategy. 
  4. See a glimpse of **LLM-based extraction** (including open-source and closed-source model options). 
  5. Crawl a **dynamic** page that loads content via JavaScript.


## 1. Introduction
Crawl4AI provides:
  * An asynchronous crawler, **`AsyncWebCrawler`**.
  * Configurable browser and run settings via **`BrowserConfig`**and**`CrawlerRunConfig`**.
  * Automatic HTML-to-Markdown conversion via **`DefaultMarkdownGenerator`**(supports optional filters).
  * Multiple extraction strategies (LLM-based or “traditional” CSS/XPath-based).


By the end of this guide, you’ll have performed a basic crawl, generated Markdown, tried out two extraction strategies, and crawled a dynamic page that uses “Load More” buttons or JavaScript updates.
## 2. Your First Crawl
Here’s a minimal Python script that creates an **`AsyncWebCrawler`**, fetches a webpage, and prints the first 300 characters of its Markdown output:
```
import asyncio
from crawl4ai import AsyncWebCrawler
async def main():
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun("https://example.com")
    print(result.markdown[:300]) # Print first 300 chars
if __name__ == "__main__":
  asyncio.run(main())

```

**What’s happening?** - **`AsyncWebCrawler`**launches a headless browser (Chromium by default). - It fetches`https://example.com`. - Crawl4AI automatically converts the HTML into Markdown.
You now have a simple, working crawl!
## 3. Basic Configuration (Light Introduction)
Crawl4AI’s crawler can be heavily customized using two main classes:
1. **`BrowserConfig`**: Controls browser behavior (headless or full UI, user agent, JavaScript toggles, etc.). 2.**`CrawlerRunConfig`**: Controls how each crawl runs (caching, extraction, timeouts, hooking, etc.).
Below is an example with minimal usage:
```
import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
async def main():
  browser_conf = BrowserConfig(headless=True) # or False to see the browser
  run_conf = CrawlerRunConfig(
    cache_mode=CacheMode.BYPASS
  )
  async with AsyncWebCrawler(config=browser_conf) as crawler:
    result = await crawler.arun(
      url="https://example.com",
      config=run_conf
    )
    print(result.markdown)
if __name__ == "__main__":
  asyncio.run(main())

```

> IMPORTANT: By default cache mode is set to `CacheMode.ENABLED`. So to have fresh content, you need to set it to `CacheMode.BYPASS`
We’ll explore more advanced config in later tutorials (like enabling proxies, PDF output, multi-tab sessions, etc.). For now, just note how you pass these objects to manage crawling.
## 4. Generating Markdown Output
By default, Crawl4AI automatically generates Markdown from each crawled page. However, the exact output depends on whether you specify a **markdown generator** or **content filter**.
  * **`result.markdown`**: The direct HTML-to-Markdown conversion.
  * **`result.markdown.fit_markdown`**: The same content after applying any configured**content filter** (e.g., `PruningContentFilter`).


### Example: Using a Filter with `DefaultMarkdownGenerator`
```
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.content_filter_strategy import PruningContentFilter
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
md_generator = DefaultMarkdownGenerator(
  content_filter=PruningContentFilter(threshold=0.4, threshold_type="fixed")
)
config = CrawlerRunConfig(
  cache_mode=CacheMode.BYPASS,
  markdown_generator=md_generator
)
async with AsyncWebCrawler() as crawler:
  result = await crawler.arun("https://news.ycombinator.com", config=config)
  print("Raw Markdown length:", len(result.markdown.raw_markdown))
  print("Fit Markdown length:", len(result.markdown.fit_markdown))

```

**Note** : If you do **not** specify a content filter or markdown generator, you’ll typically see only the raw Markdown. `PruningContentFilter` may adds around `50ms` in processing time. We’ll dive deeper into these strategies in a dedicated **Markdown Generation** tutorial.
## 5. Simple Data Extraction (CSS-based)
Crawl4AI can also extract structured data (JSON) using CSS or XPath selectors. Below is a minimal CSS-based example:
```
import asyncio
import json
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
async def main():
  schema = {
    "name": "Example Items",
    "baseSelector": "div.item",
    "fields": [
      {"name": "title", "selector": "h2", "type": "text"},
      {"name": "link", "selector": "a", "type": "attribute", "attribute": "href"}
    ]
  }
  raw_html = "<div class='item'><h2>Item 1</h2><a href='https://example.com/item1'>Link 1</a></div>"
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(
      url="raw://" + raw_html,
      config=CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        extraction_strategy=JsonCssExtractionStrategy(schema)
      )
    )
    # The JSON output is stored in 'extracted_content'
    data = json.loads(result.extracted_content)
    print(data)
if __name__ == "__main__":
  asyncio.run(main())

```

**Why is this helpful?** - Great for repetitive page structures (e.g., item listings, articles). - No AI usage or costs. - The crawler returns a JSON string you can parse or store.
> Tips: You can pass raw HTML to the crawler instead of a URL. To do so, prefix the HTML with `raw://`.
## 6. Simple Data Extraction (LLM-based)
For more complex or irregular pages, a language model can parse text intelligently into a structure you define. Crawl4AI supports **open-source** or **closed-source** providers:
  * **Open-Source Models** (e.g., `ollama/llama3.3`, `no_token`) 
  * **OpenAI Models** (e.g., `openai/gpt-4`, requires `api_token`) 
  * Or any provider supported by the underlying library


Below is an example using **open-source** style (no token) and closed-source:
```
import os
import json
import asyncio
from pydantic import BaseModel, Field
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.extraction_strategy import LLMExtractionStrategy
class OpenAIModelFee(BaseModel):
  model_name: str = Field(..., description="Name of the OpenAI model.")
  input_fee: str = Field(..., description="Fee for input token for the OpenAI model.")
  output_fee: str = Field(
    ..., description="Fee for output token for the OpenAI model."
  )
async def extract_structured_data_using_llm(
  provider: str, api_token: str = None, extra_headers: Dict[str, str] = None
):
  print(f"\n--- Extracting Structured Data with {provider} ---")
  if api_token is None and provider != "ollama":
    print(f"API token is required for {provider}. Skipping this example.")
    return
  browser_config = BrowserConfig(headless=True)
  extra_args = {"temperature": 0, "top_p": 0.9, "max_tokens": 2000}
  if extra_headers:
    extra_args["extra_headers"] = extra_headers
  crawler_config = CrawlerRunConfig(
    cache_mode=CacheMode.BYPASS,
    word_count_threshold=1,
    page_timeout=80000,
    extraction_strategy=LLMExtractionStrategy(
      provider=provider,
      api_token=api_token,
      schema=OpenAIModelFee.model_json_schema(),
      extraction_type="schema",
      instruction="""From the crawled content, extract all mentioned model names along with their fees for input and output tokens. 
      Do not miss any models in the entire content.""",
      extra_args=extra_args,
    ),
  )
  async with AsyncWebCrawler(config=browser_config) as crawler:
    result = await crawler.arun(
      url="https://openai.com/api/pricing/", config=crawler_config
    )
    print(result.extracted_content)
if __name__ == "__main__":
  # Use ollama with llama3.3
  # asyncio.run(
  #   extract_structured_data_using_llm(
  #     provider="ollama/llama3.3", api_token="no-token"
  #   )
  # )
  asyncio.run(
    extract_structured_data_using_llm(
      provider="openai/gpt-4o", api_token=os.getenv("OPENAI_API_KEY")
    )
  )

```

**What’s happening?** - We define a Pydantic schema (`PricingInfo`) describing the fields we want. - The LLM extraction strategy uses that schema and your instructions to transform raw text into structured JSON. - Depending on the **provider** and **api_token** , you can use local models or a remote API.
## 7. Dynamic Content Example
Some sites require multiple “page clicks” or dynamic JavaScript updates. Below is an example showing how to **click** a “Next Page” button and wait for new commits to load on GitHub, using **`BrowserConfig`**and**`CrawlerRunConfig`**:
```
import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
async def extract_structured_data_using_css_extractor():
  print("\n--- Using JsonCssExtractionStrategy for Fast Structured Output ---")
  schema = {
    "name": "KidoCode Courses",
    "baseSelector": "section.charge-methodology .w-tab-content > div",
    "fields": [
      {
        "name": "section_title",
        "selector": "h3.heading-50",
        "type": "text",
      },
      {
        "name": "section_description",
        "selector": ".charge-content",
        "type": "text",
      },
      {
        "name": "course_name",
        "selector": ".text-block-93",
        "type": "text",
      },
      {
        "name": "course_description",
        "selector": ".course-content-text",
        "type": "text",
      },
      {
        "name": "course_icon",
        "selector": ".image-92",
        "type": "attribute",
        "attribute": "src",
      },
    ],
  }
  browser_config = BrowserConfig(headless=True, java_script_enabled=True)
  js_click_tabs = """
  (async () => {
    const tabs = document.querySelectorAll("section.charge-methodology .tabs-menu-3 > div");
    for(let tab of tabs) {
      tab.scrollIntoView();
      tab.click();
      await new Promise(r => setTimeout(r, 500));
    }
  })();
  """
  crawler_config = CrawlerRunConfig(
    cache_mode=CacheMode.BYPASS,
    extraction_strategy=JsonCssExtractionStrategy(schema),
    js_code=[js_click_tabs],
  )
  async with AsyncWebCrawler(config=browser_config) as crawler:
    result = await crawler.arun(
      url="https://www.kidocode.com/degrees/technology", config=crawler_config
    )
    companies = json.loads(result.extracted_content)
    print(f"Successfully extracted {len(companies)} companies")
    print(json.dumps(companies[0], indent=2))
async def main():
  await extract_structured_data_using_css_extractor()
if __name__ == "__main__":
  asyncio.run(main())

```

**Key Points** :
  * **`BrowserConfig(headless=False)`**: We want to watch it click “Next Page.”
  * **`CrawlerRunConfig(...)`**: We specify the extraction strategy, pass`session_id` to reuse the same page. 
  * **`js_code`**and**`wait_for`**are used for subsequent pages (`page > 0`) to click the “Next” button and wait for new commits to load. 
  * **`js_only=True`**indicates we’re not re-navigating but continuing the existing session.
  * Finally, we call `kill_session()` to clean up the page and browser session.


## 8. Next Steps
Congratulations! You have:
  1. Performed a basic crawl and printed Markdown. 
  2. Used **content filters** with a markdown generator. 
  3. Extracted JSON via **CSS** or **LLM** strategies. 
  4. Handled **dynamic** pages with JavaScript triggers.


If you’re ready for more, check out:
  * **Installation** : A deeper dive into advanced installs, Docker usage (experimental), or optional dependencies. 
  * **Hooks & Auth**: Learn how to run custom JavaScript or handle logins with cookies, local storage, etc. 
  * **Deployment** : Explore ephemeral testing in Docker or plan for the upcoming stable Docker release. 
  * **Browser Management** : Delve into user simulation, stealth modes, and concurrency best practices. 


Crawl4AI is a powerful, flexible tool. Enjoy building out your scrapers, data pipelines, or AI-driven extraction flows. Happy crawling!
Site built with [MkDocs](https://docs.crawl4ai.com/core/quickstart/<http:/www.mkdocs.org>) and [Terminal for MkDocs](https://docs.crawl4ai.com/core/quickstart/<https:/github.com/ntno/mkdocs-terminal>). 
##### Search
xClose
Type to start searching


==================================================

# URL: https://docs.crawl4ai.com/core/simple-crawling/

[Crawl4AI Documentation](https://docs.crawl4ai.com/core/simple-crawling/<https:/docs.crawl4ai.com/>)
  * [ Home ](https://docs.crawl4ai.com/core/simple-crawling/<../..>)
  * [ Quick Start ](https://docs.crawl4ai.com/core/simple-crawling/<../quickstart/>)
  * [ Search ](https://docs.crawl4ai.com/core/simple-crawling/<#>)


  * [Home](https://docs.crawl4ai.com/core/simple-crawling/<../..>)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/core/simple-crawling/<../installation/>)
    * [Docker Deployment](https://docs.crawl4ai.com/core/simple-crawling/<../docker-deploymeny/>)
  * [Quick Start](https://docs.crawl4ai.com/core/simple-crawling/<../quickstart/>)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/core/simple-crawling/blog/>)
    * [Changelog](https://docs.crawl4ai.com/core/simple-crawling/<https:/github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md>)
  * Core
    * Simple Crawling
    * [Crawler Result](https://docs.crawl4ai.com/core/simple-crawling/<../crawler-result/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/core/simple-crawling/<../browser-crawler-config/>)
    * [Markdown Generation](https://docs.crawl4ai.com/core/simple-crawling/<../markdown-generation/>)
    * [Fit Markdown](https://docs.crawl4ai.com/core/simple-crawling/<../fit-markdown/>)
    * [Page Interaction](https://docs.crawl4ai.com/core/simple-crawling/<../page-interaction/>)
    * [Content Selection](https://docs.crawl4ai.com/core/simple-crawling/<../content-selection/>)
    * [Cache Modes](https://docs.crawl4ai.com/core/simple-crawling/<../cache-modes/>)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/core/simple-crawling/<../local-files/>)
    * [Link & Media](https://docs.crawl4ai.com/core/simple-crawling/<../link-media/>)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/core/simple-crawling/advanced/advanced-features/>)
    * [File Downloading](https://docs.crawl4ai.com/core/simple-crawling/advanced/file-downloading/>)
    * [Lazy Loading](https://docs.crawl4ai.com/core/simple-crawling/advanced/lazy-loading/>)
    * [Hooks & Auth](https://docs.crawl4ai.com/core/simple-crawling/advanced/hooks-auth/>)
    * [Proxy & Security](https://docs.crawl4ai.com/core/simple-crawling/advanced/proxy-security/>)
    * [Session Management](https://docs.crawl4ai.com/core/simple-crawling/advanced/session-management/>)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/core/simple-crawling/advanced/multi-url-crawling/>)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/core/simple-crawling/advanced/crawl-dispatcher/>)
    * [Identity Based Crawling](https://docs.crawl4ai.com/core/simple-crawling/advanced/identity-based-crawling/>)
    * [SSL Certificate](https://docs.crawl4ai.com/core/simple-crawling/advanced/ssl-certificate/>)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/core/simple-crawling/extraction/no-llm-strategies/>)
    * [LLM Strategies](https://docs.crawl4ai.com/core/simple-crawling/extraction/llm-strategies/>)
    * [Clustering Strategies](https://docs.crawl4ai.com/core/simple-crawling/extraction/clustring-strategies/>)
    * [Chunking](https://docs.crawl4ai.com/core/simple-crawling/extraction/chunking/>)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/core/simple-crawling/api/async-webcrawler/>)
    * [arun()](https://docs.crawl4ai.com/core/simple-crawling/api/arun/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/core/simple-crawling/api/parameters/>)
    * [CrawlResult](https://docs.crawl4ai.com/core/simple-crawling/api/crawl-result/>)
    * [Strategies](https://docs.crawl4ai.com/core/simple-crawling/api/strategies/>)


  * [Simple Crawling](https://docs.crawl4ai.com/core/simple-crawling/<#simple-crawling>)
  * [Basic Usage](https://docs.crawl4ai.com/core/simple-crawling/<#basic-usage>)
  * [Understanding the Response](https://docs.crawl4ai.com/core/simple-crawling/<#understanding-the-response>)
  * [Adding Basic Options](https://docs.crawl4ai.com/core/simple-crawling/<#adding-basic-options>)
  * [Handling Errors](https://docs.crawl4ai.com/core/simple-crawling/<#handling-errors>)
  * [Logging and Debugging](https://docs.crawl4ai.com/core/simple-crawling/<#logging-and-debugging>)
  * [Complete Example](https://docs.crawl4ai.com/core/simple-crawling/<#complete-example>)


# Simple Crawling
This guide covers the basics of web crawling with Crawl4AI. You'll learn how to set up a crawler, make your first request, and understand the response.
## Basic Usage
Set up a simple crawl using `BrowserConfig` and `CrawlerRunConfig`:
```
import asyncio
from crawl4ai import AsyncWebCrawler
from crawl4ai.async_configs import BrowserConfig, CrawlerRunConfig
async def main():
  browser_config = BrowserConfig() # Default browser configuration
  run_config = CrawlerRunConfig()  # Default crawl run configuration
  async with AsyncWebCrawler(config=browser_config) as crawler:
    result = await crawler.arun(
      url="https://example.com",
      config=run_config
    )
    print(result.markdown) # Print clean markdown content
if __name__ == "__main__":
  asyncio.run(main())

```

## Understanding the Response
The `arun()` method returns a `CrawlResult` object with several useful properties. Here's a quick overview (see [CrawlResult](https://docs.crawl4ai.com/core/simple-crawling/api/crawl-result/>) for complete details):
```
result = await crawler.arun(
  url="https://example.com",
  config=CrawlerRunConfig(fit_markdown=True)
)
# Different content formats
print(result.html)     # Raw HTML
print(result.cleaned_html) # Cleaned HTML
print(result.markdown)   # Markdown version
print(result.fit_markdown) # Most relevant content in markdown
# Check success status
print(result.success)   # True if crawl succeeded
print(result.status_code) # HTTP status code (e.g., 200, 404)
# Access extracted media and links
print(result.media)    # Dictionary of found media (images, videos, audio)
print(result.links)    # Dictionary of internal and external links

```

## Adding Basic Options
Customize your crawl using `CrawlerRunConfig`:
```
run_config = CrawlerRunConfig(
  word_count_threshold=10,    # Minimum words per content block
  exclude_external_links=True,  # Remove external links
  remove_overlay_elements=True,  # Remove popups/modals
  process_iframes=True      # Process iframe content
)
result = await crawler.arun(
  url="https://example.com",
  config=run_config
)

```

## Handling Errors
Always check if the crawl was successful:
```
run_config = CrawlerRunConfig()
result = await crawler.arun(url="https://example.com", config=run_config)
if not result.success:
  print(f"Crawl failed: {result.error_message}")
  print(f"Status code: {result.status_code}")

```

## Logging and Debugging
Enable verbose logging in `BrowserConfig`:
```
browser_config = BrowserConfig(verbose=True)
async with AsyncWebCrawler(config=browser_config) as crawler:
  run_config = CrawlerRunConfig()
  result = await crawler.arun(url="https://example.com", config=run_config)

```

## Complete Example
Here's a more comprehensive example demonstrating common usage patterns:
```
import asyncio
from crawl4ai import AsyncWebCrawler
from crawl4ai.async_configs import BrowserConfig, CrawlerRunConfig, CacheMode
async def main():
  browser_config = BrowserConfig(verbose=True)
  run_config = CrawlerRunConfig(
    # Content filtering
    word_count_threshold=10,
    excluded_tags=['form', 'header'],
    exclude_external_links=True,
    # Content processing
    process_iframes=True,
    remove_overlay_elements=True,
    # Cache control
    cache_mode=CacheMode.ENABLED # Use cache if available
  )
  async with AsyncWebCrawler(config=browser_config) as crawler:
    result = await crawler.arun(
      url="https://example.com",
      config=run_config
    )
    if result.success:
      # Print clean content
      print("Content:", result.markdown[:500]) # First 500 chars
      # Process images
      for image in result.media["images"]:
        print(f"Found image: {image['src']}")
      # Process links
      for link in result.links["internal"]:
        print(f"Internal link: {link['href']}")
    else:
      print(f"Crawl failed: {result.error_message}")
if __name__ == "__main__":
  asyncio.run(main())

```

Site built with [MkDocs](https://docs.crawl4ai.com/core/simple-crawling/<http:/www.mkdocs.org>) and [Terminal for MkDocs](https://docs.crawl4ai.com/core/simple-crawling/<https:/github.com/ntno/mkdocs-terminal>). 
##### Search
xClose
Type to start searching


==================================================

# URL: https://docs.crawl4ai.com/extraction/chunking/

[Crawl4AI Documentation](https://docs.crawl4ai.com/extraction/chunking/<https:/docs.crawl4ai.com/>)
  * [ Home ](https://docs.crawl4ai.com/extraction/chunking/<../..>)
  * [ Quick Start ](https://docs.crawl4ai.com/extraction/chunking/core/quickstart/>)
  * [ Search ](https://docs.crawl4ai.com/extraction/chunking/<#>)


  * [Home](https://docs.crawl4ai.com/extraction/chunking/<../..>)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/extraction/chunking/core/installation/>)
    * [Docker Deployment](https://docs.crawl4ai.com/extraction/chunking/core/docker-deploymeny/>)
  * [Quick Start](https://docs.crawl4ai.com/extraction/chunking/core/quickstart/>)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/extraction/chunking/blog/>)
    * [Changelog](https://docs.crawl4ai.com/extraction/chunking/<https:/github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md>)
  * Core
    * [Simple Crawling](https://docs.crawl4ai.com/extraction/chunking/core/simple-crawling/>)
    * [Crawler Result](https://docs.crawl4ai.com/extraction/chunking/core/crawler-result/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/extraction/chunking/core/browser-crawler-config/>)
    * [Markdown Generation](https://docs.crawl4ai.com/extraction/chunking/core/markdown-generation/>)
    * [Fit Markdown](https://docs.crawl4ai.com/extraction/chunking/core/fit-markdown/>)
    * [Page Interaction](https://docs.crawl4ai.com/extraction/chunking/core/page-interaction/>)
    * [Content Selection](https://docs.crawl4ai.com/extraction/chunking/core/content-selection/>)
    * [Cache Modes](https://docs.crawl4ai.com/extraction/chunking/core/cache-modes/>)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/extraction/chunking/core/local-files/>)
    * [Link & Media](https://docs.crawl4ai.com/extraction/chunking/core/link-media/>)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/extraction/chunking/advanced/advanced-features/>)
    * [File Downloading](https://docs.crawl4ai.com/extraction/chunking/advanced/file-downloading/>)
    * [Lazy Loading](https://docs.crawl4ai.com/extraction/chunking/advanced/lazy-loading/>)
    * [Hooks & Auth](https://docs.crawl4ai.com/extraction/chunking/advanced/hooks-auth/>)
    * [Proxy & Security](https://docs.crawl4ai.com/extraction/chunking/advanced/proxy-security/>)
    * [Session Management](https://docs.crawl4ai.com/extraction/chunking/advanced/session-management/>)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/extraction/chunking/advanced/multi-url-crawling/>)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/extraction/chunking/advanced/crawl-dispatcher/>)
    * [Identity Based Crawling](https://docs.crawl4ai.com/extraction/chunking/advanced/identity-based-crawling/>)
    * [SSL Certificate](https://docs.crawl4ai.com/extraction/chunking/advanced/ssl-certificate/>)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/extraction/chunking/<../no-llm-strategies/>)
    * [LLM Strategies](https://docs.crawl4ai.com/extraction/chunking/<../llm-strategies/>)
    * [Clustering Strategies](https://docs.crawl4ai.com/extraction/chunking/<../clustring-strategies/>)
    * Chunking
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/extraction/chunking/api/async-webcrawler/>)
    * [arun()](https://docs.crawl4ai.com/extraction/chunking/api/arun/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/extraction/chunking/api/parameters/>)
    * [CrawlResult](https://docs.crawl4ai.com/extraction/chunking/api/crawl-result/>)
    * [Strategies](https://docs.crawl4ai.com/extraction/chunking/api/strategies/>)


  * [Chunking Strategies](https://docs.crawl4ai.com/extraction/chunking/<#chunking-strategies>)
  * [Why Use Chunking?](https://docs.crawl4ai.com/extraction/chunking/<#why-use-chunking>)
  * [Methods of Chunking](https://docs.crawl4ai.com/extraction/chunking/<#methods-of-chunking>)
  * [Combining Chunking with Cosine Similarity](https://docs.crawl4ai.com/extraction/chunking/<#combining-chunking-with-cosine-similarity>)


# Chunking Strategies
Chunking strategies are critical for dividing large texts into manageable parts, enabling effective content processing and extraction. These strategies are foundational in cosine similarity-based extraction techniques, which allow users to retrieve only the most relevant chunks of content for a given query. Additionally, they facilitate direct integration into RAG (Retrieval-Augmented Generation) systems for structured and scalable workflows.
### Why Use Chunking?
1. **Cosine Similarity and Query Relevance** : Prepares chunks for semantic similarity analysis. 2. **RAG System Integration** : Seamlessly processes and stores chunks for retrieval. 3. **Structured Processing** : Allows for diverse segmentation methods, such as sentence-based, topic-based, or windowed approaches.
### Methods of Chunking
#### 1. Regex-Based Chunking
Splits text based on regular expression patterns, useful for coarse segmentation.
**Code Example** : 
```
class RegexChunking:
  def __init__(self, patterns=None):
    self.patterns = patterns or [r'\n\n'] # Default pattern for paragraphs
  def chunk(self, text):
    paragraphs = [text]
    for pattern in self.patterns:
      paragraphs = [seg for p in paragraphs for seg in re.split(pattern, p)]
    return paragraphs
# Example Usage
text = """This is the first paragraph.
This is the second paragraph."""
chunker = RegexChunking()
print(chunker.chunk(text))

```

#### 2. Sentence-Based Chunking
Divides text into sentences using NLP tools, ideal for extracting meaningful statements.
**Code Example** : 
```
from nltk.tokenize import sent_tokenize
class NlpSentenceChunking:
  def chunk(self, text):
    sentences = sent_tokenize(text)
    return [sentence.strip() for sentence in sentences]
# Example Usage
text = "This is sentence one. This is sentence two."
chunker = NlpSentenceChunking()
print(chunker.chunk(text))

```

#### 3. Topic-Based Segmentation
Uses algorithms like TextTiling to create topic-coherent chunks.
**Code Example** : 
```
from nltk.tokenize import TextTilingTokenizer
class TopicSegmentationChunking:
  def __init__(self):
    self.tokenizer = TextTilingTokenizer()
  def chunk(self, text):
    return self.tokenizer.tokenize(text)
# Example Usage
text = """This is an introduction.
This is a detailed discussion on the topic."""
chunker = TopicSegmentationChunking()
print(chunker.chunk(text))

```

#### 4. Fixed-Length Word Chunking
Segments text into chunks of a fixed word count.
**Code Example** : 
```
class FixedLengthWordChunking:
  def __init__(self, chunk_size=100):
    self.chunk_size = chunk_size
  def chunk(self, text):
    words = text.split()
    return [' '.join(words[i:i + self.chunk_size]) for i in range(0, len(words), self.chunk_size)]
# Example Usage
text = "This is a long text with many words to be chunked into fixed sizes."
chunker = FixedLengthWordChunking(chunk_size=5)
print(chunker.chunk(text))

```

#### 5. Sliding Window Chunking
Generates overlapping chunks for better contextual coherence.
**Code Example** : 
```
class SlidingWindowChunking:
  def __init__(self, window_size=100, step=50):
    self.window_size = window_size
    self.step = step
  def chunk(self, text):
    words = text.split()
    chunks = []
    for i in range(0, len(words) - self.window_size + 1, self.step):
      chunks.append(' '.join(words[i:i + self.window_size]))
    return chunks
# Example Usage
text = "This is a long text to demonstrate sliding window chunking."
chunker = SlidingWindowChunking(window_size=5, step=2)
print(chunker.chunk(text))

```

### Combining Chunking with Cosine Similarity
To enhance the relevance of extracted content, chunking strategies can be paired with cosine similarity techniques. Here’s an example workflow:
**Code Example** : 
```
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
class CosineSimilarityExtractor:
  def __init__(self, query):
    self.query = query
    self.vectorizer = TfidfVectorizer()
  def find_relevant_chunks(self, chunks):
    vectors = self.vectorizer.fit_transform([self.query] + chunks)
    similarities = cosine_similarity(vectors[0:1], vectors[1:]).flatten()
    return [(chunks[i], similarities[i]) for i in range(len(chunks))]
# Example Workflow
text = """This is a sample document. It has multiple sentences. 
We are testing chunking and similarity."""
chunker = SlidingWindowChunking(window_size=5, step=3)
chunks = chunker.chunk(text)
query = "testing chunking"
extractor = CosineSimilarityExtractor(query)
relevant_chunks = extractor.find_relevant_chunks(chunks)
print(relevant_chunks)

```

Site built with [MkDocs](https://docs.crawl4ai.com/extraction/chunking/<http:/www.mkdocs.org>) and [Terminal for MkDocs](https://docs.crawl4ai.com/extraction/chunking/<https:/github.com/ntno/mkdocs-terminal>). 
##### Search
xClose
Type to start searching


==================================================

# URL: https://docs.crawl4ai.com/extraction/clustring-strategies/

[Crawl4AI Documentation](https://docs.crawl4ai.com/extraction/clustring-strategies/<https:/docs.crawl4ai.com/>)
  * [ Home ](https://docs.crawl4ai.com/extraction/clustring-strategies/<../..>)
  * [ Quick Start ](https://docs.crawl4ai.com/extraction/clustring-strategies/core/quickstart/>)
  * [ Search ](https://docs.crawl4ai.com/extraction/clustring-strategies/<#>)


  * [Home](https://docs.crawl4ai.com/extraction/clustring-strategies/<../..>)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/extraction/clustring-strategies/core/installation/>)
    * [Docker Deployment](https://docs.crawl4ai.com/extraction/clustring-strategies/core/docker-deploymeny/>)
  * [Quick Start](https://docs.crawl4ai.com/extraction/clustring-strategies/core/quickstart/>)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/extraction/clustring-strategies/blog/>)
    * [Changelog](https://docs.crawl4ai.com/extraction/clustring-strategies/<https:/github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md>)
  * Core
    * [Simple Crawling](https://docs.crawl4ai.com/extraction/clustring-strategies/core/simple-crawling/>)
    * [Crawler Result](https://docs.crawl4ai.com/extraction/clustring-strategies/core/crawler-result/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/extraction/clustring-strategies/core/browser-crawler-config/>)
    * [Markdown Generation](https://docs.crawl4ai.com/extraction/clustring-strategies/core/markdown-generation/>)
    * [Fit Markdown](https://docs.crawl4ai.com/extraction/clustring-strategies/core/fit-markdown/>)
    * [Page Interaction](https://docs.crawl4ai.com/extraction/clustring-strategies/core/page-interaction/>)
    * [Content Selection](https://docs.crawl4ai.com/extraction/clustring-strategies/core/content-selection/>)
    * [Cache Modes](https://docs.crawl4ai.com/extraction/clustring-strategies/core/cache-modes/>)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/extraction/clustring-strategies/core/local-files/>)
    * [Link & Media](https://docs.crawl4ai.com/extraction/clustring-strategies/core/link-media/>)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/extraction/clustring-strategies/advanced/advanced-features/>)
    * [File Downloading](https://docs.crawl4ai.com/extraction/clustring-strategies/advanced/file-downloading/>)
    * [Lazy Loading](https://docs.crawl4ai.com/extraction/clustring-strategies/advanced/lazy-loading/>)
    * [Hooks & Auth](https://docs.crawl4ai.com/extraction/clustring-strategies/advanced/hooks-auth/>)
    * [Proxy & Security](https://docs.crawl4ai.com/extraction/clustring-strategies/advanced/proxy-security/>)
    * [Session Management](https://docs.crawl4ai.com/extraction/clustring-strategies/advanced/session-management/>)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/extraction/clustring-strategies/advanced/multi-url-crawling/>)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/extraction/clustring-strategies/advanced/crawl-dispatcher/>)
    * [Identity Based Crawling](https://docs.crawl4ai.com/extraction/clustring-strategies/advanced/identity-based-crawling/>)
    * [SSL Certificate](https://docs.crawl4ai.com/extraction/clustring-strategies/advanced/ssl-certificate/>)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/extraction/clustring-strategies/<../no-llm-strategies/>)
    * [LLM Strategies](https://docs.crawl4ai.com/extraction/clustring-strategies/<../llm-strategies/>)
    * Clustering Strategies
    * [Chunking](https://docs.crawl4ai.com/extraction/clustring-strategies/<../chunking/>)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/extraction/clustring-strategies/api/async-webcrawler/>)
    * [arun()](https://docs.crawl4ai.com/extraction/clustring-strategies/api/arun/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/extraction/clustring-strategies/api/parameters/>)
    * [CrawlResult](https://docs.crawl4ai.com/extraction/clustring-strategies/api/crawl-result/>)
    * [Strategies](https://docs.crawl4ai.com/extraction/clustring-strategies/api/strategies/>)


  * [Cosine Strategy](https://docs.crawl4ai.com/extraction/clustring-strategies/<#cosine-strategy>)
  * [How It Works](https://docs.crawl4ai.com/extraction/clustring-strategies/<#how-it-works>)
  * [Basic Usage](https://docs.crawl4ai.com/extraction/clustring-strategies/<#basic-usage>)
  * [Configuration Options](https://docs.crawl4ai.com/extraction/clustring-strategies/<#configuration-options>)
  * [Use Cases](https://docs.crawl4ai.com/extraction/clustring-strategies/<#use-cases>)
  * [Advanced Features](https://docs.crawl4ai.com/extraction/clustring-strategies/<#advanced-features>)
  * [Best Practices](https://docs.crawl4ai.com/extraction/clustring-strategies/<#best-practices>)
  * [Error Handling](https://docs.crawl4ai.com/extraction/clustring-strategies/<#error-handling>)


# Cosine Strategy
The Cosine Strategy in Crawl4AI uses similarity-based clustering to identify and extract relevant content sections from web pages. This strategy is particularly useful when you need to find and extract content based on semantic similarity rather than structural patterns.
## How It Works
The Cosine Strategy: 1. Breaks down page content into meaningful chunks 2. Converts text into vector representations 3. Calculates similarity between chunks 4. Clusters similar content together 5. Ranks and filters content based on relevance
## Basic Usage
```
from crawl4ai.extraction_strategy import CosineStrategy
strategy = CosineStrategy(
  semantic_filter="product reviews",  # Target content type
  word_count_threshold=10,       # Minimum words per cluster
  sim_threshold=0.3          # Similarity threshold
)
async with AsyncWebCrawler() as crawler:
  result = await crawler.arun(
    url="https://example.com/reviews",
    extraction_strategy=strategy
  )
  content = result.extracted_content

```

## Configuration Options
### Core Parameters
```
CosineStrategy(
  # Content Filtering
  semantic_filter: str = None,    # Keywords/topic for content filtering
  word_count_threshold: int = 10,  # Minimum words per cluster
  sim_threshold: float = 0.3,    # Similarity threshold (0.0 to 1.0)
  # Clustering Parameters
  max_dist: float = 0.2,      # Maximum distance for clustering
  linkage_method: str = 'ward',   # Clustering linkage method
  top_k: int = 3,          # Number of top categories to extract
  # Model Configuration
  model_name: str = 'sentence-transformers/all-MiniLM-L6-v2', # Embedding model
  verbose: bool = False       # Enable logging
)

```

### Parameter Details
1. **semantic_filter** - Sets the target topic or content type - Use keywords relevant to your desired content - Example: "technical specifications", "user reviews", "pricing information"
2. **sim_threshold** - Controls how similar content must be to be grouped together - Higher values (e.g., 0.8) mean stricter matching - Lower values (e.g., 0.3) allow more variation 
```
# Strict matching
strategy = CosineStrategy(sim_threshold=0.8)
# Loose matching
strategy = CosineStrategy(sim_threshold=0.3)

```

3. **word_count_threshold** - Filters out short content blocks - Helps eliminate noise and irrelevant content 
```
# Only consider substantial paragraphs
strategy = CosineStrategy(word_count_threshold=50)

```

4. **top_k** - Number of top content clusters to return - Higher values return more diverse content 
```
# Get top 5 most relevant content clusters
strategy = CosineStrategy(top_k=5)

```

## Use Cases
### 1. Article Content Extraction
```
strategy = CosineStrategy(
  semantic_filter="main article content",
  word_count_threshold=100, # Longer blocks for articles
  top_k=1          # Usually want single main content
)
result = await crawler.arun(
  url="https://example.com/blog/post",
  extraction_strategy=strategy
)

```

### 2. Product Review Analysis
```
strategy = CosineStrategy(
  semantic_filter="customer reviews and ratings",
  word_count_threshold=20,  # Reviews can be shorter
  top_k=10,         # Get multiple reviews
  sim_threshold=0.4     # Allow variety in review content
)

```

### 3. Technical Documentation
```
strategy = CosineStrategy(
  semantic_filter="technical specifications documentation",
  word_count_threshold=30,
  sim_threshold=0.6,    # Stricter matching for technical content
  max_dist=0.3       # Allow related technical sections
)

```

## Advanced Features
### Custom Clustering
```
strategy = CosineStrategy(
  linkage_method='complete', # Alternative clustering method
  max_dist=0.4,       # Larger clusters
  model_name='sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2' # Multilingual support
)

```

### Content Filtering Pipeline
```
strategy = CosineStrategy(
  semantic_filter="pricing plans features",
  word_count_threshold=15,
  sim_threshold=0.5,
  top_k=3
)
async def extract_pricing_features(url: str):
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(
      url=url,
      extraction_strategy=strategy
    )
    if result.success:
      content = json.loads(result.extracted_content)
      return {
        'pricing_features': content,
        'clusters': len(content),
        'similarity_scores': [item['score'] for item in content]
      }

```

## Best Practices
1. **Adjust Thresholds Iteratively** - Start with default values - Adjust based on results - Monitor clustering quality
2. **Choose Appropriate Word Count Thresholds** - Higher for articles (100+) - Lower for reviews/comments (20+) - Medium for product descriptions (50+)
3. **Optimize Performance**
```
strategy = CosineStrategy(
  word_count_threshold=10, # Filter early
  top_k=5,         # Limit results
  verbose=True       # Monitor performance
)

```

4. **Handle Different Content Types**
```
# For mixed content pages
strategy = CosineStrategy(
  semantic_filter="product features",
  sim_threshold=0.4,   # More flexible matching
  max_dist=0.3,     # Larger clusters
  top_k=3        # Multiple relevant sections
)

```

## Error Handling
```
try:
  result = await crawler.arun(
    url="https://example.com",
    extraction_strategy=strategy
  )
  if result.success:
    content = json.loads(result.extracted_content)
    if not content:
      print("No relevant content found")
  else:
    print(f"Extraction failed: {result.error_message}")
except Exception as e:
  print(f"Error during extraction: {str(e)}")

```

The Cosine Strategy is particularly effective when: - Content structure is inconsistent - You need semantic understanding - You want to find similar content blocks - Structure-based extraction (CSS/XPath) isn't reliable
It works well with other strategies and can be used as a pre-processing step for LLM-based extraction.
Site built with [MkDocs](https://docs.crawl4ai.com/extraction/clustring-strategies/<http:/www.mkdocs.org>) and [Terminal for MkDocs](https://docs.crawl4ai.com/extraction/clustring-strategies/<https:/github.com/ntno/mkdocs-terminal>). 
##### Search
xClose
Type to start searching


==================================================

# URL: https://docs.crawl4ai.com/extraction/llm-strategies/

[Crawl4AI Documentation](https://docs.crawl4ai.com/extraction/llm-strategies/<https:/docs.crawl4ai.com/>)
  * [ Home ](https://docs.crawl4ai.com/extraction/llm-strategies/<../..>)
  * [ Quick Start ](https://docs.crawl4ai.com/extraction/llm-strategies/core/quickstart/>)
  * [ Search ](https://docs.crawl4ai.com/extraction/llm-strategies/<#>)


  * [Home](https://docs.crawl4ai.com/extraction/llm-strategies/<../..>)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/extraction/llm-strategies/core/installation/>)
    * [Docker Deployment](https://docs.crawl4ai.com/extraction/llm-strategies/core/docker-deploymeny/>)
  * [Quick Start](https://docs.crawl4ai.com/extraction/llm-strategies/core/quickstart/>)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/extraction/llm-strategies/blog/>)
    * [Changelog](https://docs.crawl4ai.com/extraction/llm-strategies/<https:/github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md>)
  * Core
    * [Simple Crawling](https://docs.crawl4ai.com/extraction/llm-strategies/core/simple-crawling/>)
    * [Crawler Result](https://docs.crawl4ai.com/extraction/llm-strategies/core/crawler-result/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/extraction/llm-strategies/core/browser-crawler-config/>)
    * [Markdown Generation](https://docs.crawl4ai.com/extraction/llm-strategies/core/markdown-generation/>)
    * [Fit Markdown](https://docs.crawl4ai.com/extraction/llm-strategies/core/fit-markdown/>)
    * [Page Interaction](https://docs.crawl4ai.com/extraction/llm-strategies/core/page-interaction/>)
    * [Content Selection](https://docs.crawl4ai.com/extraction/llm-strategies/core/content-selection/>)
    * [Cache Modes](https://docs.crawl4ai.com/extraction/llm-strategies/core/cache-modes/>)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/extraction/llm-strategies/core/local-files/>)
    * [Link & Media](https://docs.crawl4ai.com/extraction/llm-strategies/core/link-media/>)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/extraction/llm-strategies/advanced/advanced-features/>)
    * [File Downloading](https://docs.crawl4ai.com/extraction/llm-strategies/advanced/file-downloading/>)
    * [Lazy Loading](https://docs.crawl4ai.com/extraction/llm-strategies/advanced/lazy-loading/>)
    * [Hooks & Auth](https://docs.crawl4ai.com/extraction/llm-strategies/advanced/hooks-auth/>)
    * [Proxy & Security](https://docs.crawl4ai.com/extraction/llm-strategies/advanced/proxy-security/>)
    * [Session Management](https://docs.crawl4ai.com/extraction/llm-strategies/advanced/session-management/>)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/extraction/llm-strategies/advanced/multi-url-crawling/>)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/extraction/llm-strategies/advanced/crawl-dispatcher/>)
    * [Identity Based Crawling](https://docs.crawl4ai.com/extraction/llm-strategies/advanced/identity-based-crawling/>)
    * [SSL Certificate](https://docs.crawl4ai.com/extraction/llm-strategies/advanced/ssl-certificate/>)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/extraction/llm-strategies/<../no-llm-strategies/>)
    * LLM Strategies
    * [Clustering Strategies](https://docs.crawl4ai.com/extraction/llm-strategies/<../clustring-strategies/>)
    * [Chunking](https://docs.crawl4ai.com/extraction/llm-strategies/<../chunking/>)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/extraction/llm-strategies/api/async-webcrawler/>)
    * [arun()](https://docs.crawl4ai.com/extraction/llm-strategies/api/arun/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/extraction/llm-strategies/api/parameters/>)
    * [CrawlResult](https://docs.crawl4ai.com/extraction/llm-strategies/api/crawl-result/>)
    * [Strategies](https://docs.crawl4ai.com/extraction/llm-strategies/api/strategies/>)


  * [Extracting JSON (LLM)](https://docs.crawl4ai.com/extraction/llm-strategies/<#extracting-json-llm>)
  * [1. Why Use an LLM?](https://docs.crawl4ai.com/extraction/llm-strategies/<#1-why-use-an-llm>)
  * [2. Provider-Agnostic via LightLLM](https://docs.crawl4ai.com/extraction/llm-strategies/<#2-provider-agnostic-via-lightllm>)
  * [3. How LLM Extraction Works](https://docs.crawl4ai.com/extraction/llm-strategies/<#3-how-llm-extraction-works>)
  * [4. Key Parameters](https://docs.crawl4ai.com/extraction/llm-strategies/<#4-key-parameters>)
  * [5. Putting It in CrawlerRunConfig](https://docs.crawl4ai.com/extraction/llm-strategies/<#5-putting-it-in-crawlerrunconfig>)
  * [6. Chunking Details](https://docs.crawl4ai.com/extraction/llm-strategies/<#6-chunking-details>)
  * [7. Input Format](https://docs.crawl4ai.com/extraction/llm-strategies/<#7-input-format>)
  * [8. Token Usage & Show Usage](https://docs.crawl4ai.com/extraction/llm-strategies/<#8-token-usage-show-usage>)
  * [9. Example: Building a Knowledge Graph](https://docs.crawl4ai.com/extraction/llm-strategies/<#9-example-building-a-knowledge-graph>)
  * [10. Best Practices & Caveats](https://docs.crawl4ai.com/extraction/llm-strategies/<#10-best-practices-caveats>)
  * [11. Conclusion](https://docs.crawl4ai.com/extraction/llm-strategies/<#11-conclusion>)


# Extracting JSON (LLM)
In some cases, you need to extract **complex or unstructured** information from a webpage that a simple CSS/XPath schema cannot easily parse. Or you want **AI** -driven insights, classification, or summarization. For these scenarios, Crawl4AI provides an **LLM-based extraction strategy** that:
  1. Works with **any** large language model supported by [LightLLM](https://docs.crawl4ai.com/extraction/llm-strategies/<https:/github.com/LightLLM>) (Ollama, OpenAI, Claude, and more). 
  2. Automatically splits content into chunks (if desired) to handle token limits, then combines results. 
  3. Lets you define a **schema** (like a Pydantic model) or a simpler “block” extraction approach.


**Important** : LLM-based extraction can be slower and costlier than schema-based approaches. If your page data is highly structured, consider using `JsonCssExtractionStrategy`[](https://docs.crawl4ai.com/extraction/llm-strategies/<../no-llm-strategies/>) or `JsonXPathExtractionStrategy`[](https://docs.crawl4ai.com/extraction/llm-strategies/<../no-llm-strategies/>) first. But if you need AI to interpret or reorganize content, read on!
## 1. Why Use an LLM?
  * **Complex Reasoning** : If the site’s data is unstructured, scattered, or full of natural language context. 
  * **Semantic Extraction** : Summaries, knowledge graphs, or relational data that require comprehension. 
  * **Flexible** : You can pass instructions to the model to do more advanced transformations or classification.


## 2. Provider-Agnostic via LightLLM
Crawl4AI uses a “provider string” (e.g., `"openai/gpt-4o"`, `"ollama/llama2.0"`, `"aws/titan"`) to identify your LLM. **Any** model that LightLLM supports is fair game. You just provide:
  * **`provider`**: The`<provider>/<model_name>` identifier (e.g., `"openai/gpt-4"`, `"ollama/llama2"`, `"huggingface/google-flan"`, etc.). 
  * **`api_token`**: If needed (for OpenAI, HuggingFace, etc.); local models or Ollama might not require it.
  * **`api_base`**(optional): If your provider has a custom endpoint.


This means you **aren’t locked** into a single LLM vendor. Switch or experiment easily.
## 3. How LLM Extraction Works
### 3.1 Flow
1. **Chunking** (optional): The HTML or markdown is split into smaller segments if it’s very long (based on `chunk_token_threshold`, overlap, etc.). 2. **Prompt Construction** : For each chunk, the library forms a prompt that includes your **`instruction`**(and possibly schema or examples). 3.**LLM Inference** : Each chunk is sent to the model in parallel or sequentially (depending on your concurrency). 4. **Combining** : The results from each chunk are merged and parsed into JSON.
### 3.2 `extraction_type`
  * **`"schema"`**: The model tries to return JSON conforming to your Pydantic-based schema.
  * **`"block"`**: The model returns freeform text, or smaller JSON structures, which the library collects.


For structured data, `"schema"` is recommended. You provide `schema=YourPydanticModel.model_json_schema()`.
## 4. Key Parameters
Below is an overview of important LLM extraction parameters. All are typically set inside `LLMExtractionStrategy(...)`. You then put that strategy in your `CrawlerRunConfig(..., extraction_strategy=...)`.
1. **`provider`**(str): e.g.,`"openai/gpt-4"` , `"ollama/llama2"`. 2. **`api_token`**(str): The API key or token for that model. May not be needed for local models. 3.**`schema`**(dict): A JSON schema describing the fields you want. Usually generated by`YourModel.model_json_schema()`. 4. **`extraction_type`**(str):`"schema"` or `"block"`. 5. **`instruction`**(str): Prompt text telling the LLM what you want extracted. E.g., “Extract these fields as a JSON array.” 6.**`chunk_token_threshold`**(int): Maximum tokens per chunk. If your content is huge, you can break it up for the LLM. 7.**`overlap_rate`**(float): Overlap ratio between adjacent chunks. E.g.,`0.1` means 10% of each chunk is repeated to preserve context continuity. 8. **`apply_chunking`**(bool): Set`True` to chunk automatically. If you want a single pass, set `False`. 9. **`input_format`**(str): Determines**which** crawler result is passed to the LLM. Options include: - `"markdown"`: The raw markdown (default). - `"fit_markdown"`: The filtered “fit” markdown if you used a content filter. - `"html"`: The cleaned or raw HTML. 10. **`extra_args`**(dict): Additional LLM parameters like`temperature` , `max_tokens`, `top_p`, etc. 11. **`show_usage()`**: A method you can call to print out usage info (token usage per chunk, total cost if known).
**Example** :
```
extraction_strategy = LLMExtractionStrategy(
  provider="openai/gpt-4",
  api_token="YOUR_OPENAI_KEY",
  schema=MyModel.model_json_schema(),
  extraction_type="schema",
  instruction="Extract a list of items from the text with 'name' and 'price' fields.",
  chunk_token_threshold=1200,
  overlap_rate=0.1,
  apply_chunking=True,
  input_format="html",
  extra_args={"temperature": 0.1, "max_tokens": 1000},
  verbose=True
)

```

## 5. Putting It in `CrawlerRunConfig`
**Important** : In Crawl4AI, all strategy definitions should go inside the `CrawlerRunConfig`, not directly as a param in `arun()`. Here’s a full example:
```
import os
import asyncio
import json
from pydantic import BaseModel, Field
from typing import List
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from crawl4ai.extraction_strategy import LLMExtractionStrategy
class Product(BaseModel):
  name: str
  price: str
async def main():
  # 1. Define the LLM extraction strategy
  llm_strategy = LLMExtractionStrategy(
    provider="openai/gpt-4o-mini",      # e.g. "ollama/llama2"
    api_token=os.getenv('OPENAI_API_KEY'),
    schema=Product.schema_json(),      # Or use model_json_schema()
    extraction_type="schema",
    instruction="Extract all product objects with 'name' and 'price' from the content.",
    chunk_token_threshold=1000,
    overlap_rate=0.0,
    apply_chunking=True,
    input_format="markdown",  # or "html", "fit_markdown"
    extra_args={"temperature": 0.0, "max_tokens": 800}
  )
  # 2. Build the crawler config
  crawl_config = CrawlerRunConfig(
    extraction_strategy=llm_strategy,
    cache_mode=CacheMode.BYPASS
  )
  # 3. Create a browser config if needed
  browser_cfg = BrowserConfig(headless=True)
  async with AsyncWebCrawler(config=browser_cfg) as crawler:
    # 4. Let's say we want to crawl a single page
    result = await crawler.arun(
      url="https://example.com/products",
      config=crawl_config
    )
    if result.success:
      # 5. The extracted content is presumably JSON
      data = json.loads(result.extracted_content)
      print("Extracted items:", data)
      # 6. Show usage stats
      llm_strategy.show_usage() # prints token usage
    else:
      print("Error:", result.error_message)
if __name__ == "__main__":
  asyncio.run(main())

```

## 6. Chunking Details
### 6.1 `chunk_token_threshold`
If your page is large, you might exceed your LLM’s context window. **`chunk_token_threshold`**sets the approximate max tokens per chunk. The library calculates word→token ratio using`word_token_rate` (often ~0.75 by default). If chunking is enabled (`apply_chunking=True`), the text is split into segments.
### 6.2 `overlap_rate`
To keep context continuous across chunks, we can overlap them. E.g., `overlap_rate=0.1` means each subsequent chunk includes 10% of the previous chunk’s text. This is helpful if your needed info might straddle chunk boundaries.
### 6.3 Performance & Parallelism
By chunking, you can potentially process multiple chunks in parallel (depending on your concurrency settings and the LLM provider). This reduces total time if the site is huge or has many sections.
## 7. Input Format
By default, **LLMExtractionStrategy** uses `input_format="markdown"`, meaning the **crawler’s final markdown** is fed to the LLM. You can change to:
  * **`html`**: The cleaned HTML or raw HTML (depending on your crawler config) goes into the LLM.
  * **`fit_markdown`**: If you used, for instance,`PruningContentFilter` , the “fit” version of the markdown is used. This can drastically reduce tokens if you trust the filter. 
  * **`markdown`**: Standard markdown output from the crawler’s`markdown_generator`.


This setting is crucial: if the LLM instructions rely on HTML tags, pick `"html"`. If you prefer a text-based approach, pick `"markdown"`.
```
LLMExtractionStrategy(
  # ...
  input_format="html", # Instead of "markdown" or "fit_markdown"
)

```

## 8. Token Usage & Show Usage
To keep track of tokens and cost, each chunk is processed with an LLM call. We record usage in:
  * **`usages`**(list): token usage per chunk or call.
  * **`total_usage`**: sum of all chunk calls.
  * **`show_usage()`**: prints a usage report (if the provider returns usage data).


```
llm_strategy = LLMExtractionStrategy(...)
# ...
llm_strategy.show_usage()
# e.g. “Total usage: 1241 tokens across 2 chunk calls”

```

If your model provider doesn’t return usage info, these fields might be partial or empty.
## 9. Example: Building a Knowledge Graph
Below is a snippet combining **`LLMExtractionStrategy`**with a Pydantic schema for a knowledge graph. Notice how we pass an**`instruction`**telling the model what to parse.
```
import os
import json
import asyncio
from typing import List
from pydantic import BaseModel, Field
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from crawl4ai.extraction_strategy import LLMExtractionStrategy
class Entity(BaseModel):
  name: str
  description: str
class Relationship(BaseModel):
  entity1: Entity
  entity2: Entity
  description: str
  relation_type: str
class KnowledgeGraph(BaseModel):
  entities: List[Entity]
  relationships: List[Relationship]
async def main():
  # LLM extraction strategy
  llm_strat = LLMExtractionStrategy(
    provider="openai/gpt-4",
    api_token=os.getenv('OPENAI_API_KEY'),
    schema=KnowledgeGraph.schema_json(),
    extraction_type="schema",
    instruction="Extract entities and relationships from the content. Return valid JSON.",
    chunk_token_threshold=1400,
    apply_chunking=True,
    input_format="html",
    extra_args={"temperature": 0.1, "max_tokens": 1500}
  )
  crawl_config = CrawlerRunConfig(
    extraction_strategy=llm_strat,
    cache_mode=CacheMode.BYPASS
  )
  async with AsyncWebCrawler(config=BrowserConfig(headless=True)) as crawler:
    # Example page
    url = "https://www.nbcnews.com/business"
    result = await crawler.arun(url=url, config=crawl_config)
    if result.success:
      with open("kb_result.json", "w", encoding="utf-8") as f:
        f.write(result.extracted_content)
      llm_strat.show_usage()
    else:
      print("Crawl failed:", result.error_message)
if __name__ == "__main__":
  asyncio.run(main())

```

**Key Observations** :
  * **`extraction_type="schema"`**ensures we get JSON fitting our`KnowledgeGraph`. 
  * **`input_format="html"`**means we feed HTML to the model.
  * **`instruction`**guides the model to output a structured knowledge graph.


## 10. Best Practices & Caveats
1. **Cost & Latency**: LLM calls can be slow or expensive. Consider chunking or smaller coverage if you only need partial data. 2. **Model Token Limits** : If your page + instruction exceed the context window, chunking is essential. 3. **Instruction Engineering** : Well-crafted instructions can drastically improve output reliability. 4. **Schema Strictness** : `"schema"` extraction tries to parse the model output as JSON. If the model returns invalid JSON, partial extraction might happen, or you might get an error. 5. **Parallel vs. Serial** : The library can process multiple chunks in parallel, but you must watch out for rate limits on certain providers. 6. **Check Output** : Sometimes, an LLM might omit fields or produce extraneous text. You may want to post-validate with Pydantic or do additional cleanup.
## 11. Conclusion
**LLM-based extraction** in Crawl4AI is **provider-agnostic** , letting you choose from hundreds of models via LightLLM. It’s perfect for **semantically complex** tasks or generating advanced structures like knowledge graphs. However, it’s **slower** and potentially costlier than schema-based approaches. Keep these tips in mind:
  * Put your LLM strategy **in`CrawlerRunConfig`**. 
  * Use **`input_format`**to pick which form (markdown, HTML, fit_markdown) the LLM sees.
  * Tweak **`chunk_token_threshold`**,**`overlap_rate`**, and**`apply_chunking`**to handle large content efficiently.
  * Monitor token usage with `show_usage()`.


If your site’s data is consistent or repetitive, consider `JsonCssExtractionStrategy`[](https://docs.crawl4ai.com/extraction/llm-strategies/<../no-llm-strategies/>) first for speed and simplicity. But if you need an **AI-driven** approach, `LLMExtractionStrategy` offers a flexible, multi-provider solution for extracting structured JSON from any website.
**Next Steps** :
1. **Experiment with Different Providers** - Try switching the `provider` (e.g., `"ollama/llama2"`, `"openai/gpt-4o"`, etc.) to see differences in speed, accuracy, or cost. - Pass different `extra_args` like `temperature`, `top_p`, and `max_tokens` to fine-tune your results.
2. **Performance Tuning** - If pages are large, tweak `chunk_token_threshold`, `overlap_rate`, or `apply_chunking` to optimize throughput. - Check the usage logs with `show_usage()` to keep an eye on token consumption and identify potential bottlenecks.
3. **Validate Outputs** - If using `extraction_type="schema"`, parse the LLM’s JSON with a Pydantic model for a final validation step. - Log or handle any parse errors gracefully, especially if the model occasionally returns malformed JSON.
4. **Explore Hooks & Automation** - Integrate LLM extraction with [hooks](https://docs.crawl4ai.com/extraction/llm-strategies/advanced/hooks-auth/>) for complex pre/post-processing. - Use a multi-step pipeline: crawl, filter, LLM-extract, then store or index results for further analysis.
**Last Updated** : 2025-01-01
That’s it for **Extracting JSON (LLM)** —now you can harness AI to parse, classify, or reorganize data on the web. Happy crawling!
Site built with [MkDocs](https://docs.crawl4ai.com/extraction/llm-strategies/<http:/www.mkdocs.org>) and [Terminal for MkDocs](https://docs.crawl4ai.com/extraction/llm-strategies/<https:/github.com/ntno/mkdocs-terminal>). 
##### Search
xClose
Type to start searching


==================================================

# URL: https://docs.crawl4ai.com/extraction/no-llm-strategies/

[Crawl4AI Documentation](https://docs.crawl4ai.com/extraction/no-llm-strategies/<https:/docs.crawl4ai.com/>)
  * [ Home ](https://docs.crawl4ai.com/extraction/no-llm-strategies/<../..>)
  * [ Quick Start ](https://docs.crawl4ai.com/extraction/no-llm-strategies/core/quickstart/>)
  * [ Search ](https://docs.crawl4ai.com/extraction/no-llm-strategies/<#>)


  * [Home](https://docs.crawl4ai.com/extraction/no-llm-strategies/<../..>)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/extraction/no-llm-strategies/core/installation/>)
    * [Docker Deployment](https://docs.crawl4ai.com/extraction/no-llm-strategies/core/docker-deploymeny/>)
  * [Quick Start](https://docs.crawl4ai.com/extraction/no-llm-strategies/core/quickstart/>)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/extraction/no-llm-strategies/blog/>)
    * [Changelog](https://docs.crawl4ai.com/extraction/no-llm-strategies/<https:/github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md>)
  * Core
    * [Simple Crawling](https://docs.crawl4ai.com/extraction/no-llm-strategies/core/simple-crawling/>)
    * [Crawler Result](https://docs.crawl4ai.com/extraction/no-llm-strategies/core/crawler-result/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/extraction/no-llm-strategies/core/browser-crawler-config/>)
    * [Markdown Generation](https://docs.crawl4ai.com/extraction/no-llm-strategies/core/markdown-generation/>)
    * [Fit Markdown](https://docs.crawl4ai.com/extraction/no-llm-strategies/core/fit-markdown/>)
    * [Page Interaction](https://docs.crawl4ai.com/extraction/no-llm-strategies/core/page-interaction/>)
    * [Content Selection](https://docs.crawl4ai.com/extraction/no-llm-strategies/core/content-selection/>)
    * [Cache Modes](https://docs.crawl4ai.com/extraction/no-llm-strategies/core/cache-modes/>)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/extraction/no-llm-strategies/core/local-files/>)
    * [Link & Media](https://docs.crawl4ai.com/extraction/no-llm-strategies/core/link-media/>)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/extraction/no-llm-strategies/advanced/advanced-features/>)
    * [File Downloading](https://docs.crawl4ai.com/extraction/no-llm-strategies/advanced/file-downloading/>)
    * [Lazy Loading](https://docs.crawl4ai.com/extraction/no-llm-strategies/advanced/lazy-loading/>)
    * [Hooks & Auth](https://docs.crawl4ai.com/extraction/no-llm-strategies/advanced/hooks-auth/>)
    * [Proxy & Security](https://docs.crawl4ai.com/extraction/no-llm-strategies/advanced/proxy-security/>)
    * [Session Management](https://docs.crawl4ai.com/extraction/no-llm-strategies/advanced/session-management/>)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/extraction/no-llm-strategies/advanced/multi-url-crawling/>)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/extraction/no-llm-strategies/advanced/crawl-dispatcher/>)
    * [Identity Based Crawling](https://docs.crawl4ai.com/extraction/no-llm-strategies/advanced/identity-based-crawling/>)
    * [SSL Certificate](https://docs.crawl4ai.com/extraction/no-llm-strategies/advanced/ssl-certificate/>)
  * Extraction
    * LLM-Free Strategies
    * [LLM Strategies](https://docs.crawl4ai.com/extraction/no-llm-strategies/<../llm-strategies/>)
    * [Clustering Strategies](https://docs.crawl4ai.com/extraction/no-llm-strategies/<../clustring-strategies/>)
    * [Chunking](https://docs.crawl4ai.com/extraction/no-llm-strategies/<../chunking/>)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/extraction/no-llm-strategies/api/async-webcrawler/>)
    * [arun()](https://docs.crawl4ai.com/extraction/no-llm-strategies/api/arun/>)
    * [Browser & Crawler Config](https://docs.crawl4ai.com/extraction/no-llm-strategies/api/parameters/>)
    * [CrawlResult](https://docs.crawl4ai.com/extraction/no-llm-strategies/api/crawl-result/>)
    * [Strategies](https://docs.crawl4ai.com/extraction/no-llm-strategies/api/strategies/>)


  * [Extracting JSON (No LLM)](https://docs.crawl4ai.com/extraction/no-llm-strategies/<#extracting-json-no-llm>)
  * [1. Intro to Schema-Based Extraction](https://docs.crawl4ai.com/extraction/no-llm-strategies/<#1-intro-to-schema-based-extraction>)
  * [2. Simple Example: Crypto Prices](https://docs.crawl4ai.com/extraction/no-llm-strategies/<#2-simple-example-crypto-prices>)
  * [3. Advanced Schema & Nested Structures](https://docs.crawl4ai.com/extraction/no-llm-strategies/<#3-advanced-schema-nested-structures>)
  * [4. Why “No LLM” Is Often Better](https://docs.crawl4ai.com/extraction/no-llm-strategies/<#4-why-no-llm-is-often-better>)
  * [5. Base Element Attributes & Additional Fields](https://docs.crawl4ai.com/extraction/no-llm-strategies/<#5-base-element-attributes-additional-fields>)
  * [6. Putting It All Together: Larger Example](https://docs.crawl4ai.com/extraction/no-llm-strategies/<#6-putting-it-all-together-larger-example>)
  * [7. Tips & Best Practices](https://docs.crawl4ai.com/extraction/no-llm-strategies/<#7-tips-best-practices>)
  * [8. Conclusion](https://docs.crawl4ai.com/extraction/no-llm-strategies/<#8-conclusion>)


# Extracting JSON (No LLM)
One of Crawl4AI’s **most powerful** features is extracting **structured JSON** from websites **without** relying on large language models. By defining a **schema** with CSS or XPath selectors, you can extract data instantly—even from complex or nested HTML structures—without the cost, latency, or environmental impact of an LLM.
**Why avoid LLM for basic extractions?**
1. **Faster & Cheaper**: No API calls or GPU overhead. 2. **Lower Carbon Footprint** : LLM inference can be energy-intensive. A well-defined schema is practically carbon-free. 3. **Precise & Repeatable**: CSS/XPath selectors do exactly what you specify. LLM outputs can vary or hallucinate. 4. **Scales Readily** : For thousands of pages, schema-based extraction runs quickly and in parallel.
Below, we’ll explore how to craft these schemas and use them with **JsonCssExtractionStrategy** (or **JsonXPathExtractionStrategy** if you prefer XPath). We’ll also highlight advanced features like **nested fields** and **base element attributes**.
## 1. Intro to Schema-Based Extraction
A schema defines:
  1. A **base selector** that identifies each “container” element on the page (e.g., a product row, a blog post card). 2. **Fields** describing which CSS/XPath selectors to use for each piece of data you want to capture (text, attribute, HTML block, etc.). 3. **Nested** or **list** types for repeated or hierarchical structures. 


For example, if you have a list of products, each one might have a name, price, reviews, and “related products.” This approach is faster and more reliable than an LLM for consistent, structured pages.
## 2. Simple Example: Crypto Prices
Let’s begin with a **simple** schema-based extraction using the `JsonCssExtractionStrategy`. Below is a snippet that extracts cryptocurrency prices from a site (similar to the legacy Coinbase example). Notice we **don’t** call any LLM:
```
import json
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
async def extract_crypto_prices():
  # 1. Define a simple extraction schema
  schema = {
    "name": "Crypto Prices",
    "baseSelector": "div.crypto-row",  # Repeated elements
    "fields": [
      {
        "name": "coin_name",
        "selector": "h2.coin-name",
        "type": "text"
      },
      {
        "name": "price",
        "selector": "span.coin-price",
        "type": "text"
      }
    ]
  }
  # 2. Create the extraction strategy
  extraction_strategy = JsonCssExtractionStrategy(schema, verbose=True)
  # 3. Set up your crawler config (if needed)
  config = CrawlerRunConfig(
    # e.g., pass js_code or wait_for if the page is dynamic
    # wait_for="css:.crypto-row:nth-child(20)"
    cache_mode = CacheMode.BYPASS,
    extraction_strategy=extraction_strategy,
  )
  async with AsyncWebCrawler(verbose=True) as crawler:
    # 4. Run the crawl and extraction
    result = await crawler.arun(
      url="https://example.com/crypto-prices",
      config=config
    )
    if not result.success:
      print("Crawl failed:", result.error_message)
      return
    # 5. Parse the extracted JSON
    data = json.loads(result.extracted_content)
    print(f"Extracted {len(data)} coin entries")
    print(json.dumps(data[0], indent=2) if data else "No data found")
asyncio.run(extract_crypto_prices())

```

**Highlights** :
  * **`baseSelector`**: Tells us where each “item” (crypto row) is.
  * **`fields`**: Two fields (`coin_name` , `price`) using simple CSS selectors. 
  * Each field defines a **`type`**(e.g.,`text` , `attribute`, `html`, `regex`, etc.).


No LLM is needed, and the performance is **near-instant** for hundreds or thousands of items.
### **XPath Example with`raw://` HTML**
Below is a short example demonstrating **XPath** extraction plus the **`raw://`**scheme. We’ll pass a**dummy HTML** directly (no network request) and define the extraction strategy in `CrawlerRunConfig`.
```
import json
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.extraction_strategy import JsonXPathExtractionStrategy
async def extract_crypto_prices_xpath():
  # 1. Minimal dummy HTML with some repeating rows
  dummy_html = """
  <html>
   <body>
    <div class='crypto-row'>
     <h2 class='coin-name'>Bitcoin</h2>
     <span class='coin-price'>$28,000</span>
    </div>
    <div class='crypto-row'>
     <h2 class='coin-name'>Ethereum</h2>
     <span class='coin-price'>$1,800</span>
    </div>
   </body>
  </html>
  """
  # 2. Define the JSON schema (XPath version)
  schema = {
    "name": "Crypto Prices via XPath",
    "baseSelector": "//div[@class='crypto-row']",
    "fields": [
      {
        "name": "coin_name",
        "selector": ".//h2[@class='coin-name']",
        "type": "text"
      },
      {
        "name": "price",
        "selector": ".//span[@class='coin-price']",
        "type": "text"
      }
    ]
  }
  # 3. Place the strategy in the CrawlerRunConfig
  config = CrawlerRunConfig(
    extraction_strategy=JsonXPathExtractionStrategy(schema, verbose=True)
  )
  # 4. Use raw:// scheme to pass dummy_html directly
  raw_url = f"raw://{dummy_html}"
  async with AsyncWebCrawler(verbose=True) as crawler:
    result = await crawler.arun(
      url=raw_url,
      config=config
    )
    if not result.success:
      print("Crawl failed:", result.error_message)
      return
    data = json.loads(result.extracted_content)
    print(f"Extracted {len(data)} coin rows")
    if data:
      print("First item:", data[0])
asyncio.run(extract_crypto_prices_xpath())

```

**Key Points** :
1. **`JsonXPathExtractionStrategy`**is used instead of`JsonCssExtractionStrategy`. 2. **`baseSelector`**and each field’s`"selector"` use **XPath** instead of CSS. 3. **`raw://`**lets us pass`dummy_html` with no real network request—handy for local testing. 4. Everything (including the extraction strategy) is in **`CrawlerRunConfig`**.
That’s how you keep the config self-contained, illustrate **XPath** usage, and demonstrate the **raw** scheme for direct HTML input—all while avoiding the old approach of passing `extraction_strategy` directly to `arun()`.
## 3. Advanced Schema & Nested Structures
Real sites often have **nested** or repeated data—like categories containing products, which themselves have a list of reviews or features. For that, we can define **nested** or **list** (and even **nested_list**) fields.
### Sample E-Commerce HTML
We have a **sample e-commerce** HTML file on GitHub (example): 
```
https://gist.githubusercontent.com/githubusercontent/2d7b8ba3cd8ab6cf3c8da771ddb36878/raw/1ae2f90c6861ce7dd84cc50d3df9920dee5e1fd2/sample_ecommerce.html

```

This snippet includes categories, products, features, reviews, and related items. Let’s see how to define a schema that fully captures that structure **without LLM**. 
```
schema = {
  "name": "E-commerce Product Catalog",
  "baseSelector": "div.category",
  # (1) We can define optional baseFields if we want to extract attributes 
  # from the category container
  "baseFields": [
    {"name": "data_cat_id", "type": "attribute", "attribute": "data-cat-id"}, 
  ],
  "fields": [
    {
      "name": "category_name",
      "selector": "h2.category-name",
      "type": "text"
    },
    {
      "name": "products",
      "selector": "div.product",
      "type": "nested_list",  # repeated sub-objects
      "fields": [
        {
          "name": "name",
          "selector": "h3.product-name",
          "type": "text"
        },
        {
          "name": "price",
          "selector": "p.product-price",
          "type": "text"
        },
        {
          "name": "details",
          "selector": "div.product-details",
          "type": "nested", # single sub-object
          "fields": [
            {
              "name": "brand",
              "selector": "span.brand",
              "type": "text"
            },
            {
              "name": "model",
              "selector": "span.model",
              "type": "text"
            }
          ]
        },
        {
          "name": "features",
          "selector": "ul.product-features li",
          "type": "list",
          "fields": [
            {"name": "feature", "type": "text"} 
          ]
        },
        {
          "name": "reviews",
          "selector": "div.review",
          "type": "nested_list",
          "fields": [
            {
              "name": "reviewer", 
              "selector": "span.reviewer", 
              "type": "text"
            },
            {
              "name": "rating", 
              "selector": "span.rating", 
              "type": "text"
            },
            {
              "name": "comment", 
              "selector": "p.review-text", 
              "type": "text"
            }
          ]
        },
        {
          "name": "related_products",
          "selector": "ul.related-products li",
          "type": "list",
          "fields": [
            {
              "name": "name", 
              "selector": "span.related-name", 
              "type": "text"
            },
            {
              "name": "price", 
              "selector": "span.related-price", 
              "type": "text"
            }
          ]
        }
      ]
    }
  ]
}

```

Key Takeaways:
  * **Nested vs. List** : 
  * **`type: "nested"`**means a**single** sub-object (like `details`). 
  * **`type: "list"`**means multiple items that are**simple** dictionaries or single text fields. 
  * **`type: "nested_list"`**means repeated**complex** objects (like `products` or `reviews`).
  * **Base Fields** : We can extract **attributes** from the container element via `"baseFields"`. For instance, `"data_cat_id"` might be `data-cat-id="elect123"`. 
  * **Transforms** : We can also define a `transform` if we want to lower/upper case, strip whitespace, or even run a custom function.


### Running the Extraction
```
import json
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
ecommerce_schema = {
  # ... the advanced schema from above ...
}
async def extract_ecommerce_data():
  strategy = JsonCssExtractionStrategy(ecommerce_schema, verbose=True)
  config = CrawlerRunConfig()
  async with AsyncWebCrawler(verbose=True) as crawler:
    result = await crawler.arun(
      url="https://gist.githubusercontent.com/githubusercontent/2d7b8ba3cd8ab6cf3c8da771ddb36878/raw/1ae2f90c6861ce7dd84cc50d3df9920dee5e1fd2/sample_ecommerce.html",
      extraction_strategy=strategy,
      config=config
    )
    if not result.success:
      print("Crawl failed:", result.error_message)
      return
    # Parse the JSON output
    data = json.loads(result.extracted_content)
    print(json.dumps(data, indent=2) if data else "No data found.")
asyncio.run(extract_ecommerce_data())

```

If all goes well, you get a **structured** JSON array with each “category,” containing an array of `products`. Each product includes `details`, `features`, `reviews`, etc. All of that **without** an LLM.
## 4. Why “No LLM” Is Often Better
1. **Zero Hallucination** : Schema-based extraction doesn’t guess text. It either finds it or not. 2. **Guaranteed Structure** : The same schema yields consistent JSON across many pages, so your downstream pipeline can rely on stable keys. 3. **Speed** : LLM-based extraction can be 10–1000x slower for large-scale crawling. 4. **Scalable** : Adding or updating a field is a matter of adjusting the schema, not re-tuning a model.
**When might you consider an LLM?** Possibly if the site is extremely unstructured or you want AI summarization. But always try a schema approach first for repeated or consistent data patterns.
## 5. Base Element Attributes & Additional Fields
It’s easy to **extract attributes** (like `href`, `src`, or `data-xxx`) from your base or nested elements using:
```
{
 "name": "href",
 "type": "attribute",
 "attribute": "href",
 "default": null
}

```

You can define them in **`baseFields`**(extracted from the main container element) or in each field’s sub-lists. This is especially helpful if you need an item’s link or ID stored in the parent`<div>`.
## 6. Putting It All Together: Larger Example
Consider a blog site. We have a schema that extracts the **URL** from each post card (via `baseFields` with an `"attribute": "href"`), plus the title, date, summary, and author:
```
schema = {
 "name": "Blog Posts",
 "baseSelector": "a.blog-post-card",
 "baseFields": [
  {"name": "post_url", "type": "attribute", "attribute": "href"}
 ],
 "fields": [
  {"name": "title", "selector": "h2.post-title", "type": "text", "default": "No Title"},
  {"name": "date", "selector": "time.post-date", "type": "text", "default": ""},
  {"name": "summary", "selector": "p.post-summary", "type": "text", "default": ""},
  {"name": "author", "selector": "span.post-author", "type": "text", "default": ""}
 ]
}

```

Then run with `JsonCssExtractionStrategy(schema)` to get an array of blog post objects, each with `"post_url"`, `"title"`, `"date"`, `"summary"`, `"author"`.
## 7. Tips & Best Practices
1. **Inspect the DOM** in Chrome DevTools or Firefox’s Inspector to find stable selectors. 2. **Start Simple** : Verify you can extract a single field. Then add complexity like nested objects or lists. 3. **Test** your schema on partial HTML or a test page before a big crawl. 4. **Combine with JS Execution** if the site loads content dynamically. You can pass `js_code` or `wait_for` in `CrawlerRunConfig`. 5. **Look at Logs** when `verbose=True`: if your selectors are off or your schema is malformed, it’ll often show warnings. 6. **Use baseFields** if you need attributes from the container element (e.g., `href`, `data-id`), especially for the “parent” item. 7. **Performance** : For large pages, make sure your selectors are as narrow as possible.
## 8. Conclusion
With **JsonCssExtractionStrategy** (or **JsonXPathExtractionStrategy**), you can build powerful, **LLM-free** pipelines that:
  * Scrape any consistent site for structured data. 
  * Support nested objects, repeating lists, or advanced transformations. 
  * Scale to thousands of pages quickly and reliably.


**Next Steps** :
  * Combine your extracted JSON with advanced filtering or summarization in a second pass if needed. 
  * For dynamic pages, combine strategies with `js_code` or infinite scroll hooking to ensure all content is loaded.


**Remember** : For repeated, structured data, you don’t need to pay for or wait on an LLM. A well-crafted schema plus CSS or XPath gets you the data faster, cleaner, and cheaper—**the real power** of Crawl4AI.
**Last Updated** : 2025-01-01
That’s it for **Extracting JSON (No LLM)**! You’ve seen how schema-based approaches (either CSS or XPath) can handle everything from simple lists to deeply nested product catalogs—instantly, with minimal overhead. Enjoy building robust scrapers that produce consistent, structured JSON for your data pipelines!
Site built with [MkDocs](https://docs.crawl4ai.com/extraction/no-llm-strategies/<http:/www.mkdocs.org>) and [Terminal for MkDocs](https://docs.crawl4ai.com/extraction/no-llm-strategies/<https:/github.com/ntno/mkdocs-terminal>). 
##### Search
xClose
Type to start searching


==================================================

