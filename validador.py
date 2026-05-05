def classificar_noticia(texto):
    """
    Classifica automaticamente a notícia baseado nas seguintes regras:
    - Não contém "FONTE" → +1 ponto
    - Contém "!!!" → +1 ponto
    - Contém "URGENTE" → +1 ponto
    - Tamanho < 10 caracteres → +1 ponto

    Retorna "confiavel", "duvidosa" ou "falsa".
    """
    texto_tratado = texto.strip().upper()  # Normaliza o texto para comparação 

    pontos = 0
    if "FONTE" not in texto_tratado:
        pontos += 1
    if "!!!" in texto_tratado:
        pontos += 1
    if "URGENTE" in texto_tratado:
        pontos += 1
    if len(texto_tratado) < 10:
        pontos += 1

    if pontos == 0:
        return "confiavel"
    elif pontos == 1:
        return "duvidosa"
    else:
        return "falsa"