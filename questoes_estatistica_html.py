import random
import math

def gerar_valores_com_media_inteira():
    n = random.randint(5, 10)  # Define o número de elementos
    media_desejada = random.randint(1, 100)  # Define uma média desejada (inteira)
    soma_desejada = media_desejada * n  # Calcula a soma necessária para ter a média desejada

    valores = [random.randint(1, 100) for _ in range(n - 1)]  # Gera n-1 valores aleatórios
        # Calcula o último valor para garantir a média
    ultimo_valor = soma_desejada - sum(valores)

    # Se o último valor não for válido (fora do intervalo de 1 a 100), gera novamente
    while ultimo_valor < 1 or ultimo_valor > 100:
        valores = [random.randint(1, 100) for _ in range(n - 1)]
        ultimo_valor = soma_desejada - sum(valores)
    
    valores.append(ultimo_valor)  # Adiciona o último valor à lista
    
    return valores

def calcular_media(valores):
    return sum(valores) / len(valores)

def calcular_variancia(valores):
    media = calcular_media(valores)
    return sum((x - media) ** 2 for x in valores) / len(valores)

def calcular_desvio_padrao(valores):
    variancia = calcular_variancia(valores)
    return math.sqrt(variancia)

def calcular_desvio_medio(valores):
    media = calcular_media(valores)
    return sum(abs(x - media) for x in valores) / len(valores)

def calcular_mediana(valores):
    valores_ordenados = sorted(valores)
    n = len(valores)
    meio = n // 2
    if n % 2 == 0:
        return (valores_ordenados[meio - 1] + valores_ordenados[meio]) / 2
    else:
        return valores_ordenados[meio]

def gerar_questao():
    valores = gerar_valores_com_media_inteira()
    
    questoes = []
    
    media = calcular_media(valores)
    questoes.append({
        "pergunta": f"Calcule a média aritmética dos seguintes valores: {valores}",
        "gabarito": f"Média = {media:.0f}"  # A média será sempre inteira
    })
    
    mediana = calcular_mediana(valores)
    questoes.append({
        "pergunta": f"Calcule a mediana dos seguintes valores: {valores}",
        "gabarito": f"Mediana = {mediana:.2f}"
    })
    
    variancia = calcular_variancia(valores)
    questoes.append({
        "pergunta": f"Calcule a variância dos seguintes valores: {valores}",
        "gabarito": f"Variância = {variancia:.2f}"
    })
    
    desvio_padrao = calcular_desvio_padrao(valores)
    questoes.append({
        "pergunta": f"Calcule o desvio padrão dos seguintes valores: {valores}",
        "gabarito": f"Desvio Padrão = {desvio_padrao:.2f}"
    })
    
    desvio_medio = calcular_desvio_medio(valores)
    questoes.append({
        "pergunta": f"Calcule o desvio médio dos seguintes valores: {valores}",
        "gabarito": f"Desvio Médio = {desvio_medio:.2f}"
    })
    
    return questoes

def gerar_html(questoes):
    html_content = '''
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Questões de Estatística</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f2f5;
                margin: 0;
                padding: 20px;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
            }
            .container {
                background-color: #fff;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
                max-width: 600px;
                width: 100%;
            }
            h1 {
                font-size: 1.8rem;
                color: #333;
                text-align: center;
                margin-bottom: 20px;
            }
            .question-container {
                margin-bottom: 15px;
            }
            .question {
                font-size: 1rem;
                color: #333;
                font-weight: bold;
                margin-bottom: 8px;
            }
            .answer {
                background-color: #e6f7ff;
                padding: 10px;
                border-radius: 5px;
                border: 1px solid #91d5ff;
                font-size: 1rem;
                color: #0050b3;
            }
            footer {
                text-align: center;
                margin-top: 30px;
                font-size: 0.9rem;
                color: #777;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Questões de Estatística</h1>

            <!-- Questões geradas -->
    '''
    
    for i, questao in enumerate(questoes):
        html_content += f'''
            <div class="question-container">
                <div class="question">{i + 1}. {questao['pergunta']}</div>
                <div class="answer">{questao['gabarito']}</div>
            </div>
        '''
    
    html_content += '''
            <footer>
                &copy; 2024 Sistema de Estatística. Todos os direitos reservados.
            </footer>
        </div>
    </body>
    </html>
    '''

    with open("questoes_estatistica.html", "w", encoding="utf-8") as file:
        file.write(html_content)

    print("Arquivo HTML gerado com sucesso!")

# Gerar as questões e o HTML
questoes = gerar_questao()
gerar_html(questoes)

