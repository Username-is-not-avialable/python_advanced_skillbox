import sys
from mod7.task1_2 import utils
import logging
import logging.config

calc_logger = logging.getLogger("calc_logger")

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
        calc_logger.info(f"Неправильная команда. Выражение должно содержать 3 операнда, получено: {len(command_split)}")
        return None
    number_1 = float(command_split[0])
    number_2 = float(command_split[2])
    operation = command_split[1]    
    return number_1, number_2, operation


def get_result(command: tuple[float, float, str] | None) -> str:    
    if command is None:
        return "Вы ввели не корректную строку, повторите попытку."
    number_1, number_2, operation = command    
    result: float = utils.calculate(number_1, number_2, operation)
    return str(result)


def give_result_to_user(result: str) -> None:    
    print(result)

def configure_logger(logger: logging.Logger):
    formatter = logging.Formatter("%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s")
    level_handler = CustomHandler()
    level_handler.setFormatter(formatter)
    logger.addHandler(level_handler)
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout, format="%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s")


class CustomHandler(logging.Handler):
    def __init__(self, mode='a'):
        super().__init__()
        self.mode = mode

    def emit(self, record: logging.LogRecord) -> None:
        message = self.format(record)
        loger_name:str = record.name
        loger_level:str = str.lower(record.levelname)
        output_file:str = f"{loger_name}_{loger_level}.log"

        with open(output_file, mode=self.mode) as f:
            f.write(message + '\n')


if __name__ == '__main__':
    configure_logger(calc_logger)
    show_list_of_commands()
    while True:
        command: str = get_command_from_user()
        processed_command = process_command(command)
        result: str = get_result(processed_command)
        give_result_to_user(result)
