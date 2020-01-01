# Week 4

# understanding how lists are stored
a = [5,10]
b = a
print("a: {}\t b:{}".format(a,b))
print("Location a[0]: {}\t Location b[0]: {}".format(id(a[0]),id(b[0])))
a[0] = 30
print("a: {}\t b: {}".format(a,b))
