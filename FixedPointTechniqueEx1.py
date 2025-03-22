import math
import numpy as np
import matplotlib.pyplot as plt

def g(x):
    """Função g(x) definida para o método do ponto fixo."""
    return math.sqrt((10 - x**3) / 4)

def f(x):
    """Função original f(x) = x^3 + 4x^2 - 10."""
    return x**3 + 4*x**2 - 10

def ponto_fixo(x0, tol=1e-6, max_iter=100):

    print("Iteração    x")
    print("----------------")

    for i in range(max_iter):
        x1 = g(x0)
        print(f"{i+1:<10} {x1:.8f}")

        if abs(x1 - x0) < tol:
            return x1, i+1  

        x0 = x1 

    raise ValueError("O método não convergiu.")

x0 = 1.5  

raiz, iteracoes = ponto_fixo(x0)

print(f"\nA raiz aproximada é {raiz:.8f}, encontrada em {iteracoes} iterações.\n")

x_vals = np.linspace(-1, 2, 400)
y_vals = f(x_vals)

plt.figure(figsize=(8, 5))
plt.plot(x_vals, y_vals, label='f(x) = x³ + 4x² - 10', color='b')
plt.axhline(0, color='black', linewidth=1, linestyle='--')  # Linha y=0
plt.axvline(raiz, color='r', linestyle='--', label=f'Raiz aproximada: {raiz:.8f}')
plt.scatter(raiz, 0, color='red', zorder=3)  # Destacar a raiz
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gráfico da função e raiz encontrada')
plt.legend()
plt.grid()
plt.show()
