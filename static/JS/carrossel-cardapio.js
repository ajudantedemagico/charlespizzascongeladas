function trocarPizza(element) {
    const sabor = element.getAttribute('data-title');
    const desc = element.getAttribute('data-desc');
    const imgSrc = element.getAttribute('src');

    // Atualiza imagem, título e descrição
    document.getElementById('pizza-img').src = imgSrc;
    document.getElementById('pizza-title').textContent = sabor;
    document.getElementById('pizza-desc').textContent = desc;

    // Atualiza o input hidden do sabor (para enviar no formulário)
    document.getElementById('input-sabor').value = sabor;

    // Zera todas as quantidades ao mudar o sabor (opcional)
    document.querySelectorAll('input[name="quantidades"]').forEach(input => input.value = 0);
}