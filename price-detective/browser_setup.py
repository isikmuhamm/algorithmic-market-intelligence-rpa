"""
Browser Setup Module
Handles Selenium WebDriver initialization and page load utilities.
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


def setup_driver():
    """
    Initializes and returns a headless Chrome WebDriver with optimized settings.
    
    Returns:
        webdriver.Chrome: Configured Chrome WebDriver instance
    """
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-software-rasterizer")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--ignore-ssl-errors')
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_argument("referer=https://www.google.com/")
    chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
    driver = webdriver.Chrome(options=chrome_options)
    return driver


def wait_for_page_load(driver, timeout=5, cloudflare_timeout=20):
    """
    Waits for page to fully load and handles Cloudflare verification screens.
    
    Args:
        driver: Active WebDriver instance
        timeout: Maximum seconds to wait for page load
        cloudflare_timeout: Maximum seconds to wait for Cloudflare bypass
    """
    try:
        # Wait for page to fully load
        WebDriverWait(driver, timeout).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
        
        # Check for Cloudflare verification screen
        if "Checking your browser" in driver.page_source or "Cloudflare" in driver.page_source:
            print("Cloudflare verification screen detected, waiting...")
            WebDriverWait(driver, cloudflare_timeout).until(
                lambda d: "Checking your browser" not in d.page_source and "Cloudflare" not in d.page_source
            )
            print("Cloudflare verification screen bypassed.")
    
    except Exception as e:
        print(f"Page load timeout or Cloudflare verification error: {e}")
