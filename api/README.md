# Documentación de la API REST

Este README proporciona documentación para la API REST en el proyecto `api`.

## Visión general

Esta API está construida usando Django y proporciona endpoints para gestionar pagos y funcionalidades relacionadas. Es parte de una aplicación más grande para la gestión de pagos, que incluye un frontend construido con Nuxt 3 y Vue.js.

## URL base

La URL base para todos los endpoints de la API es: `http://localhost:8000/api/`

## Autenticación

Se requiere autenticación para la mayoría de los endpoints. El proyecto utiliza el sistema de autenticación incorporado de Django.

## Endpoints

### Pagos

- `GET /api/payments/`: Listar todos los pagos
- `POST /api/payments/`: Crear un nuevo pago
- `GET /api/payments/{id}/`: Recuperar un pago específico
- `PUT /api/payments/{id}/`: Actualizar un pago específico
- `DELETE /api/payments/{id}/`: Eliminar un pago específico

## Modelos

### Pago

- `source_amount`: Decimal
- `source_currency`: String
- `source_country`: String
- `target_amount`: Decimal
- `target_currency`: String
- `target_country`: String
- `status`: String (opciones disponibles)
- `concept`: String
- `rate_exchange`: Decimal
- `sender_full_name`: String
- `receiver_full_name`: String

## Configuración

La API está containerizada usando Docker. Para ejecutar la API:

1. Asegúrese de que Docker y Docker Compose estén instalados en su sistema.
2. Navegue al directorio raíz del proyecto.
3. Ejecute `docker-compose up` para iniciar la API y los servicios relacionados.

## Base de datos

El proyecto utiliza PostgreSQL como su base de datos.

## Documentación interactiva

Para una documentación más detallada y interactiva de la API, puede acceder a:

- Swagger UI: `http://localhost:8000/swagger/`
- ReDoc: `http://localhost:8000/redoc/`
- DRF Docs: `http://localhost:8000/api/`

Estas interfaces proporcionan una visión completa de todos los endpoints, modelos y operaciones disponibles en la API.

## Información adicional

Para más detalles sobre la estructura del proyecto y la configuración, consulte el archivo README principal en el directorio raíz del proyecto.
