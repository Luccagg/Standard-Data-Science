from matplotlib import pyplot as plt

# DATA
friends = [ 70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
plt.scatter(friends, minutes)
#plt.show()
for i, j, k in zip(labels, friends, minutes):
    plt.annotate(i, xy=(j, k), xytext=(5,5),textcoords='offset points')

plt.title("Diary minutes vs friends number")
plt.xlabel("# friends")
plt.ylabel("min passed in site")
plt.show()
