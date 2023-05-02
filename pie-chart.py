import matplotlib.pyplot as plt
labels = 'Nenhum','Fundamental','Médio','Superior'
sizes = [86026, 28525, 57394, 25286]
colors = [ 'lightgray', 'orange', 'coral', 'red']
patches, texts, autotexts = plt.pie(sizes, colors=colors, autopct='%1.1f%%',
startangle=90)
plt.legend(patches, labels, loc="lower right")
plt.axis('equal')
plt.show()