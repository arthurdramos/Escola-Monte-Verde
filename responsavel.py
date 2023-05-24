import psycopg2 as db
from datetime import datetime
from tkinter import *


# Parâmetros de conexão com o banco de dados
db_host = "localhost"
db_port = "5432"
db_name = "escola_monte_verde"
db_user = "postgres"
db_password = "webcheats"

# Criando uma conexão com o banco de dados
conn = db.connect(
    host=db_host,
    port=db_port,
    dbname=db_name,
    user=db_user,
    password=db_password
)

# Solicitando cadastro do responsável
nome_resp = input('Digite o nome do responsável: ')
sobren_resp = input('Digite o sobrenome do responsável: ')
tipo_resp = input('Digite o tipo do responsável (PAIS, AVÓS ou OUTROS): ')
dt_nasc_resp = input('Digite a data no formato DD-MM-YYYY: ')
data = datetime.strptime(dt_nasc_resp, '%d-%m-%Y').date()
cpf_resp = int(input('Digite o CPF do responsável: '))
fone_fixo_resp = int(input('Digite o telefone fixo do responsável: '))
cel_resp = int(input('Digite o telefone celular do responsável: '))
logradouro_resp = input('Digite o logradouro do endereço do responsável: ')
num_resp = int(input('Digite o número da residência do responsável: '))
complem_resp = input('Digite o complemento do responsável: ')
bairro_resp = input('Digite o bairro do responsável: ')
cep_resp = int(input('Digite o CEP do responsável: '))
cidade_resp = input('Digite a cidade do responsável: ')
uf_resp = input('Digite o estado em que reside o responsável: ')
email_resp = input('Digite o e-mail do responsável: ')

# Inserindo os dados no banco de dados
insert_query = """
INSERT INTO responsavel (nome_resp, sobren_resp, tipo_resp, dt_nasc_resp, cpf_resp, fone_fixo_resp, cel_resp, logradouro_resp,
                        num_resp, complem_resp, bairro_resp, cep_resp, cidade_resp, uf_resp, email_resp)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

with conn.cursor() as cursor:
    cursor.execute(insert_query, (nome_resp, sobren_resp, tipo_resp, data, cpf_resp, fone_fixo_resp, cel_resp, logradouro_resp,
                                  num_resp, complem_resp, bairro_resp, cep_resp, cidade_resp, uf_resp, email_resp))
    conn.commit()

