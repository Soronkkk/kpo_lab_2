import numpy


# нужно вызвать этот метод
def findN(K, nArray):
    ti = [1, 2, 3, 4, 5, 6, 7]
    result = numerator(K, ti, nArray) / denominator(K, ti)
    return result


# числитель
def numerator(K, ti, nArray):
    result = 0
    for i in range(7):
        result += nArray[i] * ti[i] * numpy.exp(-K * ti[i])
    return result


# знаменатель
def denominator(K, ti):
    result = 0
    for i in range(7):
        result += numpy.exp(-2 * K * ti[i]) * ti[i]
    result *= K
    return result
