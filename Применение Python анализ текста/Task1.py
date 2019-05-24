# Вашей программе на вход подаются три строки s, a, b, состоящие из строчных латинских букв.
# За одну операцию вы можете заменить все вхождения строки a в строку s на строку b.
#
# Например, s = "abab", a = "ab", b = "ba", тогда после выполнения одной операции строка s перейдет в строку "baba", после выполнения двух и операций – в строку "bbaa", и дальнейшие операции не будут изменять строку s.
#
# Выведите одно число – минимальное число операций, после применения которых в строке s не останется вхождений строки a, или Impossible, если операций потребуется более 1000.
#
# Sample Input 1:
#
# ababa
# a
# b
# Sample Output 1:
#
# 1
# Sample Input 2:
#
# ababa
# b
# a
# Sample Output 2:
#
# 1
# Sample Input 3:
#
# ababa
# c
# c
# Sample Output 3:
#
# 0
# Sample Input 4:
#
# ababac
# c
# c
# Sample Output 4:
#
# Impossible

s = input()
a = input()
b = input()

counter = 0
while a in s:
    s = s.replace(a,b)
    if a in b or counter > 1000:
        counter = "Impossible"
        break
    else:
        counter += 1
print(counter)