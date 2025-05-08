import math
from collections import Counter, defaultdict

def entropy(examples):
    label_counts = Counter(example['label'] for example in examples)
    total = len(examples)
    ent = 0.0
    for count in label_counts.values():
        p = count / total
        ent -= p * math.log2(p)
    return ent

def information_gain(examples, attr):
    base_entropy = entropy(examples)
    subsets = defaultdict(list)
    for ex in examples:
        subsets[ex[attr]].append(ex)
    total = len(examples)
    subset_entropy = 0.0
    for subset in subsets.values():
        subset_entropy += (len(subset) / total) * entropy(subset)
    return base_entropy - subset_entropy

def majority_label(examples):
    label_counts = Counter(example['label'] for example in examples)
    return label_counts.most_common(1)[0][0]

def id3(examples, attributes, default=None):
    if not examples:
        return default
    labels = [ex['label'] for ex in examples]
    if labels.count(labels[0]) == len(labels):
        return labels[0]
    if not attributes:
        return majority_label(examples)
    gains = [(information_gain(examples, attr), attr) for attr in attributes]
    best_gain, best_attr = max(gains, key=lambda x: x[0])
    if best_gain == 0:
        return majority_label(examples)
    
    tree = {best_attr: {}}
    values = set(ex[best_attr] for ex in examples)
    for v in values:
        subset = [ex for ex in examples if ex[best_attr] == v]
        remaining_attrs = [a for a in attributes if a != best_attr]
        subtree = id3(subset, remaining_attrs, default=majority_label(examples))
        tree[best_attr][v] = subtree
    return tree

def classify(tree, example):
    if not isinstance(tree, dict):
        return tree
    attr = next(iter(tree))
    subtree = tree[attr].get(example.get(attr))
    if subtree is None:
        return None
    return classify(subtree, example)
if __name__ == '__main__':
    data = [
        {'Outlook':'Sunny','Temperature':'Hot','Humidity':'High','Wind':'Weak','label':'No'},
        {'Outlook':'Sunny','Temperature':'Hot','Humidity':'High','Wind':'Strong','label':'No'},
        {'Outlook':'Overcast','Temperature':'Hot','Humidity':'High','Wind':'Weak','label':'Yes'},
        {'Outlook':'Rain','Temperature':'Mild','Humidity':'High','Wind':'Weak','label':'Yes'},
        {'Outlook':'Rain','Temperature':'Cool','Humidity':'Normal','Wind':'Weak','label':'Yes'},
        {'Outlook':'Rain','Temperature':'Cool','Humidity':'Normal','Wind':'Strong','label':'No'},
        {'Outlook':'Overcast','Temperature':'Cool','Humidity':'Normal','Wind':'Strong','label':'Yes'},
        {'Outlook':'Sunny','Temperature':'Mild','Humidity':'High','Wind':'Weak','label':'No'},
        {'Outlook':'Sunny','Temperature':'Cool','Humidity':'Normal','Wind':'Weak','label':'Yes'},
        {'Outlook':'Rain','Temperature':'Mild','Humidity':'Normal','Wind':'Weak','label':'Yes'},
        {'Outlook':'Sunny','Temperature':'Mild','Humidity':'Normal','Wind':'Strong','label':'Yes'},
        {'Outlook':'Overcast','Temperature':'Mild','Humidity':'High','Wind':'Strong','label':'Yes'},
        {'Outlook':'Overcast','Temperature':'Hot','Humidity':'Normal','Wind':'Weak','label':'Yes'},
        {'Outlook':'Rain','Temperature':'Mild','Humidity':'High','Wind':'Strong','label':'No'},
    ]
    attrs = ['Outlook', 'Temperature', 'Humidity', 'Wind']
    tree = id3(data, attrs)
    print("Learned tree:")
    print(tree)
    
    test = {'Outlook':'Rain','Temperature':'Cool','Humidity':'High','Wind':'Strong'}
    print("Prediction for", test, "->", classify(tree, test))
