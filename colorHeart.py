import numpy as np
import matplotlib.pyplot as plt
import time

x_coords = np.linspace(-100, 100, 500)
y_coords = np.linspace(-100, 100, 500)
points = []
for y in y_coords:
    for x in x_coords:
        if ((x*0.03)**2+(y*0.03)**2-1)**3-(x*0.03)**2*(y*0.03)**3 <= 0:
            points.append({"x": x, "y": y})
heart_x = list(map(lambda point: point["x"], points))
heart_y = list(map(lambda point: point["y"], points))

# color_list = ["autumn", "cool", "magma", "Reds", "spring", "viridis", "gist_rainbow"]
# all_color link:https://matplotlib.org/examples/color/colormaps_reference.html

# for color in color_list:	
# 	plt.scatter(heart_x, heart_y, s=10, alpha=0.5, c=range(len(heart_x)), cmap=color)
# 	plt.show()
# 	time.sleep(1)
# 	plt.clf()
plt.scatter(heart_x, heart_y, s=10, alpha=0.5, c=range(len(heart_x)), cmap="cool")
plt.title('Raku')
plt.text(-5, 0, 'Raku', fontproperties = 'Microsoft Yahei',fontsize = 20)
plt.show()
plt.clf()