"""Minimal Playwright demo: opens a page and saves a screenshot.

Run with:  python main.py
"""

from playwright.sync_api import sync_playwright


def main() -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://example.com")
        print("Page title:", page.title())
        page.screenshot(path="screenshot.png")
        browser.close()
    print("Done. Screenshot saved to screenshot.png")


if __name__ == "__main__":
    main()
