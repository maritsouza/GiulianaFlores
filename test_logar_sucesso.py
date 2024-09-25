from selenium import webdriver
from selenium.webdriver.common.by import By

class TestLogarSucesso:
    
    url="https://www.giulianaflores.com.br/"
    
    def setup_method(self, method):
        self.driver = webdriver.Edge()
        self.driver.implicitly_wait(10)
        
        # Foi preciso colocar um tamanho fixo, pois aparecia um pop-up de notificação e não conseguia clicar no perfil
        self.driver.set_window_size(1360, 720)
        
    def teardown_method(self, method):
        self.driver.quit()
        
    def test_logar_sucesso(self):
        self.driver.get(self.url)
        self.driver.find_element(By.ID, "perfil-hidden").click()
        self.driver.find_element(By.ID, "UrlLogin").click()
        assert self.driver.find_element(By.ID, "title-defaut").text == "IDENTIFICAÇÃO"
        self.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys("mayaanaribeiro@pozzer.net")
        self.driver.find_element(By.ID, "ContentSite_txtPassword").send_keys("cM30MTn1nL")
        self.driver.find_element(By.ID, "ContentSite_ibtContinue").click()
        self.driver.find_element(By.ID, "perfil-hidden").click()
        
        # Fiz desta maneira para comparar se no texto tem o nome "Maya", pois o site muda a frase pelo horário
        assert "Maya" in self.driver.find_element(By.ID, "lblWelcome").text
        
        