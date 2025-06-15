def test(lst):
    result = {}
    for item in lst:
        result[item[0]] = item[1:]
    return result

students = [[1, 'Harry Potter', 'V'], [2, 'Hermione Granger', 'V'], [3,'Ron Weasley', 'VI'], [4, 'Draco Malfoy', 'VII'], [5, 'Luna Lovegood', 'VI']]

print("\nOriginal list of lists:")
print(students)
print("\nConverted lists to a dictionary:")
print(students)