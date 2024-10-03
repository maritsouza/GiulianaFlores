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

# Criar Cadastro
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

@then(u'sou direcionado para página de HOME de novo usuário')
def step_impl(context):
    assert context.driver.current_url == "https://www.giulianaflores.com.br/?newcustomer=1"
    
    context.driver.quit()
    
# Login Positivo
@when(u'clico em Perfil e depois em LOGIN / CADASTRAR')
def step_impl(context):
    context.driver.find_element(By.ID, "perfil-hidden").click()
    context.driver.find_element(By.ID, "UrlLogin").click()
    
@when(u'preencho os campos de login com email {email} e senha {senha}')
def step_impl(context, email, senha):
    context.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys(email)
    context.driver.find_element(By.ID, "ContentSite_txtPassword").send_keys(senha)

@when(u'clico em continuar')
def step_impl(context):
    context.driver.find_element(By.ID, "ContentSite_ibtContinue").click()
    
@then(u'sou direcionado para página de HOME')
def step_impl(context):
    assert context.driver.current_url == "https://www.giulianaflores.com.br/"
    
    context.driver.quit()
    
#Login Negativo
@then(u'aparece a mensagem de erro {mensagem}')
def step_impl(context, mensagem):
    assert context.driver.find_element(By.ID, "ContentSite_divMessages").text == mensagem
    
    context.driver.quit()
    

# Fluxo de Compra
@then(u'aparece para preencher o cep')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#boxAddress > .opt-popup-title").text == "Para onde deseja enviar?"

@when(u'preencho com o cep {cep}, clico no endereço e em aplicar')
def step_impl(context, cep):
    context.driver.find_element(By.ID, "inputSearchAddress").send_keys(cep)
    context.driver.find_element(By.ID, "listAddressItems").click()
    context.driver.find_element(By.CSS_SELECTOR, ".apply-button").click() 

@when(u'clico na primeira promoção do banner')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "span[tabindex='0']").click()
    context.driver.find_element(By.ID, "trBanner").click()

@then(u'sou direcionado para página do {promocao_banner}')
def step_impl(context, promocao_banner):
    assert context.driver.find_element(By.ID, "title-defaut").text == promocao_banner

@when(u'clico no produto "{nome_produto}" do id "{id_produto}"')
def step_impl(context, nome_produto, id_produto):
    assert context.driver.find_element(By.CSS_SELECTOR, f"a[data-idproduct='{id_produto}'] h2.title-item").text == nome_produto
    context.driver.find_element(By.CSS_SELECTOR, f"a[data-idproduct='{id_produto}'] .image-content").click()
    
@then(u'sou direcionado para página de detalhes do produto')
def step_impl(context):
    


@then(u'verifico se o nome do produto é "Buquê de 42 Rosas Cor de Rosa" e o preço é "R$ 359,90"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then verifico se o nome do produto é "Buquê de 42 Rosas Cor de Rosa" e o preço é "R$ 359,90"')


@then(u'verifico a quantidade do produto antes de adicionar ao carrinho')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then verifico a quantidade do produto antes de adicionar ao carrinho')


@when(u'clico em ADICIONAR AO CARRINHO')
def step_impl(context):
    raise NotImplementedError(u'STEP: When clico em ADICIONAR AO CARRINHO')


@then(u'verifico se sou direcionado para a interface de selecionar a data e o período de entrega')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then verifico se sou direcionado para a interface de selecionar a data e o período de entrega')


@when(u'seleciono a data de entrega para 31/10/2024 e o período para Comercial')
def step_impl(context):
    raise NotImplementedError(u'STEP: When seleciono a data de entrega para 31/10/2024 e o período para Comercial')


@when(u'clico em OK')
def step_impl(context):
    raise NotImplementedError(u'STEP: When clico em OK')


@then(u'sou direcionado para o Meu Carrinho')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then sou direcionado para o Meu Carrinho')


@then(u'verifico se é produto "Buquê de 42 Rosas Cor de Rosa" se o preço é "R$ 359,90"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then verifico se é produto "Buquê de 42 Rosas Cor de Rosa" se o preço é "R$ 359,90"')


@then(u'verifico se a quantidade é 1, o valor do frete é "R$ 15,90" e o valor total é "R$ 375,80"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then verifico se a quantidade é 1, o valor do frete é "R$ 15,90" e o valor total é "R$ 375,80"')


@then(u'sou direcionado para a página de Entrega 01')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then sou direcionado para a página de Entrega 01')


@when(u'preencho os campos de entrega com Luciana Benedita Renata Lima, 81983159224, 864, Residencial, 81983159224')
def step_impl(context):
    raise NotImplementedError(u'STEP: When preencho os campos de entrega com Luciana Benedita Renata Lima, 81983159224, 864, Residencial, 81983159224')


@when(u'clico em Não quero cartão')
def step_impl(context):
    raise NotImplementedError(u'STEP: When clico em Não quero cartão')


@then(u'sou direcionado para a página de pagamento')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then sou direcionado para a página de pagamento')


@when(u'escolho a opção de pagamento com PIX')
def step_impl(context):
    raise NotImplementedError(u'STEP: When escolho a opção de pagamento com PIX')


@when(u'clico em CONCLUIR COMPRA')
def step_impl(context):
    raise NotImplementedError(u'STEP: When clico em CONCLUIR COMPRA')


@then(u'sou direcionado para a página de confirmação de compra')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then sou direcionado para a página de confirmação de compra')