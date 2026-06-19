import numpy as np
import matplotlib.pyplot as plt

from Logistic_Regression import LogisticRegressionFromScratch

np.random.seed(42)

def main():
  X = np.random.rand(1000, 1)
  
  noise = np.random.normal(0, 0.05, size=X.shape)
  y = ((X + noise) > 0.5).astype(int)

  model = LogisticRegressionFromScratch(learning_rate=0.2, epochs=1000)
  model.fit(X, y)
  
  y_pred = model.predict(X)
  
  plt.figure(figsize=(10, 6))
  plt.scatter(X, y, color="blue", alpha=0.5, label="True Classes", s=80)
  plt.scatter(X, y_pred, color="red", marker="x", label="Predicted Classes", s=50)
  
  # Decision Boundary
  w = model.weights[0][0]
  b = model.bias
  decision_boundary = - (b / w)
  plt.axvline(
      x=decision_boundary,
      color="green",
      linestyle="--",
      label=f"Decision Boundary ({decision_boundary:.2f})",
  )
  
  # ГЕНЕРАЦІЯ ЛІНІЇ СИГМОЇДИ
  # Створюємо 500 рівновіддалених точок від 0 до 1 для плавної кривої
  X_curve = np.linspace(0, 1, 500).reshape(-1, 1)
  # Отримуємо ймовірності для цих точок від нашої моделі
  y_curve_proba = model.predict_proba(X_curve)

  # Малюємо криву ймовірностей (Сигмоїду)
  plt.plot(
      X_curve,
      y_curve_proba,
      color="purple",
      linewidth=2.5,
      label="Sigmoid (Predicted Probability)",
  )
  
  plt.xlabel("Feature X")
  plt.ylabel("Class y")
  plt.title("Logistic Regression from Scratch - Predictions")
  plt.legend()
  plt.grid(True, alpha=0.3)
  plt.show()

if __name__ == "__main__":
  main()