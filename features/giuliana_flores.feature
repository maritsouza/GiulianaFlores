Feature: Site Giuliana Flores

    Background:
        Given que acesso o site da Giuliana Flores

    Scenario Outline: Fazer cadastro de usuário
        When clico em Perfil e depois em LOGIN / CADASTRAR
        Then sou direcionado para página de IDENTICAÇÃO
        When clico em Criar cadastro
        Then sou direcionado para página de MINHA CONTA
        When preencho os campos do formulário de cadastro <nome>, <cpf>, <email>, <senha>, <cep>, <numero>, <complemento>, <telefone>
        # And espero a ação do tester de validar o recaptcha por 50 segundos
        And clico em FINALIZAR CADASTRO
        # Then sou direcionado para página de HOME de novo usuário

    Examples:
    | nome                            | cpf         | email                                     | senha      | cep      | numero | complemento | telefone    |
    | Teresinha Isabel Analu Monteiro | 81295682842 | teresinha.isabel.monteiro@metraseg.com.br | kk9y57xpBW | 05766-270 |    289 | Casa        | 11986357660 |

    Scenario: Login Positivo
        When clico em Perfil e depois em LOGIN / CADASTRAR
        Then sou direcionado para página de IDENTICAÇÃO
        When preencho os campos de login com email mayaanaribeiro@pozzer.net e senha cM30MTn1nL
        And clico em continuar
        Then sou direcionado para página de HOME

    Scenario: Login Negativo
        When clico em Perfil e depois em LOGIN / CADASTRAR
        Then sou direcionado para página de IDENTICAÇÃO
        When preencho os campos de login com email sueli_almeida@agaxtur.com.br e senha cM30MTn1nL
        And clico em continuar
        Then aparece a mensagem de erro ATENÇÃO - e-mail ou senha inválidos!

    Scenario Outline: Compra a partir do banner da home
        When clico na primeira promoção do banner 
        Then aparece para preencher o cep
        When preencho com o cep 05766270, clico no endereço e em aplicar
        Then sou direcionado para página do OUTUBRO ROSA
        When clico no produto "Dupla de Ilustre Mini Orquídea Phalaenopsis Salmão" do id "32414"
        Then sou direcionado para página de detalhes do produto
        And verifico se o nome do produto é "Dupla de Ilustre Mini Orquídea Phalaenopsis Salmão" e o preço é "R$ R$ 139,90"
        And verifico a quantidade do produto antes de adicionar ao carrinho
        When clico em ADICIONAR AO CARRINHO
        Then verifico se sou direcionado para a interface de selecionar a data e o período de entrega
        When seleciono a data de entrega para 31/10/2024 e o período para Comercial
        And clico em OK
        Then sou direcionado para o Meu Carrinho
        And verifico se é produto "Dupla de Ilustre Mini Orquídea Phalaenopsis Salmão" se o preço é "R$ R$ 139,90"
        And verifico se a quantidade é 1, o valor do frete é "R$ 15,90" e o valor total é "R$ 155,80"
        When clico em continuar
        Then sou direcionado para a página de Entrega 01
        When preencho os campos de entrega com <nome>, <telefone>, <numero>, <tipo_endereco>, <whatsapp>
        And clico em Não quero cartão
        And clico em continuar
        Then sou direcionado para a página de pagamento
        When escolho a opção de pagamento com PIX
        And clico em CONCLUIR COMPRA
        Then sou direcionado para a página de confirmação de compra

        Examples:
        | nome                            | telefone    | numero | tipo_endereco | whatsapp    |
        | Luciana Benedita Renata Lima    | 81983159224 | 864    | Residencial   | 81983159224 |
        



