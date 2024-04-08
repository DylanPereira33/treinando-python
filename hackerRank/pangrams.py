def pangrams(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    S = s.lower()
    for letter in alphabet:
        if letter not in S:
            return "not pangram"
    return "pangram"    