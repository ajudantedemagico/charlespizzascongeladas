document.addEventListener('DOMContentLoaded', () => {
    const stickers = document.querySelectorAll('.sticker');

    function animateStickers() {
        const scrollY = window.scrollY || document.documentElement.scrollTop;

        stickers.forEach(sticker => {
            const speed = parseFloat(sticker.dataset.speed || 0.5); // Velocidade de movimento
            const startOffset = parseFloat(sticker.dataset.startOffset || 0); // Onde o movimento começa na rolagem
            const limitY = parseFloat(sticker.dataset.limitY || Infinity); // Limite de movimento vertical em pixels
            const startX = sticker.offsetLeft; // Posição X inicial
            const startY = sticker.offsetTop;  // Posição Y inicial (se position:absolute)
                                               // Se position:fixed, top/left inicial do CSS

            let newY = 0;
            // Cálculo do movimento (simplificado para exemplo)
            // Se o adesivo está fixo na tela e se move 'contra' a rolagem
            newY = scrollY * speed;

            // Limitar o movimento vertical
            if (limitY !== Infinity) {
                newY = Math.min(newY, limitY); // Não exceder o limite superior
            }

            // Aplicar a transformação CSS
            sticker.style.transform = `translateY(${newY}px)`;

            // Exemplo de como você faria se quisesse mover o X também
            // const newX = scrollY * speedX;
            // sticker.style.transform = `translate(${newX}px, ${newY}px)`;
        });

        // Opcional: Para otimizar e garantir suavidade
        // requestAnimationFrame(animateStickers);
    }

    // Chama a função de animação na rolagem
    window.addEventListener('scroll', animateStickers);

    // Chama uma vez ao carregar a página para posicionar corretamente
    animateStickers();
});