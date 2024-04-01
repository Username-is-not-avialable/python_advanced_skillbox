from mod7.task1 import utils
import logging

calculator_logger = logging.getLogger("calculator_logger")

def show_list_of_commands() -> None:
    print("Доступные команды:\n"
          "\"+\" - сложение\n"
          "\"-\" - вычитание\n"
          "\"*\" - умножение\n"
          "\"/\" - деление\n"
          "\"^\" - возведение в степень\n")


def get_command_from_user() -> str:    
    command: str = input("Введите выражение с пробелами: ")    
    return command


def process_command(command: str) -> tuple[float, float, str] | None:    
    command_split: [str] = command.split()
    if len(command_split) != 3:
        calculator_logger.info(f"Неправильная команда. Выражение должно содержать 3 операнда, получено: {len(command_split)}")
        return None
    number_1 = float(command_split[0])
    number_2 = float(command_split[2])
    operation = command_split[1]    
    return number_1, number_2, operation


def get_result(command: tuple[float, float, str] | None) -> str:    
    if command is None:
        calculator_logger.info("Введена некорректная команада")
        return "Вы ввели не корректную строку, повторите попытку."
    number_1, number_2, operation = command    
    result: float = utils.calculate(number_1, number_2, operation)
    return str(result)


def give_result_to_user(result: str) -> None:    
    print(result)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    show_list_of_commands()
    while True:
        command: str = get_command_from_user()
        processed_command = process_command(command)
        result: str = get_result(processed_command)
        give_result_to_user(result)
