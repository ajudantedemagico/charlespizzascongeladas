function formatarData(data) {
    const opcoes = { day: '2-digit', month: 'long' };
    return data.toLocaleDateString('pt-BR', opcoes).toUpperCase();
}

document.addEventListener('DOMContentLoaded', () => {
    const btnDataEntrega = document.querySelector('[data-entrega]');
    const botaoPagamento = document.getElementById('inputDataEntrega');

    let calendarioAberto = false;

    const calendario = document.createElement('input');
    calendario.setAttribute('type', 'date');
    calendario.setAttribute('id', 'calendario');
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
        // Formatando manualmente para "DD DE MÊS" em maiúsculas
        const meses = [
            'JANEIRO', 'FEVEREIRO', 'MARÇO', 'ABRIL', 'MAIO', 'JUNHO',
            'JULHO', 'AGOSTO', 'SETEMBRO', 'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO'
        ];
        const mesNome = meses[parseInt(mes, 10) - 1];
        const dataFormatada = `${dia} DE ${mesNome}`;
        btnDataEntrega.textContent = `${dataFormatada} >ALTERAR`;
        botaoPagamento.disabled = false;
    }
    calendario.style.display = 'none';
    calendarioAberto = false;
});


    function configurarCalendario() {
        const hoje = new Date();
        hoje.setDate(hoje.getDate() + 2); // A partir de 2 dias

        const dia = hoje.getDate().toString().padStart(2, '0');
        const mes = (hoje.getMonth() + 1).toString().padStart(2, '0');
        const ano = hoje.getFullYear();

        calendario.min = `${ano}-${mes}-${dia}`; // Define a data mínima
        
    }

    botaoPagamento.disabled = true; // Desabilita o botão de pagamento inicialmente
});
