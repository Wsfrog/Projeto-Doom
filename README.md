# 💀 DOOM WEB FLASK

> "Rip and Tear, until it is done."

Um emulador web estilizado para rodar **DOOM (1993)** diretamente no navegador usando Python (Flask) e JS-DOS. O projeto foca em uma experiência visual imersiva com estética Retro/Arcade.

<img width="1429" height="867" alt="image" src="https://github.com/user-attachments/assets/44c3712f-ef0f-4716-96f1-2775624dfdfc" />


## 🕹️ Funcionalidades

* **Interface Retro:** Efeito de scanline (TV de tubo), brilho neon e fontes pixeladas.
* **Emulação JS-DOS v6.22:** Estável e leve.
* **Modo Turbo:** Configurado para usar o máximo de ciclos da CPU (`cycles: max`) para maior FPS.
* **Controles Modernos:** Suporte a mouse lock (mira) e tiro.
* **Responsividade:** Modo Tela Cheia (Fullscreen) ajustado para manter o formato 4:3 original sem deformar o jogo.

## 🚀 Como Rodar

### Pré-requisitos
* Python instalado.

### Passo a Passo

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/SEU-USUARIO/doom-flask.git](https://github.com/SEU-USUARIO/doom-flask.git)
    cd doom-flask
    ```

2.  **Crie e ative o Ambiente Virtual:**
    * *Windows:*
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```
    * *Linux/Mac:*
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Instale as dependências:**
    ```bash
    pip install flask
    ```

4.  **⚠️ Adicione o arquivo do Jogo:**
    Por motivos de direitos autorais, o arquivo do jogo não está incluído.
    * Consiga um arquivo **`doom.jsdos`**.
    * Coloque-o na pasta: `static/games/doom.jsdos`.

5.  **Execute o servidor:**
    ```bash
    python app.py
    ```

6.  **Jogue:**
    Abra seu navegador em: `http://127.0.0.1:5000`

## 🎮 Controles

| Tecla | Ação |
| :--- | :--- |
| **W, A, S, D** | Mover (Simulado via Setas) |
| **Mouse** | Mirar (Girar câmera) |
| **Clique Esq.** | Atirar |
| **Espaço** | Abrir Portas / Ação |
| **ESC** | Liberar o Mouse / Menu |
| **F5** | Melhorar Performance (Low Detail) |
