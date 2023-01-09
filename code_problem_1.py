def solution(x):
    # Creating list for translations
    dictionary = [chr(n) for n in range(ord("a"), ord("z") + 1)]
    encrypted_dictionary = [chr(n) for n in reversed(range(ord("a"), ord("z") + 1))]
    
    translation = ""
    
    for char in x:
        if char in dictionary:
            translation += dictionary[encrypted_dictionary.index(char)]
        else:
            translation += char
    
    return translation
