

def test_input_15():
    phrase = int(input("Set a phrase: "))
    assert phrase <= 15, "Exceeding the length"
    print(phrase)