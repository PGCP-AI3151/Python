colors = {'red','pink','green','blue','yellow','white'}
color_l = ['black','red','pink','purple','sky','white','orange']

print(colors)

for color in colors:
    print(color)

print('red' in colors)
print('black' not in colors)

colors.add('orange')
print(colors)

colors.pop()
print(colors)

colors.remove('white')

print(colors)

colors.add('white')

print(colors)
print(color_l)

u_set = colors.union(color_l)
print(u_set)

color_l = set(color_l)

u_set = colors | color_l
print(u_set)

i_set = colors.intersection(color_l)
print(i_set)

i_set = colors & color_l
print(i_set)

d_set = colors.difference(color_l)
print(d_set)

d_set = colors - color_l
print(d_set)

s_set = colors ^ color_l
print(s_set)