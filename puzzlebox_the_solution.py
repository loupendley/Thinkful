def answer(puzzlebox):
    print(dir(puzzlebox))
    print(puzzlebox.hint)
    print(puzzlebox.hint_two)
    print(puzzlebox.lock(puzzlebox.key))
    return 42
    pass

print("here is the solution {}".format(answer(1)))