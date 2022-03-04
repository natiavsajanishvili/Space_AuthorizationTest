from Common.setup import SetUp
from Tests.loginTest import LoginTest


set_up = SetUp()
set_up.run()
driver = set_up.get_driver()
login_test = LoginTest(driver)
login_test.test_login_validation()
