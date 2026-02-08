# behave-poc

<img src="./assets/behave.jpg" alt='A screenshot from the movie \"Austin Powers\" and a caption reading \"Oh behave\"' width="50%" />

- [behave-poc](#behave-poc)
  - [E2E Tests](#e2e-tests)


## E2E Tests

Siguiendo [la documentación de Behave](https://behave.readthedocs.io/en/latest/), el proyecto de testing está ubicado dentro de la carpeta /e2e/ y dividido en estos directorios:
- **/config/:** contiene un ejemplo de configuración por perfil. Es decir, si por ejemplo quisiéramos tener datos para varios entornos, podríamos tener varios archivos aquí y al proporcionar el nombre del perfil (el del archivo menos el .json del final), se cargarían automáticamente.
- **/features/:** contiene los archivos .feature en los que aparecen descritas las pruebas en lenguaje Gherkin (el formato Scenario, Given, When, Then).
  - **./environment.py:** este archivo no es estrictamente necesario, pero es el lugar ideal para utilizar los hooks de Cucumber (es decir, decoradores o funciones globales que se ejecutan, entre otros, antes de todas las pruebas, antes de pruebas específicas, de tags, después de todas, etc). Además, en este ejemplo se emplea Selenium Webdriver para automatizar pruebas E2E, con lo que sí hace falta tener un lugar en que establecer y configurar el driver que va a mover un navegador. 
  - **../steps/:** los archivos que contienen la descripción en código del comportamiento asociado a cada paso de las pruebas se incluye dentro de una carpeta llamada "steps". Esta es la configuración por defecto de Behave según la documentación. Si, por ejemplo, tenemos una prueba en un X.feature que dice "Given The user navigates to the website", dentro de la carpeta /steps/ habrá una línea que diga algo parecido a esto:
  ```python
  @given(The user navigates to the website)
  def step_impl(context):
    # Aquí vendría el código con las acciones que determinan 
    pass

  ```
- **/reports/:** aquí se guarda el XML con el informe de las pruebas que acaban de correr más recientes en el formato JUnit que emplean otras tecnologías como, por ejemplo, Jenkins. 

Para ejecutar las pruebas, hay que navegar con la terminal a la carpeta ./e2e e instalar las dependencias del proyecto. Lo recomendable es utilizar un entorno virtual de la siguiente manera:

```shell
python -m venv ./venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

Después, desde la carpeta ./e2e/ todavía, se pueden ejecutar los tests de varias formas:

```
# Ejecutar todas las pruebas
behave

# Ejecutar las pruebas con la etiqueta @smoke (las etiquetas encabezan una sección dentro del .feature)
behave --tags="@smoke"

# Ejecutar las pruebas en modo "headless" (sin que se vea el navegador) y en Firefox
behave -D headless -D browser="firefox"
```

Respecto a este último ejemplo, el argumento "-D" implica una entrada de userdata dentro del contexto que proporciona Behave. Su comportamiento (configurar el navegador como headless o elegir un driver en vez de otro) está personalizado dentro del "./environment.py" que venía más arriba.