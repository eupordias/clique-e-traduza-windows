# Clique e Traduza no Windows (QuickTranslate) 🚀

Uma ferramenta open-source leve em Python para o Windows que traduz instantaneamente qualquer texto selecionado na tela para o **Português (Brasil)** ao pressionar **`CTRL + CTRL` (duplo toque na tecla CTRL)**, exibindo o resultado em uma janela flutuante com suporte a rolagem e um botão para enviar diretamente ao **Bloco de Notas**.

---

## 🌟 Funcionalidades

- **Tradução Instantânea**: Selecione qualquer texto em qualquer aplicativo (navegador, PDF, editores, etc.) e traduza na hora.
- **Atalho Simples (`CTRL + CTRL`)**: Basta tocar duas vezes na tecla `CTRL` para capturar e traduzir o texto selecionado, sem atrapalhar outros atalhos.
- **Português do Brasil (pt-BR)**: Traduz automaticamente de qualquer idioma de origem para o português do Brasil.
- **Capacidade Ampliada**: Suporte a textos e parágrafos de até **2000 caracteres**.
- **Janela Flutuante com Rolagem**: Exibição organizada em uma janela flutuante sempre no topo (`topmost`), equipada com barra de rolagem.
- **Integração com Bloco de Notas**: Botão dedicado *"Enviar para o Bloco de Notas"* que abre instantaneamente o Notepad do Windows com o texto traduzido.
- **Totalmente Gratuito e Sem API Key**: Utiliza APIs públicas de tradução, sem necessidade de configuração de chaves complexas.

---

## 📋 Pré-requisitos

- **Python 3.8+** instalado no Windows.

---

## ⚙️ Instalação

1. Clone ou baixe este repositório:
   ```bash
   git clone https://github.com/eupordias/clique-e-traduza-windows.git
   cd clique-e-traduza-windows
   ```

2. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Como Usar

1. Execute o script principal:
   ```bash
   python main.py
   ```
2. O aplicativo rodará em segundo plano no terminal.
3. Selecione qualquer texto em qualquer programa.
4. Pressione a tecla **`CTRL` duas vezes rapidamente**.
5. Uma janela flutuante aparecerá próximo ao cursor do mouse com a tradução.
6. Clique em **"Enviar para o Bloco de Notas"** para abrir o Notepad com o texto ou clique para fechar a janela.

---

## 🛠️ Tecnologias Utilizadas

- **Python**
- **Tkinter** (Interface gráfica nativa leve)
- **Pynput** (Monitoramento de teclado global)
- **Pyperclip** (Manipulação da área de transferência)
- **Requests** (Requisições para tradução)

---

## 📄 Licença

Este projeto é distribuído sob a licença **MIT**. Sinta-se livre para usar, modificar e compartilhar.
