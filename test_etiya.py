from selenium import webdriver
from selenium.webdriver.common.by import By
#debugging
#breakpoint => kodu debug modda iken bekleteceğimiz satır
class TestEtiya():
    #setup_method => pytest tarafından tanınan
    # bulunduğunda her test öncesi otomatik çalıştırılan fonk.
    def setup_method(self):
        #her test başlangıcında çalışacak fonksiyon
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
    #teardown_method
    def teardown_method(self):
        #her test bitiminde çalışacak fonksiyon
        self.driver.quit()
    def test_header(self):
        logo = self.driver.find_element(By.CLASS_NAME, 'login_logo')
        assert logo.text == "Swag Labs"
    def test_login_invalid(self):
        loginBtn = self.driver.find_element(By.ID, 'login-button')
        loginBtn.click()
#prefix => ön ek