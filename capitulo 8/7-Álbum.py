def make_album(artista,titulo,música=1):
    Álbum = {"artistas" : artista, "titulos": titulo, "músicas": música }
    return Álbum

print(make_album("Michael Jackson","Billie Jean"))
print(make_album("Bruno Mars","Locked Out of Heaven"))
print(make_album("Beatles","Yellow Submarine",12))