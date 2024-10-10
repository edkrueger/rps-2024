import random

def check_result(human_choice, ai_choice):

    human_choice = human_choice.lower()

    if human_choice == ai_choice:
        return "tie"
    
    elif (ai_choice == "r" and human_choice == "p") or \
        (ai_choice == "p" and human_choice == "s") or \
        (ai_choice == "s" and human_choice == "r"):
        return "human"
    
    else:
        return "ai"
    
def is_valid(choice):

    if choice == None:
        return False
    if not choice.lower() in {"r", "p", "s"}:
        return False
    return True

def prompt_choice():

    choice = None

    while not is_valid(choice):
        choice = input("Choose r/p/s! ")

    return choice
  
def prompt_ai():
    options = ["r", "p", "s"]
    choice = random.choice(options)
    return choice

def play():
    
    ai_choice = prompt_ai()
    human_choice = prompt_choice()

    print(f"Computer chose {ai_choice}")

    result = check_result(human_choice, ai_choice)

    print(f"The game is a {result}")


if __name__ == "__main__":
        
    assert check_result(human_choice="r", ai_choice="r") == "tie"
    assert check_result(human_choice="p", ai_choice="r") == "human"
    assert check_result(human_choice="r", ai_choice="p") == "ai"

    
    assert is_valid("r")
    assert not is_valid("asdf")

    play()