from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains


class ChangePass:

    # Constructor
    def __init__(self, driver):
        self.driver = driver

        # Locators
        self.currentPassword_id = 'ge.space.app:id/confirmPasswordFragmentPin'
        self.newPassCode_id = 'ge.space.app:id/passwordBaseFragmentPin'
        self.closeButton_id = 'ge.space.app:id/buttonLabel'
        self.closeIcon_id = 'ge.space.app:id/homeProfileBtn'

        # Methods
    def fillCurrentPassCode(self, passcode):
        self.driver.find_element(AppiumBy.ID, self.currentPassword_id).click()

        action = ActionChains(self.driver)
        action.send_keys(passcode).perform()

    def fillNewPassCode(self, newPassCode):
        self.driver.find_element(AppiumBy.ID, self.newPassCode_id).click()

        action = ActionChains(self.driver)
        action.send_keys(newPassCode).perform()

    def clickOnCloseButton(self):
        self.driver.find_element(AppiumBy.ID, self.closeButton_id).click()

    def clickOnCloseIcon(self):
        self.driver.find_element(AppiumBy.ID, self.closeIcon_id).click()


