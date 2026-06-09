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

# def palindromCheck(text):
#   return text == text[::-1]


# print(palindromCheck("dad"))


# TASK-O

# Masalani izohi
# Array ichidagi har xil qiymatlardan faqat sonlar yig'indisini hisoblab qaytarsin.

# Masalan:
# calculateSumOfNumbers([10, "10", {"son": 10}, True, 35]) return 45

# def calculateSumOfNumbers(arr):
#   total = 0

#   for item in arr:
#        if type(item) == int or type(item) == float:
#            total += item

#    return total


# print(calculateSumOfNumbers([10, "10", {"son": 10}, True, 35]))


# TASK-P

# Masalani izohi
# Objectni nested array sifatida convert qilib qaytarsin.

# Masalan:
# objectToArray({"a": 10, "b": 20})
# return [["a", 10], ["b", 20]]

# def objectToArray(obj):
#    result = []

#   for key, value in obj.items():
#       result.append([key, value])

#  return result


# print(objectToArray({"a": 10, "b": 20}))


# TASK-Q

# Masalani izohi
# Objectda berilgan string propertysi borligini tekshirsin.

# Masalan:
# hasProperty({"name": "BMW"}, "name") return True
# hasProperty({"name": "BMW"}, "color") return False

# def hasProperty(obj: dict, prop: str) -> bool:
#   return prop in obj


# print(hasProperty({"name": "BMW"}, "name"))   # True
# print(hasProperty({"name": "BMW"}, "color"))  # False
# print(hasProperty({}, "name"))                # False

# TASK-R

# Masalani izohi
# "1 + 2" ko'rinishidagi stringni hisoblab number qaytarsin.

# Masalan:
# calculate("1 + 3") return 4

def calculate(text: str) -> int:
    return eval(text)


print(calculate("1 + 3"))  # 4
print(calculate("7 - 2"))  # 5
print(calculate("4 * 5"))  # 20
print(calculate("8 / 2"))  # 4
