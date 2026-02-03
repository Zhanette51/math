import numpy as np
import matplotlib.pyplot as plt

# Параметры a=5, b=3. Центр (0, 0)
a = 5
b = 3
c = np.sqrt(a**2 + b**2)

# Генерируем точки для построения двух ветвей гиперболы
x = np.linspace(-10, 10, 400)
# Из уравнения: y^2 = 9 * (x^2/25 - 1)
y1 = b * np.sqrt(x**2/a**2 - 1)
y2 = -b * np.sqrt(x**2/a**2 - 1)

# Фильтруем NaN значения, где x находится между асимптотами (-a, a)
# np.isfinite возвращает True для конечных чисел и False для NaN
x1_filtered = x[np.isfinite(y1)]
y1_filtered = y1[np.isfinite(y1)]
x2_filtered = x[np.isfinite(y2)]
y2_filtered = y2[np.isfinite(y2)]

plt.figure(figsize=(8, 6))
plt.plot(x1_filtered, y1_filtered, label='Гипербола (верхняя ветвь)', color='blue')
plt.plot(x2_filtered, y2_filtered, label='Гипербола (нижняя ветвь)', color='blue')

# Обозначение фокусов
plt.scatter([-c, c], [0, 0], color='red', marker='x', label=f'Фокусы (±{c:.2f}, 0)')

# Настройки графика
plt.title('Гипербола: x²/25 - y²/9 = 1')
plt.xlabel('X ось')
plt.ylabel('Y ось')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.axis('equal')
plt.show()
