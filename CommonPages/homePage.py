from appium.webdriver.common.appiumby import AppiumBy


class HomePage:

    # Constructor
    def __init__(self, driver):
        self.driver = driver

        # Locators
        self.biometricPopUp_id = 'ge.space.app:id/alertNegativeButton'
        self.noMoreOffer_xpath = '(//android.widget.TextView)[4]'
        self.profileIcon_id = 'ge.space.app:id/homeProfileBtn'

        # Methods
    def clickOnBiometricPopUp(self):
        self.driver.find_element(AppiumBy.ID, self.biometricPopUp_id).click()

    def clickOnNoMoreOffer(self):
        self.driver.find_element(AppiumBy.XPATH, self.noMoreOffer_xpath).click()

    def clickOnProfileIcon(self):
        self.driver.find_element(AppiumBy.ID, self.profileIcon_id).click()
