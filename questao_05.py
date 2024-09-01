"""
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;

"""

# Função para inverter os caracteres de uma string
def inverter_string(s):
    # Inicializa uma string vazia para armazenar o resultado
    string_invertida = ""
    
    # o loop for intera sobre a string de tras pra frente 
    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]
    
    return string_invertida

# Entrada da string
entrada = input("Digite a string a ser invertida: ")

# Inverte a string
resultado = inverter_string(entrada)

# Exibe o resultado
print("String invertida:", resultado)
