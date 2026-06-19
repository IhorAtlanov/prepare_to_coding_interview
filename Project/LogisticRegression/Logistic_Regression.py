import numpy as np

class LogisticRegressionFromScratch:
  def __init__(self, learning_rate, epochs):
    self.learning_rate = learning_rate
    self.epochs = epochs
    self.weights = None
    self.bias = None
    self.loss_history = []
    
  def _sigmoid(self, z):
    return 1/ (1+ np.exp(-z))  
  
    
  def fit(self, X, y):
    n_samples, n_features = X.shape
    self.weights = np.zeros((n_features, 1))
    self.bias = 0.0
    
    y = y.reshape(-1, 1)
    
    for _ in range(self.epochs):
      # 1. Forward propagation
      z = np.dot(X, self.weights) + self.bias
      y_pred = self._sigmoid(z)
      
      # 2. Compute cost (Log-Loss)
      epsilon = 1e-15
      y_pred = np.clip(y_pred, epsilon, 1 - epsilon)
      loss = -1 / n_samples * np.sum(y * np.log(y_pred) + (1 - y) * np.log(1 - y_pred))
      self.loss_history.append(loss)
      
      # 3. Backward propagation
      dw = 1 / n_samples * np.dot(X.T, (y_pred - y))
      db = 1 / n_samples * np.sum(y_pred - y)

      # 4. Update parameters
      self.weights -= self.learning_rate * dw
      self.bias -= self.learning_rate * db
      
      if _ % 100 ==0:
        print(f'Epoch {_}, Loss: {loss:.4f}')
    
    print(f'Final Loss: {self.loss_history[-1]:.4f}')
      
  def predict_proba(self, X):
    z = np.dot(X, self.weights) + self.bias # type: ignore
    return self._sigmoid(z)
  
  def predict(self, X):
    y_proba = self.predict_proba(X)
    return np.where(y_proba >= 0.5, 1, 0)
