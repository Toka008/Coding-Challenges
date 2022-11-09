def common_letters(first_word, second_word):
    first_word = list(first_word.lower())
    second_word = list(second_word.lower())
    common_char = []
    for i in first_word:
        if i in second_word:
            common_char.append(i)
            common_char.sort()
        
        
    return print(common_char)


common_letters("house","computers")
common_letters("Hi","there")
common_letters("Foo","bar")




