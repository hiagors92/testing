from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def enter_credentials(self, username, password):
        username_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "user-name"))
        )
        username_field.send_keys(username)

        password_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "password"))
        )
        password_field.send_keys(password)

    def click_button(self):
        login_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'login-button'))
        )
        login_button.click()

    def home_page_is_displayed(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'inventory_container'))
        )
        return self.driver.find_element(By.ID, 'inventory_container').is_displayed()

    def error_message_is_displayed(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'error-message-container'))
        )
        return self.driver.find_element(By.CLASS_NAME, 'error-message-container').is_displayed()

    def enter_password(self, password):
        self.driver.find_element(By.ID, "password").send_keys(password)

    def password_asterisks(self):
        password = self.driver.find_element(By.ID, "password").get_attribute("value")
        return password

    def menu(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'bm-burger-button'))
        )
        self.driver.find_element(By.ID, 'react-burger-menu-btn').click()

    def logout(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'logout_sidebar_link'))
        )
        self.driver.find_element(By.ID, 'logout_sidebar_link').click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'login_button_container'))
        )
        return self.driver.find_element(By.ID, 'login_button_container').is_displayed()

    def input_empty(self):
        self.driver.find_element(By.ID, "user-name").send_keys("")
        self.driver.find_element(By.ID, "password").send_keys("")



