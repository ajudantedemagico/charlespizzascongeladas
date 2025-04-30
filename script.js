document.addEventListener('DOMContentLoaded', () => {
    const elementosParallax = document.querySelectorAll('.parallax-elemento');
  
    window.addEventListener('scroll', () => {
      elementosParallax.forEach(elemento => {
        const velocidade = parseFloat(elemento.dataset.velocidade) || 0.2;
        const posicaoScroll = window.scrollY;
        elemento.style.transform = `translateY(${posicaoScroll * velocidade}px)`;
      });
    });
  });