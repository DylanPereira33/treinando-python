def pangrams(s):
    visto = set()
    for letra in s.upper():
        if ord(letra) >= 65 and ord(letra) <= 90:
            visto.add(letra)
    if len(visto) == 26:
        return "pangram"
    return "not pangram"

print(pangrams("a"))
print(pangrams(""))
print(pangrams("ab"))
print(pangrams("aBCAqas"))
print(pangrams("abcdefghijklmnopqrstuvwxyz"))
print(pangrams("abCdEfgHijklmNopqrStuVwxyz"))
print(pangrams("bcdefghijklmnopqrstuvwxyz9"))