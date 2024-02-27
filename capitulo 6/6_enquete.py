favorite_langueges = {'Jen':'python','Sarah':'c','Phil':'python','Edward': 'ruby'}
pessoas = {'matheus','Derick','Jen','Phil'}

for pessoa in pessoas:
    if pessoa in favorite_langueges.keys():
        print(f"{pessoa}, obrigado por ter respondido à enquete")
    else:
        print(f"{pessoa},responda nossa enquete")

