import numpy as np
import matplotlib.pyplot as plt

def bissecao():
    def f(x):
    #    return x**3 + 4*x**2 - 10
        return (x**3 - x -1)
    
    # ntervalo inicial 
    a = 1
    b = 2
#    a = -1.25
#    b = 2.5
    
    # Critério de parada
    tol = 1e-4
    max_iter = 100
    iter_count = 1
    
    if f(a) * f(b) > 0:
        print(f"\nERRO! A função deve ter sinais opostos nos extremos do intervalo; f({a})={f(a)} e f({b})={f(b)}.\n")
        exit(0)
    
    print("\nIteração\ta\t\tb\t\tAprox.\t\tf((a+b)/2)")
    print("----------------------")
    
    # Método da bisecção
    while (b - a) / 2 > tol and iter_count < max_iter:
        c = (a + b) / 2
        
        print(f"{iter_count}\t\t{a:.4f}\t{b:.4f}\t{c:.4f}\t{f(c): .4f}")
        
        if f(c) == 0:  # Encontramos a raiz exata
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        
        iter_count += 1
    
    # Aproximação final da raiz
    raiz = (a + b) / 2
    print(f"\nPrecisão: {(b-a)/2:.4f}")
    print(f"\nRaiz aproximada: {raiz:.4f}")
    print(f"Número de iterações: {iter_count-1}")
    
    # Plotar a função
    x_vals = np.linspace(a - 1, b + 1, 400)
    y_vals = f(x_vals)
    
    plt.figure(figsize=(8, 6))
    plt.plot(x_vals, y_vals, label=r'$f(x) = x^3 -x -1$', color='b')
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(raiz, color='r', linestyle='--', label=f'Raiz aproximada: {raiz:.4f}')
    plt.scatter(raiz, f(raiz), color='red', zorder=3)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Gráfico da função e raiz aproximada')
    plt.legend()
    plt.grid()
    plt.show()
    
    return raiz

bissecao()
