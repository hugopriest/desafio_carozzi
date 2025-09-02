# Desafío Cargo Data Scientist - Carozzi

## Caso: Proyección de ventas por Store

1. Antecedentes dataset

Data.csv = Corresponden a las ventas de salas de supermercados en Ecuador y tiene las siguientes columnas:

Stores.csv = Corresponde a información complementaria de las salas de supermercado y tiene las siguientes columnas:

Oil.csv= Corresponde al precio del petróleo de manera diaria y contiene las siguientes columnas:

2. Objetivo del caso

* Predecir el volumen de ventas de manera semanal, para cada store_nbr, en un horizonte de medio semestre (26 semanas), desde la última observación presente en el dataset. (considera el periodo de entrenamiento/pruebas y la metodología de evaluación que estimes necesarios)
* Evaluar cómo se ven impactadas las ventas por factores como, precio del petróleo, promociones y otras variables relevantes que puedas crear o integrar y aporten valor al modelo

3. Estructura para considerar en el desarrollo del caso

Para que el comité pueda reproducir y auditar tu trabajo, todo el desarrollo debe venir empaquetado en un único .zip y, a la vez, versionado en un repositorio Git (público o privado) cuyo enlace nos compartirás.

4. Temas específicos para resolver: Se espera que el desarrollador sea capaz de responder mediante la resolución del caso al menos a las siguientes preguntas durante el desarrollo de su presentación del caso:

a) Monto a predecir: ¿Cuánto se estima que será el monto a vender, en los próximos 6 meses desde la última observación en los datos? Considere agregar semanalmente la serie y calcule además indicadores como % crecimiento proyectado en las ventas de este periodo y compárelo contra los crecimientos en los mismos periodos, pero en años anteriores
b) Análisis del modelo: métricas de calidad, predicción, insights relevantes
c) Análisis de Tendencias: ¿Qué patrones estacionales o tendencias observaste en los datos de ventas a lo largo del tiempo? 
d) Relación entre Promociones y Ventas: ¿Cómo influyen las promociones en el volumen de ventas? ¿Es este impacto constante a lo largo de todas las categorías de productos o varía en función de la categoría y la tienda?
e) Precio del Petróleo y Comportamiento del Consumidor: ¿Existe alguna correlación significativa entre el precio del petróleo y las ventas? Si es así, ¿cómo podrías justificar este hallazgo en términos de comportamiento del consumidor o costo operativo?
f) Recomendaciones para el Negocio: Con base en tus hallazgos, ¿qué estrategias recomendarías para optimizar las ventas durante eventos especiales o en tiendas que muestran una mayor sensibilidad a variables externas?
