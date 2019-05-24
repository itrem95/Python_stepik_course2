# В этой задаче вам необходимо воспользоваться API сайта numbersapi.com
#
# Вам дается набор чисел. Для каждого из чисел необходимо узнать, существует ли интересный математический факт об этом числе.
#
# Для каждого числа выведите Interesting, если для числа существует интересный факт, и Boring иначе.
# Выводите информацию об интересности чисел в таком же порядке, в каком следуют числа во входном файле.
#
# Пример запроса к интересному числу:
# http://numbersapi.com/31/math?json=true
#
# Пример запроса к скучному числу:
# http://numbersapi.com/999/math?json=true
#
# Пример входного файла:
# 31
# 999
# 1024
# 502
#
# ﻿Пример выходного файла:
# Interesting
# Boring
# Interesting
# Boring

import requests

api_url = "http://numbersapi.com/"
answer = []
with open ("dataset_24476_3.txt", "r") as file_of_numbers:
    for number in file_of_numbers:
        number = number.strip()
        params = {
                "number" : number
        }
        res = requests.get(api_url + number + "/math?json=true", params=params)
        data = res.json()
        if data["found"]:
            answer.append("Interesting")
        else:
            answer.append("Boring")

with open ("answer.txt", "w") as file_of_answers:
    for answers in answer:
        file_of_answers.write(answers + "\n")