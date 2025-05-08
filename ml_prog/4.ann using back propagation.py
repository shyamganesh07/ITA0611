import numpy as np

def sigmoid(x):
    return 1.0/(1.0+np.exp(-x))

def sigmoid_derivative(y):
    return y*(1-y)

class SimpleANN:
    def __init__(self, n_inputs, n_hidden, n_outputs, learning_rate=0.5):
        self.lr=learning_rate
        self.w_input_hidden=np.random.randn(n_inputs+1,n_hidden)*0.1
        self.w_hidden_output=np.random.randn(n_hidden+1,n_outputs)*0.1

    def forward(self,X):
        X_bias=np.append(X,1.0)
        self.hidden_out=sigmoid(np.dot(X_bias,self.w_input_hidden))
        hidden_bias=np.append(self.hidden_out,1.0)
        self.final_out=sigmoid(np.dot(hidden_bias,self.w_hidden_output))
        return self.final_out

    def backward(self,X,y_true):
        y_pred=self.forward(X)
        delta_output=(y_true-y_pred)*sigmoid_derivative(y_pred)
        w_ho_no_bias=self.w_hidden_output[:-1,:]
        delta_hidden=np.dot(delta_output,w_ho_no_bias.T)*sigmoid_derivative(self.hidden_out)
        hidden_bias=np.append(self.hidden_out,1.0).reshape(-1,1)
        self.w_hidden_output+=self.lr*np.dot(hidden_bias,delta_output.reshape(1,-1))
        X_bias=np.append(X,1.0).reshape(-1,1)
        self.w_input_hidden+=self.lr*np.dot(X_bias,delta_hidden.reshape(1,-1))
        return np.mean((y_true-y_pred)**2)

    def train(self,X_train,y_train,epochs=1000):
        for epoch in range(epochs):
            mse=0.0
            for X,y in zip(X_train,y_train):
                mse+=self.backward(X,y)
            if epoch%100==0:
                print(f"Epoch {epoch}, MSE: {mse/len(X_train):.4f}")

    def predict(self,X):
        return (self.forward(X)>0.5).astype(int)

if __name__=="__main__":
    X=np.array([[0,0],[0,1],[1,0],[1,1]])
    y=np.array([[0],[1],[1],[0]])
    ann=SimpleANN(2,2,1,0.5)
    ann.train(X,y,5000)
    for xi,yi in zip(X,y):
        print("Input:",xi,"Predicted:",ann.predict(xi)[0],"True:",yi[0])
