import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='2082639a',
    appPackage='org.telegram.messenger',
    appActivity='org.telegram.ui.LaunchActivity',
    language='en',
    locale='US',
    noReset='true'
)

appium_server_url = 'http://localhost:4723'

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()
#   send /start command for welcoming, and sending a text message for test (the bot should welcome us and give an error message for a text message)
    def test1(self) -> None:
        element_menu = self.driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="Bot menu"]')
        element_menu.click()
        element_start = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="start"]')
        element_start.click()
        element_message = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Message"]')
        element_message.send_keys('This is a text')
        element_send = self.driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="Send"]')
        element_send.click()
#   open device local gallery
    def test2(self) -> None:
        element_attach = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ImageView[@content-desc="Attach media"]')
        element_attach.click()
#   choosing file that contains *.jpg but actually is a txt file for test (the bot should give us an error for incorrect file)
    def test3(self) -> None:
        element_file = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@text="File"]/android.widget.ImageView')
        element_file.click()
        element_doc = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="image.jpg.txt"]')
        element_doc.click()
        element_sendc = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@text="Send 1 file"]/android.view.View')
        element_sendc.click()
#   open device local gallery
    def test4(self) -> None:
        element_attachm = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ImageView[@content-desc="Attach media"]')
        element_attachm.click()
#   choose an image that is *.jpg for test (the bot should give us a hash)
    def test5(self) -> None:
        element_img = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@text="Photo. Sep 12 2024, 1:21 PM"]/android.widget.FrameLayout[1]/android.view.View')
        element_img.click()
#   send the chosen image
    def test6(self) -> None:
        element_sendm = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ImageView[@content-desc="Send"]')
        element_sendm.click()

if __name__ == '__main__':
    unittest.main()