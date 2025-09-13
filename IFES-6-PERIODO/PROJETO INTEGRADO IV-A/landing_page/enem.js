// Simulação de desconto com nota do ENEM
function calcularDesconto() {
    const nota = parseFloat(document.getElementById("notaEnem").value);
    const resultado = document.getElementById("resultado");
    
    if (isNaN(nota) || nota < 0 || nota > 1000) {
        resultado.innerHTML = "⚠️ Insira uma nota válida entre 0 e 1000.";
        resultado.style.color = "#ff4444";
        return;
    }

    let desconto = 0;

    if (nota >= 900) desconto = 100;
    else if (nota >= 800) desconto = 75;
    else if (nota >= 700) desconto = 50;
    else if (nota >= 600) desconto = 30;
    else desconto = 10;

    resultado.style.color = "#00ffcc";
    resultado.innerHTML = `🎉 Parabéns! \nVocê conquistou <strong>${desconto}%</strong> de desconto na 1ª mensalidade.`;
}

// Imagem Carrosel
const track = document.querySelector(".carousel-track");
const slides = Array.from(track.children);
let index = 0;
// função para mover o carrossel
function moveCarousel() {
  index++;
  if (index >= slides.length) {
    index = 0;
  }
  const slideWidth = slides[0].getBoundingClientRect().width;
  track.style.transform = `translateX(-${index * slideWidth}px)`;
}

// troca de imagem a cada 3 segundos
setInterval(moveCarousel, 3000);




