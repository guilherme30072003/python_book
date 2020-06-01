#Programa que simula um site de dicionários de sinônimos, onde você pode adicionar palavras.

print("Sinônimos.com.gui")
print("Fonte: www.sinonimos.com.br")
dicionario = {"casa" : ["residência", "moradia", "lar"],
              "bola" : ["globo", "esfera", "pelota"],
              "problema" : ["adversidade", "contratempo", "dificuldade"]}

while True:
    plvra_pedida = input("\nDigite uma palavra para ver seus sinônimos('f' para sair): ")
    if plvra_pedida == "f":
        break
    if plvra_pedida in dicionario:
        print("\nOs sinônimos são: %s" % dicionario[plvra_pedida])
    else:
        add_plvra = input("Palavra não encontrada, deseja adicioná-la? (s/n): ")
        if add_plvra == "s":
            chave = plvra_pedida
            valor = input("Diga pelo menos 3 sinônimos dessa palavra: ").split(", ")
            dicionario[chave] = valor
            print("Palavra e sinônimos adicionados!")
