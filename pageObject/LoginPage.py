from selenium.webdriver.common.by import By


class LoginPage:
    username_id = "username"
    password_id = "password"
    submitBtn_id = "submit"
    logoutBtn_xpath = "//*[@id='loop-container']/div/article/div[2]/div/div/div/a"


    def __init__(self,driver):
        self.driver = driver


    def setUsername(self,username):
        self.driver.find_element(By.ID,self.username_id).clear()
        self.driver.find_element(By.ID,self.username_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.ID,self.password_id).clear()
        self.driver.find_element(By.ID,self.password_id).send_keys(password)

    def setIncorrectUsername(self,incorrect_username):
        self.driver.find_element(By.ID,self.username_id).clear()
        self.driver.find_element(By.ID,self.username_id).send_keys(incorrect_username)

    def setIncorrectPassword(self,incorrect_password):
        self.driver.find_element(By.ID,self.password_id).clear()
        self.driver.find_element(By.ID,self.password_id).send_keys(incorrect_password)

    def setSubmitBtn(self):
        self.driver.find_element(By.ID,self.submitBtn_id).click()