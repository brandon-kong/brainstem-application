from utils.printer import Printer


class InputUtility:
    @staticmethod
    def get_int_input(prompt: str) -> int:
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                Printer.error("Invalid input. Please enter an integer.")

    @staticmethod
    def get_float_input(prompt: str) -> float:
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                Printer.error("Invalid input. Please enter a number.")

    @staticmethod
    def get_string_input(prompt: str) -> str:
        return input(prompt)

    @staticmethod
    def get_bool_input(prompt: str) -> bool:
        while True:
            try:
                return bool(input(prompt))
            except ValueError:
                Printer.error("Invalid input. Please enter a boolean value.")

    @staticmethod
    def get_yes_no_input(prompt: str) -> bool:
        prompt += " (y/n): "
        while True:
            try:
                inp = input(prompt).lower().strip()
                print()
                if inp in ['y', 'yes']:
                    return True
                elif inp in ['n', 'no']:
                    return False
                else:
                    raise ValueError
            except ValueError:
                Printer.error("Invalid input. Please enter 'y' or 'n'.\n")

    def get_comma_separated_string_input(prompt: str, valid_values: list = None) -> list:
        while True:
            inp = input(prompt).split(',')
            inp = [x.strip() for x in inp]
            if valid_values is not None:
                if all([x in valid_values for x in inp]):
                    return inp
                else:
                    Printer.error(f"Invalid input. Please enter a comma-separated list of values from {valid_values}.\n")
            else:
                return inp