lst=['Apple', 'Guava', 'Mango', 'Banana', 'Kiwi']

print("Length of list:", len(lst))
print("First Element:", lst[0])
print("Last Element:", lst[-1])

lst.append('papaya')
print("updated List :", lst)

lst.remove('Guava')
print("Updated List:", lst)

lst.sort()
print("Sorted List:", lst)

lst.pop(1)
print("Updated List :", lst)

lst.reverse()
print("Reversed List:", lst)