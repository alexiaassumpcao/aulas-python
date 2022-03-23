tabela_preco = {
    "sonho": 5.0,
    "croissant": 4.0,
    "coxinha": 3.0,
    "pastel": 4.5,
    "refrigerante": 6.0,
}

def produto_existe(chave: str) -> float :
    return tabela_preco.get(chave)

def ler_produto(msg: str) -> str:
    while True:
        item = input(msg).lower()
        if produto_existe(item):            
            return item
        else:
            print("Produto indisponível")

print("Digite os dois itens desejados:")    
item_um = ler_produto("item 1: ")
item_dois = ler_produto("item 2: ")

total = tabela_preco.get(item_um) + tabela_preco.get(item_dois)

print(f"R$ {total:.2f}")
