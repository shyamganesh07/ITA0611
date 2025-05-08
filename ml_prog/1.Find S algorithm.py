def find_s_algorithm(dataset):
    for example in dataset:
        if example[-1] == 'Yes':
            hypothesis = example[:-1]
            break
    for example in dataset:
        if example[-1] == 'Yes':  
            for i in range(len(hypothesis)):
                if hypothesis[i] != example[i]:
                    hypothesis[i] = '?' 
    return hypothesis
data = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']
]
hypothesis = find_s_algorithm(data)
print("Final Hypothesis:", hypothesis)
