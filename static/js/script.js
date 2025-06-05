// static/js/script.js
document.getElementById('exposureForm').addEventListener('submit', async function(event) {
    event.preventDefault(); // Previne o envio padrão do formulário

    const paisAltaRenda = document.getElementById('paisAltaRenda').checked;

    const response = await fetch('/calcular_exposicao', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            paisAltaRenda: paisAltaRenda
        })
    });

    const data = await response.json();
    const probabilidade = data.probabilidade_exposicao; 
    const detalhes = data.detalhes_calculo;

    // Atualiza os detalhes do cálculo na UI
    document.getElementById('detail-P_A').textContent = `P(A): ${detalhes.P_A}% (probabilidade a priori de uma ocupação estar potencialmente exposta à IA)`;
    document.getElementById('detail-P_NAO_A').textContent = `P(~A): ${detalhes.P_NAO_A}% (probabilidade a priori de uma ocupação NÃO estar potencialmente exposta à IA)`;

    document.getElementById('probabilidade_exposicao').textContent = probabilidade;

    if(!paisAltaRenda){

        document.getElementById('is_pais_alta_renda').textContent = 'não';
        document.getElementById('detail-P_B_A_1').textContent = `P(~B | A): ${detalhes.P_NAO_B_DADO_A}% (chance de uma ocupação não estar em um país de renda alta, dado que ela está exposta à IA)`;
        document.getElementById('detail-P_B_A_2').textContent = `P(~B | ~A): ${detalhes.P_NAO_B_DADO_NAO_A}% (valor inventado da chance de uma ocupação não estar em um país de alta renda, dada que ela não é exposta à IA)`;
        document.getElementById('detail-P_B').textContent = `P(~B): ${detalhes.P_NAO_B}% (probabilidade marginal de uma ocupação não estar em país de renda alta)`;

        document.getElementById('pergunta').textContent = `P(A | ~B)`;

        document.getElementById('formula').textContent = 'P(A | ~B) = [ P(~B | A) * P(A) ] / P(~B)';

    } else {

        document.getElementById('is_pais_alta_renda').textContent = '';
        document.getElementById('detail-P_B_A_1').textContent = `P(B | A): ${detalhes.P_B_DADO_A}% (chance de uma ocupação estar em um país de renda alta, dado que ela está exposta à IA)`;
        document.getElementById('detail-P_B_A_2').textContent = `P(B | ~A): ${detalhes.P_B_DADO_NAO_A}% (valor inventado da chance e uma ocupação estar em um país de renda alta, dado que ela não está exposta à IA)`;
        document.getElementById('detail-P_B').textContent = `P(B): ${detalhes.P_B}% (probabilidade marginal de uma ocupação estar em país de renda alta)`;
        document.getElementById('pergunta').textContent = `P(A | B)`;

        document.getElementById('formula').textContent = 'P(A | B) = [ P(B | A) * P(A) ] / P(B)';
    }
    document.getElementById('result').style.display = 'block'; // Mostra a caixa de resultado
});