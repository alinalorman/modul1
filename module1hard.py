# Дано:
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]] # список оценок в алфавитном порядке
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'} # неупорядоченный список учеников

students = list(sorted(students)) # переводим множество в список учеников и сортируем значения по алфавиту

# Создаем словарь:
dictionary = {}

# Заполняем словарь ключами и значениями:
dictionary[students[0]] = sum(grades[0]) / len(grades[0])
dictionary[students[1]] = sum(grades[1]) / len(grades[1])
dictionary[students[2]] = sum(grades[2]) / len(grades[2])
dictionary[students[3]] = sum(grades[3]) / len(grades[3])
dictionary[students[4]] = sum(grades[4]) / len(grades[4])

# Выводим словарь на экран:
print(dictionary)