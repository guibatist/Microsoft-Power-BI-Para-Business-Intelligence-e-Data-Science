import pandas as pd
import sqlite3

conn = sqlite3.connect('db_dsa_cap15.db')

# Consulta SQL para selecionar todos os dados de uma tabela
query = "SELECT * FROM TB_DSA_CLIENTES"

# Lendo os dados do banco de dados e armazenando em um DataFrame
df = pd.read_sql_query(query, conn)

# Imprimindo as primeiras linhas do DataFrame
print(df.head())
