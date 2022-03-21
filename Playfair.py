plain_text = "university"  # input("Enter Plain text")
key = "monarchy"  # input("Enter key")


def generate_pair(text):
    text_pair = []
    temp = 0
    while temp < len(text):
        if temp + 1 >= len(text) or text[temp] == text[temp + 1]:
            text_pair.append(text[temp] + 'x')
            temp = temp + 1
        else:
            text_pair.append(text[temp] + text[temp + 1])
            temp = temp + 2
    return text_pair


table = key
for i in range(ord("a"), ord("z") + 1):
    if chr(i) not in key:
        if chr(i) == 'j':
            continue
        table = table + chr(i)
matrix = [[table[i + t] for t in range(5)] for i in range(0, len(table), 5)]

print("Playfair Table: ")
for i in matrix:
    print(i)
print()
plain_Text_pair = generate_pair(plain_text)
print(f"Message text pair: {plain_Text_pair}")

encoded = ""

for i, j in plain_Text_pair:
    if i == 'j':
        i = 'i'
    if j == 'j':
        j = 'i'
    x1, y1 = -1, -1
    x2, y2 = -1, -1
    for x in range(5):
        if i in matrix[x]:
            x1, y1 = x, matrix[x].index(i)
        if j in matrix[x]:
            x2, y2 = x, matrix[x].index(j)
    if x1 == x2:
        y1 = (y1 + 1) % 5
        y2 = (y2 + 1) % 5
        # print(matrix[x1][y1], matrix[x2][y2])
        encoded += matrix[x1][y1] + matrix[x2][y2]

    elif y1 == y2:
        x1 = (x1 + 1) % 5
        x2 = (x2 + 1) % 5
        # print(matrix[x1][y1], matrix[x2][y2])
        encoded += matrix[x1][y1] + matrix[x2][y2]
    else:
        # print(matrix[x1][y2], matrix[x2][y1])
        encoded += matrix[x1][y2] + matrix[x2][y1]

print(f"Encoded Message: {encoded}")

cipher_text_pair = generate_pair(encoded)
print(f"Cipher text pair: {cipher_text_pair}")
decoded = ""
for i, j in cipher_text_pair:
    if i == 'j':
        i = 'i'
    if j == 'j':
        j = 'i'
    x1, y1 = -1, -1
    x2, y2 = -1, -1
    for x in range(5):
        if i in matrix[x]:
            x1, y1 = x, matrix[x].index(i)
        if j in matrix[x]:
            x2, y2 = x, matrix[x].index(j)
    if x1 == x2:
        y1 = (y1 - 1) % 5
        y2 = (y2 - 1) % 5
        # print(matrix[x1][y1], matrix[x2][y2])
        decoded += matrix[x1][y1] + matrix[x2][y2]

    elif y1 == y2:
        x1 = (x1 - 1) % 5
        x2 = (x2 - 1) % 5
        # print(matrix[x1][y1], matrix[x2][y2])
        decoded += matrix[x1][y1] + matrix[x2][y2]
    else:
        # print(matrix[x1][y2], matrix[x2][y1])
        decoded += matrix[x1][y2] + matrix[x2][y1]
print(f"Decoded Message: {decoded}")
