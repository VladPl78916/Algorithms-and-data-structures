marks = [2, 2, 3, 4]
lst = [True, "Истина", 1, 1.0] # ссылки на объекты
lst.append(5) # O(1)
lst.insert(0, 'First') # O(n)

el_3 = marks[2]

print(el_3)

n = len(marks)

print(lst)

marks[0] = 3 # O(1)
print(marks)

print(marks + lst) # O(n + m)

lst = [1, 2, 3, 4, 5, 6]
print(lst[1:6]) # O(n)