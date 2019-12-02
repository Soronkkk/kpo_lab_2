import numpy as np
from matplotlib import pyplot as plt

import findN0 as fn
import functions as f
import justCopy as t

# очищаем файл
file = open("output.txt", 'w')
file.close()

input_mass = []

print("input values")

input_mass = (input().split(' '))

for i in range(7):
    input_mass[i] = int(input_mass[i])

# input_mass = [5, 4, 2, 2, 1, 1, 0]

K = 0.001
check = f.comprasion_k(K, input_mass)
while not check:
    K += 0.001
    print("K = ", K)
    check = f.comprasion_k(K, input_mass)
    if (K > 0.999):
        break

n = fn.findN(K, input_mass)
print("n = ", n)

o = n * K * 1
op = 0

result_mass = []
for i in range(7):
    op = o * np.exp(-1 * K * (i + 1))
    print("Δn", i + 1, " = ", op)
    result_mass.append(op)
    n -= op

print("n, после приращения количества обнаруженных ошибок = ", n)

plt.title("Решение по модели Джелинского – Моранды,\nточки исходных данных")
plt.scatter(range(1, 8), input_mass, color='r')
plt.plot(range(1, 8), result_mass)
plt.grid(True, linestyle='-', color='0.5')
plt.savefig("plotOne.png")
plt.show()

nevyz = []

for i in range(7):
    nevyz.append(f.nevyzka(input_mass[i], result_mass[i]))

plt.title("Невязки")
plt.plot(range(1, 8), nevyz)
plt.grid(True, linestyle='-', color='0.5')
plt.savefig("plotNevyz.png")
plt.show()

for i in range(7):
    nevyz[i] = nevyz[i] ** 2

plt.title("Квадраты невязок")
# plt.scatter(range(1, 8), input_mass, color='r')
plt.plot(range(1, 8), nevyz)
plt.grid(True, linestyle='-', color='0.5')
plt.savefig("plotKvadNevyz.png")
plt.show()

sumKvadNevyz = sum(nevyz)
print("\nсумма квадратов невязок = " + str(sumKvadNevyz))

t.mnkGP(range(1, 8), input_mass)

exit()
