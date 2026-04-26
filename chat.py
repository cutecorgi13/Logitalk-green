import customtkinter as ctk

# ===== ЗЕЛЕНА ТЕМА =====
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")  # головне!

GREEN_MAIN = "#2ecc71"
GREEN_HOVER = "#27ae60"
DARK_BG = "#1a1a1a"


# ===================== ЧАТ =====================
class ChatApp(ctk.CTk):
    def __init__(self, username):
        super().__init__()

        self.username = username

        self.title(f"LogiTalk | {self.username}")
        self.geometry("700x500")

        # ===== Sidebar =====
        self.sidebar = ctk.CTkFrame(self, width=150, fg_color="#14532d")
        self.sidebar.pack(side="left", fill="y")

        self.settings_label = ctk.CTkLabel(
            self.sidebar,
            text="Налаштування",
            text_color="#bbf7d0"
        )
        self.settings_label.pack(pady=10)

        self.theme_button = ctk.CTkButton(
            self.sidebar,
            text="Світла / Темна",
            fg_color=GREEN_MAIN,
            hover_color=GREEN_HOVER,
            command=self.toggle_theme
        )
        self.theme_button.pack(pady=5)

        # ===== Основна зона =====
        self.main_frame = ctk.CTkFrame(self, fg_color=DARK_BG)
        self.main_frame.pack(side="right", expand=True, fill="both")

        # Чат
        self.chat_box = ctk.CTkTextbox(
            self.main_frame,
            fg_color="#111827",
            text_color="#d1fae5"
        )
        self.chat_box.pack(padx=10, pady=10, fill="both", expand=True)

        # Ввід
        self.entry = ctk.CTkEntry(
            self.main_frame,
            placeholder_text="Введіть повідомлення...",
            fg_color="#064e3b",
            text_color="white"
        )
        self.entry.pack(padx=10, pady=5, fill="x")

        # Кнопка
        self.send_button = ctk.CTkButton(
            self.main_frame,
            text="Надіслати",
            fg_color=GREEN_MAIN,
            hover_color=GREEN_HOVER,
            command=self.send_message
        )
        self.send_button.pack(pady=5)

        self.entry.bind("<Return>", lambda event: self.send_message())

    def send_message(self):
        message = self.entry.get()

        if message.strip():
            self.chat_box.insert("end", f"{self.username}: {message}\n")
            self.chat_box.see("end")
            self.entry.delete(0, "end")

    def toggle_theme(self):
        current = ctk.get_appearance_mode()
        ctk.set_appearance_mode("light" if current == "dark" else "dark")


# ===================== ЛОГІН =====================
class LoginWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("LogiTalk - Вхід")
        self.geometry("300x200")

        self.configure(fg_color="#022c22")

        self.label = ctk.CTkLabel(
            self,
            text="Введіть ім'я",
            text_color="#bbf7d0"
        )
        self.label.pack(pady=15)

        self.username_entry = ctk.CTkEntry(
            self,
            placeholder_text="Ім'я користувача",
            fg_color="#064e3b",
            text_color="white"
        )
        self.username_entry.pack(pady=10)

        self.button = ctk.CTkButton(
            self,
            text="Увійти",
            fg_color=GREEN_MAIN,
            hover_color=GREEN_HOVER,
            command=self.login
        )
        self.button.pack(pady=10)

        self.username_entry.bind("<Return>", lambda event: self.login())

    def login(self):
        username = self.username_entry.get()

        if username.strip():
            self.destroy()
            app = ChatApp(username)
            app.mainloop()


# ===================== ЗАПУСК =====================
if __name__ == "__main__":
    login = LoginWindow()
    login.mainloop()

