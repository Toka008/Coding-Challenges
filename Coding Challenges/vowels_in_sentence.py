def vowels_in_sentence(input_string):
    vowels = ["a", "e", "i", "o"," u"]
    choosen_vowels = []
    input_string = input_string.lower()
    for i in input_string:
        if i in vowels:
            choosen_vowels.append(i)
            choosen_vowels.sort()

    return choosen_vowels



print(vowels_in_sentence("Hello there Toka"))