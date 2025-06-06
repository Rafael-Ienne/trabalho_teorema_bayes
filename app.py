from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# --- Probabilidades (Baseadas no trecho fornecido da notícia e algumas inferências) ---
# Evento A: Ocupação potencialmente exposta à IA generativa
# Evento B: Ocupação em um país de renda alta

# P(A) - Probabilidade a priori de uma ocupação estar potencialmente exposta à IA
# Notícia: "25% do emprego global estão em ocupações potencialmente expostas à IA generativa"
P_A = 0.25

# P(~A) - Probabilidade a priori de uma ocupação NÃO estar potencialmente exposta à IA
P_NAO_A = 1 - P_A

# P(B | A) - Verossimilhança
# Se uma ocupação está exposta, qual a chance de ela estar em um país de renda alta?
# Notícia: "participações maiores em países de renda alta (34%)" 
P_B_DADO_A = 0.34

# P(B | ~A) - Verossimilhança
# Se uma ocupação NÃO está exposta, qual a chance de ela estar em um país de renda alta?
P_B_DADO_NAO_A = 0.20 # VALOR INVENTADO

# P(B) - Probabilidade marginal (A priori, ou de base, de uma ocupação estar em país de renda alta)
# P(País de Renda Alta) = P(País de Renda Alta | Exposta) * P(Exposta) + P(País de Renda Alta | Não Exposta) * P(Não Exposta)
P_B = (P_B_DADO_A * P_A) + (P_B_DADO_NAO_A * P_NAO_A)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular_exposicao', methods=['POST'])
def calcular_exposicao():
    data = request.json
    is_pais_alta_renda = data.get('paisAltaRenda')

    # Vamos calcular P(Exposta | País de Renda Alta) ou P(Exposta | Não País de Renda Alta),
    # com base no input do usuário no checkbox
    # Teorema de Bayes: P(A|B) = [P(B|A) * P(A)] / P(B)

    # Definir as probabilidades baseadas na evidência (País de Renda Alta ou Não)
    if is_pais_alta_renda:
        # Queremos P(Exposta | País de Renda Alta)
        # P(B|A) = P_B_DADO_A
        # P(A) = P_A
        # P(B) = P_B (calculado acima)
        
        prob_numerador = P_B_DADO_A * P_A
        prob_denominador = P_B # Usamos a probabilidade marginal calculada

    else:
        # Queremos P(Exposta | Não País de Renda Alta)
        # P(~B|A) = P( Não País de Renda Alta | Exposta) = 1 - P_B_DADO_A
        # P(A) = P_A
        # P(~B) = P(Não País de Renda Alta) = 1 - P_B
        
        prob_numerador = (1 - P_B_DADO_A) * P_A
        prob_denominador = (1 - P_B)

    # Evita divisão por zero
    if prob_denominador == 0:
        prob_exposta_dado_evidencia = 0.0
    else:

        prob_exposta_dado_evidencia = prob_numerador / prob_denominador

    return jsonify({
        'probabilidade_exposicao': round(prob_exposta_dado_evidencia * 100, 2),
        'detalhes_calculo': {
            'P_A': round(P_A * 100, 2),
            'P_NAO_A': round(P_NAO_A * 100, 2),
            'P_B_DADO_A': round(P_B_DADO_A * 100, 2),
            'P_B_DADO_NAO_A': round(P_B_DADO_NAO_A * 100, 2),
            'P_NAO_B_DADO_A': round((1 - P_B_DADO_A) * 100, 2),
            'P_B': round(P_B * 100, 2),
            'P_NAO_B': round((1 - P_B) * 100, 2),
            'P_NAO_B_DADO_NAO_A': round((1 - P_B_DADO_NAO_A) * 100, 2),
        }
    })

if __name__ == '__main__':
    app.run(debug=False)