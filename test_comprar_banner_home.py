from selenium import webdriver
from selenium.webdriver.common.by import By

class TestComprarBannerHome:
    
    url="https://www.giulianaflores.com.br/"
    
    def setup_method(self, method):
        self.driver = webdriver.Edge()
        self.driver.implicitly_wait(10)
        self.driver.set_window_size(1360, 720)
        
    def teardown_method(self, method):
        self.driver.quit()
        
    def test_comprar_banner_home(self):
        self.driver.get(self.url)
        self.driver.find_element(By.ID, "perfil-hidden").click()
        self.driver.find_element(By.ID, "UrlLogin").click()
        assert self.driver.find_element(By.ID, "title-defaut").text == "IDENTIFICAÇÃO"
        self.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys("mayaanaribeiro@pozzer.net")
        self.driver.find_element(By.ID, "ContentSite_txtPassword").send_keys("cM30MTn1nL")
        self.driver.find_element(By.ID, "ContentSite_ibtContinue").click()
        self.driver.find_element(By.ID, "trBanner").click()
        self.driver.find_element(By.ID, "inputSearchAddress").send_keys("54410395")
        self.driver.find_element(By.ID, "listAddressItems").click()
        self.driver.find_element(By.CSS_SELECTOR, ".apply-button").click() 
        assert self.driver.find_element(By.CSS_SELECTOR, "ul.ulPrincipal > li:first-child h2.title-item").text == "Delicado Mix de Flores Silvestres"
        assert self.driver.find_element(By.CSS_SELECTOR, "ul.ulPrincipal > li:first-child span.actual-price").text == "R$ 109,90"
        self.driver.find_element(By.CSS_SELECTOR, "ul.ulPrincipal > li:first-child .product-item").click()
        self.driver.find_element(By.ID, "ContentSite_lblProductDsName").text == "Delicado Mix de Flores Silvestres"
        self.driver.find_element(By.ID, "ContentSite_dvListPrice").text == "R$ 109,90"
        self.driver.find_element(By.ID, "ContentSite_txtQtdBy").text == "1"
        self.driver.find_element(By.ID, "ContentSite_divBtBuy").click()
        self.driver.find_element(By.ID, "shippingCalendar").text == "SELECIONE A DATA E O PERÍODO DE ENTREGA"
        self.driver.find_element(By.ID, "").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "#title-defaut > h1").text == "MEU CARRINHO"
        assert self.driver.find_element(By.CSS_SELECTOR, ".prodBasket_nome > a") == "Delicado Mix de Flores Silvestres"
        assert self.driver.find_element(By.CSS_SELECTOR, ".input_qtd").text == "1"
        assert self.driver.find_element(By.CSS_SELECTOR, ".precoPor_basket").text == "R$ 109,90"            
        assert self.driver.find_element(By.ID, "valorfrete").text == "R$ 15,90"
        assert self.driver.find_element(By.ID, "ContentSite_Basketcontrol1_rptBasket_totalTitle_0").text == "R$ 125,80"
        self.driver.find_element(By.ID, "ContentSite_Basketcontrol1_rptBasket_imbFinalize_0").click()