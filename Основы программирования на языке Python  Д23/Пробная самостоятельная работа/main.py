# Доброе утро
# хуйня

# Победа в битве
string1 = input()
string2 = input()
step = int(input())
start_length = min(len(string1), len(string2))
end_length = max(len(string1), len(string2))
result = [i for i in range(start_length, end_length, step)]
print(*result)

# Что придет в голову
word_check = input().lower()
number_lin = int(input())
stoy_lines = 0
lines = []
for _ in range(number_lin):
    line = input()
    lines.append(line)
    if word_check in line.lower() or "туннел" in line.lower():
        stoy_lines += 1
if stoy_lines >= 3:
    print("МЫСЛЬ ЕСТЬ!")
else:
    print("ПОСИДИМ ЕЩЕ")
ost = ((number_lin - stoy_lines) / number_lin) * 100
print(ost)
