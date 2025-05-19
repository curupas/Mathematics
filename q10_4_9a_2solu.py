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

# 3. Implementar o método de Newton
def newton_sistema(p0, tol=1e-4, max_iter=100):
    historico = [np.array(p0)]
    p = np.array(p0, dtype=float)
    
    print(f"p0 = [{p[0]:.4f}, {p[1]:.4f}]")
    print(f"f1(p0) = {sistema(p)[0]:.4f}, f2(p0) = {sistema(p)[1]:.4f}\n")
    
    for k in range(max_iter):
        F = sistema(p)
        J = jacobiana(p)
        delta_p = np.linalg.solve(J, -F)
        p += delta_p
        historico.append(p.copy())
        
        print(f"p{k+1} = [{p[0]:.4f}, {p[1]:.4f}]")
        print(f"f1(p{k+1}) = {sistema(p)[0]:.4f}, f2(p{k+1}) = {sistema(p)[1]:.4f}")
        print(f"Delta: [{delta_p[0]:.4f}, {delta_p[1]:.4f}]\n")
        
        if np.linalg.norm(delta_p) < tol:
            print(f"Convergência alcançada após {k+1} iterações.")
            return p, historico
    print("Máximo de iterações alcançado sem convergência.")
    return p, historico

# 4. Função de plotagem melhorada
def plot_solucao(historico):
    plt.figure(figsize=(12, 10))
    
    # Definir regiões de plotagem - ajustamos x1_max para incluir mais à direita
    historico_array = np.array(historico)
    x1_min = min(historico_array[:,0])-1
    x1_max = max(3.0, max(historico_array[:,0])+1)  # Pelo menos até x1=3, ou mais se necessário
    x2_min = min(historico_array[:,1])-1
    x2_max = max(historico_array[:,1])+1
    
    # Criar grid - aumentamos o limite superior de x1
    x1 = np.linspace(x1_min, x1_max, 400)
    x2 = np.linspace(x2_min, x2_max, 400)
    X1, X2 = np.meshgrid(x1, x2)
    
    # Calcular as funções
    F1 = X1 * (1 - X1) + 4 * X2 - 12
    F2 = (X1 - 2)**2 + (2 * X2 - 3)**2 - 25
    
    # Plot das curvas (mantido igual)
    plt.contour(X1, X2, F1, levels=np.linspace(-20, 20, 11), colors='blue', linewidths=1, alpha=0.3)
    plt.contour(X1, X2, F1, levels=[0], colors='blue', linewidths=3)
    plt.contour(X1, X2, F2, levels=np.linspace(-20, 20, 11), colors='red', linewidths=1, alpha=0.3)
    plt.contour(X1, X2, F2, levels=[0], colors='red', linewidths=3)
    
    # Trajetória de Newton (mantido igual)
    plt.plot(historico_array[:, 0], historico_array[:, 1], 'o-', color='green', 
             markersize=6, linewidth=1.5, alpha=0.7, label='Trajetória de Newton')
    
    # Destacar pontos importantes (mantido igual)
    for i, p in enumerate(historico_array):
        if i == 0:
            plt.scatter(p[0], p[1], color='cyan', s=100, edgecolors='black', zorder=5, label=f'p0 ({p[0]:.1f}, {p[1]:.1f})')
        elif i == 1:
            plt.scatter(p[0], p[1], color='orange', s=100, edgecolors='black', zorder=5, label=f'p1 ({p[0]:.1f}, {p[1]:.1f})')
        elif i == 2:
            plt.scatter(p[0], p[1], color='purple', s=100, edgecolors='black', zorder=5, label=f'p2 ({p[0]:.1f}, {p[1]:.1f})')
    
    # Solução final (mantido igual)
    solucao = historico_array[-1]
    plt.scatter(solucao[0], solucao[1], color='gold', s=150, edgecolors='black', 
                zorder=5, label=f'Solução ({solucao[0]:.4f}, {solucao[1]:.4f})')
    
    # Configurações do gráfico (mantido igual)
    plt.xlabel('$x_1$', fontsize=14)
    plt.ylabel('$x_2$', fontsize=14)
    plt.title('Método de Newton para Sistema Não-Linear', fontsize=16)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend(fontsize=12, loc='upper right')
    plt.axis('equal')
    
    # Ajustar limites - modificamos para forçar mostrar mais à direita
    buffer_x1 = 0.5  # Reduzimos o buffer para não cortar a direita
    buffer_x2 = 0.2 * (x2_max - x2_min)
    
    # Garantir que estamos mostrando até pelo menos x1=3
    x1_right = max(x1_max, 3.0)
    plt.xlim(x1_min - buffer_x1, x1_right + buffer_x1)
    plt.ylim(x2_min - buffer_x2, x2_max + buffer_x2)
    
    plt.tight_layout()
    plt.show()
    
if __name__ == "__main__":
    p0 = [0.0, 0.0]
    try:
        solucao, historico = newton_sistema(p0)
        print(f"\nSolução encontrada: x1 = {solucao[0]:.6f}, x2 = {solucao[1]:.6f}")
        plot_solucao(historico)
    except Exception as e:
        print(f"Erro durante a execução: {str(e)}")
