import csv
with open("C:\\Users\\ganes\\Downloads\\dataset.csv") as file:
    data = [row for row in csv.reader(file)]
    header = data[0]
    data = data[1:]
num_attributes = len(data[0]) - 1
S = data[0][:-1] if data[0][-1] == 'Yes' else ['∅'] * num_attributes
G = [['?'] * num_attributes]
for row in data:
    inputs, output = row[:-1], row[-1]
    
    if output == 'Yes':
        for i in range(num_attributes):
            if S[i] != inputs[i]:
                S[i] = '?'
        G = [g for g in G if all(g[i] == '?' or g[i] == S[i] for i in range(num_attributes))]
        
    else:
        new_G = []
        for i in range(num_attributes):
            if S[i] != '?' and S[i] != inputs[i]:
                new_hypothesis = ['?'] * num_attributes
                new_hypothesis[i] = S[i]
                new_G.append(new_hypothesis)
        G.extend(new_G)
print("Final Specific Hypothesis (S):", S)
print("Final General Hypotheses (G):")
for g in G:
    print(g)
