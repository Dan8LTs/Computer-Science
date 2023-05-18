sorted_a = ["cod", "herring", "marlin"]
sorted_b = ["asp", "carp", "ide", "trout"]


def union(a, b):
    result = []
    while a and b:
        if a[0] < b[0]:
            result.append(a[0])
            a.remove(a[0])
        else:
            result.append(b[0])
            b.remove(b[0])
    return result + a + b


print(union(sorted_a, sorted_b))


def palindrome(word):
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    return palindrome(word[1:-1])


print(palindrome("whyhw"))


def merge_sort(list):
    if len(list) <= 1:
        return list
    left = list[0:len(list) // 2]
    right = list[len(list) // 2:len(list)]
    return union(merge_sort(left), merge_sort(right))


print(merge_sort([5, 4, 4, 2, 1]))


def trade(list):
    if len(list) <= 1:
        return 0
    left = list[0:len(list) // 2]
    right = list[len(list) // 2:len(list)]
    difference = max(right) - min(left)
    return max(trade(left), trade(right), difference)


print(trade([123, 42, 52, 12, 128, 1132, 8]))


def trade_dp(list):
    best_day_for_purchase = [1] + [0] * (len(list) - 1)
    sell_day = 1
    best_profit = 0
    for i in range(1, len(list)):
        if list[i] < list[best_day_for_purchase[i - 1]]:
            best_day_for_purchase[i] = i
        else:
            best_day_for_purchase[i] = best_day_for_purchase[i - 1]

        profit = list[i] - list[best_day_for_purchase[i]]
        if profit > best_profit:
            best_profit = profit
            sell_day = i
    return best_profit, list[best_day_for_purchase[sell_day]], list[sell_day]


print(trade_dp([123, 42, 52, 12, 128, 1132, 8]))

m = [12, 32, 52, 21, 24]
m.insert(0, "hello")
m.pop(0)
m.sort()
m.reverse()
print(list)

a = ("b", "g", "a", "d", "f", "c", "h", "e")
x = sorted(a)
print(a, "\n", x)

b = {1: 12, 2: 43, 3: 34, 4: 53}
b[5] = 52
b.pop(1)
b.get(4)
print(b)

c = set()
c.add(12)
c.add(15)
c.remove(15)
print(c)


def check(number):
    if type(number) != str:
        return True
    else:
        return False


def map_func(element):
    return element * 4


def plus(a, b):
    return a + b


s = [1, 2, 8, "WHAT?"]
res = list(filter(check, s))
res2 = list(map(map_func, s))

# def reduce(s, init_val, func):
#     accumulator = init_val
#     for item in s:
#         accumulator = func(accumulator, item)
#     return accumulator
# res3 = reduce(res, 0, plus)
from functools import reduce

res3 = reduce(plus, res)
print(res)
print(res2)
print(res3)

sentences = ["Hi, my friend!", "Where are you from?"]


def wsum(a, b):
    return len(a.split()) + len(b.split())


number_of_words = reduce(wsum, sentences)
print(number_of_words)


# каррированная функция
def sum(base_number):
    def special_sum(number):
        return base_number + number

    return special_sum


special = sum(int(input("Enter number: ")))
print(special(2))


def power_generator(base):
    def power(x):
        return x ** base

    return power


square = power_generator(2)
print(square(62))

cube = power_generator(4)
print(cube(26))