import numpy as np

class LinearRegression_From_Scratch:
    def __init__(self, epochs, learning_rate):
      self.epochs = epochs
      self.learning_rate = learning_rate
      self.weights = None
      self.bias = None
    
    def fit(self, X, Y):
      n_sample, n_features = X.shape
      
      self.weights = np.zeros(n_features)
      self.bias = 0
      
      for epoch in range(self.epochs):
        y_predict = np.dot(X, self.weights) + self.bias
        
        dw = (2 / n_sample) * np.dot(X.T, (y_predict - Y))
        db = (2 / n_sample) * np.sum(y_predict - Y)
        
        self.weights -= self.learning_rate * dw
        self.bias -= self.learning_rate * db
        
        if epoch % 100 == 0:
          print(f"Epoch {epoch}: Weights: {self.weights}, Bias: {self.bias}")
          loss = np.mean((Y - y_predict) ** 2)
          print(f"Loss: {loss:.4f}")
      
    def predict(self, X):
      return np.dot(X, self.weights) + self.bias # type: ignore