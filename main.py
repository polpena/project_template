import app.io.input as input
import app.io.output as output 

def main():
    # Виклик функцій для вводу тексту з консолі та виводу його у консоль
    text_from_console = input.input_text_from_console()
    output.output_text_to_console(text_from_console)

    # Виклик функцій для зчитування з файлу та запису в файл за допомогою вбудованих можливостей Python
    file_content = input.read_from_file('data/example.txt')
    output.write_to_file('output.txt', file_content)

    # Виклик функцій для зчитування з файлу та запису в файл за допомогою бібліотеки pandas
    dataframe = input.read_from_file_with_pandas('data/example.csv')
    output.write_to_file_with_pandas('output.csv', dataframe)

if __name__ == "__main__":
    main()
