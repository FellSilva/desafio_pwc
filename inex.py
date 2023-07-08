def inverter_ordem_palavras(frase):
    palavras = frase.split()
    palavras_revertidas = palavras[::-1]
    frase_revertida = ' '.join(palavras_revertidas)
    return frase_revertida

frase_input = input("Digite uma frase: ")
frase_output = inverter_ordem_palavras(frase_input)
print("Frase invertida:", frase_output)
