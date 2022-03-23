print("Digite 3 palavras: ")
primeira, segunda, terceira = input("Primeira: "), input("Segunda: "), input("Terceira: ")

primeira_upper = primeira.upper()

segunda_lower = segunda.lower()

vogal_list = ["A", "E", "I", "O", "U"]
terceira_upper = terceira.upper()
for vogal in vogal_list:
    terceira_upper = terceira_upper.replace(vogal, "")

print(f"Resultado, primeira palavra: {primeira_upper}; segunda palavra: {segunda_lower}; terceira palavra: {terceira_upper}")