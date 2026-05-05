# 🔍 Safe News Check – Monitoramento de Fake News

**Safe News Check** é um sistema simples em Python que **classifica automaticamente** notícias como **confiável**, **duvidosa** ou **falsa**, baseado em regras textuais.  
Você envia a notícia e nós verificamos a sua confiabilidade com base em critérios pré-definidos.

## 🚀 Funcionalidades

- ✅ Adicionar notícia para verificação da confiabilidade;
- ✅ Verificação da confiabilidade de notícias com base em:
        - Presença de fonte;
        - Presença de títulos sensacionalistas;
        - Presença de fortes exclamações;
        - Tamanho do título da notícia.
- ✅ Listar todas as notícias cadastradas;

## 📊 Regras de classificação

| Critérios de confiabilidade      | Pontos |
|----------------------------------|
| Não contém `"FONTE"`             |   +1   |
| Contém `"!!!"`                   |   +1   |
| Contém `"URGENTE"`               |   +1   |
| Texto com menos de 10 caracteres |   +1   |

**Resultado:**
- 0 pontos → `confiavel`
- 1 ponto → `duvidosa`
- ≥2 pontos → `falsa`

## ▶️ Como executar

### 📌 Pré-requisitos

* Python 3.10 ou superior (necessário para `match`)
* Git instalado

### 🚀 Passos

1. Clone o repositório:

   ```bash
   git clone https://github.com/josefrancisco341/safe-news-check.git
   ```

2. Acesse a pasta do projeto:

   ```bash
   cd safe-news-check
   ```

3. (Opcional, mas recomendado) Crie e ative um ambiente virtual:

   **Linux / macOS:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   **Windows (CMD):**

   ```cmd
   python -m venv venv
   venv\Scripts\activate
   ```

   **Windows (PowerShell):**

   ```powershell
   python -m venv venv
   venv\Scripts\Activate.ps1
   ```

4. Execute o projeto:

   **Linux / macOS:**

   ```bash
   python3 main.py
   ```

   **Windows:**

   ```cmd
   python main.py
   ```
