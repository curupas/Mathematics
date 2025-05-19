import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

def problema3():
    # Configuração do gráfico
    plt.figure(figsize=(12, 7))
    
    # Definindo os intervalos para plotar tan(x) (evitando as assíntotas)
    x1 = np.linspace(0, np.pi/2 - 0.1, 500)
    x2 = np.linspace(np.pi/2 + 0.1, 3*np.pi/2 - 0.1, 500)
    x3 = np.linspace(3*np.pi/2 + 0.1, 5*np.pi/2 - 0.1, 500)
    x_linear = np.linspace(0, 5*np.pi/2, 500)
    
    # Plotando g(x) = x
    plt.plot(x_linear, x_linear, 'b-', linewidth=2, label='$g(x) = x$')
    
    # Plotando h(x) = tan(x)
    plt.plot(x1, np.tan(x1), 'r-', linewidth=2, label='$h(x) = \tan(x)$')
    plt.plot(x2, np.tan(x2), 'r-', linewidth=2)
    plt.plot(x3, np.tan(x3), 'r-', linewidth=2)
    
    # Assíntotas verticais
    plt.axvline(x=np.pi/2, color='gray', linestyle='--', alpha=0.7)
    plt.axvline(x=3*np.pi/2, color='gray', linestyle='--', alpha=0.7)
    plt.axvline(x=5*np.pi/2, color='gray', linestyle='--', alpha=0.7)
    
    # Método da bissecção para encontrar x = tan(x)
    def f(x):
        return x - np.tan(x)
    
#    a, b = 4.4, 4.5
    a, b = 3.1416, 4.7124
    tol = 1e-5
    max_iter = 50
    resultados = []
    p = None
    
    print("\nMétodo da bissecção para resolver x = tan(x):")
    print(f"Intervalo inicial: [{a}, {b}], tolerância: {tol}\n")
    
    for i in range(1, max_iter + 1):
        p = (a + b) / 2
        fp = f(p)
        resultados.append([i, a, b, p, fp])
        
        if abs(fp) < tol:
            break
        
        if f(a) * fp < 0:
            b = p
        else:
            a = p
    
    # Imprimindo a tabela de iterações
    print(tabulate(resultados, headers=["Iteração", "a", "b", "p", "f(p)"], floatfmt=".6f"))
    print(f"\nSolução encontrada: x ≈ {p:.6f}")
    
    # Plotando o ponto de interseção encontrado
    plt.plot(p, p, 'ko', markersize=8, label=f'Solução: $x \\approx {p:.5f}$')
    plt.annotate(f'({p:.5f}, {p:.5f})', 
                 xy=(p, p), 
                 xytext=(10, 20), 
                 textcoords='offset points',
                 bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.7),
                 arrowprops=dict(arrowstyle='->'))
    
    # Configurações finais do gráfico
    plt.xlim(0, 8)
    plt.ylim(-5, 10)
    plt.xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi, 5*np.pi/2, p],
               ['0', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$', r'$5\pi/2$', f'{p:.2f}'])
    plt.yticks(np.arange(-5, 11, 1))
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.title('Solução de $x = \tan(x)$ com Método da Bissecção', fontsize=14)
    plt.legend(loc='upper left', fontsize=12)
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.tight_layout()
    plt.show()

# Executar o problema 3
print("="*60)
print(" SOLUÇÃO PARA O PROBLEMA 3: x = tan(x) ")
print("="*60)
problema3()