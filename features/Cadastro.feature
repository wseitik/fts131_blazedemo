Feature: Cadastro de um novo usuario
  Scenario: Cadastrar um novo usuario
    Given que acesso o site Blazedemo
    # Parametros fixos
    When realizo o cadastro de um novo usuario
    And clico na opção Home
    And clico na opção Register
    And preencho os dados de cadastro como <Name> <Company> <EmailAddress> <Password> <ConfirmPassword>
         | Name    | Company   | EmailAddress   | Password | ConfirmPassword |
         | 'Maria' | 'empresa x' | 'maria@test.com' | '1234'   |'1234'            |
    And clico no botão Register
    Then valido se o cadastro foi realizado com sucesso