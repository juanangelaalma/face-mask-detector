from unicodedata import name


data = []

names = [["juan", "angela", "alma"], ["aldila", "elfana", "fauziza"]]

for i in range(len(names)):
  x = []
  for j in names[i]:
    x.append(j)
  data.append(x)


print(data)