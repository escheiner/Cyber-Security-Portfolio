import re

filename = "kennedy.txt"
regex_pattern =r'\b(\w+)\b'

outcomes = {}

with open(filename,'r') as f:
    line = f.readline().strip()
    while line:
        results = re.findall(regex_pattern,line)
        for res in  results:
            res = res.lower()
            if res in outcomes.keys():
                outcomes[res] += 1
            else:
                outcomes[res] = 1
        line = f.readline()

# Sort the dictionary object, descending by value, words with highest occurance first
outcomes_sorted = sorted(outcomes.items(), key=lambda x: x[1], reverse=True)
#for word,occurances in outcomes_sorted:
print("Most frequent IP address",":\t", outcomes_sorted[0],)
