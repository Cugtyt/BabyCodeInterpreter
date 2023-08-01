from colorama import Fore, Back, Style


def user_indicator(message=None):
    print(Fore.GREEN + Back.LIGHTYELLOW_EX + "You |>", end="")
    if message:
        print(Fore.GREEN + Back.RESET + " " + message, end="")
    return input(Fore.GREEN + Back.RESET + ' ')


def assistant_indicator():
    print(Fore.YELLOW + Back.LIGHTBLUE_EX + "Assistant |>", end="")


def error_indicator(message):
    print(Fore.RED + Back.RESET + "Error |> " + message)


def approve_indicator():
    print(Fore.GREEN + Back.RESET +
          "Press 'ENTER' to approve or give feedback: ", end="")
    print(Fore.GREEN + Back.LIGHTYELLOW_EX + "|>", end="")
    return input(Fore.GREEN + Back.RESET + ' ')


def print_function_args(function, args):
    print(Fore.CYAN + f'{"=" * 80}\nFunction: {function}')
    # print(Fore.CYAN + f'Arguments:')
    # for key, value in args.items():
    #     value = value if '\n' not in value else '\n' + \
    #         '-' * 60 + '\n' + value + '\n' + '-' * 60
    #     print(Fore.CYAN + f'\t{key}: {value}')
    print(Fore.CYAN + f'{"=" * 80}')


def print_function_result(result):
    print(Fore.CYAN + f'{"=" * 80}')
    print(Fore.CYAN + f'Result:')
    print(Fore.CYAN + f'\t{result}')
    print(Fore.CYAN + f'{"=" * 80}')
