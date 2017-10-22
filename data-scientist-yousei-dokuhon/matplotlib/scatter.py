import matplotlib.pyplot as plt

x=[1,2,3,4]
y=[3,5,4,7]
plt.scatter(x,y)
plt.show()

# 複数系列を含む散布図
y1=[1,5,4,3]
y2=[5,4,1,7]

plt.scatter(x,y1,marker="o",c="b")
plt.scatter(x,y2,marker="+",c="r")
plt.show()