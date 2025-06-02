const menuButton = document.getElementById('menu');
const closeButton = document.getElementById('menu2');
const menuOverlay = document.getElementById('menuOverlay');

// Abre o menu
menuButton.addEventListener('click', function(event) {
  event.preventDefault(); 
  menuOverlay.style.display = 'block'; 
});

// Fecha o menu
closeButton.addEventListener('click', function(event) {
  event.preventDefault(); 
  menuOverlay.style.display = 'none'; 
});

//mensagem de erro no login
function fecharErro() {
  const box = document.getElementById("erroBox");
  if (box) {
      box.style.display = "none";
  }
  // Limpa os campos
  document.getElementById("email").value = '';
  document.getElementById("senha").value = '';
}