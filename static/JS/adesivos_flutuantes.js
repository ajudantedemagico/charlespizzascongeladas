document.addEventListener('DOMContentLoaded', () => {
    const animatedImages = document.querySelectorAll('.animated-scroll-image');

    const activeAnimations = new Map();

    const options = {
        root: null, 
        rootMargin: '0px',
        threshold: 0.2 
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            const img = entry.target;
            const speed = parseFloat(img.dataset.speed) || 1;

            if (entry.isIntersecting) {
                img.classList.add('is-visible'); 

                if (!activeAnimations.has(img)) {
                    let angle = Math.random() * Math.PI * 2;
                    const rotationSpeed = (Math.random() - 0.5) * 0.002; 
                    let currentRotation = Math.random() * 36;

                    function animateFloat() {
                        const floatX = Math.sin(angle) * (8 * speed); 
                        const floatY = Math.cos(angle) * (6 * speed); 

                        img.style.transform = `translate(${floatX}px, ${floatY}px) rotate(${currentRotation}deg)`;

                        angle += 0.005 * (speed / 2);
                        currentRotation += rotationSpeed;

                        if (img.classList.contains('is-visible')) {
                            activeAnimations.set(img, requestAnimationFrame(animateFloat));
                        } else {
                            cancelAnimationFrame(activeAnimations.get(img));
                            activeAnimations.delete(img);
                        }
                    }
                    animateFloat();
                }

            } else {
                img.classList.remove('is-visible');
                if (activeAnimations.has(img)) {
                    cancelAnimationFrame(activeAnimations.get(img));
                    activeAnimations.delete(img);
                }
                img.style.transform = 'translate(0px, 0px) rotate(0deg)';
            }
        });
    }, options);

    animatedImages.forEach(img => {
        observer.observe(img);
    });
});