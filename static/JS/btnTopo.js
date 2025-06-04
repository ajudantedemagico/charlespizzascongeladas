const scrollTopBtn = document.getElementById("scrollTopBtn");

    // Mostrar o botão ao rolar para baixo
    window.addEventListener("scroll", () => {
      if (window.scrollY > 300) {
        scrollTopBtn.classList.add("show");
      } else {
        scrollTopBtn.classList.remove("show");
      }
    });

    // Voltar ao topo ao clicar no botão
    scrollTopBtn.addEventListener("click", () => {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });