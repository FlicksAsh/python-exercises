def duplicate_encode(word):
    lowercase = word.lower()
    letters = []
    letters[:] = lowercase
    encoded = ""
    for char in lowercase:
        if letters.count(char) > 1:
            encoded += ")"
        else:
            encoded += "("
        

    return encoded

