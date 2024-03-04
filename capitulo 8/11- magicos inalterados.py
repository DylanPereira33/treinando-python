def show_magician(magicians):
    for magician in magicians:
        print(magician) 

def make_great(magicians, great_magicians):
    while magicians:
        magician = magicians.pop()
        modified_magician = f"O Grande {magician}"
        print(modified_magician)
        great_magicians.append(modified_magician)

magicians = ['Houdini', 'David Copperfield', 'Criss Angel']
great_magicians = []

make_great(magicians[:], great_magicians)
print(magicians)
print(great_magicians)

