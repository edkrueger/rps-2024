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
    
if __name__ == "__main__":
    assert check_result(human_choice="r", ai_choice="r") == "tie"
    assert check_result(human_choice="p", ai_choice="r") == "human"
    assert check_result(human_choice="r", ai_choice="p") == "ai"