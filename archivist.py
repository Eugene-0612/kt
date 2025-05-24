import tkinter as tk
from tkinter import ttk, font, filedialog
from PIL import Image, ImageTk
import sys

class ArchivistApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Archivist - Домашняя Библиотека")
        self.root.geometry("700x500")
        # Размеры окна не фиксированы, пользователь может изменять
        self.root.resizable(False, False)  # Запрет изменения размеров главного окна

        # Центрирование основного окна
        self.center_window(self.root, 700, 500)

        # Иконка программы (замените 'book_icon.ico' на путь к вашей иконке)
        try:
            self.root.iconbitmap("book_icon.ico")  # Поместите icon.ico в ту же папку, что и скрипт
        except:
            pass # Если иконка не найдена, не выводим ошибку
            #print("Фоновое изображение не найдено, убедитесь что файл 'icon.ico' находиться в папке с программой")

        self.setup_ui()

    def setup_ui(self):
        # === Настройка стилей (цвета, шрифты и т.д.) ===
        self.bg_color = "#f0f0f0"  # Цвет фона (можно изменить)
        self.button_color = "#4CAF50"  # Цвет кнопок (можно изменить)
        self.button_hover_color = "#367C39" # Цвет кнопок при наведении
        self.text_color = "#000000" # Цвет текста
        self.font_family = "Arial"  # Шрифт (можно изменить)
        self.font_size = 12  # Размер шрифта (можно изменить)

        self.default_font = font.Font(family=self.font_family, size=self.font_size)

        self.root.configure(bg=self.bg_color) # Устанавливаем цвет фона окна

        # === Кнопки ===
        self.button_frame = tk.Frame(self.root, bg=self.bg_color)  # Фрейм для кнопок
        self.button_frame.pack(pady=30)

        self.add_book_button = tk.Button(self.button_frame, text="Добавить книгу", font=self.default_font, bg=self.button_color, fg="white", activebackground=self.button_hover_color, relief=tk.FLAT, padx=20, pady=10, bd=0, highlightthickness=0, command=self.open_add_book_window) # Добавлено command
        self.add_book_button.pack(side=tk.LEFT, padx=10)
        self.add_book_button.bind("<Enter>", lambda event: self.add_book_button.config(bg=self.button_hover_color))
        self.add_book_button.bind("<Leave>", lambda event: self.add_book_button.config(bg=self.button_color))

        self.list_books_button = tk.Button(self.button_frame, text="Список книг", font=self.default_font, bg=self.button_color, fg="white", activebackground=self.button_hover_color, relief=tk.FLAT, padx=20, pady=10, bd=0, highlightthickness=0)
        self.list_books_button.pack(side=tk.LEFT, padx=10)
        self.list_books_button.bind("<Enter>", lambda event: self.list_books_button.config(bg=self.button_hover_color))
        self.list_books_button.bind("<Leave>", lambda event: self.list_books_button.config(bg=self.button_color))

        self.help_button = tk.Button(self.button_frame, text="Справка", font=self.default_font, bg=self.button_color, fg="white", activebackground=self.button_hover_color, relief=tk.FLAT, padx=20, pady=10, bd=0, highlightthickness=0)
        self.help_button.pack(side=tk.LEFT, padx=10)
        self.help_button.bind("<Enter>", lambda event: self.help_button.config(bg=self.button_hover_color))
        self.help_button.bind("<Leave>", lambda event: self.help_button.config(bg=self.button_color))


        # === Фон или изображение ===
        #  Попробуйте загрузить изображение, если его нет, будет просто фон
        try:
            self.bg_image = Image.open("archivist.png")  # Замените 'background.jpg' на путь к вашему изображению
            self.bg_image = ImageTk.PhotoImage(self.bg_image)
            self.bg_label = tk.Label(self.root, image=self.bg_image)
            self.bg_label.place(x=0, y=100, relwidth=1, relheight=1) # покрывает всю оставшуюся часть окна
        except:
            # Если картинка не загрузилась, ничего не делаем. Будет просто фон окна
            pass
            #print("Фоновое изображение не найдено, убедитесь что файл 'icon.ico' находиться в папке с программой")

    def center_window(self, window, width, height):
        """Центрирует окно на экране."""
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        window.geometry(f"{width}x{height}+{x}+{y}")

    def open_add_book_window(self):
        """Открывает окно 'Добавить книгу'."""
        self.add_book_window = Second_window(self.root)  # Создаем экземпляр Second_window
        self.add_book_window.title("Добавить книгу")
        w = ((self.root.winfo_screenwidth() // 2) - 200)  # Изменено для вашей ширины
        h = ((self.root.winfo_screenheight() // 2) - 275)  # Изменено для вашей высоты
        self.add_book_window.geometry('400x550+{}+{}'.format(w, h))  # Размеры и положение
        self.add_book_window.resizable(False, False)
        #self.add_book_window.focus_force()
        self.add_book_window.attributes("-topmost", True) # попробуйте и этот вариант

    def clear_fields(self):
        """Очищает поля ввода."""
        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.genre_entry.delete(0, tk.END)
        self.binding_entry.delete(0, tk.END)
        self.year_entry.delete(0, tk.END)
        self.publisher_entry.delete(0, tk.END)
        self.description_text.delete("1.0", tk.END) # Очистка Text виджета
        self.image_path.set("") # Очистка пути к изображению

    def select_image(self):
        """Открывает диалог выбора изображения."""
        self.add_book_window.attributes("-topmost", False)  # Отключаем topmost перед открытием диалога
        self.add_book_window.withdraw()  # Скрываем окно
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")]
        )
        if file_path:
            self.image_path.set(file_path)  # Сохраняем путь к изображению
        self.add_book_window.deiconify()  # Показываем окно обратно
        self.add_book_window.attributes("-topmost", True)  # Включаем topmost после закрытия диалога
        self.add_book_window.focus_force() # Возвращаем фокус
    

class Second_window(tk.Toplevel):
    def __init__(self, master=None, *args, **kwargs):  # Добавлен параметр master
        tk.Toplevel.__init__(self, master, *args, **kwargs) # Передаем master в tk.Toplevel
        self.master = master # Сохраняем ссылку на родительское окно
        self.title("Добавить книгу")
        w = ((self.winfo_screenwidth() // 2) - 200)  # Изменено для вашей ширины
        h = ((self.winfo_screenheight() // 2) - 275)  # Изменено для вашей высоты
        self.geometry('400x550+{}+{}'.format(w, h))
        self.resizable(False, False)
        self.attributes("-topmost", True) # Включаем topmost по умолчанию

        # === Добавление полей ввода ===
        # Название книги
        title_label = tk.Label(self, text="Название книги:", anchor="w")
        title_label.pack(pady=(10,2), padx=10, fill="x") # Отступ сверху больше
        self.title_entry = tk.Entry(self)
        self.title_entry.pack(pady=(0,5), padx=10, fill="x")

        # Автор
        author_label = tk.Label(self, text="Автор:", anchor="w")
        author_label.pack(pady=(5,2), padx=10, fill="x")
        self.author_entry = tk.Entry(self)
        self.author_entry.pack(pady=(0,5), padx=10, fill="x")

        # Жанр
        genre_label = tk.Label(self, text="Жанр:", anchor="w")
        genre_label.pack(pady=(5,2), padx=10, fill="x")
        self.genre_entry = tk.Entry(self)
        self.genre_entry.pack(pady=(0,5), padx=10, fill="x")

        # Переплет
        binding_label = tk.Label(self, text="Переплет:", anchor="w")
        binding_label.pack(pady=(5,2), padx=10, fill="x")
        self.binding_entry = tk.Entry(self)
        self.binding_entry.pack(pady=(0,5), padx=10, fill="x")

        # Год издания
        year_label = tk.Label(self, text="Год издания:", anchor="w")
        year_label.pack(pady=(5,2), padx=10, fill="x")
        self.year_entry = tk.Entry(self)
        self.year_entry.pack(pady=(0,5), padx=10, fill="x")

        # Издательство
        publisher_label = tk.Label(self, text="Издательство:", anchor="w")
        publisher_label.pack(pady=(5,2), padx=10, fill="x")
        self.publisher_entry = tk.Entry(self)
        self.publisher_entry.pack(pady=(0,5), padx=10, fill="x")

        # Краткое описание (используем Text)
        description_label = tk.Label(self, text="Краткое описание:", anchor="w")
        description_label.pack(pady=(5,2), padx=10, fill="x")
        self.description_text = tk.Text(self, height=5) # Высота текстового поля
        self.description_text.pack(pady=(0,5), padx=10, fill="x")
        self.description_text.insert("1.0", "")  # Начальный текст (пусто)

        # Добавить изображение (пока просто метка)
        image_label = tk.Label(self, text="Добавить изображение:", anchor="w")
        image_label.pack(pady=(5,2), padx=10, fill="x")
        self.image_path = tk.StringVar() # Для хранения пути к изображению
        self.image_button = tk.Button(self, text="Выбрать изображение", command=self.select_image) # Кнопка выбора изображения, command
        self.image_button.pack(pady=(0,5), padx=10, fill="x")
        self.image_label = tk.Label(self, textvariable=self.image_path, wraplength=380) # Метка для отображения пути к файлу
        self.image_label.pack(pady=(0,5), padx=10, fill="x")

        # === Кнопка "Сохранить" ===
        self.save_button = tk.Button(self, text="Сохранить", command=self.clear_fields) # Привязка к функции clear_fields
        self.save_button.pack(pady=20)
        #self.save_button.place(relx=0.5, rely=0.95, anchor=tk.CENTER) # Размещение по центру внизу

    def clear_fields(self):
        """Очищает поля ввода."""
        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.genre_entry.delete(0, tk.END)
        self.binding_entry.delete(0, tk.END)
        self.year_entry.delete(0, tk.END)
        self.publisher_entry.delete(0, tk.END)
        self.description_text.delete("1.0", tk.END) # Очистка Text виджета
        self.image_path.set("") # Очистка пути к изображению

    def select_image(self):
        """Открывает диалог выбора изображения."""
        self.attributes("-topmost", False)  # Отключаем topmost перед открытием диалога
        self.withdraw()  # Скрываем окно
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")]
        )
        if file_path:
            self.image_path.set(file_path)  # Сохраняем путь к изображению
        self.deiconify()  # Показываем окно обратно
        self.attributes("-topmost", True)  # Включаем topmost после закрытия диалога
        self.focus_force() # Возвращаем фокус

if __name__ == "__main__":
    root = tk.Tk()
    app = ArchivistApp(root)
    root.mainloop()