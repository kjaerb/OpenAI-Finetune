import os
import openai
import inquirer

openai.api_key = os.getenv("OPENAI_API_KEY")

openai_finetune_list = openai.FineTune.list()

finetune_ids = []
for item in openai_finetune_list['data']:
    result = {
        'id': item['id'],
        'model': item['model'],
    }
    finetune_ids.append(result)

cancelable_ids = []
for item in openai_finetune_list['data']:
    if item["status"] == "pending":
        cancelable_ids.append(item["id"])

command_question = [
    inquirer.List("command",
                  message="Select command to run",
                  choices=["Create model", "Retreive model", "Cancel model tune", "Delete model",
                           "Get org ID", "List event of model", "Get list of models", "Exit"]
                  ),
]

finetune_id_question = [
    inquirer.List("finetune_id",
                  message="Select ID of a model",
                  choices=finetune_ids
                  )
]

finetune_id_cancel_question = [
    inquirer.List("cancel_id",
                  message="Select ID for model to cancel training",
                  choices=cancelable_ids
                  )
]

delete_fine_tune_question = [
    inquirer.List("delete_id",
                  message="Select ID for model to delete",
                  choices=finetune_ids
                  )
]

while True:
    answer = inquirer.prompt(command_question)
    command = answer["command"]

    if command == "Create model":
        pass
    elif command == "Retreive model":
        finetune_id = inquirer.prompt(finetune_id_question)[
            "finetune_id"]["id"]
        print(openai.FineTune.retrieve(id=finetune_id))
    elif command == "Cancel model tune":
        cancel_id = inquirer.prompt(finetune_id_cancel_question)["cancel_id"]
        print(openai.FineTune.cancel(id=cancel_id))
    elif command == "Get org ID":
        org_ids = set()
        for item in openai_finetune_list['data']:
            org_ids.add(item["organization_id"])
        print(org_ids)

    elif command == "List event of model":
        finetune_id = inquirer.prompt(finetune_id_question)[
            "finetune_id"]["id"]
        print(openai.FineTune.retrieve(id=finetune_id))
    elif command == "Get list of models":
        for id in finetune_ids:
            print(id)
    elif command == "Delete model":
        delete_id = inquirer.prompt(delete_fine_tune_question)[
            "delete_id"]["id"]
        are_you_sure_input = input(
            "Are you sure you want to delete the model? [Y/n]")
        if are_you_sure_input == "Y" or are_you_sure_input == "y":
            print(openai.FineTune.delete(id=delete_id))
        else:
            break
    elif command == "Exit":
        exit(0)
    else:
        print("Command not recognized")
