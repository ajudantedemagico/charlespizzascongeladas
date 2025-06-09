document.addEventListener('DOMContentLoaded', () => {
    console.log('[entrega.js] DOM carregado.');

    const btnDataEntrega = document.querySelector('[data-entrega]');
    const inputDataEntrega = document.getElementById('inputDataEntrega');
    const formPedido = document.querySelector('form.botaopagar');

    if (!btnDataEntrega || !inputDataEntrega || !formPedido) {
        console.warn('Elementos data-entrega, inputDataEntrega ou formPedido não encontrados.');
        return;
    }

    let calendarioAberto = false;

    const calendario = document.createElement('input');
    calendario.type = 'date';
    calendario.id = 'calendario';
    calendario.style.display = 'none';
    calendario.style.position = 'absolute';
    calendario.style.backgroundColor = 'white';
    calendario.style.border = '2px solid #29c7e6';
    calendario.style.padding = '10px';
    calendario.style.boxShadow = '0px 4px 8px rgba(0,0,0,0.2)';
    calendario.style.borderRadius = '9px';

    btnDataEntrega.parentElement.appendChild(calendario);

    btnDataEntrega.addEventListener('click', (e) => {
        e.stopPropagation();
        if (!calendarioAberto) {
            configurarCalendario();
            calendario.style.display = 'block';
            calendario.style.top = `${btnDataEntrega.offsetTop + btnDataEntrega.offsetHeight}px`;
            calendario.style.left = `${btnDataEntrega.offsetLeft}px`;
            calendarioAberto = true;
        } else {
            calendario.style.display = 'none';
            calendarioAberto = false;
        }
    });

    document.addEventListener('click', () => {
        if (calendarioAberto) {
            calendario.style.display = 'none';
            calendarioAberto = false;
        }
    });

    calendario.addEventListener('change', () => {
        const valor = calendario.value;  
        if (valor) {
            const [ano, mes, dia] = valor.split('-');
            const dataFormatada = `${dia}/${mes}/${ano}`;

            btnDataEntrega.textContent = `${dataFormatada} >ALTERAR`;
            inputDataEntrega.value = valor;  
            inputDataEntrega.removeAttribute('disabled'); 
            console.log('Data de entrega selecionada:', valor);
        }

        calendario.style.display = 'none';
        calendarioAberto = false;
    });

    function configurarCalendario() {
        const hoje = new Date();
        hoje.setDate(hoje.getDate() + 2);
        const dia = String(hoje.getDate()).padStart(2, '0');
        const mes = String(hoje.getMonth() + 1).padStart(2, '0');
        const ano = hoje.getFullYear();
        calendario.min = `${ano}-${mes}-${dia}`;
    }

    inputDataEntrega.setAttribute('disabled', 'true');

    formPedido.addEventListener('submit', (e) => {
        if (!inputDataEntrega.value) {
            e.preventDefault();
            alert('Por favor, selecione a data de entrega antes de finalizar o pedido.');
        }
    });
});
