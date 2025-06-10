const carrosselImages = document.querySelector('.carrossel-images');
    const totalItems = document.querySelectorAll('.carrossel-item').length;
    const prevButton = document.getElementById('prev');
    const nextButton = document.getElementById('next');
    let currentIndex = 0;

    function updateCarrossel() {
        const offset = -currentIndex * 100;
        carrosselImages.style.transform = `translateX(${offset}%)`;
    }

    prevButton.addEventListener('click', () => {
        currentIndex = (currentIndex - 1 + totalItems) % totalItems;
        updateCarrossel();
    });

    nextButton.addEventListener('click', () => {
        currentIndex = (currentIndex + 1) % totalItems;
        updateCarrossel();
    });