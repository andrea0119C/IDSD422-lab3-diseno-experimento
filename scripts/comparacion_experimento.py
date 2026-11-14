# comparacion_experimento.py — Comparación de grupos (Python)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   python scripts/comparacion_experimento.py

# TODO 1: carga plantillas/registro_experimento.csv con pandas
import pandas as pd

df=pd.read_csv("plantillas/registro_experimento.csv")
print("Datos:")
print(df.head())
print()
# TODO 2: calcula e imprime el promedio de ventas_producto por ubicacion
promedio_ventas=df.groupby("ubicacion")["ventas_producto"].mean()
print(promedio_ventas)
print()
# TODO 3: imprime el número de registros por grupo (value_counts)
num_registros=df["ubicacion"].value_counts()
print(num_registros)

# TODO 4: escribe 2–3 líneas de interpretación (sección 9 de la plantilla):
#         por qué con 4 filas no se puede concluir y qué le faltaría al análisis
print("\n")
print("Interpretación:")
print(
    "Al contar únicamente con 4 registros, no es posible determinar si existen diferencias significativas en las ventas según la ubicación del producto, debido a que la cantidad de datos es muy limitada para representar la población. Para obtener resultados más confiables, sería necesario recopilar más información y realizar un análisis estadístico que permita evaluar mejor las diferencias entre ambas ubicaciones."
    )

#Diseño del experimento
import numpy as np
import pandas as pd
from scipy import stats


tiendas=["Quito Norte","Quito Sur","Guayaquil Centro","Guayaquil Norte","Cuenca Centro","Cuenca Sur",
          "Ambato Centro","Manta","Loja", "Machala"]

semanas=[1,2,3,4]

#Condición inicial: asignar aleatoriamente a cada tienda una ubicación inicial (pasillo_principal o habitual)
rng = np.random.default_rng(1234597) #Semilla para que sea reproducible
primera= rng.choice(["pasillo_principal", "habitual"],size=len(tiendas))
print("\nAsignación aleatoria inicial:")
for tienda, ubicacion in zip(tiendas, primera):
    print(tienda, ":", ubicacion)

filas=[]
for tienda, cond in zip(tiendas, primera):
    otra= "habitual" if cond=="pasillo_principal" else "pasillo_principal"
    for s in semanas:
        filas.append({"tienda":tienda,
                      "semana": s,
                      "ubicacion": cond if s%2 ==1 else otra})

diseno = pd.DataFrame(filas)
print("\nDiseño experimental:")
print(diseno)
print("\nTotal de registros:", len(diseno))
#Simulacion de la ejecución
rng = np.random.default_rng(1234598)  # Semilla para reproducibilidad
efecto_tienda = dict(zip(tiendas, rng.normal(1100, 120, len(tiendas)))) 
efecto_semana = {1: 0, 2: 30, 3: 60, 4: 90}  
diseno["ventas_producto"] = (
     diseno["tienda"].map(efecto_tienda) +
     diseno["semana"].map(efecto_semana) + 
     (diseno["ubicacion"] == "pasillo_principal")*220 +
     rng.normal(0, 90, len(diseno))
 ).round(0).astype(int)

#Promocion simultanea: solo la tienda Guayaquil Centro en la semana 1 tiene promoción simultánea
diseno["promocion_simultanea"] = "no"

diseno.loc[(diseno["tienda"]== "Guayaquil Centro") & (diseno["semana"] == 1), "promocion_simultanea"] = "si" 
diseno.loc[diseno["promocion_simultanea"] == "si", "ventas_producto"] += 180
print("\nPromociones simultáneas:")
print(diseno[diseno["promocion_simultanea"] == "si"])
#loc nos permite acceder a un grupo de filas y columnas por etiquetas o una matriz booleana. 
#En este caso, se utiliza para identificar la fila correspondiente a la tienda "Guayaquil Centro" en la semana 1
#y asignar "si" a la columna "promocion_simultanea". Luego, se incrementa el valor de "ventas_producto" en 180 para esa fila específica.

diseno.to_csv("plantillas/resultado_simulacion.csv", index=False)

#Analisis pareado: una fila por tienda con sus condiciones de ubicacion y ventas_producto
piv = diseno.groupby(["tienda", "ubicacion"])["ventas_producto"].mean().unstack()
piv["diferencia"] = piv["pasillo_principal"] - piv["habitual"]

media = piv["diferencia"].mean()
dev = piv["diferencia"].std(ddof=1)

print("\n")
print("Promedio de la diferencia de ventas entre ubicaciones:", media)
print("Desviación estándar de la diferencia de ventas entre ubicaciones:", dev)

n=len(piv)
t_crit=stats.t.ppf(0.975, df=9)
ic_inf=media -(t_crit*dev/n**0.5)
ic_sup=media +(t_crit*dev/n**0.5)
## independiente del numero de veces que se corra
## el experimento podemos decir que con un 95% de certeza
## el valor promedio de la diferencia de ventas del producto
## entre el pasillo principal y el habitual va a caer en el rango
print(f"Intervalo de confianza 95%: [{ic_inf}, {ic_sup}]")

# prueba p-value
prueba= stats.ttest_rel(piv["pasillo_principal"], piv["habitual"])
print(f"p-value: {prueba.pvalue}")
