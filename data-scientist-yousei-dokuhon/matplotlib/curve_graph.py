import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-5,5,100) # -5から5までの間を100個に刻む
print("np.linspace(-5,5,100): \n{}".format(np.linspace(-5,5,100)))
y=x**2 # ブロードキャスティングを使っている
print("y: \n{}".format(y))

plt.plot(x,y)
plt.show()