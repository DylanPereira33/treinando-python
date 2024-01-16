alien_0 = {'color': 'green', 'points': 5, 'speed':'slow'}
alien_1 = {'color': 'yellow', 'points': 10, 'speed':'medium'}
alien_2 = {'color': 'red', 'points': 15, 'speed':'fast'}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(f"aliens {alien['color']} valem {alien['points']} pontos e tem velocidade {alien['speed']}")
    print("\n")