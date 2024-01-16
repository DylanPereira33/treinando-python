texto = "absjhdfaskvdjqpwoehqopihgaeipovtqwpoeriucqwiopcuoisdbhoahkçjaaaaaaavjsdklogfafovpofuapoevuyfapaugfhynvfasuofpyfvanypfpoyndfvjahsdkflbasdfiuaiausfiuabsfdguiabfouasgdfuiasgfklagsfkgaskgfduoqywf"
letras = {}
for letra in texto:
    if letra in letras:
        letras[letra] = letras[letra] + 1
    else:
        letras[letra] = 1

for letra in letras.keys():
    print(f'{letra}: {letras[letra]}')