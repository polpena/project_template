def input_text_from_console():
    """
    Функція для вводу тексту з консолі.

    Returns:
        str: Введений текст.
    """
    text = input("Введіть текст: ")
    return text

def read_from_file(file_path):
    """
    Функція для зчитування з файлу за допомогою вбудованих можливостей Python.

    Args:
        file_path (str): Шлях до файлу.

    Returns:
        str: Вміст файлу.
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"Файл '{file_path}' не знайдено.")
        return None

def read_from_file_with_pandas(file_path):
    """
    Функція для зчитування з файлу за допомогою бібліотеки pandas.

    Args:
        file_path (str): Шлях до файлу.

    Returns:
        pandas.DataFrame or None: Зміст файлу у вигляді DataFrame або None, якщо файл не знайдено.
    """
    try:
        import pandas as pd
        df = pd.read_csv(file_path)  # Якщо файл має формат CSV
        return df
    except FileNotFoundError:
        print(f"Файл '{file_path}' не знайдено.")
        return None
