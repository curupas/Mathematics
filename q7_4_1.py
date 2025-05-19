import numpy as np

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

# Caso 1: p0 = -1
print("Caso p0 = -1:")
result_p0_minus1 = newton_method(p0=-1)
for i, p in enumerate(result_p0_minus1):
    print(f"p_{i} = {p:.4f}")

# Caso 2: p0 = 0
print("\nCaso p0 = 0:")
result_p0_zero = newton_method(p0=0)
for i, p in enumerate(result_p0_zero):
    print(f"p_{i} = {p:.6f}")

# Resultados finais
print("\nResultados finais:")
print(f"Com p0 = -1, p2 = {result_p0_minus1[2]:.4f}")
print(f"Com p0 = 0, o método falha pois a derivada é zero na primeira iteração.")
