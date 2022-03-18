import time
import unittest

from CommonPages.homePage import HomePage
from CommonPages.loginPage import LoginInSpace
from CommonPages.parametersPage import Parameters
from CommonPages.changePassPage import ChangePass
from dotenv import load_dotenv
import os


class LoginTest(unittest.TestCase):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        load_dotenv()

    def test_login_validation(self):
        driver = self.driver

        login = LoginInSpace(driver)
        home = HomePage(driver)
        parameters = Parameters(driver)
        changePass = ChangePass(driver)

        self.driver.implicitly_wait(15)

# click on start button
        login.clickOnStart()

# fill mobile number
        login.fillMobileNumber(os.environ.get("MOBILE_NUMBER"))
        driver.implicitly_wait(10)

# fill passcode
        login.fillPasscode(os.environ.get("CURRENTPASSCODE"))
        driver.implicitly_wait(15)

# click "later" on biometric popup
        home.clickOnBiometricPopUp()
        driver.implicitly_wait(10)

# click no more offer on reliable device popup
        home.clickOnNoMoreOffer()
        driver.implicitly_wait(5)

# click on profile icon
        home.clickOnProfileIcon()
        time.sleep(5)

# click on safety
        parameters.clickOnSecurity()
        driver.implicitly_wait(5)

# click on change password
        parameters.clickOnchangePassword()

# fill current password
        changePass.fillCurrentPassCode(os.environ.get("CURRENTPASSCODE"))
        driver.implicitly_wait(5)

# fill new password
        changePass.fillNewPassCode(os.environ.get("NEWPASSCODE"))
        driver.implicitly_wait(5)

# fill new password again
        changePass.fillNewPassCode(os.environ.get("newPassCode"))
        driver.implicitly_wait(10)

# click on close button
        changePass.clickOnCloseButton()
        time.sleep(10)

# click on close icon
        changePass.clickOnCloseIcon()
        driver.implicitly_wait(10)

# click on profile icon
        home.clickOnProfileIcon()
        time.sleep(5)

# click on logout button
        parameters.clickOnLogOut()
        driver.implicitly_wait(10)

# negative case: fill incorrect passcode
        login.fillPasscodeWrong("123456")
        driver.implicitly_wait(10)

# check error message
        login.checkErrorMessage()
        driver.implicitly_wait(5)

# click on error message button close
        login.clickOnClose()
        driver.implicitly_wait(10)

# login with new pass code
        login.fillCorrectPassCode(os.environ.get("newPassCode"))
        time.sleep(10)

# validate login and log out
        home.clickOnProfileIcon()
        time.sleep(5)
        parameters.clickOnLogOut()
        driver.implicitly_wait(2)
