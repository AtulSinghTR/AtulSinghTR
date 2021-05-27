def score(word):
    marks = {'1':['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'], '2':['D', 'G' ], '3': ['B', 'C', 'M', 'P'], '4': ['F', 'H', 'V', 'W', 'Y'], '5': ['K'], '8': ['J', 'K'], '10': ['Q','Z']}
    print(marks.values())
    
    if 'A' in marks.values():
        print('exists')
    

print(score('ABCD'))