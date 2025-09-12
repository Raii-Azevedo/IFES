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
        <img src="img/faesa-logo.png" alt="Logo FAESA" class="logo">
        <h1>Bem-vindo à FAESA!</h1>
        <p>Uma das melhores instituições de ensino do Brasil. Construa seu futuro com a gente!</p>
    </header>

    <main>
        <section class="sobre">
            <h2>Por que escolher a FAESA?</h2>
            <p>
                A FAESA é reconhecida pela qualidade de ensino, infraestrutura moderna e 
                professores qualificados. Oferecemos cursos que preparam você para o mercado de trabalho.
            </p>
            <img src="img/campus.jpg" alt="Campus FAESA" class="imagem-campus">
        </section>

        <section class="formulario">
            <h2>Entre em contato</h2>
            <form action="processa.php" method="POST">
                <label for="nome">Nome*</label>
                <input type="text" id="nome" name="nome" required>

                <label for="email">E-mail*</label>
                <input type="email" id="email" name="email" required>

                <label for="mensagem">Mensagem*</label>
                <textarea id="mensagem" name="mensagem" minlength="10" required></textarea>

                <button type="submit">Enviar</button>
            </form>
        </section>
    </main>

    <footer>
        <p>&copy; <?php echo date("Y"); ?> FAESA - Todos os direitos reservados.</p>
    </footer>
</body>
</html>
