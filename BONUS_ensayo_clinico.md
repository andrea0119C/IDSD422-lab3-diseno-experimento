
# BONUS — Adaptación del diseño experimental a un ensayo clínico de una vacuna

**Laboratorio 3: Diseño de un experimento**  
**Caso:** Evaluación de la eficacia de una vacuna  
**Puntaje adicional:** 5 puntos

## 1. Pregunta e hipótesis

**Pregunta de investigación:** ¿La aplicación de una vacuna experimental reduce la cantidad de personas que desarrollan una enfermedad en comparación con el grupo de control?

**Hipótesis:** Las personas que reciben la vacuna experimental presentan una menor proporción de casos de la enfermedad durante el período de seguimiento que las personas del grupo de control.

- **Hipótesis nula (H₀):** La vacuna experimental no reduce el riesgo de desarrollar la enfermedad respecto al control.
- **Hipótesis alternativa (H₁):** La vacuna experimental reduce el riesgo de desarrollar la enfermedad respecto al control.

## 2. Unidad experimental

La unidad experimental será cada persona que participe voluntariamente en el ensayo clínico.

Para ilustrar el diseño, se propone trabajar con 200 participantes adultos, distribuidos en dos grupos de 100 personas cada uno.

Antes de participar, deberán cumplir los criterios de selección y firmar un consentimiento informado.

**Total propuesto:** 200 participantes.

Este número es únicamente un ejemplo académico. En un estudio real, el tamaño de muestra debe calcularse según el riesgo esperado de enfermedad y el efecto que se desea detectar.

## 3. Factor, niveles y tratamiento

- **Factor:** Intervención preventiva recibida.
- **Nivel 1:** Vacuna experimental.
- **Nivel 2:** Vacuna de comparación autorizada, cuando exista una alternativa eficaz indicada para esa población.
- **Tratamiento:** Administración de la vacuna experimental siguiendo el protocolo clínico aprobado.
- **Control:** Administración de la vacuna de comparación.

El objetivo será evaluar si la vacuna experimental ofrece una mejor protección frente a la enfermedad.

## 4. Grupo de control

El grupo de control estará formado por participantes que reciban la vacuna de comparación autorizada.

Su función será servir como referencia para determinar si la vacuna experimental ofrece una protección diferente.

A diferencia del experimento de RetailAndina, cada persona permanecerá en el grupo asignado. No se alternarán las vacunas cada semana.

El uso de placebo solamente podría considerarse si está científicamente justificado y no implica privar a los participantes de una intervención eficaz que necesitan.

## 5. Aleatorización

Los participantes se distribuirán aleatoriamente entre los dos grupos mediante Python.

**Código de asignación:**

```python
import numpy as np

rng = np.random.default_rng(1234597)

participantes = np.arange(1, 201)

grupos = np.array(
    ["Vacuna experimental"] * 100 +
    ["Vacuna de comparacion"] * 100
)

rng.shuffle(grupos)

for participante, grupo in zip(participantes, grupos):
    print(participante, grupo)
```

**Procedimiento:**

Se preparan 200 asignaciones, correspondientes a 100 participantes por grupo. Después se mezclan aleatoriamente utilizando una semilla fija.

**Justificación:** La aleatorización permite reducir el sesgo en la asignación y ayuda a distribuir las características personales entre ambos grupos.

En un ensayo real, la asignación debe mantenerse oculta hasta el momento correspondiente y puede utilizarse un diseño doble ciego, cuando sea posible.

## 6. Respuesta y medición

- **Variable respuesta principal:** Presencia o ausencia de la enfermedad durante el seguimiento.
- **Período de seguimiento propuesto:** Seis meses.
- **Registro:** Personal médico capacitado registrará los casos confirmados mediante criterios diagnósticos previamente definidos.

También se registrarán posibles efectos adversos, aunque estos se analizarán como resultados de seguridad y no como la variable principal de eficacia.

Al finalizar, se comparará la proporción de personas que desarrollaron la enfermedad en cada grupo.

## 7. Factores a controlar

