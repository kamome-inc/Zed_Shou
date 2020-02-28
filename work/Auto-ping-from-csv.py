from pythonping import ping


a = open('1.csv', 'r')
b = a.readlines()
a.close()
arr = []
for line in b:
    mass_value = [line.split(';')[0], line.split(';')[3].strip(' ')]
    arr.append(mass_value)

for name, adr in arr[:]:
    if 6 < len(adr) < 16:
        print(adr)
        print(ping(adr))
        # print(name + ' ' + str(resp))