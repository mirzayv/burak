# TASK-L

# Masalani izohi
# So'zlarni ketma-ketligini buzmasdan har bir so'zni alohida teskarisiga o'girib beradigan function tuzing.

# Masalan:
# reverseSentence("we like coding!") return "ew ekil !gnidoc"

def reverseSentence(text):
    words = text.split(" ")
    result = []

    for word in words:
        result.append(word[::-1])

    return " ".join(result)


print(reverseSentence("we like coding!"))