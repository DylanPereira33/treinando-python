grupo = []
if grupo:
    for participante in grupo:
        if participante == "admin":
            print("olá administrador, gostaria de ver um relátorio")
        else:
            print(f"{participante}, obrigado por fazer login novamente." )
else:
    print("precisamos encontrar alguns usuários")
   