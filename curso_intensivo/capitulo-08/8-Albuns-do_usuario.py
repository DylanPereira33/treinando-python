def make_album(artista,título,música):
    Álbum = {"artistas" : artista, "títulos": título, "músicas": música }
    return Álbum
while True:
    print("\nQual album, você gostaria de ter?")
    print("Ao terminar, digite q")
 
    artistas = input("Quem é o artista?")
    if artistas == "q":
         break
     
    títulos = input("Qual é o título?")
    if títulos == "q":
         break
     
    músicas = input("Qual música?")
    if músicas == "q":
         break
     
    Álbum = make_album(artistas,títulos,músicas)
    print(Álbum)