| Factor a controlar | Cómo se controla o registra |
|---|---|
| Edad | Registrar la edad y procurar una distribución equilibrada entre los grupos. |
| Enfermedades previas | Recopilar antecedentes médicos relevantes antes del ensayo. |
| Exposición a la enfermedad | Registrar condiciones laborales y hábitos que puedan modificar el riesgo de exposición. |
| Vacunación previa | Registrar antecedentes de vacunación y definir criterios de selección. |
| Condiciones de seguimiento | Aplicar el mismo calendario de evaluaciones y criterios diagnósticos a ambos grupos. |
| Medicamentos utilizados | Registrar tratamientos que puedan modificar la respuesta inmunitaria. |

Estos controles permiten identificar otros factores que pueden influir en el resultado, independientemente de la vacuna administrada.

## 8. Limitaciones del diseño

Una limitación es que los participantes pueden tener distintos niveles de exposición a la enfermedad.

También pueden existir diferencias en sus condiciones de salud o respuestas inmunitarias.

El número de participantes y los seis meses propuestos podrían ser insuficientes para detectar algunos efectos o eventos poco frecuentes.

Además, podrían existir abandonos durante el seguimiento, lo que afectaría el análisis.

Finalmente, todo ensayo clínico debe contar con aprobación ética, consentimiento informado, supervisión médica y mecanismos para proteger a los participantes.

## 9. Comparación de resultados

Se calculará la proporción de participantes que desarrollaron la enfermedad en cada grupo.

Para evaluar la eficacia relativa de la vacuna experimental frente a la comparación se puede utilizar:

**Reducción relativa del riesgo:**

RRR = (1 - Riesgo experimental / Riesgo control) × 100

**Ejemplo hipotético:**

- Grupo experimental: 10 casos entre 100 participantes.
- Grupo de control: 20 casos entre 100 participantes.

**Cálculo:**

- Riesgo experimental = 10/100 = 0.10
- Riesgo control = 20/100 = 0.20
- RRR = (1 - 0.10/0.20) × 100 = 50%

**Interpretación:**

En este ejemplo inventado, el grupo que recibió la vacuna experimental presenta un riesgo 50% menor de desarrollar la enfermedad en comparación con el grupo de control.

Sin embargo, no se puede asegurar que la diferencia sea estadísticamente significativa sin realizar un análisis adicional, calcular un intervalo de confianza y evaluar la cantidad de participantes y casos observados.

## 10. Relación con el experimento original

| Elemento | RetailAndina | Ensayo clínico |
|---|---|---|
| Objetivo | Aumentar las ventas | Reducir el riesgo de enfermedad |
| Unidad experimental | Tienda durante una semana | Persona participante |
| Factor | Ubicación del producto | Intervención preventiva |
| Tratamiento | Pasillo principal | Vacuna experimental |
| Control | Ubicación habitual | Vacuna de comparación |
| Aleatorización | Sorteo de ubicación inicial | Sorteo de participantes por grupo |
| Variable respuesta | Ventas semanales | Aparición de enfermedad |
| Medición | Sistema de ventas POS | Seguimiento médico |
| Limitaciones | Promociones e inventario | Exposición, salud y seguimiento |

## Conclusión

Ambos experimentos utilizan una asignación aleatoria y un grupo de control para comparar los efectos de una intervención.

La diferencia principal es que el experimento comercial busca mejorar las ventas, mientras que el ensayo clínico pretende evaluar una intervención relacionada con la salud.

En este último caso, también es indispensable proteger a los participantes y cumplir con los requisitos éticos y médicos establecidos para la investigación clínica.

## Referencias

- Organización Mundial de la Salud. (s. f.). *Clinical evaluation of vaccines*. https://www.who.int/teams/health-product-policy-and-standards/standards-and-specifications/norms-and-standards/vaccine-standardization/clinical-evaluation-of-vaccines

- Council for International Organizations of Medical Sciences. (2016). *International ethical guidelines for health-related research involving humans*. https://www.who.int/docs/default-source/ethics/web-cioms-ethicalguidelines.pdf