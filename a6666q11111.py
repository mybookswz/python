import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

# Helper functions
def generate_binomial_tree(S, u, d, n):
    return [[S * (u ** j) * (d ** (i - j)) for j in range(i + 1)] for i in range(n + 1)]

def draw_binomial_tree(tree, title, node_color="lightblue"):
    G = nx.DiGraph()
    pos = {}
    labels = {}

    for i in range(len(tree)):
        for j in range(len(tree[i])):
            node = f"{i}-{j}"
            G.add_node(node)
            pos[node] = (i, -j)
            labels[node] = f"{tree[i][j]:.2f}"

            if i > 0:
                if j < len(tree[i - 1]):
                    G.add_edge(f"{i - 1}-{j}", node)
                if j > 0:
                    G.add_edge(f"{i - 1}-{j - 1}", node)

    plt.figure(figsize=(10, 5))
    nx.draw(G, pos, with_labels=False, node_size=1500, node_color=node_color)
    nx.draw_networkx_labels(G, pos, labels, font_size=10)
    plt.title(title)
    plt.axis("off")
    plt.show()

# Parameters for Problem 11
S = 484
K = 480
r = 0.10
q = 0.03
sigma = 0.25
T = 2 / 12
n = 4

dt = T / n
u = np.exp(sigma * np.sqrt(dt))
d = 1 / u
p = (np.exp((r - q) * dt) - d) / (u - d)
discount = np.exp(-r * dt)

# Stock price tree
stock_tree = generate_binomial_tree(S, u, d, n)

# Option value tree
option_tree = [[0] * (i + 1) for i in range(n + 1)]
for j in range(n + 1):
    option_tree[n][j] = max(K - stock_tree[n][j], 0)
for i in range(n - 1, -1, -1):
    for j in range(i + 1):
        stock_price = stock_tree[i][j]
        hold = discount * (p * option_tree[i + 1][j + 1] + (1 - p) * option_tree[i + 1][j])
        exercise = max(K - stock_price, 0)
        option_tree[i][j] = round(max(hold, exercise), 4)

# Draw Trees
draw_binomial_tree(stock_tree, "Stock Price Tree (Problem 11)", node_color="skyblue")
draw_binomial_tree(option_tree, "American Put Option Tree (Problem 11)", node_color="salmon")

print("American Put Option Value (Problem 11):", option_tree[0][0])
