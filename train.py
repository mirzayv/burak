# TASK-L

# Masalani izohi
# So'zlarni ketma-ketligini buzmasdan har bir so'zni alohida teskarisiga o'girib beradigan function tuzing.

# Masalan:
# reverseSentence("we like coding!") return "ew ekil !gnidoc"

# def reverseSentence(text):
#    words = text.split(" ")
#    result = []

#    for word in words:
#        result.append(word[::-1])

#    return " ".join(result)


# print(reverseSentence("we like coding!"))


# TASK-M

# Masalani izohi
# Array ichidagi har bir raqam uchun
# raqamning o'zi va uning kvadratidan
# tashkil topgan object hosil qilib qaytarsin.

# Masalan:
# getSquareNumbers([1, 2, 3])
# return [
#   {"number": 1, "square": 1}, ...]

# def getSquareNumbers(arr):
#    result = []

#    for num in arr:
#        result.append({
#            "number": num,
#            "square": num * num
#        })

#   return result


# print(getSquareNumbers([1, 2, 3]))


# TASK-N

# Masalani izohi
# Stringni palindrom ekanligini aniqlab
# true yoki false qaytarsin.

# Masalan:
# palindromCheck("dad")
# return true

def palindromCheck(text):
    return text == text[::-1]


print(palindromCheck("dad"))
