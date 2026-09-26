numbers = list(map(int,input("Enter List :-").split()))
lookup =set()
res = []
for i in numbers:
    if i not in lookup:
        lookup.add(i)
        res.append(i)

print(f"Original List :- {numbers}\nList After Removing Duplicates :- {res}")