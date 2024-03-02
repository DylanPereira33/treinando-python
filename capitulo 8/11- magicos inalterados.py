def show_magician(magicians):
    for magician in magicians:
        print(magician) 

def make_great(magicians):
    great_magicians = []
    while magicians:
        magician = magicians.pop()
        modified_magician = f"O Grande {magician}"
        print(modified_magician)
        great_magicians.append(modified_magician)
    return great_magicians

magicians = ['Houdini', 'David Copperfield', 'Criss Angel']
original_magicians = magicians[:]  # Fazendo uma cópia da lista original
wizard = []

wizard = make_great(magicians[:])  # Passando uma cópia da lista original para a função
show_magician(original_magicians)

