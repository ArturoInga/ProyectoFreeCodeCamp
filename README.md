Cree una función llamada calculate()que mean_var_std.pyutilice Numpy para generar la media, la varianza, la desviación estándar, el máximo, el mínimo y la suma de las filas, columnas y elementos de una matriz de 3 x 3.

La entrada de la función debe ser una lista de 9 dígitos. La función debe convertir la lista en una matriz Numpy de 3 x 3 y luego devolver un diccionario con la media, la varianza, la desviación estándar, el máximo, el mínimo y la suma en ambos ejes y para la matriz aplanada.

El diccionario devuelto debe seguir este formato:

{

  'mean': [axis1, axis2, flattened],
  
  'variance': [axis1, axis2, flattened],
  
  'standard deviation': [axis1, axis2, flattened],
  
  'max': [axis1, axis2, flattened],
  
  'min': [axis1, axis2, flattened],
  
  'sum': [axis1, axis2, flattened]
  
}

Si se pasa a la función una lista con menos de 9 elementos, esta debería generar una ValueErrorexcepción con el mensaje: "La lista debe contener nueve números". Los valores del diccionario devuelto deben ser listas, no matrices Numpy.

Por ejemplo, calculate([0,1,2,3,4,5,6,7,8])debería devolver:

{

  'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
  
  'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
  
  'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
  
  'max': [[6, 7, 8], [2, 5, 8], 8],
  
  'min': [[0, 1, 2], [0, 3, 6], 0],
  
  'sum': [[9, 12, 15], [3, 12, 21], 36]
  
}

Desarrollo

Escribe tu código en formato mean_var_std.py. Para desarrollo, puedes usarlo main.pypara probar tu código. Para ejecutarlo, escribe python3 main.pyen la terminal de GitPod y pulsa Intro. Esto hará que el intérprete de CPython incluido ejecute el main.pyarchivo.

Pruebas

Las pruebas unitarias de este proyecto se encuentran en [nombre del archivo test_module.py]. Las importamos de [ test_module.pynombre del archivo] main.pypara su comodidad.

Sumisión

Copia la URL de tu proyecto y envíala a freeCodeCamp.
