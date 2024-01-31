
#
# #Consultoria Equipo 2

El propósito de este proyecto es la lectura, limpieza, análisis de los datos y la visualización de gran alcance de un hotel para el análisis y optimización de Cancelaciones de Reservas. Con el objetivo de reducir la tasa de cancelación de la empresa.

Nuestra misión es identificar factores clave que influyen en la cancelacion de los clientes y, en última instancia, el tipo de reserva de los clientes.

En resumen, en este proyecto, presentaremos los resultados de nuestro análisis exploratorio de datos, diseñaremos un visualización para ver las preguntas críticas de la propia empresa y analizaremos los resultados para proporcionar al hotel la información valiosa que informe sus decisiones estratégicas.



## Índice


1. [Descripción](#descripción)
2. [Archivos](#archivos)
3. [Metodología](#metodología)
4. [Resultados](#resultados)
5. [Contribución](#contribución)
6. [Autor](#autor)
7. [Licencia](#licencia)



## Descripción

El objetivo es reducir la tasa de cancelación de los clientes y mejorar su estancia en el hotel. Esto se ha podido hacer con las distintas fases:

Fase 1: Análisis Exploratorio de Datos(EDA)

Fase 2: Transformación de los datos

Fase 3: Visualizacion en Power BI

Fase 4: Reporte de los resultados



## Archivos

Carpeta "data": 

   - "data_tasa": Varios archivos .csv con tasas por cada columna del archivo limpio

`bookings_clean_ok.csv` : Archivo .csv limpio

`bookings.csv`:Archivo .csv con datos

`finanzas-hotel-bookings.csv` : Archivo original en .csv

`info.csv`: Archivo .csv con datos

Carpeta "imagenes": imágenes para crear la visualización del dashboard

Carpeta "notebooks":

`01_exploracion.ipynb`: Exploración inicial de los datos

`02_analisis.ipynb`: 1º Análisis de los datos

`03_analisis.ipynb`: 2º Análisis de los datos

`04.tasa_cancelacion.ipynb`:CSV limpio

Fuera de las carpetas:

`Presentación_final.pbix`: dashboard en Power BI



## Metodología

Pasos de limpieza de datos: Fase 1 y 2

Técnicas de visualización utilizadas: Power BI 

Herramientas y bibliotecas empleadas: jupyter notebook, pandas, numpy, scipy.stats, warnings, matplotlib, seaborn en Python.



## Resultados

Según los datos obtenidos y haciendo los análisis de datos podemos observar en las cancelaciones:

Hay un tasa de cancelación del 35,98%

Los City Hotel presentan una Tasa de Cancelación más alta, por lo que se podría limitar el numero de cancelaciones gratuitas a pernoctas largas.

La temporada alta en verano registra mayor Tasa de Cancelación, debido al alto volumen de reserva. Se podría elaborar un estudio sobre la influencia de la anticipación de la reserva y la cancelación en temporada alta.

Las habitaciones de tipo A tienen más cancelaciones, por lo que se debería revisar las características para reducir tanto en el segmento de reserva como asignación las mismas.

No ofrecer la habitación L (50% TC) si no existe para no tener que volver a reasignar, ni alterar la medición de las cancelaciones.

Los clientes nuevos cancelan un +14pp más que los recurrentes(fidelizados), no obstante el volumen de nuevos clientes (78%) es mayor que recurrentes. El hotel debería trabajar en medidas de fidelización como paquetes loyalty (descuento x noche, media pensión incluida en el precio, códigos de descuento en email marketing...)

Alto riesgo de cancelación en estadías de entre 15-20 días tanto para noches entre semana como para fines de semana. Revisar este tipo de reservas con detenimiento ya que afectan a la disponibilidad directa.

A más antelación de reserva, mayor incremento de cancelaciones. Posible medida de reducción sería, exigir un depósito o el pago parcial de la reserva . Limitar la reserva con tanta antelación solo a reservas para grupos, reservas de compañías o eventos como bodas.




## Contribución

Este proyecto de Análisis Datos y Visualización se realizó específicamente para un propósito interno y actualmente no está abierto a contribuciones externas. El análisis fue llevado a cabo por un equipo designado de analistas de datos y ha sido finalizado con el objetivo de satisfacer las necesidades específicas de la empresa.

Agradecemos el interés en este proyecto, sin embargo, en este momento no estamos buscando activamente contribuciones externas o modificaciones al análisis.

Si tienes preguntas sobre el análisis o estás interesado en colaborar de alguna manera, por favor, contáctanos a través de los detalles proporcionados en la sección de [Autor](#autor).



## Autor

El Análisis de Datos y Visualización fue realizado por [Equipo 2 : Elena Bermejo, Sara Gómez, Carla Álvarez y Yohanna Gutiérrez]. Somos un equipo de analistas de datos en [Equipo 2], especializados en la exploración y análisis de datos para obtener información útil y acciones significativas.



## Licencia

MIT License

Se concede permiso, de forma gratuita, a cualquier persona que obtenga una copia de este software y de los archivos de documentación asociados (el "Software"), para tratar el Software sin restricciones, incluidos, entre otros, los derechos de uso, copia, modificación, fusión, publicación, distribución, sublicencia y/o venta de copias del Software, y para permitir a las personas a las que se les proporcione el Software a hacer lo mismo, sujeto a las siguientes condiciones:

El aviso de copyright anterior y este aviso de permiso se incluirán en todas las copias o partes sustanciales del Software.

EL SOFTWARE SE PROPORCIONA "TAL CUAL", SIN GARANTÍA DE NINGÚN TIPO, EXPRESA O IMPLÍCITA, INCLUYENDO PERO NO LIMITADO A LAS GARANTÍAS DE COMERCIABILIDAD, IDONEIDAD PARA UN PROPÓSITO PARTICULAR Y NO INFRACCIÓN. EN NINGÚN CASO LOS AUTORES O TITULARES DE DERECHOS DE AUTOR SERÁN RESPONSABLES DE NINGUNA RECLAMACIÓN, DAÑOS U OTRAS RESPONSABILIDADES, YA SEA EN UNA ACCIÓN DE CONTRATO, AGRAVIO O DE OTRO MODO, DERIVADAS DE, FUERA DE O EN CONEXIÓN CON EL SOFTWARE O EL USO U OTROS TRATOS EN EL SOFTWARE.
