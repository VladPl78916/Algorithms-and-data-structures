t = "лилила"

# Формирование префикс-массива p (m операций)
p = [0] * len(t)
j = 0
i = 1

while i < len(t):
    if t[j] == t[i]:
        p[i] = j + 1
        i += 1
        j += 1
    else:
        if j == 0:
            p[i] = 0
            i += 1
        else:
            j = p[j - 1]

print(p)

# Поиск образа в строке

a = "лилилось лилилась"
m = len(t)
n = len(a)

i = 0
j = 0
while i < n:
    if a[i] == t[j]:
        i += 1
        j += 1
        if j == m:
            print("Образ найден")
            break

    else:
        if j > 0:
            j = p[j -1]
        else:
            i += 1

if i == n:
    print("Образ не найден")