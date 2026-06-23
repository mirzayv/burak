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

# def calculate(text: str) -> int:
#   return eval(text)


# print(calculate("1 + 3"))  # 4
# print(calculate("7 - 2"))  # 5
# print(calculate("4 * 5"))  # 20
# print(calculate("8 / 2"))  # 4


# TASK-S

# Masalani izohi
# Array ichidagi tushib qolgan sonni topib qaytarsin.

# Masalan:
# missingNumber([3, 0, 1]) return 2

# def missingNumber(nums: list) -> int:
#     n = len(nums)
#     return n * (n + 1) // 2 - sum(nums)


# print(missingNumber([3, 0, 1]))  # 2
# print(missingNumber([0, 1]))     # 2
# print(missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))  # 8


# # TASK-T

# # Masalani izohi
# # Ikkita arrayni qabul qilib, ularni birlashtirib
# # tartiblangan holda qaytarsin.

# # Masalan:
# # mergeSortedArrays([0, 3, 4], [4, 6]) return [0, 3, 4, 4, 6]

# def mergeSortedArrays(arr1: list, arr2: list) -> list:
#     merged = arr1 + arr2
#     # arr1 + arr2 — ikki arrayni birlashtirish
#     # [0, 3, 4] + [4, 6] = [0, 3, 4, 4, 6]

#     return sorted(merged)
#     # sorted() — o'sish tartibida tartiblaydi
#     # [0, 3, 4, 4, 6]


# print(mergeSortedArrays([0, 3, 4], [4, 6]))   # [0, 3, 4, 4, 6]
# print(mergeSortedArrays([1, 5, 9], [2, 6]))   # [1, 2, 5, 6, 9]
# print(mergeSortedArrays([], [1, 2]))           # [1, 2]


# TASK V

# Masalani izohi
# Stringdagi har bir harf necha marta takrorlanganini object sifatida qaytarsin.

# Masalan:
# countChars("hello") return {"h": 1, "e": 1, "l": 2, "o": 1}

# def countChars(text: str) -> dict:
#     pass

# def countChars(text: str) -> dict:
#    result = {}
#        if char in result:
#            result[char] += 1
#        else:
#            result[char] = 1

#    return result


# print(countChars("hello"))


# TASK W

# Masalani izohi
# Arrayni berilgan uzunlikda bo'laklarga ajratib qaytarsin.

# Masalan:
# chunkArray([1, 2, 3, 4, 5], 2) return [[1, 2], [3, 4], [5]]

def chunkArray(arr, size):
    result = []

    for i in range(0, len(arr), size):
        result.append(arr[i:i + size])

    return result


print(chunkArray([1, 2, 3, 4, 5], 2))
