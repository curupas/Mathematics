import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

def newton_method(f, df, ddf, x0, tol=1e-4, max_iter=100):
    """
    Implementação do método de Newton para encontrar o mínimo de uma função.
    
    Parâmetros:
    f - função objetivo
    df - primeira derivada da função
    ddf - segunda derivada da função
    x0 - estimativa inicial
    tol - tolerância para convergência
    max_iter - número máximo de iterações
    
    Retorna:
    x - ponto de mínimo aproximado
    history - histórico das iterações
    """
    x = x0
    history = []
    for i in range(max_iter):
        grad = df(x)
        hess = ddf(x)
        current_distance = np.sqrt(f(x))
                
        if abs(grad) < tol:
            break
            
        delta_x = -grad / hess
        x += delta_x
        history.append((x, f(x), grad))
        print(f"Iteração {i+1}: x = {x: .4f} f(x) = {f(x): 4f}, f'(x) = {grad: .4f} Coordenada de y = {x**2:.4f} Distância = {current_distance: .4f}")
#        print(f"Iteração {i+1}: x = {x:.4f}, f(x) = {f(x):.4f}, f'(x) = {grad:.4f}")
        
    return x, history

# Definindo a função distância ao quadrado e suas derivadas
def distance_squared(x):
    return (x - 1)**2 + (x**2)**2

def df_distance_squared(x):
    return 2*(x - 1) + 4*x**3

def ddf_distance_squared(x):
    return 2 + 12*x**2

# Parâmetros do método
initial_guess = 0.5  # Estimativa inicial
tolerance = 1e-4
target_point = (1, 0)

# Aplicando o método de Newton
solution, history = newton_method(distance_squared, df_distance_squared, 
                                ddf_distance_squared, initial_guess, tolerance)

# Preparando dados para os gráficos
x_vals = np.linspace(0, 1.5, 400)
y_parabola = x_vals**2
y_distance = distance_squared(x_vals)

# Ponto encontrado
solution_point = (solution, solution**2)

# Criando a figura com subplots
plt.figure(figsize=(15, 5))

# Gráfico 1: Função distância ao quadrado
plt.subplot(1, 3, 1)
plt.plot(x_vals, y_distance, label='d(x)² = (x-1)² + x⁴')
plt.scatter([x for x, _, _ in history], [f for _, f, _ in history], 
            c='red', label='Iterações Newton')
plt.scatter([solution], [distance_squared(solution)], 
            c='green', s=100, label='Solução')
plt.xlabel('x')
plt.ylabel('Distância quadrada')
plt.title('Minimização da distância quadrada')
plt.legend()
plt.grid(True)

# Gráfico 2: Parábola e ponto mais próximo
plt.subplot(1, 3, 2)
plt.plot(x_vals, y_parabola, label='y = x²')
plt.scatter(*target_point, c='blue', s=100, label='Ponto (1,0)')
plt.scatter(solution_point[0], solution_point[1], 
            c='green', s=100, label='Ponto mais próximo')

# Desenhar a distância mínima
plt.plot([target_point[0], solution_point[0]], 
         [target_point[1], solution_point[1]], 
         'r--', label='Distância mínima')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Ponto mais próximo na parábola')
plt.legend()
plt.axis('equal')
plt.grid(True)

# Gráfico 3: Visualização em 2D
plt.subplot(1, 3, 3)
plt.plot(x_vals, y_parabola, label='y = x²')
plt.scatter(*target_point, c='blue', s=100, label='Ponto (1,0)')
plt.scatter(solution_point[0], solution_point[1], 
            c='green', s=100, label='Ponto mais próximo')

# Círculo com centro em (1,0) e raio igual à distância mínima
min_distance = np.sqrt(distance_squared(solution))
circle = Circle(target_point, min_distance, fill=False, 
                linestyle='--', color='orange', label='Distância mínima')
plt.gca().add_patch(circle)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Visualização geométrica')
plt.legend()
plt.axis('equal')
plt.grid(True)

plt.tight_layout()
plt.show()

# Resultados numéricos
print("\nResultado final:")
print(f"O ponto mais próximo tem coordenada x = {solution:.4f}")
print(f"Coordenada y correspondente = {solution**2:.4f}")
print(f"Distância mínima = {min_distance:.4f}")
print(f"Número de iterações = {len(history)}")
