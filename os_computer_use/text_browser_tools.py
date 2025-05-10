# Text-based browser and tools for agentic use, adapted from smolagents/examples/open_deep_research/scripts/text_web_browser.py
# Dependencies: cookies.py, mdconvert.py (copy from the same example directory)

import re
from smolagents import Tool

# Import or copy these dependencies into this directory:
# from .cookies import COOKIES
# from .mdconvert import FileConversionException, MarkdownConverter, UnsupportedFormatException

# Placeholder for COOKIES, MarkdownConverter, etc. (copy the full code for production use)
COOKIES = {}


class MarkdownConverter:
    def convert_response(self, response):
        return type("obj", (object,), {"title": "", "text_content": response.text})()


class SimpleTextBrowser:
    def __init__(self, request_kwargs=None):
        self.request_kwargs = request_kwargs or {}
        self.request_kwargs["cookies"] = COOKIES
        self._mdconvert = MarkdownConverter()
        self._page_content = ""
        self.page_title = None
        self.history = []

    @property
    def page_content(self):
        return self._page_content

    def visit_page(self, url):
        import requests

        response = requests.get(url, **self.request_kwargs)
        response.raise_for_status()
        res = self._mdconvert.convert_response(response)
        self.page_title = res.title
        self._page_content = res.text_content
        self.history.append((url,))
        return self._page_content


class GetTrendingPumpFunTool(Tool):
    name = "get_trending_pump_fun_text"
    description = "Get trending meme tokens from pump.fun using text-based browser."
    inputs = {}
    output_type = "string"

    def __init__(self, browser=None):
        super().__init__()
        self.browser = browser or SimpleTextBrowser()

    def forward(self):
        self.browser.visit_page("https://pump.fun/")
        page_content = self.browser.page_content
        # Example: find $TOKEN symbols (adjust regex as needed)
        tokens = re.findall(r"\$[A-Za-z0-9_]+", page_content)
        return "\n".join(tokens) if tokens else "No trending tokens found."


class GetTrendingDexscreenerTool(Tool):
    name = "get_trending_dexscreener_text"
    description = (
        "Get trending meme tokens from dexscreener.com/solana using text-based browser."
    )
    inputs = {}
    output_type = "string"

    def __init__(self, browser=None):
        super().__init__()
        self.browser = browser or SimpleTextBrowser()

    def forward(self):
        self.browser.visit_page("https://dexscreener.com/solana")
        page_content = self.browser.page_content
        # Example: find $TOKEN symbols (adjust regex as needed)
        tokens = re.findall(r"\$[A-Za-z0-9_]+", page_content)
        return "\n".join(tokens) if tokens else "No trending tokens found."


class WebSearchTool(Tool):
    name = "web_search_text"
    description = "Perform a Google search and return the titles of the first few results using text-based browser."
    inputs = {"query": {"type": "string", "description": "The search query."}}
    output_type = "string"

    def __init__(self, browser=None):
        super().__init__()
        self.browser = browser or SimpleTextBrowser()

    def forward(self, query):
        import urllib.parse

        search_url = f"https://www.google.com/search?q={urllib.parse.quote(query)}"
        self.browser.visit_page(search_url)
        page_content = self.browser.page_content
        # Extract result titles (very basic, adjust as needed)
        titles = re.findall(r"\n([A-Za-z0-9 ,.!?\-]+) - [^\n]+\n", page_content)
        return "\n".join(titles[:5]) if titles else "No results found."


# Example registration in your agent setup:
# browser = SimpleTextBrowser()
# get_trending_pump_fun_tool = GetTrendingPumpFunTool(browser)
# agent = CodeAgent(tools=[..., get_trending_pump_fun_tool, ...], ...)
