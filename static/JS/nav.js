document.addEventListener("DOMContentLoaded", async () => {
  const carrinho = window.location.pathname.includes("/meu-carrinho") || window.location.pathname.includes("/carrinho");

  let nomeUsuario = null;

  // Verificar se o usuário está logado
  try {
    const response = await fetch("/api/usuario/logado");
    const data = await response.json();
    if (data.logado) {
      nomeUsuario = data.nome;
    }
  } catch (error) {
    console.error("Erro ao verificar login:", error);
  }

  const navMobile = `
    <nav id="navmobile">
      <img class="logo" src="/static/img/logotipo.png" alt="logotipo">
      <div class="icones">
        <a href="/meu-carrinho"><img class="icon" src="/static/img/icon_cart_azul.png" alt="carrinho"></a>

        ${
          carrinho
            ? '<a href="/"><img class="icon" src="/static/img/icone-home.png" alt="home"></a>'
            : nomeUsuario
              ? '<a href="/meus-pedidos"><img class="icon" src="/static/img/icon_login_azul.png" alt="cliente"></a>'
              : '<a href="/login"><img class="icon" src="/static/img/icon_login_azul.png" alt="login"></a>'
        }

        <a href="#"><img class="icon" id="menu" src="/static/img/icon_menu_azul.png" alt="menu"></a>
        <div class="menu" id="menuOverlay">
          <a href="#"><img class="icon" id="menu2" src="/static/img/icon_menu_azul.png" alt="menu"></a>
          <ul class="menu-list" id="menuList">
            <li><a href="/#comofunciona">Como Funciona</a></li>
            <li><a href="/#avaliacao">Avaliações</a></li>
            <li><a href="/#cardapio">Cardápio</a></li>
            <li><a href="/#entrega">Entrega</a></li>

            ${
              nomeUsuario === "Administrador"
                ? '<li><a href="/admin/usuarios">Área Administrativa</a></li>'
                : nomeUsuario
                  ? '<li><a href="/meus-pedidos">Área do Cliente</a></li>'
                  : ""
            }

            ${
              nomeUsuario
                ? '<li><a href="/logout">Sair</a></li>'
                : '<li><a href="/login">Login</a></li>'
            }
          </ul>
        </div>
      </div>
    </nav>
  `;

  const navDesk = `
    <nav id="navdesk">
      <img class="logo" src="/static/img/logotipo.png" alt="logotipo">
      <ul class="menudesk">
        <li><a href="/#comofunciona">Como Funciona</a></li>
        <li><a href="/#avaliacao">Avaliações</a></li>
        <li><a href="/#cardapio">Cardápio</a></li>
        <li><a href="/#entrega">Entrega</a></li>

        ${
          nomeUsuario === "Administrador"
            ? '<li><a href="/admin/usuarios">Área Administrativa</a></li>'
            : nomeUsuario
              ? '<li><a href="/meus-pedidos">Área do Cliente</a></li>'
              : ""
        }
      </ul>
      <div class="icones2">
        <a href="/meu-carrinho"><img class="icon" src="/static/img/icon_cart_azul.png" alt="carrinho"></a>

        ${
          carrinho
            ? '<a href="/"><img class="icon" src="/static/img/icone-home.png" alt="home"></a>'
            : nomeUsuario
              ? '<a href="/meus-pedidos"><img class="icon" src="/static/img/icon_login_azul.png" alt="cliente"></a>'
              : '<a href="/login"><img class="icon" src="/static/img/icon_login_azul.png" alt="login"></a>'
        }
      </div>
    </nav>
  `;

  document.body.insertAdjacentHTML("afterbegin", navDesk);
  document.body.insertAdjacentHTML("afterbegin", navMobile);

  const menuButton = document.getElementById('menu');
  const closeButton = document.getElementById('menu2');
  const menuOverlay = document.getElementById('menuOverlay');

  // Abrir o menu
  menuButton.addEventListener('click', function (event) {
    event.preventDefault();
    menuOverlay.style.display = 'block';
  });

  // Fechar o menu
  closeButton.addEventListener('click', function (event) {
    event.preventDefault();
    menuOverlay.style.display = 'none';
  });
});

// Função para fechar o box de erro (login)
function fecharErro() {
  const box = document.getElementById("erroBox");
  if (box) {
    box.style.display = "none";
  }
  document.getElementById("email").value = '';
  document.getElementById("senha").value = '';
}
 function fecharPopup() {
        window.location.href = "/login";
    }