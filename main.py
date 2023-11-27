
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def f(x1, x2):
    return x1 * x1 + x1 * x2 + x2 * x2 - 3 * x1 - 6 * x2

def grad_f(x1, x2):
    df_dx1 = 2 * x1 + x2 - 3
    df_dx2 = x1 + 2 * x2 - 6
    return np.array([df_dx1, df_dx2])

# Начальное приближение
x = np.array([3, 2])

# Коэффициент скорости обучения
learning_rate = 0.1
# Начальное приближение
x1 = 3.00
x2 = 2.00
# Списки для хранения истории значений x1, x2 и f(x1, x2)
x1_history = [x1]
x2_history = [x2]
f_history = [f(x1, x2)]

# Количество итераций
num_iterations = 100

for i in range(num_iterations):
    grad = grad_f(x1, x2)
    x1 -= learning_rate * grad[0]
    x2 -= learning_rate * grad[1]


# Вывод результатов
print("Минимум найден в точке (x1, x2) =", (x1, x2))
#print(x1)
#print("{:10.6f}".format(x1))
print("Значение функции в минимуме f(x1, x2) =", f(x1, x2))

# Создание пустого графика
fig, ax = plt.subplots()
x1 = np.linspace(0, 5, 100)
x2 = np.linspace(0, 5, 100)
X1, X2 = np.meshgrid(x1, x2)
Z = f(X1, X2)
contour = ax.contour(X1, X2, Z, levels=20)

# Функция для обновления анимации
def update(i):
    global x
    ax.clear()
    ax.contour(X1, X2, Z, levels=20)

    gradient = grad_f(x[0], x[1])
    x = x - learning_rate * gradient

    ax.plot(x[0], x[1], 'ro')
    ax.annotate(f'Min: {f(x[0], x[1]):.2f}', (x[0], x[1]), textcoords="offset points", xytext=(0, 10))


# Создание анимации
ani = FuncAnimation(fig, update, frames=range(50), repeat=False)

plt.show()
