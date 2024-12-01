numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
prime = []
not_prime = []
for i in range(len(numbers)):
    elem = numbers[i]
    is_prime = True
    for devider in range(2, elem):
        if elem % devider == 0:
            is_prime = False
    if is_prime and elem == 1:
        continue
    elif is_prime:
        prime.append(elem)

    else:
        not_prime.append(elem)
print("Простые: ", prime)
print("Не простые: ", not_prime)

