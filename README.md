# Búsqueda de anillos con clustering

### Estructura del código:
Se ha divido el código en 5 archivos diferentes.
- schema.py: Aquí se guarda la estructuras de datos necesaria para el algoritmo.
- methods.py: Se encuentran todos los métodos usados para este trabajo.
- plot_state.py: métodos para mostrar las gráficas necesarias.
- soft_clustering.py: El archivo principal del trabajo, dónde se encuentra el código fuente que ejecunta el algoritmo.
- main.py: Aquí hemos implementado una pequeña aplicación de consola para hacer más amigable la ejecución del algoritmo.

### Uso de la interfaz por consola:
Para probar la interfaz por consola que se ha implementado, sólo tiene que ejecutar 
la clase main.py y ya el usuario final irá eligiendo las opciones que desee.
	
Se podrá escoger entre probar el algoritmo con un conjuntos de puntos aleatorios y tres
clústeres también aleatorios o escoger la función de importar la nube de puntos mediante
csv. Nosotros proporcionamos 2 ejemplos para importar mediante csv pero se puede añadir 
si se desea.
	
Le dejamos a continuación el formato que deberá seguir el archivo .csv: cada línea
pertenece a un punto y la estructura a seguir los puntos es la siguiente "9,8". Los
archivos a importar se deben introducir en el mismo directorios que los anteriores
nombrados.
	
Se puede editar manualmente el número de clústeres que se quiere para su nube de puntos
personalizada, en main.py al final se encuentra dicho apartado.
	
Los experimentos realizados se han basado en nubes de puntos y clústeres aleatorios, probando 
la función de crear nubes de puntos aleatorias e introduciendo manualmente los parámetros de 
entrada del método. Y se ha ido escogiendo los que representaban casos distintos con resultados 
diferentes.
