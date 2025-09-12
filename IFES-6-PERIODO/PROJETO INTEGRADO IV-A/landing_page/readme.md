# 📌 Landing Page FAESA  

Este projeto foi desenvolvido como parte da disciplina **Projeto Integrador IV-A** dos cursos de **Análise e Desenvolvimento de Sistemas** e **Sistemas de Informação**.  

A proposta consiste em criar uma **landing page da FAESA** com um **formulário de contato**, onde os dados inseridos pelos usuários são **validados e armazenados em um banco de dados MySQL** utilizando **HTML, CSS e PHP**.  

---

## 🚀 Funcionalidades  

- Página de apresentação da **FAESA**, com imagens e informações institucionais.  
- Formulário de contato com os seguintes campos:  
  - **Nome** (obrigatório)  
  - **E-mail** (obrigatório e validado no formato correto)  
  - **Mensagem** (obrigatória, mínimo de 10 caracteres)  
- Validação de dados no **front-end (HTML)** e no **back-end (PHP)**.  
- Armazenamento das informações no banco de dados **MySQL**.  
- Estilo visual com **CSS** e design responsivo.  

---

## 🛠️ Tecnologias Utilizadas  

- **HTML5** → Estrutura da página  
- **CSS3** → Estilização da página  
- **PHP** → Lógica de validação e integração com banco de dados  
- **MySQL** → Armazenamento das informações do formulário  

---

## 📂 Estrutura do Projeto  

/landing-faesa
│── index.php # Página inicial com formulário
│── processa.php # Script PHP que valida e insere dados no BD
│── style.css # Arquivo de estilização
│── /img # Pasta com imagens utilizadas


---

## 💾 Banco de Dados  

No **phpMyAdmin** ou MySQL, criar um banco e a tabela com os comandos abaixo:  

```sql
CREATE DATABASE landing_faesa;

USE landing_faesa;

CREATE TABLE contatos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL,
    mensagem TEXT NOT NULL,
    data_envio TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

▶️ Como Executar

Instale o XAMPP ou outro servidor PHP/MySQL.

Coloque a pasta do projeto dentro do diretório htdocs (no caso do XAMPP).

Inicie o Apache e o MySQL pelo painel do XAMPP.

Crie o banco de dados conforme instruções acima.

Acesse no navegador:

http://localhost/landing_page/index.php

---
👩‍💻 Author

Raissa Azevedo


