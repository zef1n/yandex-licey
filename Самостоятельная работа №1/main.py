# Задание 1
razd = input()
a = input()
name = input()
find = a.split("")
hot = []
rez = name.split(razd)
for i in range(len(rez)):
    for ik in range(len(find)):
        if find[ik] in rez[i]:
            hot.append(rez[i])
print(", ".join(rez))
print(find)
print(hot)
print(rez)
