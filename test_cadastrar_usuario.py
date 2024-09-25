from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCadastrarUsuario:
    
    url="https://www.giulianaflores.com.br/"
    
    def setup_method(self, method):
        self.driver = webdriver.Edge()
        self.driver.implicitly_wait(10)
        
        # Foi preciso colocar um tamanho fixo, pois aparecia um pop-up de notificação e não conseguia clicar no perfil
        self.driver.set_window_size(1360, 720)

        
    def teardown_method(self, method):
        self.driver.quit()
        
    def test_cadastrar_usuario(self):        
        self.driver.get(self.url)
        self.driver.find_element(By.ID, "perfil-hidden").click()
        self.driver.find_element(By.ID, "UrlLogin").click()
        assert self.driver.find_element(By.ID, "title-defaut").text == "IDENTIFICAÇÃO"
        self.driver.find_element(By.ID, "ContentSite_ibtNewCustomer").click()
        assert self.driver.find_element(By.ID, "title-defaut").text == "MINHA CONTA"
        
        # O pop-up de cookies ficava atrapalhando o clique nas checkboxes
        self.driver.find_element(By.LINK_TEXT, "Aceitar").click()
        self.driver.find_element(By.ID, "ContentSite_txtName").send_keys("Elza Rayssa Santos")
        self.driver.find_element(By.ID, "ContentSite_txtCpf").send_keys("37330241415")
        self.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys("elzarayssasantos@avoeazul.com.br")
        self.driver.find_element(By.ID, "ContentSite_txtPasswordNew").send_keys("8m6rRHGyiL")
        self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtZip").send_keys("52081700")
        self.driver.find_element(By.ID, "ContentSite_CustomerAddress_btnAddressFind").click()
        self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtAddressNumber").send_keys("139")
        self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtComplement").send_keys("Casa")
        self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtPhoneCelularNum").send_keys("81984788464")
        self.driver.find_element(By.ID, "ContentSite_chkRcvSMS").click()
        self.driver.find_element(By.ID, "ContentSite_chkRcvWhatsApp").click()
        
        # Não foi possível clicar no botão devido ao recaptcha
        # self.driver.find_element(By.XPATH, '//*[@id="recaptcha-anchor"]').click()  
        
        self.driver.find_element(By.ID, "ContentSite_btnCreateCustomer").click()
        