def factorial(number):
    result = 1
    for x in range(1, number + 1):
        result *= x
        print(str(x) + "!\t = " + str(result))
    return result


factorial(53)
