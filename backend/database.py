
import mysql.connector
from dotenv import load_dotenv
import os

# Carregar variáveis do .env
load_dotenv()

# Configurações da conexão
def conectar():

    conexao = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

    cursor = conexao.cursor()

    return conectar

