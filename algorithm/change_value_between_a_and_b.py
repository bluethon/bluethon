a = 5
b = 3

print('a: %s\tb: %s' % (a, b))

a = a ^ b
print('a: %s\tb: %s' % (a, b))
b = a ^ b
print('a: %s\tb: %s' % (a, b))
a = a ^ b

print('a: %s\tb: %s' % (a, b))
