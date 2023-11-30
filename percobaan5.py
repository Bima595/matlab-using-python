import matplotlib.pyplot as plt
import numpy as np

sample = np.random.normal(loc=50, scale=5, size=1000)

print(sample)

plt.title('Histogram Sample Data Normal')
plt.xlabel('Nilai')
plt.ylabel('Frekuensi Relatif')
plt.hist(sample, bins=4, density=True)
plt.show()