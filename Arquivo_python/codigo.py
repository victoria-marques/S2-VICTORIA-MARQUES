# Estoque de jogos
estoque = {
    "1": "The Legend of Zelda: Breath of the Wild",
    "2": "Super Mario Odyssey",
    "3": "God of War",
    "4": "Minecraft",
    "5": "The Last of Us Part II"
}

# Exibe os jogos disponíveis
print("Bem-vindo à loja de videogames!")
print("Aqui estão os jogos disponíveis:")
for chave, jogo in estoque.items():
    print(f"{chave}: {jogo}")

    # Recebendo a escolha do usuário
escolha = input("Digite o número do filme que você deseja assistir: ")

# Verificando a escolha
if escolha.isdigit() and 1 <= int(escolha) <= len(filmes):
    filme_escolhido = filmes[int(escolha) - 1]
    print(f"Você escolheu assistir: {filme_escolhido}!")
else:
    print("Escolha inválida! Por favor, digite um número correspondente à lista de filmes.")
