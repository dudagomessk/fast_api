import os
from pathlib import Path

import mysql.connector
from dotenv import load_dotenv

load_dotenv(Path(__file__).with_name(".env"))

# Conecta no servidor (ainda sem escolher o banco)
conexao = mysql.connector.connect(
    host=os.environ["DB_HOST"],
    port=int(os.environ["DB_PORT"]),
    user=os.environ["DB_USER"],
    password=os.environ["DB_PASSWORD"],
)
cursor = conexao.cursor()

nome_banco = os.environ["DB_NAME"]
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {nome_banco} CHARACTER SET utf8mb4")
cursor.execute(f"USE {nome_banco}")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS tutores (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        telefone VARCHAR(20) NOT NULL
    ) ENGINE=InnoDB
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS pets (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        especie VARCHAR(50) NOT NULL,
        tutor_id INT NOT NULL,
        CONSTRAINT fk_pets_tutor FOREIGN KEY (tutor_id) REFERENCES tutores (id)
    ) ENGINE=InnoDB
""")

# Só insere os dados de exemplo se a tabela estiver vazia
cursor.execute("SELECT COUNT(*) FROM tutores")
if cursor.fetchone()[0] == 0:
    cursor.execute(
        "INSERT INTO tutores (nome, telefone) "
        "VALUES ('Ana', '47 99999-1111'), ('Carlos', '47 99999-2222')"
    )
    cursor.execute(
        "INSERT INTO pets (nome, especie, tutor_id) "
        "VALUES ('Rex', 'Cachorro', 1), ('Mel', 'Gato', 1), ('Thor', 'Cachorro', 2)"
    )

conexao.commit()
cursor.close()
conexao.close()

print("Banco criado com sucesso!")