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

if __name__ == "__main__":
    assert is_valid("r")
    assert not is_valid("asdf")

    prompt_choice()