from .address_book_main import address_book_main_func, addressbook_hello
from .notes_main import notes_main_func, notes_hello
from .sort_main import sort_main_func
from rich import print as rprint
from abc import ABC, abstractmethod


TEXT_COLOR = {
    "red": "\033[31m",
    "green": "\033[32m",
    "reset": "\033[0m"
}


class CommandsOutputAbstract(ABC):
    @abstractmethod
    def hello(self):
        ...

    @abstractmethod
    def output(self):
        ...


class HelloABC(CommandsOutputAbstract):
    def hello(self):
        print("\nHi, I'm your personal helper!")

    def output(self):
        rprint("\nYou can run: \n-'addressbook'\n-'notebook' \n-'sorting_files *path*'\n\nOr close your personal helper by 'close' or 'exit'")
        choose_program_inp = input('\nChoose the program >>> ')
        return choose_program_inp
    

class NotesABC(CommandsOutputAbstract):
    def hello(self):
        notes_hello()

    def output(self):
        notes_main_func()


class AddressBookABC(CommandsOutputAbstract):
    def hello(self):
        addressbook_hello()

    def output(self):
        address_book_main_func()


class CommandsHandler:
    def __init__(self, command: CommandsOutputAbstract):
        self.output_message = command

    def greeting(self):
        self.output_message.hello()

    def send_message(self):
        x = self.output_message.output()
        return x


def main_func():
    first_command_output = HelloABC()

    command_output_hello = CommandsHandler(first_command_output)
    command_output_hello.greeting()

    while True:
        choose_program_inp = command_output_hello.send_message()
        input_split_list = choose_program_inp.split(' ')

        if choose_program_inp == 'addressbook':
            address_book = AddressBookABC()
            command_output_addressbook = CommandsHandler(address_book)
            command_output_addressbook.greeting()
            command_output_addressbook.send_message()
        
        elif choose_program_inp == 'notebook':
            notes = NotesABC()
            command_output_notes = CommandsHandler(notes)
            command_output_notes.greeting()
            command_output_notes.send_message()

        elif input_split_list[0] == 'sorting_files':
            try:
                arg = input_split_list[1]
                confirm_input = input(TEXT_COLOR['red'] + f"\nAre you sure you want to sort all the files in ({arg}) path !? \n(y/n) >>> " + TEXT_COLOR['reset'])
                if confirm_input.lower() == 'y':
                    sort_main_func(arg)
                elif confirm_input.lower() == 'n':
                    print('\nOk')
                else:
                    print(TEXT_COLOR['red'] + '\nIncorrect input!\n' + TEXT_COLOR['reset'])
            except IndexError:
                print(TEXT_COLOR['red'] + "\nTo sort files in folder you need to write 'sorting_files *path*'\n" + TEXT_COLOR["reset"])
        
        elif choose_program_inp in ['close', 'exit']:
            print('\nGood bye!')
            break
        
        else:
            print(TEXT_COLOR['red'] + 'Incorrect command!'+ TEXT_COLOR['reset'])


if __name__ == "__main__":
    main_func()