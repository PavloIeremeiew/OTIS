import matplotlib.pyplot as plt
import numpy as np
#x=list(range(-10,10))
x = np.linspace(-10, 10)
y=0.3*x**2+abs(x)
plt.plot(x, y,'g--', label='f(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.savefig('function.png',dpi=500)
plt.show()