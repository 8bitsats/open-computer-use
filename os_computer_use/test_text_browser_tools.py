from os_computer_use.text_browser_tools import (
    SimpleTextBrowser,
    GetTrendingPumpFunTool,
    GetTrendingDexscreenerTool,
    WebSearchTool,
)

# Initialize the browser and tools
browser = SimpleTextBrowser()
pump_fun_tool = GetTrendingPumpFunTool(browser)
dexscreener_tool = GetTrendingDexscreenerTool(browser)
web_search_tool = WebSearchTool(browser)

# Test pump.fun trending tokens
print("Pump.fun trending tokens:")
print(pump_fun_tool.forward())
print("\n" + "=" * 40 + "\n")

# Test dexscreener.com/solana trending tokens
print("Dexscreener.com/solana trending tokens:")
print(dexscreener_tool.forward())
print("\n" + "=" * 40 + "\n")

# Test Google search
print("Google search for 'trending Solana meme tokens':")
print(web_search_tool.forward("trending Solana meme tokens"))
