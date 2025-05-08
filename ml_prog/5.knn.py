import numpy as np
from collections import Counter

def euclidean(a,b):
    return np.sqrt(np.sum((a-b)**2))

def knn(X_train,y_train,x_test,k):
    distances=[(euclidean(x_test,x),label) for x,label in zip(X_train,y_train)]
    neighbors=sorted(distances,key=lambda t:t[0])[:k]
    votes=[label for _,label in neighbors]
    vote_counts=Counter(votes)
    prediction=vote_counts.most_common(1)[0][0]
    return neighbors,vote_counts,prediction

X_train=np.array([[1,2],[2,3],[3,1],[6,5],[7,7],[8,6]])
y_train=np.array([0,0,0,1,1,1])
X_test=np.array([[2,2],[7,5]])
k=3

for point in X_test:
    neighbors,vote_counts,pred=knn(X_train,y_train,point,k)
    print("Test point",point)
    print("Nearest neighbors (distance,label):",neighbors)
    print("Vote counts:",dict(vote_counts))
    print("Predicted label:",pred,"\n")
