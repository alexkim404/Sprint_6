from selenium.webdriver.common.by import By


class HeaderFooterLocators:
    # принять куки
    COOKIE_BUTTON = (By.XPATH, '//button[@id="rcc-confirm-button" and '
                               'contains(@class, "App_CookieButton")]')
    # лого Яндекс
    YANDEX_LOGO = (
        By.XPATH,
        "//*[contains(@class, 'Header_LogoYandex')]")
    # лого Самокат
    SAMOKAT_LOGO = (
        By.XPATH,
        "//*[contains(@class, 'Header_LogoScooter')]")
    # лого Дзен
    DZEN_LOGO = (By.XPATH, '//a[@aria-label="Логотип Бренда"]')
