Feature: Site Giuliana Flores

    Scenario Outline: Fazer cadastro de usuário
        Given que acesso o site da Giuliana Flores
        When clico em Perfil e depois em "LOGIN / CADASTRAR"
        Then sou direcionado para página de IDENTICAÇÃO
        When clico em Criar cadastro
        Then sou direcionado para página de MINHA CONTA
        When preencho os campos do formulário de cadastro <nome>, <cpf>, <email>, <senha>, <cep>, <numero>, <complemento>, <telefone>
        And espero a ação do tester de validar o recaptcha por 5 segundos
        And clico em FINALIZAR CADASTRO
        Then sou direcionado para página de HOME

    Examples:
    | nome                            | cpf         | email                                     | senha      | cep      | numero | complemento | telefone    |
    | Teresinha Isabel Analu Monteiro | 81295682842 | teresinha.isabel.monteiro@metraseg.com.br | kk9y57xpBW | 05766-270 |    289 | Casa        | 11986357660 |
