-- Banco de dados: Tutores e Pets
-- Executar no MySQL Workbench (botao do raio)

CREATE DATABASE IF NOT EXISTS petshop CHARACTER SET utf8mb4;
USE petshop;

CREATE TABLE IF NOT EXISTS tutores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    telefone VARCHAR(20) NOT NULL
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS pets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    especie VARCHAR(50) NOT NULL,
    tutor_id INT NOT NULL,
    CONSTRAINT fk_pets_tutor FOREIGN KEY (tutor_id) REFERENCES tutores (id)
) ENGINE=InnoDB;

INSERT INTO tutores (nome, telefone)
VALUES ('Ana', '47 99999-1111'), ('Carlos', '47 99999-2222');

INSERT INTO pets (nome, especie, tutor_id)
VALUES ('Rex', 'Cachorro', 1), ('Mel', 'Gato', 1), ('Thor', 'Cachorro', 2);

SELECT * FROM tutores;
SELECT * FROM pets;