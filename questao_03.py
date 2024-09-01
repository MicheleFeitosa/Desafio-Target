""" 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média; """

import json

with open('faturamento.json', 'r') as file:
    dados = json.load(file)
   # print(dados)

# filtro pra ignorar os dias sem faturamento 
faturamentos = [dia['valor'] for dia in dados if dia['valor'] > 0]  

# O menor valor de faturamento ocorrido em um dia do mês;
menor_faturamento = min(faturamentos)

# O maior valor de faturamento ocorrido em um dia do mês;
maior_faturamento = max(faturamentos)

# média de faturamentos
media_faturamento = sum(faturamentos) / len(faturamentos)

# dias de faturamento acima da media 
dias_acima_da_media = len([valor for valor in faturamentos if valor > media_faturamento])

print("Menor valor de faturamento:", menor_faturamento)
print("Maior valor de faturamento:", maior_faturamento)
print("Média de faturamento: {:.2f}".format(media_faturamento))
print("Número de dias com faturamento acima da média:", dias_acima_da_media)
