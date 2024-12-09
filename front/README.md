# Aplicación de Gestión de Pagos - Test Frontend

Esta aplicación es parte del proyecto de prueba técnica para evaluar las habilidades de desarrollo frontend, con énfasis en la funcionalidad. El objetivo es crear una interfaz de usuario eficiente para gestionar pagos de servicios, integrada con APIs de países y divisas.

## Funcionalidades Principales

1. **Listar Pagos**
   - Mostrar una tabla con todos los pagos existentes
   - Implementar paginación para manejar grandes volúmenes de datos
   - Permitir ordenar por diferentes campos (fecha, monto, etc.)

2. **Agregar Pagos**
   - Formulario para crear nuevas entradas de pago
   - Validación en tiempo real de los campos del formulario
   - Integración con API para obtener tasas de cambio actualizadas

3. **Editar Pagos**
   - Formulario pre-poblado con datos existentes
   - Actualización en tiempo real de los campos relacionados (ej. monto destino al cambiar monto origen)

4. **Eliminar Pagos**
   - Confirmación antes de eliminar
   - Actualización inmediata de la lista de pagos tras la eliminación

5. **Búsqueda y Filtrado**
   - Barra de búsqueda para filtrar pagos por diferentes criterios
   - Filtros avanzados (por rango de fechas, estado del pago, país, etc.)

6. **Visualización de Datos**
   - Gráficos para mostrar estadísticas de pagos (ej. distribución por país, moneda)
   - Panel de resumen con totales y promedios

7. **Internacionalización**
   - Soporte para múltiples idiomas (mínimo español e inglés)
   - Cambio dinámico de idioma sin recargar la página

## Información adicional

Para más detalles sobre la estructura del proyecto y la configuración, consulte el archivo README principal en el directorio raíz del proyecto.
