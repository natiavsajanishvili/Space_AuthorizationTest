from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains


class LoginInSpace:

    # Constructor
    def __init__(self, driver):
        self.driver = driver

        # Locators
        self.startButton_id = 'demoStartButton'
        self.mobileNumberInput_id = 'ge.space.app:id/editTextWithTitleHint'
        self.passcodeInput_id = 'ge.space.app:id/passwordBaseFragmentPin'
        self.wrongPasscodeInput_id = 'ge.space.app:id/loginPinEntryEditText'
        self.errorMessage_id = 'ge.space.app:id/alertMessage'
        self.correctPassCode_id = 'ge.space.app:id/loginPinEntryEditText'
        self.errorMessagePopUpClose_id = 'ge.space.app:id/alertPositiveText'

        # Methods

    def clickOnStart(self):
        self.driver.find_element(AppiumBy.ID, self.startButton_id).click()

    def fillMobileNumber(self, mobileNumber):
        self.driver.find_element(AppiumBy.ID, self.mobileNumberInput_id).clear()
        self.driver.find_element(AppiumBy.ID, self.mobileNumberInput_id).click()

        action = ActionChains(self.driver)
        action.send_keys(mobileNumber).perform()

    def fillPasscode(self, passcode):
        self.driver.find_element(AppiumBy.ID, self.passcodeInput_id).send_keys(passcode)

    def fillPasscodeWrong(self, passcode):
        self.driver.find_element(AppiumBy.ID, self.wrongPasscodeInput_id).send_keys(passcode)

    def checkErrorMessage(self):
        errorMessage = self.driver.find_element(AppiumBy.ID, self.errorMessage_id).get_attribute('text')
        assert (errorMessage == 'შეყვანილი მონაცემები არასწორია, კიდევ სცადე')

    def fillCorrectPassCode(self, newPassCode):
        self.driver.find_element(AppiumBy.ID, self.correctPassCode_id).send_keys(newPassCode)

    def clickOnClose(self):
        self.driver.find_element(AppiumBy.ID, self.errorMessagePopUpClose_id).click()
