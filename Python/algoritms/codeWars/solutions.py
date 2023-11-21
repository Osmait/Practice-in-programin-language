def name_shuffler(arr: list[int]) -> int | None:
    for i, v in enumerate(arr):
        current = v + 1
        if i < len(arr) - 1:
            print(v)
            next = arr[i + 1]
            if current != next:
                return next

    return None


print(name_shuffler([1, 2, 3, 4, 5, 6, 8]))


def nameShuffler(s: str) -> str:
    return " ".join(s.split(" ")[::-1])


print(nameShuffler("saul burgos"))


def GetSum(a, b):
    return int((a + b) * (abs(a - b) + 1) / 2)


def simpleMultiplication(n):
    return n * 9 if n % 2 else n * 8


def oddOrEven(numbers: list):
    return "even" if sum(numbers) % 2 == 0 else "odd"


def rowWeights(n):
    a, b = 0, 0
    for i, v in enumerate(n):
        if i % 2 == 0:
            a += v
        else:
            b += v
    return a, b


def predictAge(*ages):
    return int(sum(age**2 for age in ages) ** 0.5 // 2)


def getMiddle(s):
    return s[(len(s) - 1) // 2: len(s) // 2 + 1]


def CalculateAge(birth, current):
    age = current - birth
    if age == 0:
        return "You were born this very year!"
    if age > 0:
        return f"You are {age} year{'' if age == 1 else 's'} old."
    else:
        return f"You will be born in {-age} year{'' if -age == 1 else 's'}."


def evaporator(content: int, evap_per_day: int, threshold: int) -> int:
    days = 0
    limit = content * (threshold / 100)
    while content > limit:
        content -= content * (evap_per_day / 100)
        days += 1

    return days


def MaxAbsLengthDiff(a1: list, a2: list) -> int:
    if len(a1) == 0 or len(a2) == 0:
        return -1
    max_diff = 0
    for i in range(len(a1)):
        for j in range(len(a2)):
            diff = abs(len(a1[i]) - len(a2[j]))
            if diff > max_diff:
                max_diff = diff
    return max_diff


a1 = [
    "hoqq",
    "bbllkw",
    "oox",
    "ejjuyyy",
    "plmiis",
    "xxxzgpsssa",
    "xxwwkktt",
    "znnnnfqknaz",
    "qqquuhii",
    "dvvvwz",
]
a2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]

print(MaxAbsLengthDiff(a1, a2))


def CalculateYears(years):
    if years < 0:
        return None
    elif years == 1:
        return [1, 15, 15]
    elif years == 2:
        return [2, 14, 14]
    else:
        cat_years = 24 + (years - 2) * 4
        dog_years = 24 + (years - 2) * 5
        return [years, cat_years, dog_years]
