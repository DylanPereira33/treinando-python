def show_magician(magicians):
    for magician in magicians:
        print(magician) 

def make_great(magicians, wizard):
    while magicians:
        magician = magicians.pop()
        modified_magician = f"O Grande {magician}"
        print(modified_magician)
        wizard.append(modified_magician)

magicians = ['Houdini', 'David Copperfield', 'Criss Angel']
wizard = []

make_great(magicians, wizard)
show_magician(wizard)


