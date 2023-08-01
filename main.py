import json
from colorama import Fore, Back, Style


import gpt
from functions import execute_python_code, mail_paper_copy_to
from print_helper import approve_indicator, assistant_indicator, error_indicator, print_function_args, print_function_result, user_indicator


conversation = []
function_set = {
    "execute_python_code": execute_python_code,
    "mail_paper_copy_to": mail_paper_copy_to,
}

while True:
    user_input = user_indicator()
    conversation.append({"role": "user", "content": user_input})
    response_message = gpt.call(conversation)

    assistant_indicator()
    while response_message.get("function_call"):
        try:
            function_name = response_message["function_call"]["name"]
            execute_function = function_set[function_name]
        except KeyError:
            conversation.append(
                {
                    "role": "function",
                    "name": function_name,
                    "content": "Function not found, please check the function name carefully.",
                }
            )
            error_indicator("Function not found: " + function_name)
            response_message = gpt.call(conversation)
            continue

        try:
            function_args = json.loads(
                response_message["function_call"]["arguments"])
        except json.decoder.JSONDecodeError:
            conversation.append(
                {
                    "role": "function",
                    "name": function_name,
                    "content": "Bad arguments format, please carefully pass the parameters with required format to function.",
                }
            )
            print(Fore.RED + Back.RESET + "\nBad arguments format:")
            print(Fore.RED + Back.RESET + '\t' +
                  response_message["function_call"]["arguments"])
            response_message = gpt.call(conversation)
            continue

        # trick to display the conversation of using the function
        print(Fore.YELLOW + Back.RESET + ' ' +
              function_args['information_to_user'])

        print_function_args(function_name, function_args)

        conversation.append(
            {"role": "assistant", "content": function_args['explanation']})
        conversation.append(
            {
                "role": response_message["role"],
                "name": response_message["function_call"]["name"],
                "content": response_message["function_call"]["arguments"],
            }
        )

        user_feedback = approve_indicator().strip()
        if user_feedback:
            conversation.append(
                {"role": "user", "content": user_feedback})
            response_message = gpt.call(conversation)

            continue

        function_response = execute_function(**function_args)
        print_function_result(function_response)

        conversation.append(
            {
                "role": "function",
                "name": function_name,
                "content": function_response,
            }
        )
        response_message = gpt.call(conversation)

    conversation.append(
        {"role": "assistant", "content": response_message['content']})

    print(Fore.YELLOW + Back.RESET + ' ' + response_message['content'])
    print()
