# Функция для проверки наличия перевёрнутого слова в строке
def luna_and_bezdna(line, reversed_w):
    words = line.split()
    for word in words:
        if word == reversed_w:
            return True
    return False


linees = []
dark = input().strip()
revers = dark[::-1]

while True:
    try:
        text = input().strip()
        if luna_and_bezdna(text, revers):
            linees.append(text)
    except EOFError:
        break

for text in linees:
    print(text)


def horror(word, search='Cthulhu'):
    global universe
    found = False
    for i in range(len(universe)):
        if universe[i][-1].lower() == word[0].lower():
            universe.insert(0, universe[i])
            universe[i + 1] = search
            found = True
            break
    if not found:
        universe.append(word)


universe = ['I', 'saw', 'horror', 'universe', 'contains']
horror('Squid', search='creature')
print(universe)


def bravery(new_word, creature='Cyclops'):
    global monsters

    for i, word in enumerate(monsters):
        if len(set(word.lower()) & set(creature.lower())) >= 2:

            index = len(monsters) // 2 if len(monsters) % 2 == 1 else len(monsters) // 2 + 1

            monsters.insert(index, new_word)

            monsters[i] = new_word
            return


# Примеры использования
monsters = ['hi', 'squid', 'jelly', 'green', 'Cthulhu', 'body']
bravery('Calamaris')
print(monsters)

monsters = ['wave', 'whale', 'fish', 'Dragon', 'pie']
bravery('Horror', creature='Grass')
print(monsters)
