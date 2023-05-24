import psycopg2 as db
from datetime import datetime, date
from tkinter import *

# Parâmetros de conexão com o banco de dados
db_host = "localhost"
db_port = "5432"
db_name = "escola_monte_verde"
db_user = "postgres"
db_password = "webcheats"

# Criar uma conexão com o banco de dados
conn = db.connect(
    host=db_host,
    port=db_port,
    dbname=db_name,
    user=db_user,
    password=db_password)

# Solicitando cadastro de matrícula
cod_turma = int(input('Digite o código da turma'))
dt_inicio = date.today()

# Inserindo os dados na tabela matricula
insert_matricula_query = """
INSERT INTO matricula (cod_turma, dt_inicio)
VALUES (%s, %s)
RETURNING cod_matr
"""

with conn.cursor() as cursor:
    cursor.execute(insert_matricula_query, (cod_turma, dt_inicio))
    cod_matr = cursor.fetchone()[0]  # Obter o valor gerado para cod_matr

# Solicitando cadastro do aluno
nome_aluno = input('Digite o nome do aluno: ')
sobren_aluno = input('Digite o sobrenome do aluno: ')
dt_nasc_aluno = input('Digite a data de nascimento do aluno: ')
data = datetime.strptime(dt_nasc_aluno, '%d-%m-%Y').date()
cpf_aluno = int(input('Digite o cpf do aluno: '))
cod_resp = int(input('Digite o código do responsável: '))

# Inserindo os dados na tabela aluno
insert_aluno_query = """
INSERT INTO aluno (cod_matr, cod_turma, nome_aluno, sobren_aluno, dt_nasc_aluno, cpf_aluno, cod_resp)
VALUES (%s, %s, %s, %s, %s, %s, %s)
"""

with conn.cursor() as cursor:
    cursor.execute(insert_aluno_query, (cod_matr, cod_turma, nome_aluno, sobren_aluno, data, cpf_aluno, cod_resp))
    conn.commit()

