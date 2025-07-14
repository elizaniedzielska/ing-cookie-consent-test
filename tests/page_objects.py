from playwright.sync_api import Page

class CookieConsentPage:
    def __init__(self, page: Page) -> None:
        self.page = page

        self.analytics_section = page.locator("div.cookie-policy-type:has(h3#header-2-analytical)") 
        self.customize_button = page.locator('.js-cookie-policy-main-settings-button')
        self.analytics_toggle = self.analytics_section.locator("span.cookie-policy-toggle-slider")
        self.accept_selected_button = page.locator("button.js-cookie-policy-settings-decline-button.cookie-policy-button.is--primary", has_text="Zaakceptuj zaznaczone")
        