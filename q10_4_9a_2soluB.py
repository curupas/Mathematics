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

# 3. Método de Newton melhorado
def newton_sistema(p0, tol=1e-6, max_iter=100):
    historico = [np.array(p0)]
    p = np.array(p0, dtype=float)
    
    for k in range(max_iter):
        F = sistema(p)
        J = jacobiana(p)
        try:
            delta_p = np.linalg.solve(J, -F)
        except np.linalg.LinAlgError:
            print("Matriz Jacobiana singular. Tentando ajuste...")
            delta_p = np.linalg.lstsq(J, -F, rcond=None)[0]
        
        p += delta_p
        historico.append(p.copy())
        
        if np.linalg.norm(delta_p) < tol:
            return p, historico
    print("Aviso: Máximo de iterações alcançado sem convergência.")
    return p, historico

# 4. Função para encontrar todas as soluções
def encontrar_solucoes(pontos_iniciais):
    solucoes = []
    for p0 in pontos_iniciais:
        sol, hist = newton_sistema(p0)
        # Verificar se é uma nova solução
        nova_sol = True
        for s in solucoes:
            if np.linalg.norm(s - sol) < 0.1:  # tolerância para considerar mesma solução
                nova_sol = False
                break
        if nova_sol:
            solucoes.append(sol)
            print(f"Solução encontrada a partir de {p0}: x1 = {sol[0]:.6f}, x2 = {sol[1]:.6f}")
            print(f"Verificação: f1 = {sistema(sol)[0]:.2e}, f2 = {sistema(sol)[1]:.2e}\n")
    return solucoes

# 5. Função de plotagem atualizada
def plot_solucao_completa(solucoes):
    plt.figure(figsize=(12, 10))
    
    # Definir região de plotagem para mostrar ambas as soluções
    x1_min, x1_max = -2, 6
    x2_min, x2_max = 0, 6
    x1 = np.linspace(x1_min, x1_max, 400)
    x2 = np.linspace(x2_min, x2_max, 400)
    X1, X2 = np.meshgrid(x1, x2)
    
    F1 = X1 * (1 - X1) + 4 * X2 - 12
    F2 = (X1 - 2)**2 + (2 * X2 - 3)**2 - 25
    
    # Plot das curvas
    plt.contour(X1, X2, F1, levels=[0], colors='blue', linewidths=3, alpha=0.7)
    plt.contour(X1, X2, F2, levels=[0], colors='red', linewidths=3, alpha=0.7)
    plt.contour(X1, X2, F1, levels=np.linspace(-20, 20, 11), colors='blue', linewidths=1, alpha=0.2)
    plt.contour(X1, X2, F2, levels=np.linspace(-20, 20, 11), colors='red', linewidths=1, alpha=0.2)
    
    # Plot das soluções
    cores = ['gold', 'lime', 'cyan', 'magenta']
    for i, sol in enumerate(solucoes):
        plt.scatter(sol[0], sol[1], color=cores[i%len(cores)], s=200, edgecolors='black', 
                    zorder=5, label=f'Solução {i+1}: ({sol[0]:.4f}, {sol[1]:.4f})')
    
    # Configurações do gráfico
    plt.xlabel('$x_1$', fontsize=14)
    plt.ylabel('$x_2$', fontsize=14)
    plt.title('Soluções do Sistema Não-Linear', fontsize=16)
    plt.grid(True, linestyle='--', alpha=0.3)
    plt.legend(fontsize=12, loc='best')
    plt.axis('equal')
    plt.xlim(x1_min, x1_max)
    plt.ylim(x2_min, x2_max)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Pontos iniciais para encontrar todas as soluções
    pontos_iniciais = [
        [0, 0],      # Primeiro chute inicial
        [3, 3],      # Para encontrar a solução à direita
        [2, 4],      # Outro ponto para garantir
        [5, 2]       # Mais um ponto inicial
    ]
    
    print("Encontrando todas as soluções...\n")
    solucoes = encontrar_solucoes(pontos_iniciais)
    
    if len(solucoes) > 0:
        print("\nTodas as soluções encontradas:")
        for i, sol in enumerate(solucoes):
            print(f"Solução {i+1}: x1 = {sol[0]:.8f}, x2 = {sol[1]:.8f}")
            print(f"  f1(x) = {sistema(sol)[0]:.2e}")
            print(f"  f2(x) = {sistema(sol)[1]:.2e}\n")
        
        plot_solucao_completa(solucoes)
    else:
        print("Nenhuma solução foi encontrada.")
        