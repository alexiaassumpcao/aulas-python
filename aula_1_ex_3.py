sentence = input("Escreva uma frase: ")

sentence_pieces = sentence.split(" ")
first_letters = list()
remaning_letters = list()
for piece in sentence_pieces:
    first_letters.append(piece[:2])
    if len(piece) > 2:
        remaning_letters.append(piece[2:])

first_str = " ".join(first_letters)
remaning_str = " ".join(remaning_letters)
print(f"Primeiras letras: {first_str}")
print(f"Letras restantes: {remaning_str}")