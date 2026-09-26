numbers = tuple(map(int,input("Enter Numbers :- ").split()))
lookup = set()
res = []
for i in numbers:
    if i  in lookup:
        res.append(i)
    lookup.add(i)

print(f"Original Tuple :- {numbers}\nRepeated Element :- {res}")