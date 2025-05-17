import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations_with_replacement

# 1. Generate non-linearly separable data (like microchip test results)
np.random.seed(0)
m = 100
x1 = np.random.uniform(-1, 1, m)
x2 = np.random.uniform(-1, 1, m)
y = ((x1**2 + x2**2 + 0.25 * np.random.randn(m)) < 0.8).astype(int)

X = np.column_stack((x1, x2))

# 2. Map features into polynomial terms
def map_feature(x1, x2, degree=6):
    terms = [np.ones_like(x1)]
    for i in range(1, degree + 1):
        for j in range(i + 1):
            terms.append((x1 ** (i - j)) * (x2 ** j))
    return np.column_stack(terms)

X_poly = map_feature(X[:, 0], X[:, 1])
theta = np.zeros(X_poly.shape[1])

# 3. Sigmoid, cost, gradient with regularization
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def compute_cost_reg(X, y, theta, lambda_):
    m = len(y)
    h = sigmoid(X @ theta)
    reg_term = (lambda_ / (2 * m)) * np.sum(theta[1:] ** 2)
    return -(1/m) * np.sum(y * np.log(h) + (1 - y) * np.log(1 - h)) + reg_term

def gradient_reg(X, y, theta, lambda_):
    m = len(y)
    h = sigmoid(X @ theta)
    grad = (1/m) * (X.T @ (h - y))
    grad[1:] += (lambda_ / m) * theta[1:]
    return grad

# 4. Gradient descent optimizer
def gradient_descent(X, y, theta, alpha, iterations, lambda_):
    for _ in range(iterations):
        grad = gradient_reg(X, y, theta, lambda_)
        theta -= alpha * grad
    return theta

# 5. Plot decision boundary
def plot_decision_boundary(X, y, theta, lambda_):
    u = np.linspace(-1, 1.5, 50)
    v = np.linspace(-1, 1.5, 50)
    z = np.zeros((len(u), len(v)))

    for i in range(len(u)):
        for j in range(len(v)):
            mapped = map_feature(np.array([u[i]]), np.array([v[j]]))
            z[i, j] = mapped @ theta

    plt.contourf(u, v, z.T >= 0, alpha=0.3, cmap='coolwarm')
    plt.contour(u, v, z.T, levels=[0], linewidths=2, colors='black')

    plt.scatter(X[:, 0][y == 1], X[:, 1][y == 1], c='blue', label='Pass')
    plt.scatter(X[:, 0][y == 0], X[:, 1][y == 0], c='red', label='Fail')
    plt.title(f"Decision Boundary (λ={lambda_})")
    plt.xlabel("Microchip Test 1")
    plt.ylabel("Microchip Test 2")
    plt.legend()
    plt.show()

# 6. Train for different lambdas and plot
lambdas = [0, 1, 100]
alpha = 1
iterations = 1000

for lambda_ in lambdas:
    theta = np.zeros(X_poly.shape[1])
    theta = gradient_descent(X_poly, y, theta, alpha, iterations, lambda_)
    plot_decision_boundary(X, y, theta, lambda_)

    predictions = (sigmoid(X_poly @ theta) >= 0.5).astype(int)
    acc = np.mean(predictions == y) * 100
    print(f"λ = {lambda_} | Training Accuracy = {acc:.2f}%")
