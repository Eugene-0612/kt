import tkinter as tk
from tkinter import ttk, font
from PIL import Image, ImageTk

class ArchivistApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Archivist - Домашняя Библиотека")
        self.root.geometry("700x500")
        # Размеры окна не фиксированы, пользователь может изменять

        # Иконка программы (замените 'icon.ico' на путь к вашей иконке)
        try:
            self.root.iconbitmap("icon.ico")  # Поместите icon.ico в ту же папку, что и скрипт
        except:
            pass # Если иконка не найдена, не выводим ошибку
            #print("Иконка не найдена, убедитесь что файл 'icon.ico' находиться в папке с программой")

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

        # === Заголовок ===
        #self.title_label = tk.Label(self.root, text="Archivist - Домашняя Библиотека", font=(self.font_family, 16, "bold"), bg=self.bg_color, fg=self.text_color) # fg=self.text_color - цвет текста
        #self.title_label.pack(pady=5)  # Отступ сверху и снизу

        # === Кнопки ===
        self.button_frame = tk.Frame(self.root, bg=self.bg_color)  # Фрейм для кнопок
        self.button_frame.pack(pady=30)

        self.add_book_button = tk.Button(self.button_frame, text="Добавить книгу", font=self.default_font, bg=self.button_color, fg="white", activebackground=self.button_hover_color, relief=tk.FLAT, padx=20, pady=10, bd=0, highlightthickness=0)
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
            #print("Фоновое изображение не найдено, используеться цвет фона")


if __name__ == "__main__":
    root = tk.Tk()
    app = ArchivistApp(root)
    root.mainloop()