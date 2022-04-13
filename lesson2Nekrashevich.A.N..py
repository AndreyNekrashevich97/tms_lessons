# 1. создать 3 переменные с одинаковыми данными с одинаковыми идентификаторами.
m = 'mark'
print(m)
print(id(m))
m1 = m
print(m1)
print(id(m1))
m2 = m
print(m2)
print(id(m2))

# 2. cоздать 2ерменные с одинаковыми данными с разными идентификаторами.
m3 = ['mark']
print(m3)
print(id(m3))
m4 = ['mark']
print(m4)
print(id(m4))

# 3. поменять их типы так, чтобы у 1х трех были разные идентификаторы,а у 2х последних были одинаковые.

m5 = ['mark']
print(m5)
print(id('m5'))
m6 = ['mark']
print(m6)
print(id(m6))
m7 = ['mark']
print(m7)
print(id(m7))
m8 = 'mark'
print(m8)
print(id(m8))
m9 = 'mark'
print(m9)
print(id(m9))