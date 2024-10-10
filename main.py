def is_valid(choice):
    if not choice.lower() in {"r", "p", "s"}:
        return False
    return True

if __name__ == "__main__":
    assert is_valid("r")
    assert not is_valid("asdf")