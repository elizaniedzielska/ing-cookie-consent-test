import time
from playwright.sync_api import sync_playwright
from page_objects import CookieConsentPage

def test_accept_analytics_cookies():
    with sync_playwright() as p:
        for browser_type in [p.chromium, p.firefox]:  
            browser = browser_type.launch(headless=True)
            context = browser.new_context()
            page = context.new_page()

            page.goto("https://www.ing.pl", wait_until="domcontentloaded")
            page.wait_for_load_state("networkidle")

            cookie_page = CookieConsentPage(page)
            try:
                cookie_page.customize_button.wait_for(timeout=20000)
            except Exception as e:
                page.screenshot(path=f"screenshot-{browser_type.name}.png")
                raise RuntimeError(f"{browser_type.name}: customize button not found!") from e

            cookie_page.customize_button.click()
            # cookie_page.customize_button.wait_for(timeout=20000)
            # cookie_page.customize_button.click()
            cookie_page.analytics_toggle.click()
            cookie_page.accept_selected_button.click()

        page.reload()
        page.wait_for_timeout(1000)

        cookies = context.cookies()
        for c in cookies:
            print(f"{c['name']}: {c['value']} (domain: {c['domain']})")

        analytics_cookies = [c for c in cookies if any(key in c['name'].lower() for key in ["ga", "analytics", "gid", "amcv", "s_"])]

        assert analytics_cookies, "Nie znaleziono ciasteczek analitycznych po akceptacji"

        browser.close()