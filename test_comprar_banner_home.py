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
        
        # Logando no site
        self.driver.find_element(By.ID, "perfil-hidden").click()
        self.driver.find_element(By.ID, "UrlLogin").click()
        self.driver.find_element(By.LINK_TEXT, "Aceitar").click()
        assert self.driver.find_element(By.ID, "title-defaut").text == "IDENTIFICAÇÃO"
        self.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys("mayaanaribeiro@pozzer.net")
        self.driver.find_element(By.ID, "ContentSite_txtPassword").send_keys("cM30MTn1nL")
        self.driver.find_element(By.ID, "ContentSite_ibtContinue").click()
        
        # Clicando no banner inicial
        self.driver.find_element(By.ID, "trBanner").click()
        self.driver.find_element(By.ID, "inputSearchAddress").send_keys("54410395")
        self.driver.find_element(By.ID, "listAddressItems").click()
        self.driver.find_element(By.CSS_SELECTOR, ".apply-button").click() 
        
        # Selecionando o primeiro produto
        assert self.driver.find_element(By.CSS_SELECTOR, "ul.ulPrincipal > li:first-child h2.title-item").text == "Delicado Mix de Flores Silvestres"
        assert self.driver.find_element(By.CSS_SELECTOR, "ul.ulPrincipal > li:first-child span.actual-price").text == "R$ 109,90"
        self.driver.find_element(By.CSS_SELECTOR, "ul.ulPrincipal > li:first-child .product-item").click()
        self.driver.find_element(By.ID, "ContentSite_lblProductDsName").text == "Delicado Mix de Flores Silvestres"
        self.driver.find_element(By.ID, "ContentSite_dvListPrice").text == "R$ 109,90"
        self.driver.find_element(By.ID, "ContentSite_txtQtdBy").text == "1"
        self.driver.find_element(By.ID, "ContentSite_divBtBuy").click()
        self.driver.find_element(By.ID, "shippingCalendar").text == "SELECIONE A DATA E O PERÍODO DE ENTREGA"
        self.driver.find_element(By.CSS_SELECTOR, ".seta-calendario-right").click()
        self.driver.find_element(By.LINK_TEXT, "15").click()
        self.driver.find_element(By.CSS_SELECTOR, "[idperiod='100']").click()
        self.driver.find_element(By.ID, "btConfirmShippingData").click()
        
        # Verificando o carrinho
        assert self.driver.find_element(By.CSS_SELECTOR, "#title-defaut > h1").text == "MEU CARRINHO"
        assert self.driver.find_element(By.CSS_SELECTOR, ".prodBasket_nome").text == "Delicado Mix de Flores Silvestres"
        assert self.driver.find_element(By.ID, "ContentSite_Basketcontrol1_rptBasket_rptBasketItems_0_nuQty_0").get_attribute("value") == "1"
        assert self.driver.find_element(By.CSS_SELECTOR, ".precoPor_basket").text == "R$ 109,90"            
        assert self.driver.find_element(By.CSS_SELECTOR, ".fretepago").text == "R$ 15,90"
        assert self.driver.find_element(By.CSS_SELECTOR, ".total-linha-calculado span.valor-total-carrinho").text == "R$ 125,80"
        self.driver.find_element(By.CSS_SELECTOR, ".btn-continuar").click()
        
        # Finalizando a compra
        assert self.driver.find_element(By.CSS_SELECTOR, "#title-defaut > h2").text == "ENTREGA"	
        self.driver.find_element(By.ID, "txtDsDestinationName").send_keys("Maya Ana Ribeiro")
        self.driver.find_element(By.ID, "txtPhone").send_keys("81996125745")
        self.driver.find_element(By.ID, "txtDsZip").send_keys("54410395")
        self.driver.find_element(By.ID, "txtDsNumber").send_keys("139")
        self.driver.find_element(By.ID, "ContentSite_rptDeliveryAddress_rbtFgPersonalAddress_0_0_0").click()
        self.driver.find_element(By.ID, "chkSms").click()
        self.driver.find_element(By.ID, "txtDsSmsNumber").send_keys("81996125745")
        self.driver.find_element(By.ID, "rbWhithoutGiftCard").click()
        self.driver.find_element(By.ID, "btnContinue").click()
        self.driver.find_element(By.ID, "ContentSite_spanPix").click()
        self.driver.find_element(By.ID, "ContentSite_ibtFinalizeOrderWithPix").click()