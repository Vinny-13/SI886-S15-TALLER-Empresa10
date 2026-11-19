# Evidencias de la Semana 15
Caso académico confidencial. Copiar el contenido al repositorio privado del equipo y revisar la correspondencia P01–P04 con los códigos reales de su PETI.

- 08_riesgos contiene criterios, registro, cálculo, tratamiento, matriz, lista de carga y Sección 8.
- graficos contiene el mapa de densidad. Cada celda muestra el número de riesgos en la pareja P e I.
- evidencias/S15/salidas contiene las salidas de Python, la validación y, si está disponible, el log local de preparación.
- anexos contiene los formatos solicitados en el taller. El mapa del Anexo B corresponde a graficos/RG_mapa_calor.png.
- Repetir desde 08_riesgos con Python 3.11+ y pandas, numpy y matplotlib: python RG03_evaluacion.py y python RG05_residual.py. Ejecutar desde esa carpeta para que las rutas coincidan.

## Cierre del equipo
1. Obtener el acta y fecha de aprobación de criterios y conservar su historial. Si los criterios cambian, reevaluar. Revisar los objetivos y códigos con el PETI del equipo. Confirmar con el equipo la evidencia de aula del pre-mortem.
2. En el laboratorio, iniciar SimpleRisk y MariaDB con el procedimiento del Paso C de la guía. Configurar P × I, escalas y criterio. Cargar manualmente RG07_carga_SimpleRisk.csv como lista de trabajo. Registrar responsable, tratamiento, plazo, residual y señal desde RG04 y comprobar la cantidad cargada. Tomar capturas reales de configuración, lista y un riesgo con tratamiento, numeradas y guardadas en evidencias/S15.
3. Crear la rama del taller, elevar el PR a develop, incorporar las evidencias reales y publicar las etiquetas v0.15 y taller-15 sobre el commit entregado. Incorporar al informe las URL verificadas, incluida la del PR. Obtener las firmas de los dueños competentes para la aceptación de residuales y el acta de Gerencia General.
