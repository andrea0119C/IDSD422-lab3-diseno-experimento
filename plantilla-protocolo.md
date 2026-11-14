# Plantilla de protocolo — Experimento de ubicación de producto

**Equipo:** ___ · **Integrantes:** Andrea Cumbal · **Fecha:** 27/10/2026

Completa cada sección. Usa commits por sección; la historia del repositorio se revisa.

## 1. Pregunta e hipótesis

**Pregunta de investigación:** 

*¿El producto en el pasillo principal vende más en promedio que su ubicación habitual en ventas semanales durante 4 semanas?*

**Hipótesis:** 

El producto ubicado en el pasillo principal presenta, en promedio, mayores ventas semanales que cuando se encuentra en su ubicación habitual, durante un período de cuatro semanas.

- **Hipótesis nula (H₀):**

 No existe un aumento en las ventas promedio al colocar el producto en el pasillo principal.

- **Hipótesis alternativa (H₁):**

 Las ventas promedio aumentan cuando el producto se coloca en el pasillo principal.

## 2. Unidad experimental

Se trabajará con 10 tiendas de RetailAndina durante cuatro semanas, obteniendo 40 observaciones de tienda-semana.

La unidad experimental es la tienda durante una semana, ya que en ese período se aplica una ubicación determinada al producto.

Cada tienda participará en ambas condiciones para comparar sus resultados y reducir las diferencias propias entre establecimientos.

**Total:** 10 tiendas × 4 semanas = 40 unidades tienda-semana.


## 3. Factor, niveles y tratamiento

- **Factor** (variable manipulada): Ubicación del producto dentro de la tienda.
- **Niveles** (valores del factor): 
  - Pasillo principal.
  - Ubicación habitual.
- **Tratamiento:** Colocar el producto en el pasillo principal durante las semanas asignadas.
- **Condición de control:** Mantener el producto en su ubicación habitual durante las semanas correspondientes.

Cada tienda utilizará ambas ubicaciones durante el experimento, alternando las condiciones semanalmente.

## 4. Grupo de control

El control corresponde a las ventas obtenidas cuando el producto permanece en su ubicación habitual.

Su función es servir como referencia para comparar si las ventas cambian cuando el producto se traslada al pasillo principal.

En este diseño, las mismas tiendas pasan por ambas condiciones, por lo que cada establecimiento funciona como su propio control. Esto permite reducir las diferencias relacionadas con el tamaño, la clientela o la ubicación geográfica de las tiendas.

## 5. Aleatorización

Se asignará aleatoriamente la ubicación inicial del producto a cada una de las 10 tiendas.

Para realizar el sorteo se utilizará Python con NumPy y una semilla fija, de manera que la asignación pueda reproducirse.

**Código de asignación:**

```python
import numpy as np

tiendas = [
    "Quito Norte", "Quito Sur",
    "Guayaquil Centro", "Guayaquil Norte",
    "Cuenca Centro", "Cuenca Sur",
    "Ambato Centro", "Manta", "Loja", "Machala"
]

rng = np.random.default_rng(1234597)

primera = rng.choice(
    ["pasillo_principal", "habitual"],
    size=len(tiendas)
)

for tienda, ubicacion in zip(tiendas, primera):
    print(tienda, ubicacion)
```

**Procedimiento:**

Primero se realiza el sorteo para definir la ubicación inicial de cada tienda. Después, durante las cuatro semanas, las condiciones se alternan de la siguiente manera:

- **Semanas 1 y 3:** ubicación inicial asignada.
- **Semanas 2 y 4:** ubicación contraria.

De esta forma, cada tienda participa dos semanas en cada condición.

**Justificación:** El sorteo evita que la ubicación inicial dependa de la decisión de los investigadores. Además, ayuda a distribuir las características desconocidas entre las condiciones, aunque no garantiza un equilibrio perfecto.

**Resultado de la corrida:**

Al ejecutar el código con la semilla `1234597`, se obtuvo la siguiente asignación aleatoria de la ubicación inicial para las 10 tiendas:

| Tienda | Ubicación inicial |
|---|---|
| Quito Norte | habitual |
| Quito Sur | pasillo_principal |
| Guayaquil Centro | habitual |
| Guayaquil Norte | pasillo_principal |
| Cuenca Centro | pasillo_principal |
| Cuenca Sur | habitual |
| Ambato Centro | habitual |
| Manta | habitual |
| Loja | habitual |
| Machala | pasillo_principal |

**Interpretación:** La asignación se realizó de forma aleatoria y reproducible mediante una semilla fija. Cada tienda comenzará con la ubicación asignada y alternará a la otra condición durante las semanas siguientes. Así, todas las tiendas participarán dos semanas en cada ubicación, permitiendo comparar sus ventas bajo ambas condiciones.


