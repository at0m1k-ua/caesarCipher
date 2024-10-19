import tkinter as tk
from tkinter import messagebox, filedialog

from Alphabet import Alphabet
from CaesarCipher import CaesarCipher


class CaesarCipherApp(tk.Tk):
    def __init__(self, alphabet_path):
        super().__init__()
        self.title("Шифр Цезаря")
        self.geometry("600x400")

        self.alphabet = Alphabet.load_from_json(alphabet_path)
        self.cipher = CaesarCipher(self.alphabet)

        self.text_area = tk.Text(self, wrap='word', height=15)
        self.text_area.pack(expand=True, fill='both')

        self.key_label = tk.Label(self, text="Ключ шифру (число):")
        self.key_label.pack(pady=5)
        self.key_entry = tk.Entry(self)
        self.key_entry.pack(pady=5)

        self.encrypt_button = tk.Button(self, text="Шифрувати", command=self.encrypt_file)
        self.decrypt_button = tk.Button(self, text="Розшифрувати", command=self.decrypt_file)
        self.encrypt_button.pack(side=tk.LEFT, padx=10, pady=10)
        self.decrypt_button.pack(side=tk.LEFT, padx=10, pady=10)

        menu_bar = tk.Menu(self)
        self.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Файл", menu=file_menu)
        file_menu.add_command(label="Створити", command=self.create_file)
        file_menu.add_command(label="Відкрити", command=self.open_file)
        file_menu.add_command(label="Зберегти", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Вихід", command=self.quit_app)

        help_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Довідка", menu=help_menu)
        help_menu.add_command(label="Про програму", command=self.about)

        self.current_file = None

    def create_file(self):
        self.text_area.delete(1.0, tk.END)
        self.current_file = None
        messagebox.showinfo("Створити", "Новий файл створено.")

    def open_file(self):
        file_path = filedialog.askopenfilename(
            title="Відкрити файл",
            filetypes=(("Текстові файли", "*.txt"), ("Усі файли", "*.*"))
        )
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                file_content = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, file_content)
                self.current_file = file_path
            messagebox.showinfo("Відкрити", f"Файл відкрито: {file_path}")

    def save_file(self):
        if self.current_file:
            file_content = self.text_area.get(1.0, tk.END)
            with open(self.current_file, 'w', encoding='utf-8') as file:
                file.write(file_content)
            messagebox.showinfo("Зберегти", f"Файл збережено: {self.current_file}")
        else:
            self.save_file_as()

    def save_file_as(self):
        file_path = filedialog.asksaveasfilename(
            title="Зберегти файл як",
            defaultextension=".txt",
            filetypes=(("Текстові файли", "*.txt"), ("Усі файли", "*.*"))
        )
        if file_path:
            file_content = self.text_area.get(1.0, tk.END)
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(file_content)
            self.current_file = file_path
            messagebox.showinfo("Зберегти", f"Файл збережено: {file_path}")

    def encrypt_file(self):
        try:
            key = int(self.key_entry.get())
            plaintext = self.text_area.get(1.0, tk.END).strip()
            ciphertext = self.cipher.encrypt(plaintext, key)
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, ciphertext)
            messagebox.showinfo("Шифрування", "Текст зашифровано.")
        except ValueError:
            messagebox.showerror("Помилка", "Будь ласка, введіть правильне число для ключа.")

    def decrypt_file(self):
        try:
            key = int(self.key_entry.get())
            ciphertext = self.text_area.get(1.0, tk.END).strip()
            plaintext = self.cipher.decrypt(ciphertext, key)
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, plaintext)
            messagebox.showinfo("Розшифрування", "Текст розшифровано.")
        except ValueError:
            messagebox.showerror("Помилка", "Будь ласка, введіть правильне число для ключа.")

    def about(self):
        messagebox.showinfo("Про програму",
                            "Ця програма реалізує шифр Цезаря.\n"
                            "Ви можете зашифрувати або розшифрувати текст, використовуючи числовий ключ.\n"
                            "Розробник: Іван Куруч")

    def quit_app(self):
        self.quit()
