function trocarPizza(element) {
  const novaImagem = element.getAttribute('src');
  const novoTitulo = element.getAttribute('data-title');
  const novaDescricao = element.getAttribute('data-desc');

  document.getElementById('pizza-img').src = novaImagem;
  document.getElementById('pizza-title').innerText = novoTitulo;
  document.getElementById('pizza-desc').innerText = novaDescricao;
}