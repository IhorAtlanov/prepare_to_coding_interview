import numpy as np
import matplotlib.pyplot as plt

from LinearReg import LinearRegression_From_Scratch

def main():
  # Generate some sample data
  X = np.random.rand(100, 1)
  Y = (1 * X + np.random.rand(100, 1) * 0.1).flatten()

  # Create and train the model
  model = LinearRegression_From_Scratch(epochs=1000, learning_rate=0.01)
  model.fit(X, Y)
  
  y_predict = model.predict(X)
  
  plt.figure(figsize=(10, 6))
  plt.scatter(X, Y, color='blue', label='Data Points')
  plt.plot(X, y_predict, color='red', label='Predicted Line')
  plt.xlabel('X')
  plt.ylabel('Y')
  plt.title('Linear Regression')
  plt.legend()
  plt.show()

if __name__ == "__main__":
  main()