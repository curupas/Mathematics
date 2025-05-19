import numpy as np
import matplotlib.pyplot as plt

# Configuração do intervalo amplo
x1 = np.linspace(-10, 10, 1000)  # Intervalo amplo para x1
x2 = np.linspace(-5, 10, 1000)   # Intervalo amplo para x2
X1, X2 = np.meshgrid(x1, x2)

# Cálculo das funções
F1 = X1 * (1 - X1) + 4 * X2 - 12      # Equação 1
F2 = (X1 - 2)**2 + (2 * X2 - 3)**2 - 25  # Equação 2

# Plot das curvas de nível zero
plt.figure(figsize=(12, 8))
plt.contour(X1, X2, F1, levels=[0], colors='blue', linewidths=2, linestyles='-', label='$x_1(1-x_1)+4x_2=12$')
plt.contour(X1, X2, F2, levels=[0], colors='red', linewidths=2, linestyles='-', label='$(x_1-2)^2+(2x_2-3)^2=25$')

# Configurações do gráfico
plt.title('Comportamento das Funções do Sistema', fontsize=16)
plt.xlabel('$x_1$', fontsize=14)
plt.ylabel('$x_2$', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(fontsize=12)

# Limites dos eixos (ajuste manualmente aqui!)
plt.xlim(-10, 10)  # Altere estes valores para dar zoom
plt.ylim(-5, 10)   # Altere estes valores para dar zoom

# Destacar os eixos
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

plt.tight_layout()
plt.show()
