<?php
?>
<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <title>FAESA - Landing Page</title>
    <link rel="stylesheet" href="style.css">
</head>

<body>
    <header>
        <img src="imgs/logo.png" alt="Logo FAESA" class="logo">
        <h1>Bem-vindo à FAESA!</h1>
        <p>Uma das melhores instituições de ensino do Brasil. <br>Construa seu futuro com a gente!</p>
    </header>

    <main>
        <section class="sobre">
            <h2>Por que escolher a FAESA?</h2>
            <p>
                A FAESA é reconhecida pela qualidade de ensino, infraestrutura moderna e
                professores qualificados. Oferecemos cursos que preparam você para o mercado de trabalho.
            </p>

            <div class="carousel">
                <div class="carousel-track">
                    <img src="imgs/campus1.png" alt="Campus FAESA 1">
                    <img src="imgs/campus2.jpg" alt="Campus FAESA 2">
                    <img src="imgs/campus3.jpg" alt="Campus FAESA 3">
                    <img src="imgs/campus4.jpg" alt="Campus FAESA 4">
                    <img src="imgs/campus5.png" alt="Campus FAESA 5">
                </div>
            </div>
        </section>

        <section class="cursos">
            <h2>Nossos Cursos</h2>
            <p>Escolha a área que combina com você e construa o seu futuro na FAESA.</p>

            <div class="cursos-container">
                <div class="curso-card">
                    <h3>Engenharias</h3>
                    <p>Formação completa para desenvolver soluções inovadoras e transformar o mundo.</p>
                </div>

                <div class="curso-card">
                    <h3>Saúde</h3>
                    <p>Cursos que preparam profissionais para cuidar das pessoas com excelência.</p>
                </div>

                <div class="curso-card">
                    <h3>Tecnologia</h3>
                    <p>Capacitação em TI, dados e inovação digital para o mercado do futuro.</p>
                </div>

                <div class="curso-card">
                    <h3>Negócios</h3>
                    <p>Administração, Contabilidade e Gestão para liderar no mundo corporativo.</p>
                </div>
            </div>
        </section>

        <section class="enem">
            <h2>Simule seu Desconto com a Nota do ENEM</h2>
            <p>Insira sua nota do ENEM e veja o desconto que você pode conquistar na FAESA!</p>

            <div class="enem-simulador">
                <label for="notaEnem">Sua Nota do ENEM*</label>
                <input type="number" id="notaEnem" min="0" max="1000" placeholder="Ex: 750" required>
                <button onclick="calcularDesconto()">Calcular Desconto</button>
                <p id="resultado"></p>
            </div>
        </section>


        <section class="formulario">
            <h2>Entre em contato</h2>
            <form action="processa.php" method="POST">

                <div class="input-group">
                    <label for="nome">Nome*</label>
                    <input type="text" id="nome" name="nome" placeholder="Digite seu nome completo" required>
                </div>

                <div class="input-group">
                    <label for="email">E-mail*</label>
                    <input type="email" id="email" name="email" placeholder="exemplo@email.com" required>
                </div>

                <div class="input-group">
                    <label for="telefone">Telefone (opcional)</label>
                    <input type="tel" id="telefone" name="telefone" placeholder="(99) 99999-9999">
                </div>

                <div class="input-group">
                    <label for="assunto">Assunto*</label>
                    <select id="assunto" name="assunto" required>
                        <option value="" disabled selected>Selecione uma opção</option>
                        <option value="cursos">Informações sobre cursos</option>
                        <option value="inscricao">Processo de inscrição</option>
                        <option value="parcerias">Parcerias</option>
                        <option value="outros">Outros</option>
                    </select>
                </div>

                <div class="input-group">
                    <label for="mensagem">Mensagem*</label>
                    <textarea id="mensagem" name="mensagem" minlength="10" placeholder="Digite sua mensagem"
                        required></textarea>
                </div>

                <button type="submit">📩 Enviar</button>
            </form>
        </section>

    </main>

    <footer>
        <p>&copy;
            <?php echo date("Y"); ?> FAESA - Todos os direitos reservados.
        </p>
    </footer>
</body>
<script src="enem.js"></script>

</html>