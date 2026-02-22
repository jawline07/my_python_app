alpha = 'abcdefghijklmnopqrstuvwxyz'

i = 0
print(alpha[i])  # a
print(alpha[i+1])  # b

print(type(alpha))
print(alpha.isalpha())
print(alpha.isnumeric())
print(alpha.upper())


name = "Ajith"
name = name.lower()
print(alpha[alpha.index(name[0])+1]+alpha[alpha.index(name[1])+1] +
      alpha[alpha.index(name[2])+1]+alpha[alpha.index(name[3])+1]+alpha[alpha.index(name[4])+1])
