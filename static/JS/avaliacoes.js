let slideIndex = 0;
mostrarSlide(slideIndex);

function mudarSlide(n) {
  mostrarSlide(slideIndex += n);
}

function mostrarSlide(n) {
  let slides = document.getElementsByClassName("slide");
  
  if (n >= slides.length) slideIndex = 0;
  if (n < 0) slideIndex = slides.length - 1;

  for (let i = 0; i < slides.length; i++) {
    slides[i].classList.remove("ativo");
  }

  slides[slideIndex].classList.add("ativo");
}
