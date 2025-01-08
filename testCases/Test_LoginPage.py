import time

from selenium.webdriver.common.by import By

from pageObject.LoginPage import LoginPage


class Test_LoginPage:
    username = "student"
    password = "Password123"
    incorrect_username = "incorrectUser"
    incorrect_password = "incorrectPassword"
    practiceURL = "https://practicetestautomation.com/practice-test-login/"

    def test_CorrectLogin(self,setUp):
        self.driver = setUp
        self.driver.get(self.practiceURL)
        self.driver.maximize_window()
        self.obj_LoginPage = LoginPage(self.driver)
        self.obj_LoginPage.setUsername(self.username)
        self.obj_LoginPage.setPassword(self.password)
        self.obj_LoginPage.setSubmitBtn()
        currentURL = self.driver.current_url
        if "successfully" in currentURL:
            print("Present")
        else:
            print("Not present")

        pageSource = self.driver.page_source
        if "Congratulations" in pageSource:
            assert True
        else:
            assert False

        logout = self.driver.find_element(By.XPATH,self.obj_LoginPage.logoutBtn_xpath)
        if logout.is_displayed():
            print("Displayed")
        else:
            print("Not displayed")

        time.sleep(4)
        self.driver.quit()


    def test_IncorrectUsername(self,setUp):
        self.driver = setUp
        self.driver.get(self.practiceURL)
        self.obj_LoginPage = LoginPage(self.driver)
        self.driver.maximize_window()
        self.obj_LoginPage.setUsername(self.incorrect_username)
        self.obj_LoginPage.setPassword(self.password)
        self.obj_LoginPage.setSubmitBtn()
        errorMsg = self.driver.find_element(By.ID,"error")
        if errorMsg.is_displayed():
            print("Error msg is displayed")
        else:
            print("Error msg is not displayed")

        if errorMsg.text == "Your username is invalid!":
            print("This is error msg")
        self.driver.quit()

    def test_IncorrectPassword(self,setUp):
        self.driver = setUp
        self.driver.get(self.practiceURL)
        self.obj_LoginPage = LoginPage(self.driver)
        self.driver.maximize_window()
        self.obj_LoginPage.setUsername(self.username)
        self.obj_LoginPage.setIncorrectPassword(self.incorrect_password)
        self.obj_LoginPage.setSubmitBtn()
        errorMsg = self.driver.find_element(By.ID,"error")
        if errorMsg.is_displayed():
            print("Error msg is displayed")
        else:
            print("Error msg is not displayed")

        if errorMsg.text == "Your password is invalid!":
            print("This is error msg")
        self.driver.quit()
