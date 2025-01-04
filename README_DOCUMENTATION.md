# 🌟 Proyecto de Prueba Técnica para Zexel - Gestión de Pagos 💸
Esta documentación indica como llevaría acabo la prueba técnica. Como os comenté en la entrevista, tendría que repasar concienzudamente las tecnologias que me indicais, ya que hace años que no las uso. 

Usaré los puntos que indicáis en el plan de acción para ir redactando lo que sería mi solución.

### 📝 Plan de Acción

1. 🏁 Inicialización del Repositorio:

    *Solicitado*:
   - Crea un nuevo repositorio en GitHub o similar.
   - Sube el código actual a la rama base.
   - Crea una nueva rama de desarrollo.

    *Realizado*:
   - Se ha creado un nuevo repositorio que tendréis en el correo.
   - Se ha creado la rama Main. Esta rama tendrá el código original.
   - Se ha creado la rama Dev. Esta rama se ha creado posteriormente por error, ya que creía que esta rama la había creado inicialmente.
   - Se han creado ramas feature/** por cada nueva tarea que se ha realizado.

2. 🔍 Evaluación y Planificación:

    *Solicitado*:
   - Revisa exhaustivamente el código existente y la arquitectura del proyecto.
   - Identifica áreas de mejora y posibles cambios en la infraestructura o tecnologías utilizadas.
   - Prioriza las tareas pendientes basándote en su impacto y complejidad.

    *Realizado*:
   - He mirado el código por encima, veo un código con necesidad de algunas mejoras. De ahí, supongo que las tareas que se indican.
   - Sobre las tareas propuestas las realizaria en el siguiente orden:
        - Tarea: BACKEND. Infraestructura.
            - Configura PostgreSQL con Docker.
              - Crea un contenedor Docker para PostgreSQL
              - Configura las variables de entorno necesarias
            - Integra Django con PostgreSQL:
              - Modifica la configuración de Django para usar PostgreSQL
              - Realiza las migraciones necesarias

          *Explicación*
          - He considerado que lo más importante es tener una infraestructura inicial teniendo en cuenta las necesidades/requisitos.
          - No he realizado un Dockerfile y una carpeta propia para DB porque he visto que el archivo entrypoint.sh lleva datos iniciales para insertarlos en la BBDD.
          - Respecto a las migraciones, no las he realizado de forma local, ya que cuando ejecutamos docker realiza todas las migraciones y las aplica.

        - Tarea: BACKEND. Refuerza validaciones en el modelo de Pagos:
            - Implementa validación para asegurar que el monto sea positivo
            - Verifica que los códigos de país sean ISO válidos
            - Valida que los códigos de moneda sean ISO válidos
            - Asegúrate de que el país origen y destino sean diferentes
          
          *Explicación*
          - Esta tarea la he realizado en segundo lugar, porque considero que tener un modelo estable en validaciones es importante para poder desarrollar la aplicación, ya que nos impide introducir datos no validos en nuestra BBDD.
          - Gracias a realizar esta tarea hemos ejecutado los test que hay hasta la fecha en el proyecto, para verificar que todo funciona correctamente con nuestras modificaciones. En ese momento, nos hemos dado cuenta de que había errores en los test. Por tanto, nuestra tercera tarea ha sido aquella relacionada con los test.
        
        - Tarea: BACKEND. Testing
            - Repara bug tests de cantidad negativa
          
          *Explicación*
          - Los test deben realizarse en la medida de lo posible durante el desarrollo de la aplicacion de ese modo sabemos que todo lo que modifiquemos no esta afectando a otras partes.
          - De hecho no solo estaban erroneos los test de cantidad negativa, también había otros test relacionados con el status que he procedido a arreglar.
          - IMPORTANTE: Creo que sería conveniente utilizar github actions o jenkins para realizar un despliegue automatico siempre y cuando se pasen las pruebas para las ramas dev y main. Es algo que me hubiera gustado implementar y que creo que aporta un valor no tangible para el cliente pero si una estabilidad en el desarrollo del proyecto.

        - Tarea: BACKEND. Optimiza Modelos:
            - Revisa y ajusta los tipos de datos en los modelos para mayor eficiencia
          
          *Explicación*
          - En mi opinión, no es una tarea sumamente relevante, pero sí importante para la BBDD. Dicho de otro modo, a nivel de aplicación no iba a impactar o ser más óptima pero no es lo mismo tener una BBDD cuyo tamaño por una tabla sea de 1MG que de 1Kb. Por ello, realizar una optimización de las longitudes y/o tipos nos permite ser más óptimos y que nuestra BBDD no "pese" demasiado.
        
        - Tarea: FRONTEND. Completa funcionalidades CRUD:
            - Implementa la funcionalidad de edición de pagos existentes
          
          *Explicación*
          - Es el objetivo basico de nuestra aplicación desde el frontend. Dicho de otro modo, hasta ahora hemos realizado todo en el backend, pero necesitamos que nuestro frontend sea capaz de realizar todas las acciones que hemos implementado.
        
        - Tarea: FRONTEND. Optimiza campos ISO:
          - Convierte los campos de país y moneda en selectores desplegables
          - Asegúrate de que se envíen los códigos ISO correctos al backend

          *Explicación*
          - Utilizaría la api de Countries Now (exactamente la misma que he utilizado en el backend) De ese modo, con una sola llamada, obtendría todos los datos necesarios para los codigos de los campos de país y moneda, pudiéndolos convertir en desplegables en los que mostraria el país y el código, aunque al backend solo se envíe los códigos. Al mostrar en el desplegable el país y el código es más facil e intuitiva para los usuarios.
          - Tambien añadiría limitaciones de longitud en el frontend en los campos del tipo charfield, como por ejemplo: nombre del emisor y nombre del receptor, siguiendo la longitud establecida en el backend.
          - Tambien establecería los campos numéricos como tal, impidiendo que se puedan guardar o escribir nombres como actualmente pasa.
        
        - Tarea: FRONTEND. Testing
          - Implementa tests unitarios y de integración con Cypress

          *Explicación*

          - Como he explicado anteriormente en la parte backend. Los test unitarios debemos realizarlos desde el principio, de ese modo, cualquier modificación que afecte a cualquier otra parte del sistema sería detectada rápidamente.
        
        - Tareas: FRONTEND. 
          - Implementa Navbar:
            - Diseña y crea un navbar responsive con los enlaces principales
            - Reemplaza los botones de navegación existentes por el nuevo navbar
          - Mejora Componente de Alerta:
            - Crea un componente de alerta global reutilizable
            - Implementa un sistema de colores para diferentes tipos de mensajes (error, éxito, información)
            - Integra la visualización de mensajes de error provenientes de las APIs.
          - Mejora la Tabla de Pagos:
            - Añade filtros dinámicos por país y moneda
            - Implementa ordenación por columnas, incluyendo país y moneda
          - Implementa selección de idioma:
            - Añade un selector de idioma en el navbar o en una ubicación prominente

          *Explicación*
          - He juntado todas estas tareas porque considero que son mejoras visuales. Dicho de otro modo, o al menos desde mi punto de vista, es el eterno debate entre funcionalidad y UX. Un producto puede tener muy buena funcionalidad, pero si no es atractivo para el usuario, no tendrá éxito. Ocurre lo mismo al contrario, si un producto es muy atractivo, pero no cumple con la funcionalidad que el usuario espera, lo desechará. En ambos casos, es muy difícil volver a captar o que ese usuario le dé una nueva oportunidad. Por ello, UX y funcionalidad deben ir de la mano. 
          
            Dicho esto, si tuviera que establecer un orden para la realización de las tareas por impacto y aportación seria:
            - Mejora la Tabla de Pagos
            - Implementa Navbar.
            - Implementa selección de idioma.
            - Mejora Componente de Alerta.

        - Tareas: BACKEND. Implementa Sistema de Cambio de Divisas:
          - Integra una librería de conversión de divisas (ej. Forex-Python)
          - Crea un servicio para manejar las conversiones de moneda en tiempo real

          *Explicación*
          - Confieso que esta tarea me genera dudas dejarla para el final. Creo que aporta un valor funcional muy importante, ya que estamos entendiendo que los pagos no siempre se van a realizar dentro del mismo país. Seguramente paralelizaría de algún modo la realización de la parte frontend con esta parte, ya que también es necesaria para poder guardar pagos reales entre diferentes países.


3. 🛠️ Implementación de Mejoras:

    *Solicitado*:
   - Aborda las tareas pendientes en la lista, enfocándote en lo que consideres más importante.
   - Considera la posibilidad de reescribir partes del proyecto si identificas una mejor aproximación.


    *Realizado*:
    - En el punto anterior he explicado algunas mejoras que realizaría. 
    - A nivel de infraestructura, crearía esta parte como un servicio independiente. De esta forma, si en el futuro debemos replicar esta funcionalidad, se podría. Dicho de otro modo, en lugar de dockerizar, realizaría funciones serverless que me permitirían tener más control sobre el balance de carga y peticiones en un momento dado.

4. 🔒 Mantenimiento de la Funcionalidad Core:

    *Solicitado*:
   - Asegúrate de que todas las mejoras y cambios mantengan el enfoque principal en la funcionalidad de gestión de pagos.


    *Realizado*::
   - He establecido la priorización en base a eso.

5. 📚 Documentación y Pruebas:

    *Solicitado*:
   - Actualiza la documentación del proyecto a medida que implementes cambios.
   - Desarrolla y ejecuta pruebas exhaustivas para garantizar la calidad y robustez del código.

    *Realizado*:
   - A lo largo del proyecto, veréis comentarios sobre cada modificación.
   - Faltan más pruebas en el backend que es la parte que más he tocado. Soy consciente de ello, pero no me ha sido posible por falta de tiempo.


## NOTA

Espero que con el desarrollo realizado y la explicación de este documento podáis conocerme mejor en mi faceta profesional, así como verme abordar los diferentes desafíos que se pueden dar en el día a día. Quedo a vuestra disposición para cualquier consulta o aclaración necesarias.

