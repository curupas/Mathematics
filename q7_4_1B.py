import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return -x**3 - np.cos(x)

def df(x):
    # Derivada de f(x): -3x² + sen(x)
    return -3*x**2 + np.sin(x)

def newton_method(p0, max_iter=10, tol=1e-4):
    """
    Implementação do método de Newton para encontrar raízes.
    
    Args:
        p0: aproximação inicial
        max_iter: número máximo de iterações
        tol: tolerância para convergência
        
    Returns:
        Lista com todas as aproximações calculadas
    """
    approximations = [p0]
    for i in range(max_iter):
        p = approximations[-1]
        fp = f(p)
        dfp = df(p)
        
        # Verifica se a derivada é zero para evitar divisão por zero
        if abs(dfp) < tol:
            print(f"Derivada zero em p={p}. O método falhou.")
            return approximations
        
        p_next = p - fp / dfp
        approximations.append(p_next)
        
        # Verifica convergência
        if abs(p_next - p) < tol:
            break
            
    return approximations

def plot_p2(x_range, approximations, title):
    """Plota a função e destaca p2 com linha vertical"""
    x = np.linspace(x_range[0], x_range[1], 400)
    y = f(x)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label='f(x) = -x³ - cos(x)')
    plt.axhline(0, color='black', linewidth=0.5)
    
    # Verifica se temos pelo menos 3 pontos (p0, p1, p2)
    if len(approximations) >= 3:
        p2 = approximations[2]
        p2_value = f(p2)
        
        # Linha vertical em p2
        plt.axvline(x=p2, color='red', linestyle='--', alpha=0.7)
        
        # Ponto p2 no gráfico
        plt.scatter(p2, p2_value, color='red', zorder=5)
        
        # Label com o valor de p2
        plt.text(p2, p2_value, f' p2 = {p2:.4f}', 
                verticalalignment='bottom', horizontalalignment='right')
    
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Caso 1: p0 = -1
print("Caso p0 = -1:")
result_p0_minus1 = newton_method(p0=-1)
for i, p in enumerate(result_p0_minus1):
    print(f"p_{i} = {p:.4f}")

# Plotar apenas p2 para o primeiro caso
plot_p2([-1.5, 0.5], result_p0_minus1, 
        "Método de Newton - Destaque para p2 (p0 = -1)")

# Caso 2: p0 = 0
print("\nCaso p0 = 0:")
result_p0_zero = newton_method(p0=0)
for i, p in enumerate(result_p0_zero):
    print(f"p_{i} = {p:.6f}")

# Resultados finais
print("\nResultados finais:")
print(f"Com p0 = -1, p2 = {result_p0_minus1[2]:.4f}")
print(f"Com p0 = 0, o método falha pois a derivada é zero na primeira iteração.")