## 6. Respuesta y medición

- **Variable respuesta:** Ventas semanales del producto estrella, medidas en dólares estadounidenses (USD).
- **Período de medición:** Cuatro semanas.
- **Quién registra y cómo:** Las ventas se recopilarán al finalizar cada semana mediante el sistema de punto de venta (POS) de cada tienda.

Se registrarán los siguientes datos:

- Tienda.
- Semana.
- Ubicación del producto.
- Ventas del producto.
- Existencia de promociones simultáneas.
- Observaciones relevantes.

El personal encargado de recopilar los resultados utilizará los registros del sistema para evitar depender de estimaciones manuales.

Los vendedores no pueden estar completamente cegados a la ubicación, ya que esta es visible dentro de la tienda. Sin embargo, el análisis de las ventas puede realizarse sin identificar inicialmente qué ubicación corresponde a cada grupo.

## 7. Factores a controlar (mínimo 4)

| Factor a controlar | Cómo se controla o registra |
|---|---|
| Clima | Registrar las condiciones climáticas que puedan afectar la asistencia de clientes a las tiendas. |
| Eventos locales | Identificar feriados, festividades o eventos que puedan aumentar o reducir las ventas. |
| Inventario disponible | Mantener suficiente stock del producto durante las cuatro semanas y registrar posibles faltantes. |
| Cambios de personal | Registrar modificaciones en el personal y procurar mantener condiciones similares de atención. |
| Promociones | Evitar descuentos exclusivos para una condición o registrar las promociones realizadas durante el experimento. |
| Precio del producto | Mantener el mismo precio durante el período experimental, salvo cambios generales que deberán registrarse. |

Estos controles permiten identificar situaciones que podrían modificar las ventas independientemente de la ubicación del producto.

## 8. Limitaciones del diseño

El experimento presenta algunas limitaciones que deben considerarse al interpretar los resultados.

Primero, las promociones simultáneas pueden aumentar las ventas y dificultar la identificación del efecto de la ubicación.

Segundo, puede existir canibalización de ventas, ya que algunos clientes podrían comprar el producto destacado en lugar de otros productos.

Además, cuatro semanas representan un período relativamente corto para evaluar cambios de comportamiento a largo plazo.

La alternancia semanal también puede producir efectos de arrastre, porque algunos clientes podrían continuar buscando el producto en la ubicación utilizada durante la semana anterior.

Finalmente, al trabajar con 10 tiendas, los resultados podrían no representar completamente el comportamiento de todas las sucursales de RetailAndina.

## 9. Comparación en código (Python/R)

Se utilizarán los archivos `scripts/comparacion_experimento.py` y `scripts/comparacion_experimento.R` para comparar las ventas promedio del producto según su ubicación.

Los programas deben cargar el archivo `plantillas/registro_experimento.csv` y calcular el promedio de ventas por ubicación, además del número de observaciones de cada grupo.

**Resultados obtenidos con la plantilla original:**


```text
ubicacion
habitual            1040.0
pasillo_principal   1335.0
Name: ventas_producto, dtype: float64

ubicacion
pasillo_principal    2
habitual             2
Name: count, dtype: int64
```

### ¿Qué grupo muestra mayor venta promedio en la plantilla?

El pasillo principal presenta mayores ventas promedio, con 1335 USD, mientras que la ubicación habitual registra 1040 USD. La diferencia observada es de 295 USD a favor del pasillo principal.

### ¿Por qué con cuatro filas no se puede concluir nada sobre el efecto de la ubicación?

Al contar únicamente con cuatro registros, no es posible determinar si existen diferencias significativas en las ventas según la ubicación del producto. Además, los datos no permiten verificar una asignación aleatoria adecuada ni controlar completamente otros factores que podrían influir en los resultados. Por ello, se necesita una muestra mayor y un análisis estadístico más completo.

### Si el experimento se ejecutara con tu protocolo, ¿qué le faltaría a este análisis para ser justo?

Sería necesario contar con los registros de las 10 tiendas durante las cuatro semanas, respetar la asignación aleatoria y controlar factores como promociones, inventario y eventos locales. También se deberían comparar las ventas de cada tienda bajo ambas condiciones y evaluar la variabilidad de las diferencias antes de establecer conclusiones.

### Interpretación final

Aunque la plantilla muestra mayores ventas promedio en el pasillo principal, este resultado es únicamente descriptivo. No es suficiente para afirmar que cambiar la ubicación provoca un aumento en las ventas.

El experimento propuesto permitiría obtener información más completa y realizar una comparación estadística de las dos condiciones.