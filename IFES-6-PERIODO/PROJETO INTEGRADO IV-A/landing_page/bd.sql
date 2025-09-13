// Script para criar o banco de dados e a tabela de contatos
CREATE DATABASE landing_faesa;
USE landing_faesa;

CREATE TABLE contatos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL,
    telefone VARCHAR(20),
    curso_interesse VARCHAR(100),
    nota_enem DECIMAL(5,2), -- Nota do ENEM com duas casas decimais
    mensagem TEXT,
    data_envio TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
