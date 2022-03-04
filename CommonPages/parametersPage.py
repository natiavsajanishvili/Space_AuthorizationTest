from appium.webdriver.common.appiumby import AppiumBy


class Parameters:

    # Constructor
    def __init__(self, driver):
        self.driver = driver

        # Locators
        self.security_id = 'ge.space.app:id/profileSecurity'
        self.changePassword_id = 'ge.space.app:id/securityChangePassButton'
        self.logOut_id = 'ge.space.app:id/contractLabel'

        # Methods
    def clickOnSecurity(self):
        self.driver.find_element(AppiumBy.ID, self.security_id).click()

    def clickOnchangePassword(self):
        self.driver.find_element(AppiumBy.ID, self.changePassword_id).click()

    def clickOnLogOut(self):
        self.driver.find_element(AppiumBy.ID, self.logOut_id).click()
