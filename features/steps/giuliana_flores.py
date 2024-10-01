from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given(u'que acesso o site da Giuliana Flores')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)    
    context.driver.get('https://www.giulianaflores.com.br/')

@when(u'clico em Perfil e depois em "LOGIN / CADASTRAR"')
def step_impl(context):
    context.driver.find_element(By.ID, "perfil-hidden").click()
    context.driver.find_element(By.ID, "UrlLogin").click()

@then(u'sou direcionado para página de IDENTICAÇÃO')
def step_impl(context):
    assert context.driver.find_element(By.ID, "title-defaut").text == "IDENTIFICAÇÃO"

@when(u'clico em Criar cadastro')
def step_impl(context):
    context.driver.find_element(By.ID, "ContentSite_ibtNewCustomer").click()

@then(u'sou direcionado para página de MINHA CONTA')
def step_impl(context):
    assert context.driver.find_element(By.ID, "title-defaut").text == "MINHA CONTA"

@when(u'preencho os campos do formulário de cadastro {nome}, {cpf}, {email}, {senha}, {cep}, {numero}, {complemento}, {telefone}')
def step_impl(context, nome, cpf, email, senha, cep, numero, complemento, telefone):
    context.driver.find_element(By.LINK_TEXT, "Aceitar").click()
    context.driver.find_element(By.ID, "ContentSite_txtName").send_keys(nome)
    context.driver.find_element(By.ID, "ContentSite_txtCpf").send_keys(cpf)
    context.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys(email)
    context.driver.find_element(By.ID, "ContentSite_txtPasswordNew").send_keys(senha)
    context.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtZip").send_keys(cep)
    context.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtAddressNumber").send_keys(numero)
    context.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtComplement").send_keys(complemento)
    context.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtPhoneCelularNum").send_keys(telefone)
    context.driver.find_element(By.ID, "ContentSite_chkRcvSMS").click()
    context.driver.find_element(By.ID, "ContentSite_chkRcvWhatsApp").click()

@when(u'espero a ação do tester de validar o recaptcha por 5 segundos')
def step_impl(context):
    # Não foi possível clicar no botão devido ao recaptcha
    time.sleep(50)

@when(u'clico em FINALIZAR CADASTRO')
def step_impl(context):
    context.driver.find_element(By.ID, "ContentSite_btnCreateCustomer").click()

@then(u'sou direcionado para página de HOME')
def step_impl(context):
    context.driver.get_current_url == "https://www.giulianaflores.com.br/?newcustomer=1"
    
    context.driver.quit()
    
