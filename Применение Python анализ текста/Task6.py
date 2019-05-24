# Вам дано описание наследования классов в формате JSON.
# Описание представляет из себя массив JSON-объектов, которые соответствуют классам. У каждого JSON-объекта есть поле name, которое содержит имя класса, и поле parents, которое содержит список имен прямых предков.
#
# Пример:
# [{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]
#
# ﻿Эквивалент на Python:
#
# class A:
#     pass
#
# class B(A, C):
#     pass
#
# class C(A):
#     pass
#
# Гарантируется, что никакой класс не наследуется от себя явно или косвенно, и что никакой класс не наследуется явно от одного класса более одного раза.
#
# Для каждого класса вычислите предком скольких классов он является и выведите эту информацию в следующем формате.
#
# <имя класса> : <количество потомков>
#
# Выводить классы следует в лексикографическом порядке.
#
# Sample Input:
#
# [{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]
# Sample Output:
#
# A : 3
# B : 1
# C : 2

import json


def search(obj):
    for element in data:
        if obj['name'] in element['parents']:
            answer[member['name']].add(element['name'])
            search(element)

data = json.loads(input())
answer = {}

for member in data:
    answer[member['name']] = {1} # member- словарь из списка data
    search(member)

for member in sorted(answer):
    print(member, len(answer[member]), sep=" : ")