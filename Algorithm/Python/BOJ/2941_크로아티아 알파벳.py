input = input()
croa = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in croa:
    if i in input:
        input = input.replace(i, '*')
print(len(input))