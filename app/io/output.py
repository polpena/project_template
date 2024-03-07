def output_text_to_console(text):
    """
    Функція для виводу тексту у консоль.

    Args:
        text (str): Текст для виводу.
    """
    print(text)

def write_to_file(file_path, content):
    """
    Функція для запису до файлу за допомогою вбудованих можливостей Python.

    Args:
        file_path (str): Шлях до файлу.
        content (str): Вміст для запису до файлу.
    """
    with open(file_path, 'w') as file:
        file.write(content)

def write_to_file_with_pandas(file_path, dataframe):
    """
    Функція для запису до файлу за допомогою бібліотеки pandas.

    Args:
        file_path (str): Шлях до файлу.
        dataframe (pandas.DataFrame): DataFrame для запису до файлу.
    """
    try:
        import pandas as pd
        dataframe.to_csv(file_path, index=False)  # Якщо хочемо записати у форматі CSV
    except ImportError:
        print("Пакет pandas не знайдено. Будь ласка, встановіть його перед використанням цієї функції.")
