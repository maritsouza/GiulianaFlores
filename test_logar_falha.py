from selenium import webdriver
from selenium.webdriver.common.by import By

class TestLogarFalha:
    
    url="https://www.giulianaflores.com.br/"
    
    def setup_method(self, method):
        self.driver = webdriver.Edge()
        self.driver.implicitly_wait(10)
        self.driver.set_window_size(1360, 720)
        
    def teardown_method(self, method):
        self.driver.quit()
        
    def test_logar_falha(self):
        self.driver.get(self.url)
        self.driver.find_element(By.ID, "perfil-hidden").click()
        self.driver.find_element(By.ID, "UrlLogin").click()
        assert self.driver.find_element(By.ID, "title-defaut").text == "IDENTIFICAÇÃO"
        self.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys("mayaanaribeiro@pozzer.ne")
        self.driver.find_element(By.ID, "ContentSite_txtPassword").send_keys("123456")
        self.driver.find_element(By.ID, "ContentSite_ibtContinue").click()
        self.driver.find_element(By.ID, "ContentSite_divMessages").text == "ATENÇÃO - e-mail ou senha inválidos!"
        