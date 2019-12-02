import matplotlib.pyplot as plt


def mnkGP(x, y):  # функция которую можно использзовать в програме
    n = len(x)  # количество элементов в списках
    s = sum(y)  # сумма значений y
    s1 = sum([1 / x[i] for i in range(0, n)])  # сумма 1/x
    s2 = sum([(1 / x[i]) ** 2 for i in range(0, n)])  # сумма (1/x)**2
    s3 = sum([y[i] / x[i] for i in range(0, n)])  # сумма y/x
    a = round((s * s2 - s1 * s3) / (n * s2 - s1 ** 2), 3)  # коэфициент а с тремя дробными цифрами
    b = round((n * s3 - s1 * s) / (n * s2 - s1 ** 2), 3)  # коэфициент b с тремя дробными цифрами
    s4 = [a + b / x[i] for i in range(0, n)]  # список значений гиперболической функции

    plt.title('Аппроксимация с исходными точками')
    plt.plot(x, y, color='r', linestyle=' ', marker='o', label='Data(x,y)')
    plt.plot(x, s4, linewidth=2, label='Data(x,f(x)=a+b/x')

    plt.grid(True)
    plt.savefig("plotApprox.png")
    plt.show()

    print('Коэффициент A = ' + str(a))
    print('Коэффициент В = ' + str(b))
