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