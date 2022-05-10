n = int(input())
s = input()

result, bonus = 0, 0
for idx, answer in enumerate(s):
    if answer == "O":
        result, bonus = result + idx + 1 + bonus, bonus + 1
    else:
        bonus = 0
print(result)

