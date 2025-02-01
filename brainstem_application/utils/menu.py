from typing import Dict, Callable

from utils.printer import Printer, Color

type Options = Dict[str, Callable[[], None]]

class Menu:
    """
    The Menu class provides a way to create a menu that allows the user to select an option from a list of options.
    Ensure that the options are a dictionary where the key is the option and the value is the action to be performed.
    The key should be a string that also describes the action to be performed.

    Example:

    ```python
    options = {
        'Perform K-means clustering': lambda: print('Performing K-means clustering'),
        'Perform PCA': lambda: print('Performing PCA'),
        'Perform t-SNE': lambda: print('Performing t-SNE'),
    }

    menu = Menu(options)

    menu.run()
    ```

    """

    def __init__(
        self,
        options: Options,
        start_message: str = "Please select an option from the menu below:",
        include_exit: bool = False,
        include_back: bool = True,
        stop_on_selection: bool = False,
        max_page_size: int = 10,
    ):

        self.options = options
        self.start_message = start_message
        self.include_exit = include_exit
        self.include_back = include_back
        self.stop_on_selection = stop_on_selection
        self.stopped = False
        self.max_page_size = max_page_size
        self.current_page = 0

    def run(self):
        while True and not self.stopped:
            Printer.print(f"\n{self.start_message}\n")

            if self.include_exit:
                self.options["Exit"] = lambda: "back"

            if self.include_back:
                self.options["Back"] = lambda: "back"

            options_list = list(self.options.keys())
            total_pages = (len(options_list) + self.max_page_size - 1) // self.max_page_size if self.max_page_size > 0 else 1

            if self.max_page_size > 0:
                start_index = self.current_page * self.max_page_size
                end_index = start_index + self.max_page_size
                paginated_options = options_list[start_index:end_index]
            else:
                paginated_options = options_list

            for i, option in enumerate(paginated_options):
                if option == "Back":
                    Printer.custom(f"[back] {option}", color=Color.YELLOW)
                elif option == "Exit":
                    Printer.custom(f"[exit] {option}", color=Color.RED)
                else:
                    Printer.print(f"[{i + 1}] {option}")

            if self.max_page_size > 0 and total_pages > 1:
                Printer.print(f"\nPage {self.current_page + 1} of {total_pages}")
                Printer.print("Enter 'n' for next page, 'p' for previous page, or select an option.")

            # Print an extra line
            print()

            choice = input("Enter your choice: ")

            if choice.lower() == "exit" and self.include_exit:
                break

            if choice.lower() == "back" and self.include_back:
                return

            if self.max_page_size > 0 and total_pages > 1:
                if choice.lower() == 'n':
                    self.current_page = (self.current_page + 1) % total_pages
                    continue
                elif choice.lower() == 'p':
                    self.current_page = (self.current_page - 1) % total_pages
                    continue

            # Check if the choice is a number
            if not choice.isdigit():
                Printer.error("Invalid option")
                continue

            choice = int(choice) - 1

            if choice < 0 or choice >= len(paginated_options):
                Printer.error("Invalid option")
                continue

            selected_option = paginated_options[choice]
            action = self.options.get(selected_option)

            if action:
                action()
                if self.stop_on_selection:
                    return
            else:
                Printer.error("Invalid option")

    def stop(self):
        self.stopped = True