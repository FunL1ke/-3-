file_path = "F:\\Универ\\Програмирование\\text.txt"

with open(file_path, 'r') as file:
    text = file.read()
    words = text.split()
    count = 0
    for word in words:
        cleaned_word = ''.join([bukva for bukva in word if bukva.isalpha()])
        if cleaned_word.isalpha():
            count += 1

print(count)
