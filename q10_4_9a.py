import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# 1. Definir as funções do sistema
def sistema(x):
    x1, x2 = x
    f1 = x1 * (1 - x1) + 4 * x2 - 12
    f2 = (x1 - 2)**2 + (2 * x2 - 3)**2 - 25
    return np.array([f1, f2])

# 2. Definir a matriz Jacobiana
def jacobiana(x):
    x1, x2 = x
    return np.array([
        [1 - 2*x1, 4],
        [2*(x1 - 2), 4*(2*x2 - 3)]
    ])

# 3. Implementar o método de Newton (FUNÇÃO QUE FALTAVA)
def newton_sistema(p0, tol=1e-4, max_iter=100):
    historico = [np.array(p0)]
    p = np.array(p0, dtype=float)
    
    print(f"p0 = [{p[0]:.4f}, {p[1]:.4f}]")  # Imprime o ponto inicial
    
    for k in range(max_iter):
        F = sistema(p)
        J = jacobiana(p)
        delta_p = np.linalg.solve(J, -F)
        p += delta_p
        historico.append(p.copy())
        
        print(f"p{k+1} = [{p[0]:.4f}, {p[1]:.4f}]")  # Imprime cada ponto iterado
        
        if np.linalg.norm(delta_p) < tol:
            print(f"Convergência alcançada após {k+1} iterações.")
            return p, historico
    print("Máximo de iterações alcançado sem convergência.")
    return p, historico
# 4. Função de plotagem (já existente no seu código)
def plot_solucao(historico):
    plt.figure(figsize=(10, 8))
    
    # Foco na região ao redor da solução (-1.0, 3.5)
    x1 = np.linspace(-3, 1, 400)  # Ajustado para região x1 negativa
    x2 = np.linspace(2, 5, 400)   # Foco em x2 ~ 3.5
    X1, X2 = np.meshgrid(x1, x2)
    
    # Cálculo preciso das funções
    F1 = X1 * (1 - X1) + 4 * X2 - 12
    F2 = (X1 - 2)**2 + (2 * X2 - 3)**2 - 25
    
    # Plot das curvas com nível zero ajustado
    plt.contour(X1, X2, F1, levels=[0], colors='blue', linewidths=2, linestyles='solid')
    plt.contour(X1, X2, F2, levels=[0], colors='red', linewidths=2, linestyles='solid')
    

    # Trajetória e ponto final
    historico = np.array(historico)
    plt.plot(historico[:, 0], historico[:, 1], 'o-', color='green', markersize=6, linewidth=1.5, alpha=0.7)
    plt.scatter(-1.0, 3.5, color='gold', s=20, edgecolors='black', zorder=5)
    
  # Destacar p2 com um marcador diferente
    if len(historico) > 2:
        plt.scatter(historico[2, 0], historico[2, 1], color='purple', s=20, edgecolors='black', zorder=5, label='p2')
  
     # Verificação manual do ponto na curva (debug)
    print("Verificação do ponto (-1.0, 3.5):")
    print("f1(-1.0, 3.5) =", (-1.0)*(1 - (-1.0)) + 4*3.5 - 12)
    print("f2(-1.0, 3.5) =", (-1.0 - 2)**2 + (2*3.5 - 3)**2 - 25)

    # Elementos da legenda
    legend_elements = [
        Line2D([0], [0], color='blue', label='$x_1(1-x_1)+4x_2=12$'),
        Line2D([0], [0], color='red', label='$(x_1-2)^2+(2x_2-3)^2=25$'),
        Line2D([0], [0], marker='o', color='green', label='Trajetória de Newton', linestyle='-'),
        Line2D([0], [0], marker='o', color='purple', label='p2: (-23.9426, 7.6087)', markeredgecolor='black', linestyle='None'),
        Line2D([0], [0], marker='o', color='gold', label='Solução (-1.0, 3.5)', 
               markeredgecolor='black', linestyle='None')
    ]
    
    plt.legend(handles=legend_elements, loc='upper right', fontsize=10)
    plt.xlabel('$x_1$', fontsize=12)
    plt.ylabel('$x_2$', fontsize=12)
    plt.title('Método de Newton - Verificação da Solução', fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.3)
    plt.axis('equal')
    plt.tight_layout()
    
    # Zoom final para garantir precisão visual
    plt.xlim(-25, 0.5)
    plt.ylim(3.0, 4.0)
    plt.show()

if __name__ == "__main__":
    p0 = [0.0, 0.0]
    try:
        solucao, historico = newton_sistema(p0)
        print(f"Solução encontrada: x1 = {solucao[0]:.4f}, x2 = {solucao[1]:.4f}")
        plot_solucao(historico)
    except Exception as e:
        print(f"Erro durante a execução: {str(e)}")
