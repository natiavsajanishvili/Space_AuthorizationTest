from appium import webdriver


class SetUp:

    def __init__(self):
        self.driver = None

    def run(self):
        desired_caps = {
            "deviceName": "RF8N20R4S0E",
            "platformName": "Android",
            "appPackage": "ge.space.app",
            "appActivity": "com.space.app.app.activity.ui.SPApplicationActivity"
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(10)

    def get_driver(self):
        return self.driver
