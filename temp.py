import csv

indices = ['1', '2', '3', '4']
results = []
with open('data/LeetCode.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if str(i) in indices:
            problem_name = row[0]
            problem_link = row[1]
            results.append([problem_name, problem_link])

# print(results)