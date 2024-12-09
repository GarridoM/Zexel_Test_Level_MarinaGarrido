# 🌟 Proyecto de Prueba Técnica para Zexel - Gestión de Pagos 💸

Este proyecto es una prueba técnica personalizada para tu candidatura en Zexel, específicamente diseñada para el proyecto /tests/. Tu objetivo es crear una aplicación de gestión de pagos que demuestre tus habilidades en desarrollo frontend y backend.

## 🌈 Temática de la Aplicación

La aplicación te permitirá gestionar pagos entre diferentes países y monedas, utilizando APIs externas para obtener información actualizada sobre países y divisas.

## 🎯 Objetivo del Proyecto

Como nuevo responsable principal de este proyecto, tu tarea es mejorar y completar la aplicación de gestión de pagos, abordando tareas pendientes con la más alta calidad.

**Tu primer paso crucial es subir el código actual a un repositorio en GitHub o similar, estableciendo una rama como base.** 🚀 Este paso es fundamental para que inicies el proceso de desarrollo y control de versiones. **Todos los cambios y mejoras los realizarás en una nueva rama de desarrollo**, lo que te permitirá un desarrollo organizado y seguro.

### 📝 Plan de Acción

1. 🏁 Inicialización del Repositorio:
   - Crea un nuevo repositorio en GitHub o similar.
   - Sube el código actual a la rama base.
   - Crea una nueva rama de desarrollo.

2. 🔍 Evaluación y Planificación:
   - Revisa exhaustivamente el código existente y la arquitectura del proyecto.
   - Identifica áreas de mejora y posibles cambios en la infraestructura o tecnologías utilizadas.
   - Prioriza las tareas pendientes basándote en su impacto y complejidad.

3. 🛠️ Implementación de Mejoras:
   - Aborda las tareas pendientes en la lista, enfocándote en lo que consideres más importante.
   - Considera la posibilidad de reescribir partes del proyecto si identificas una mejor aproximación.

4. 🔒 Mantenimiento de la Funcionalidad Core:
   - Asegúrate de que todas las mejoras y cambios mantengan el enfoque principal en la funcionalidad de gestión de pagos.

5. 📚 Documentación y Pruebas:
   - Actualiza la documentación del proyecto a medida que implementes cambios.
   - Desarrolla y ejecuta pruebas exhaustivas para garantizar la calidad y robustez del código.

Este enfoque te permitirá tomar control total del proyecto, implementando mejoras significativas mientras mantienes la integridad de la funcionalidad core de gestión de pagos. Estás preparado para tomar decisiones importantes sobre la dirección del proyecto, incluyendo posibles cambios en la stack tecnológica o la arquitectura, siempre con el objetivo de crear una aplicación robusta, eficiente y fácil de mantener.

Únicamente se limita que se siga utilizando Nuxt (versión 3) y Vue (versión 3) con Django (versión 4.2 o superior) y DRF (Django Rest Framework, versión 3.14 o superior).

🌟 Recordatorio: Como el único responsable de este software en el mundo, tienes completa libertad para tomar decisiones audaces y creativas. No te limites por convenciones o expectativas preexistentes. Aprovecha esta oportunidad para innovar, optimizar y crear una solución verdaderamente excepcional. Tu visión y experiencia son los únicos límites. Confía en tu instinto y conocimientos para llevar este proyecto al siguiente nivel. Eso sí, respetando y aplicando las buenas prácticas de desarrollo de software.

## 🌐 APIs Utilizadas

Para obtener información sobre países y monedas, este proyecto utiliza las siguientes APIs:

1. 🌍 Countries Now API:
   - URL: https://countriesnow.space
   - Documentación: https://documenter.getpostman.com/view/1134062/T1LJjU52
   - Te proporciona información detallada sobre países, incluyendo nombres, códigos, banderas y más, así como tasas de cambio actualizadas entre diferentes monedas.

Estas APIs las utilizarás tanto en el backend (Django) como en el frontend (Nuxt 3/Vue.js) para proporcionar datos precisos y actualizados sobre países y conversiones de moneda.

## 🚀 Funcionalidades Principales

- 💰 Gestión de pagos (crear, leer, actualizar, eliminar)
- 💱 Conversión de monedas en tiempo real
- 🗺️ Visualización de datos de países
- 🖥️ Interfaz de usuario intuitiva y responsive

## 🛠️ Tecnologías Utilizadas

- 🐍 Backend: Django (Python)
- 🖌️ Frontend: Nuxt 3 (Vue.js)
- 🗄️ Base de datos: PostgreSQL
- 🐳 Contenedorización: Docker

Para más detalles sobre la implementación y cómo ejecutar el proyecto, consulta los README específicos en los directorios `api/` y `front/`.

## 📋 Lista de Tareas

### 🏗️ Infraestructura
- [ ] Configura PostgreSQL con Docker:
  - Crea un contenedor Docker para PostgreSQL
  - Configura las variables de entorno necesarias
- [ ] Integra Django con PostgreSQL:
  - Modifica la configuración de Django para usar PostgreSQL
  - Realiza las migraciones necesarias

### 🎨 Frontend
- Implementa Navbar:
  - [ ] Diseña y crea un navbar responsive con los enlaces principales
  - [ ] Reemplaza los botones de navegación existentes por el nuevo navbar
- Mejora Componente de Alerta:
  - [ ] Crea un componente de alerta global reutilizable
  - [ ] Implementa un sistema de colores para diferentes tipos de mensajes (error, éxito, información)
  - [ ] Integra la visualización de mensajes de error provenientes de las APIs
- Completa funcionalidades CRUD:
  - [ ] Implementa la funcionalidad de edición de pagos existentes
- Optimiza campos ISO:
  - [ ] Convierte los campos de país y moneda en selectores desplegables
  - [ ] Asegúrate de que se envíen los códigos ISO correctos al backend
- Mejora la Tabla de Pagos:
  - [ ] Añade filtros dinámicos por país y moneda
  - [ ] Implementa ordenación por columnas, incluyendo país y moneda
- Implementa selección de idioma:
  - [ ] Añade un selector de idioma en el navbar o en una ubicación prominente
- Testing
  - [ ] Implementa tests unitarios y de integración con Cypress

### 🔧 Backend
- Refuerza validaciones en el modelo de Pagos:
  - [ ] Implementa validación para asegurar que el monto sea positivo
  - [ ] Verifica que los códigos de país sean ISO válidos
  - [ ] Valida que los códigos de moneda sean ISO válidos
  - [ ] Asegúrate de que el país origen y destino sean diferentes
- Optimiza Modelos:
  - [ ] Revisa y ajusta los tipos de datos en los modelos para mayor eficiencia
- Implementa Sistema de Cambio de Divisas:
  - [ ] Integra una librería de conversión de divisas (ej. Forex-Python)
  - [ ] Crea un servicio para manejar las conversiones de moneda en tiempo real
- Testing
  - [ ] Repara bug tests de cantidad negativa

Estas tareas están diseñadas para que mejores la funcionalidad, usabilidad y robustez de la aplicación de gestión de pagos, abordando aspectos clave tanto en el frontend como en el backend.
