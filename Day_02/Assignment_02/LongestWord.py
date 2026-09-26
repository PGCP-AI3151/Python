def longsword(word):
    lengths = [len(item) for item in word]
    idx=lengths.index(max(lengths))
    print(f'Word :- {word[idx]}')
    print(f'Length :- {lengths[idx]}')


words = input("Enter List Of Words :-").split()
print("-----Longest Word-----")
longsword(words)
