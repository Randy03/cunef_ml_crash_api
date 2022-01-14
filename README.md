Tomas Ramella

## Rest API y shiny dashboard para el modelo de prediccion de Canadian Accidents

- Imagen Docker: https://hub.docker.com/r/randy2019/canadiancrash
- Repositorio Github: https://github.com/Randy03/cunef_ml_crash_api.git

### Estructura de la API
La API esta organizada en las siguientes 5 subcarpetas:
- blueprints: Contiene los flask blueprints para aislar cada componente, hay dos blueprints que funcionan como routes, prediction (/api/predict) y home (/api/), y hay un blueprint para controlar los mensajes de error de la api y otro para controlar los logs de los request y response sobre una base de datos sqlite
- models: Contiene las estructuras de datos que se usaran en la API, hay dos estructuras para manejar las predicciones (una para input y otra para output), y hay otro home que solo contiene un mensaje.
- resources: contiene los archivos necesarios para el funcionamiento de la API, contiene el archivo prediction_model.joblib que es el modelo generado por el notebook models del repositorio https://github.com/Randy03/cunef_ml_canadian_crash.git y se usara para que la API pueda realizar las predicciones, y ademas esta el archivo flask_logs.db que guardara informacion sobre los llamados a la API que luego sera utilizada por el shiny dashboard
- schemas: Contiene los componentes nesesarios para validar y transformar los llamados a la API, aqui estan especificados los parametros y los valores que puede tomar cada uno.
- services: Tiene la logica necesaria para realizar la prediccion sobre si hay fallecidos o no.
<br>
Archivo config.json: aca se configuran los path donde se encuentrar los resources, pero tambien se puede usar para configurar cualquier variable de configuracion de flask

Archivo filldb.py: script que se utilizo para pre cargar la base sqlite, lo que hace es tomar una muestra de datos del archivo crash_transformed_c_sev.csv generado por el notebook EDA_C_SEV del repositorio https://github.com/Randy03/cunef_ml_canadian_crash.git y llamar a la API para que haga la prediccion. (Aclaracion: para la muestra se tomo 50% de accidentes que tienen fallecidos y 50% que no tienen)

#### Como llamar a la API

  curl -X GET http://localhost:5000/api/predict?C_MNTH=03&C_WDAY=2&C_HOUR=3&C_VEHS=10&C_CONF=01&C_RCFG=13&C_WTHR=1&C_RSUR=4&C_RALN=4&C_TRAF=04&V_TYPE=24&P_SEX=M&P_AGE=67&P_SAFE=10&C_PERS=20&V_AGE=4

### Shiny dashboard

Se realizo un dashboard en shiny ara evaluar ciertas metricas de la API, el dashboard utiliza la misma base de datos que la API y contiene 4 graficos:
- Grafico de barras en el que se pueden ver la cantidad de llamados a la API segun el codigo de status http, el metodo http que se uso, y la ruta a la que se esta llamando
- Serie temporal de la evolucion de llamados a la api, puede agruparse por minutos o segundos
- Grafico que muestra la cantidad de predicciones con fallecimientos y sin fallecimientos que se han hecho, ademas se puede seleccionar cualquier variable input como subcategoria para reflejar cuantos llamados se realizaron a la api con ese input.
- Histograma con la distribucion de probabilidad de que haya al menos un fallecido en el accidente, puede configurarse el numero de bins
<br>
Ademas de shiny se utilizo la libreria shinydashboard para darle estilo a la UI

### Docker

La imagen se puede descargar con: docker pull randy2019/canadiancrash
<br>
La imagen esta basada en centos:8 y tiene instaladas todas las dependencias necesarias de python y r para poder ejecutar la API y el dashboard en un mismo contenedor, ademas expone los puertos 5000 que sirve la API y el 5001 que es para el dashboard
