cubes = {}
for i in range(3,9):
    cubes[i] = i**4
for k in cubes.keys():
    print("{} : {}".format(k,cubes[k]))
