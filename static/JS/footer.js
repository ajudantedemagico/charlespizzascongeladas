document.addEventListener("DOMContentLoaded", () => {
  const footerHTML = `
    <footer>
      <div class="conteudofooter">
        <img class="logofooter" src="/static/img/logotipo.png" alt="logotipofooter">
        <h1>SIGA-NOS NAS REDES SOCIAIS</h1>
        <p>@CHARLESPIZZASCONGELADAS</p>
      </div>
    </footer>
  `;

  document.body.insertAdjacentHTML("beforeend", footerHTML);
});
