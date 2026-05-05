from dados import noticias

def validar_texto(texto):
    #Levanta ValueError se o texto for vazio ou só espaços.
    if not texto or texto.strip() == "":
        raise ValueError("Texto da notícia não pode ser vazio.")
    return texto.strip()

def adicionar_noticia(texto, classificacao):
    #Adiciona notícia. Retorna True se o texto for válido ou False se for vazio.
    try:
        texto_valido = validar_texto(texto)
        noticias.append({"texto": texto_valido, "classificacao": classificacao})
        return True
    except ValueError as e:
        print(f"Erro: {e}")
        return False

def listar_noticias():
    #Exibe todas as notícias cadastradas.
    if not noticias:
        print("Nenhuma notícia cadastrada.")
        return
    for i, n in enumerate(noticias, 1):
        print(f"\n--- Notícia {i} ---")
        print(f"Texto: {n['texto']}")
        print(f"Classificação: {n['classificacao']}")
    print("-" * 30)