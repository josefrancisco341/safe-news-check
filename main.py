from validador import classificar_noticia
from gerenciador import adicionar_noticia, listar_noticias

def opcao_adicionar():
    #Lê o texto, classifica automaticamente e adiciona.
    texto = input("\nDigite o texto da notícia: ")
    classificacao = classificar_noticia(texto)
    if adicionar_noticia(texto, classificacao):
        print(f"Notícia adicionada! Classificação: {classificacao}")

def opcao_listar():
    listar_noticias()

def menu():
    while True:
        print("\n===== SAFE NEWS =====")
        print("1 - Verificar confiabilidadade de notícia")
        print("2 - Listar notícias")
        print("3 - Sair")
        opcao = input("Digite a opção desejada: ")

        match opcao:
            case "1":
                opcao_adicionar()
            case "2":
                opcao_listar()
            case "3":
                print("Saindo...")
                break
            case _:
                print("Opção inválida. Digite 1, 2 ou 3.")

if __name__ == "__main__":
    menu()