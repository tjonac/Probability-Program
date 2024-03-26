import matplotlib.pyplot as plt
 
## Declaramos valores para el eje x
eje_x = ['Python', 'R', 'Node.js', 'PHP']
 
## Declaramos valores para el eje y
eje_y = [50,20,35,47]
 
## Creamos Gráfica
plt.bar(eje_x, eje_y, color="#757bc8")
 
## Mostramos Gráfica
plt.show()