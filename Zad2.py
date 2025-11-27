# Zadanie 2

count = 0
number = 2
result = ""

while True:
    is_prime = True
    i = 2
    while i * i <= number:
        if number % i == 0:
            is_prime = False
            break
        i += 1

    if is_prime:
        result += str(number)
        count += 1
        if count == 10:
            break
        result += ","

    number += 1

print(result)
