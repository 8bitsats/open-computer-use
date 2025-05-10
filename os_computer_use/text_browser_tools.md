# Text-Based Browser Tools for Agentic Use

This page documents the addition of robust, text-based browser tools to the agent framework. These tools allow your agent to browse the web, search Google, and extract trending tokens from popular Solana meme token sites—all without relying on GUI automation or a graphical environment.

## Motivation

Traditional browser automation (e.g., Selenium, Helium) often requires a graphical environment (X11, VNC, etc.), which can be slow, fragile, and difficult to set up in headless or cloud environments. By using a text-based browser approach, agents can fetch and parse web content directly, making them faster, more reliable, and portable across Mac, Linux, and cloud setups.

## Included Tools

### 1. `SimpleTextBrowser`
A minimal, robust, text-based browser that fetches and parses web pages using `requests` and markdown conversion. It is the core utility used by all the tools below.

### 2. `GetTrendingPumpFunTool`
Fetches the pump.fun homepage and extracts trending meme token symbols using regex.

### 3. `GetTrendingDexscreenerTool`
Fetches the dexscreener.com/solana page and extracts trending meme token symbols using regex.

### 4. `WebSearchTool`
Performs a Google search and returns the titles of the first few results by scraping the search results page.

## How to Register and Use These Tools

First, ensure you have copied the full `cookies.py` and `mdconvert.py` from the example directory into `os_computer_use/` for robust HTML/text parsing.

Then, register the tools in your agent setup:

```python
from os_computer_use.text_browser_tools import (
    SimpleTextBrowser,
    GetTrendingPumpFunTool,
    GetTrendingDexscreenerTool,
    WebSearchTool,
)

browser = SimpleTextBrowser()
get_trending_pump_fun_tool = GetTrendingPumpFunTool(browser)
get_trending_dexscreener_tool = GetTrendingDexscreenerTool(browser)
web_search_tool = WebSearchTool(browser)

agent = CodeAgent(
    tools=[
        get_trending_pump_fun_tool,
        get_trending_dexscreener_tool,
        web_search_tool,
        # ... other tools ...
    ],
    # ... other params ...
)
```

## Example Usage

You can now prompt your agent with:
- `Use get_trending_pump_fun_text to get trending meme tokens from pump.fun.`
- `Use get_trending_dexscreener_text to get trending meme tokens from dexscreener.com/solana.`
- `Use web_search_text to search Google for 'trending Solana meme tokens'.`

## Setup Notes

- **Dependencies:**
  - `requests` (for HTTP requests)
  - `smolagents` (for the Tool base class)
  - `cookies.py` and `mdconvert.py` (for robust HTML/text parsing; copy from the example directory)
- **Regex Extraction:**
  - The tools use simple regexes to extract `$TOKEN` symbols or result titles. Adjust these as needed for more precise extraction.
- **No GUI Required:**
  - These tools work in any environment, including headless servers and cloud sandboxes.

## Extending

You can easily add more tools using the `SimpleTextBrowser` pattern. For example, to scrape another site, create a new `Tool` subclass, visit the page, and extract the desired information from `browser.page_content`.

---

For questions or improvements, see the source in `os_computer_use/text_browser_tools.py` or the original examples in `smolagents/examples/open_deep_research/scripts/`. 