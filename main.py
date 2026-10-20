import tkinter as tk
import time
import threading
import subprocess
import pyperclip
import requests
from pynput import keyboard

class TranslatorApp:
    def __init__(self):
        self.root = None
        self.target_lang = "pt-BR"  # Brazilian Portuguese
        self.last_trigger_time = 0
        self.ctrl_pressed = False

    def translate_text(self, text):
        if not text.strip():
            return "Nenhum texto selecionado."
        
        if len(text) > 2000:
            text = text[:2000]

        try:
            url = f"https://api.mymemory.translated.net/get?q={requests.utils.quote(text)}&langpair=autodetect|{self.target_lang}"
            response = requests.get(url, timeout=8)
            data = response.json()
            if data.get("responseStatus") == 200:
                return data["responseData"]["translatedText"]
            else:
                return f"Erro na tradução: {data.get('responseDetails', 'Erro desconhecido')}"
        except Exception as e:
            return f"Erro de conexão: {str(e)}"

    def send_to_notepad(self, translated_text):
        try:
            file_path = "traducao_recente.txt"
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(translated_text)
            subprocess.Popen(["notepad.exe", file_path])
        except Exception as e:
            print(f"Erro ao abrir o Bloco de Notas: {e}")
        self.close_popup()

    def show_popup(self, translated_text):
        if self.root:
            try:
                self.root.destroy()
            except:
                pass

        self.root = tk.Tk()
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)

        # Position near mouse cursor
        try:
            from pynput.mouse import Controller as MouseController
            mouse_ctrl = MouseController()
            x, y = mouse_ctrl.position
            x += 15
            y += 15
        except:
            x, y = 100, 100

        self.root.geometry(f"+{x}+{y}")

        main_frame = tk.Frame(self.root, bg="#2d3748", bd=2, relief="solid")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Text display with scrollbar
        text_frame = tk.Frame(main_frame, bg="#2d3748")
        text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        text_widget = tk.Text(
            text_frame,
            bg="#2d3748",
            fg="#edf2f7",
            font=("Segoe UI", 10),
            wrap=tk.WORD,
            width=50,
            height=10,
            bd=0,
            highlightthickness=0
        )
        text_widget.insert("1.0", translated_text)
        text_widget.config(state="disabled")
        text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=text_widget.yview, bg="#2d3748")
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        text_widget.config(yscrollcommand=scrollbar.set)

        # Button frame at the bottom
        btn_frame = tk.Frame(main_frame, bg="#1a202c", padx=10, pady=8)
        btn_frame.pack(fill=tk.X, side=tk.BOTTOM)

        notepad_btn = tk.Button(
            btn_frame,
            text="Enviar para o Bloco de Notas",
            command=lambda: self.send_to_notepad(translated_text),
            bg="#4a5568",
            fg="#ffffff",
            font=("Segoe UI", 9, "bold"),
            relief="flat",
            padx=10,
            pady=5,
            cursor="hand2"
        )
        notepad_btn.pack(side=tk.LEFT, fill=tk.X, expand=True)

        close_btn = tk.Button(
            btn_frame,
            text="Fechar",
            command=self.close_popup,
            bg="#718096",
            fg="#ffffff",
            font=("Segoe UI", 9),
            relief="flat",
            padx=10,
            pady=5,
            cursor="hand2"
        )
        close_btn.pack(side=tk.RIGHT, padx=(5, 0))

        # Close on Escape
        self.root.bind("<Escape>", lambda e: self.close_popup())

        self.root.mainloop()

    def close_popup(self):
        if self.root:
            try:
                self.root.destroy()
            except:
                pass
            self.root = None

    def on_press(self, key):
        try:
            if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
                current_time = time.time()
                # Double-tap CTRL within 0.4 seconds triggers translation
                if current_time - self.last_ctrl_press_time < 0.4:
                    self.trigger_translation()
                    self.last_ctrl_press_time = 0
                else:
                    self.last_ctrl_press_time = current_time
            else:
                # Any other key resets ctrl double tap
                self.last_ctrl_press_time = 0
        except Exception as e:
            pass

    def trigger_translation(self):
        current_time = time.time()
        if current_time - self.last_trigger_time < 0.6:
            return
        self.last_trigger_time = current_time

        time.sleep(0.05)
        # Simulate Ctrl+C to copy selected text
        from pynput.keyboard import Controller as KeyboardController, Key
        kb = KeyboardController()
        with kb.pressed(Key.ctrl):
            kb.press('c')
            kb.release('c')

        time.sleep(0.15)
        selected_text = pyperclip.paste()

        if selected_text.strip():
            translated = self.translate_text(selected_text)
            threading.Thread(target=self.show_popup, args=(translated,)).start()

    def run(self):
        print("Tradutor para Português (Brasil) iniciado! Atalho: Pressione CTRL duas vezes rapidamente.")
        print("Selecione qualquer texto e aperte CTRL duas vezes para traduzir.")
        print("Pressione Ctrl+C no terminal para sair.")

        # Start keyboard listener
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()

if __name__ == "__main__":
    app = TranslatorApp()
    app.run()
