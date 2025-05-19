import numpy as np
import matplotlib.pyplot as plt

def bissecao():
    
    def f(x):
        return (x-2**(-x))
    
    def df(x):  # Derivada de f(x)
        return 1+ (log(2)) * 2**(-x)
    
 
    
    # intervalo inicial 
    a = 0
    b = 1
    
    # Critério de parada
    tol = 1e-5
    max_iter = 100
    iter_count = 1

    # para usar na formatação do print e plot
    precisao=.5
    latex_label_plot=r'$f(x) = x - 2^{-x}$'

        
    if f(a) * f(b) > 0:
        print(f"\nERRO! A função deve ter sinais opostos nos extremos do intervalo; f({a})={f(a)} e f({b})={f(b)}.\n")
        print("\nBuscando mínimo de |f(x)| via derivada (f'(x) = 0):")
        # Aplicar bissecção em f'(x) = 0
        a_deriv, b_deriv = a, b
        iter_count = 0
        while (b_deriv - a_deriv) / 2 > tol and iter_count < max_iter:
            c = (a_deriv + b_deriv) / 2
            if df(c) == 0:
                break
            elif df(a_deriv) * df(c) < 0:
                b_deriv = c
            else:
                a_deriv = c
            iter_count += 1
        x_min = (a_deriv + b_deriv) / 2
        print(f"x que minimiza |f(x)|: {x_min:{precisao}f}")
        print(f"f(x_min) = {f(x_min):{precisao}f}")

        # Plot
        x_vals = np.linspace(a, b, 400)
        plt.figure(figsize=(8, 6))
        plt.plot(x_vals, f(x_vals), label=latex_label_plot, color='b')
        plt.axhline(0, color='black', linewidth=0.5)
        plt.scatter(x_min, f(x_min), color='red', label=f'Mínimo: x={x_min:{precisao}f}')
        plt.title('Ponto de mínimo de |f(x)|')
        plt.legend()
        plt.grid()
        plt.show()
        exit(0)
    

    print("\nIteração\ta\t\tb\t\tAprox.\t\tf((a+b)/2)")
    print("----------------------")

    # Método da bisecção
    while (b - a) / 2 > tol and iter_count < max_iter:
        c = (a + b) / 2
        
        print(f"{iter_count}\t\t{a:{precisao}f}\t\t{b:{precisao}f}\t\t{c:{precisao}f}\t\t{f(c): {precisao}f}")
        
        if f(c) == 0:  # Encontramos a raiz exata
            print(f"\n\n{iter_count}\t\t{a:{precisao}f}\t\t{b:{precisao}f}\t\t{raiz:{precisao}f}\t\t{f(raiz): {precisao}f}")
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        
        iter_count += 1
    
    # Aproximação final da raiz
    raiz = (a + b) / 2

    print(f"\n\n{iter_count}\t\t{a:{precisao}f}\t\t{b:{precisao}f}\t\t{raiz:{precisao}f}\t\t{f(raiz): {precisao}f}")


    print(f"\nPrecisão: {(b-a)/2:{precisao}f}")
    print(f"\nRaiz aproximada: {raiz:{precisao}f}")
    print(f"Número de iterações: {iter_count}")
    
    # Plotar a função
    x_vals = np.linspace(a - 1, b + 1, 400)
    y_vals = f(x_vals)
    
    plt.figure(figsize=(8, 6))
    plt.plot(x_vals, y_vals, label=latex_label_plot, color='b')
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(raiz, color='r', linestyle='--', label=f'Raiz aproximada: {raiz:{precisao}f}')
    plt.scatter(raiz, f(raiz), color='red', zorder=3)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Gráfico da função e raiz aproximada')
    plt.legend()
    plt.grid()
    plt.show()
    
    return raiz

bissecao()
