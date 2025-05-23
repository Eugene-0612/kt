import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import os

class AddBookWindow:
    def __init__(self, master):
        self.master = master
        master.title("Добавить книгу")
        try:  # Добавлено try-except для обработки ошибки загрузки иконки
            master.iconbitmap("book_icon.ico")
        except tk.TclError:
            print("Не удалось загрузить иконку 'book_icon.ico'")

        self.create_widgets()

    def create_widgets(self):
        labels = ["Автор", "Название", "Жанр", "Переплет", "Год издания", "Издательство", "Краткое описание", "Изображение"]
        self.add_book_entries = {}

        for i, label_text in enumerate(labels):
            label = tk.Label(self.master, text=label_text, anchor="w", width=15)
            label.grid(row=i, column=0, padx=5, pady=5, sticky="w")

            if label_text == "Краткое описание":
                self.text_description = tk.Text(self.master, height=4, width=30)  # Сохраняем ссылку на Text
                self.text_description.grid(row=i, column=1, padx=5, pady=5, sticky="w")
            elif label_text == "Изображение":
                entry = tk.Entry(self.master, width=30)
                browse_button = tk.Button(self.master, text="Обзор", command=self.browse_image)
                browse_button.grid(row=i, column=2, padx=5, pady=5, sticky="w")
            else:
                entry = tk.Entry(self.master, width=30)

            entry.grid(row=i, column=1, padx=5, pady=5, sticky="w")
            self.add_book_entries[label_text] = entry

        # Привязка клавиш после создания виджетов
        if hasattr(self, 'text_description'):
            self.text_description.bind("<Control-v>", self.paste_from_clipboard)  # Для Windows/Linux
            self.text_description.bind("<Command-v>", self.paste_from_clipboard)  # Для macOS
            self.text_description.focus_set() # Устанавливаем фокус на поле

    def browse_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
        if file_path:
            self.add_book_entries["Изображение"].delete(0, tk.END)
            self.add_book_entries["Изображение"].insert(0, file_path)

    def save_book(self):
        book_data = {}
        for label, entry in self.add_book_entries.items():
            if label == "Краткое описание":
                book_data[label] = self.text_description.get("1.0", tk.END).strip() # Используем self.text_description
            else:
                book_data[label] = entry.get()

        print("Данные книги:", book_data)

        for entry in self.add_book_entries.values():
            if isinstance(entry, tk.Text):
                entry.delete("1.0", tk.END)
            else:
                entry.delete(0, tk.END)

    def paste_from_clipboard(self, event):
        try:
            text = self.master.clipboard_get()
            self.master.clipboard_append(text) # Добавляем текст во временный буфер
            self.text_description.event_generate("<<Paste>>") # Генерируем событие вставки
            self.master.clipboard_clear() # Очищаем временный буфер
        except tk.TclError:
            # Буфер обмена пуст или содержит нетекстовые данные
            print("Буфер обмена пуст или содержит нетекстовые данные")  # Выводим сообщение в консоль
        except Exception as e:
            print(f"Ошибка при вставке из буфера обмена: {e}")  # Выводим сообщение об ошибке


class Archivist:
    def __init__(self, master):
        self.master = master
        master.title("Archivist")
        try: # Добавлено try-except для обработки ошибки загрузки иконки
            master.iconbitmap("book_icon.ico")
        except tk.TclError:
            print("Не удалось загрузить иконку 'book_icon.ico'")

        master.geometry("700x400")
        self.bg_color = "lightgray"
        master.configure(bg=self.bg_color)
        self.background_image = None
        self.tab_color = "lightgray"
        self.tab_font = ("Arial", 10, "bold")
        self.create_widgets()
        master.bind("<Configure>", self.resize_background)

    def create_widgets(self):
        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack(padx=0, pady=(3, 3), fill="x")

        style = ttk.Style()
        style.theme_use('default')
        style.configure("TNotebook", background=self.bg_color, borderwidth=0)
        style.configure("TNotebook.Tab", background=self.tab_color, borderwidth=0, font=self.tab_font)
        style.map("TNotebook.Tab", background=[("selected", self.bg_color)])

        self.add_book_tab = ttk.Frame(self.notebook)
        self.book_list_tab = ttk.Frame(self.notebook)
        self.about_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.add_book_tab, text="Добавить книгу")
        self.notebook.add(self.book_list_tab, text="Список книг")
        self.notebook.add(self.about_tab, text="Об авторе")
        self.notebook.select(self.book_list_tab)

        # Получаем индекс вкладки "Добавить книгу"
        self.add_book_tab_index = self.notebook.index(self.add_book_tab)

        # Используем <<NotebookTabChanged>> event
        self.notebook.bind("<<NotebookTabChanged>>", self.open_add_book_window)

        self.background_frame = tk.Frame(self.master, bg=self.bg_color)
        self.background_frame.pack(fill="both", expand=True)

        self.background_label = tk.Label(self.background_frame, bd=0)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.create_background()

    def create_background(self):
        try:
            self.original_image = Image.open("archivist.png")
            self.resize_background()
        except FileNotFoundError:
            print("Файл 'archivist.png' не найден. Будет использоваться только цвет фона.")
        except Exception as e:
            print(f"Ошибка при загрузке изображения: {e}")

    def resize_background(self, event=None):
        width = self.background_frame.winfo_width()
        height = self.background_frame.winfo_height()

        if width > 0 and height > 0 and hasattr(self, 'original_image'):
            resized_image = self.original_image.resize((width, height), Image.LANCZOS)
            self.background_image = ImageTk.PhotoImage(resized_image)
            self.background_label.config(image=self.background_image)

    def open_add_book_window(self, event):
        # Получаем индекс текущей вкладки
        current_tab_index = self.notebook.index("current")
        # Сравниваем с индексом вкладки "Добавить книгу"
        if current_tab_index == self.add_book_tab_index:
            add_book_window = tk.Toplevel(self.master)
            AddBookWindow(add_book_window)

if __name__ == "__main__":
    root = tk.Tk()
    app = Archivist(root)
    root.mainloop()