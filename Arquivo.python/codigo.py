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

# Solicita ao usuário que escolha um jogo
escolha = input("Digite o número do jogo que você deseja comprar: ")

# Verifica se a escolha está no estoque
if escolha in estoque:
    print(f"Você escolheu: {estoque[escolha]}. Obrigado pela compra!")
else:
    print("Desculpe, esse jogo não está disponível. Por favor, escolha um número válido.")

print("Até a próxima!")
