from playwright.sync_api import sync_playwright
from page_objects import CookieConsentPage

def test_accept_analytics_cookies():
    with sync_playwright() as p:
        for browser_type in [p.chromium, p.firefox, p.webkit]:  
            browser = browser_type.launch(headless=True)
            context = browser.new_context()
            page = context.new_page()

            page.goto("https://www.ing.pl")

            cookie_page = CookieConsentPage(page)
            page.wait_for_selector(".js-cookie-policy-main-settings-button", timeout=10000)
            cookie_page.customize_button.click()
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