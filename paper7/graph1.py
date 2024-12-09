from main import *

"Визуализация показывает различие между видами ирисов по длине и ширине лепестков, где Iris-setosa явно выделяется."

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.scatterplot(data=iris_data, x="PetalLengthCm", y="PetalWidthCm", hue="Species", palette="bright")
plt.title('Длина и ширина лепестков')
plt.xlabel('Длина лепестка (см)')
plt.ylabel('Ширина лепестка (см)')
plt.axhline(0, color='grey', lw=0.5)
plt.axvline(0, color='grey', lw=0.5)
plt.grid()
plt.show()