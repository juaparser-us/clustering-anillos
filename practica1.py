import pandas
import numpy
from sklearn import preprocessing
from sklearn import model_selection


cars = pandas.read_csv('cars.csv', header=None,
                       names=['buying', 'maint', 'doors', 'persons',
                              'lug_boot', 'safety', 'acceptability']);
print(cars.shape);  # Número de filas y columnas
cars.head(10);  # 10 primeras filas

atributos = cars.loc[:, 'buying':'safety'];  # selección de las columnas de atributos
objetivo = cars['acceptability'];

codificador_atributos = preprocessing.OrdinalEncoder();
codificador_atributos.fit(atributos);
print(codificador_atributos.categories_);  # Categorías detectadas por el codificador para cada atributo
atributos_codificados = codificador_atributos.transform(atributos);
print(atributos_codificados);
print(codificador_atributos.inverse_transform([[3., 3., 0., 0., 2., 1.],
                                               [1., 1., 3., 2., 0., 1.]]));

codificador_objetivo = preprocessing.LabelEncoder();
objetivo_codificado = codificador_objetivo.fit_transform(objetivo);  # El método fit_transform ajusta la codificación y la aplica a los datos a continuación
print(codificador_objetivo.classes_);  # Clases detectadas por el codificador para la variable objetivo
print(objetivo_codificado);
print(codificador_objetivo.inverse_transform([2, 1, 3]));                             

print(cars.shape[0]); # Cantidad total de ejemplos
print(pandas.Series(objetivo).value_counts(normalize=True));  # Frecuencia total de cada clase de aceptabilidad

atributos_entrenamiento, atributos_prueba, objetivo_entrenamiento, objetivo_prueba = model_selection.train_test_split(
    atributos_codificados, objetivo_codificado,  # Conjuntos de datos a dividir, usando los mismos índices para ambos
    random_state=12345,  # Valor de la semilla aleatoria, para que el muestreo sea reproducible, a pesar de ser aleatorio
    test_size=.33,  # Tamaño del conjunto de prueba
    stratify=objetivo_codificado);  # Estratificamos respecto a la distribución de valores en la variable objetivo

# Comprobamos que el conjunto de prueba contiene el 33 % de los datos, en la misma proporción
# con respecto a la variable objetivo
print(atributos_prueba.shape[0], len(objetivo_prueba), 1728 * .33);
print(pandas.Series(codificador_objetivo.inverse_transform(objetivo_prueba)).value_counts(normalize=True));

# Comprobamos que el conjunto de entrenamiento contiene el resto de los datos, en la misma
# proporción con respecto a la variable objetivo
print(atributos_entrenamiento.shape[0], len(objetivo_entrenamiento), 1728 * .67);
print(pandas.Series(objetivo_entrenamiento).value_counts(normalize=True));