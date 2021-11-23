from behave import *


@given('que acesso o link Blazedemo')
def que_acesso_o_link_Blazedemo(context):
    print('Passo 1 - Abriu o site')


@when('realizo o cadastro de um novo usuario')
def cadastro_de_um_novo_usuario(context):
    print(f'Clicar na opção Home')


@When('clico na opção Home')
def clicar_opcao_home(context):
    print('Clicar na opcao Home')


@When('clico na opção Register')
def clicar_opcao_register(context):
    print('Clicar na opcao Register')


@when('preencho os dados de cadastro como {Name} {Company} {EmailAddress} {Password} {ConfirmPassword}')
def preencho_os_dados_de_cadastro(context, Name, Company, EmailAddress, Password, ConfirmPassword):
    print('Campos Populados')


@When('Clico no botão {Register}')
def botao_Register(context, Register):
    print('Botão Register pressionado')


@then('valido se o cadastro foi realizado com sucesso')
def valido_se_cadastro_foi_realizado_com_sucesso(context):
    print('cadastro foi realizado com sucesso')
