# Луна и бездна
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


# Я слишком много знаю
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
