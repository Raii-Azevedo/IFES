<?php
// Conexão com o banco
$conn = new mysqli("localhost", "root", "", "landing_faesa");

// Verifica conexão
if ($conn->connect_error) {
    die("Erro na conexão: " . $conn->connect_error);
}

// Recebe dados do formulário com segurança
$nome = trim($_POST['nome']);
$email = trim($_POST['email']);
$mensagem = trim($_POST['mensagem']);

// Validação
$erros = [];

if (empty($nome)) {
    $erros[] = "O nome é obrigatório.";
}
if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    $erros[] = "E-mail inválido.";
}
if (strlen($mensagem) < 10) {
    $erros[] = "A mensagem deve ter pelo menos 10 caracteres.";
}

if (count($erros) > 0) {
    echo "<h3>Erros encontrados:</h3><ul>";
    foreach ($erros as $erro) {
        echo "<li>$erro</li>";
    }
    echo "</ul><a href='index.php'>Voltar</a>";
} else {
    // Prepara SQL (previne SQL Injection)
    $stmt = $conn->prepare("INSERT INTO contatos (nome, email, mensagem) VALUES (?, ?, ?)");
    $stmt->bind_param("sss", $nome, $email, $mensagem);

    if ($stmt->execute()) {
        echo "<h2>Obrigado pelo contato, $nome!</h2>";
        echo "<p>Seus dados foram enviados com sucesso.</p>";
        echo "<a href='index.php'>Voltar</a>";
    } else {
        echo "Erro ao enviar: " . $stmt->error;
    }

    $stmt->close();
}

$conn->close();
?>
