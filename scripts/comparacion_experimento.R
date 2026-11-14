# comparacion_experimento.R — Comparación de grupos (R)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   Rscript scripts/comparacion_experimento.R


# TODO 1: Leer el archivo CSV
datos <- read.csv("plantillas/registro_experimento.csv",
                  stringsAsFactors = FALSE)

cat("Datos originales:\n")
print(datos)

# TODO 2: Promedio de ventas por ubicacion
cat("\nPromedio de ventas por ubicacion:\n")
promedios <- aggregate(ventas_producto ~ ubicacion,
                       data = datos, FUN = mean)
print(promedios)

# TODO 3: Numero de registros por grupo
cat("\nNumero de registros por grupo:\n")
print(table(datos$ubicacion))

# TODO 4: Interpretacion
cat("\nInterpretacion:\n")
cat("Al contar con solo cuatro registros, no es posible determinar
si la ubicacion del producto produce diferencias significativas
en las ventas. Se necesita recopilar mas informacion y controlar
otros factores para obtener resultados confiables.\n")

cat("\n--- ANALISIS DE LA SIMULACION ---\n")

df <- read.csv("plantillas/resultado_simulacion.csv",stringsAsFactors = FALSE)
print(aggregate(ventas_producto ~ ubicacion, data = df, FUN = mean))
#print(df[, c("tienda","semana","ubicacion","ventas_producto","promocion_simultanea")])

media_tienda <- tapply(df$ventas_producto, list(df$tienda, df$ubicacion), mean)
#print(round(media_tienda, 0))

diferencias <- media_tienda[, "pasillo_principal"] - media_tienda [, "habitual"]
print(mean(diferencias))

prueba <- t.test(media_tienda[, "pasillo_principal"], media_tienda[, "habitual"], paired = TRUE)

print(prueba$conf.int)
print(prueba$p.value)

cat("\n=== INTERPRETACIÓN FINAL ===\n")

cat(
  "Se analizaron las ventas medias de las dos ubicaciones ",
  "en cada una de las diez tiendas que participaron en el experimento.\n",
  sep = ""
)

cat(
  "Con la prueba t pareada se evaluaron las diferencias ",
  "de ventas entre ambas condiciones, utilizando los ",
  "promedios calculados para cada tienda.\n",
  sep = ""
)

cat(
  "Es importante señalar que la información utilizada fue simulada, ",
  "por lo que estos resultados no permiten asegurar que cambiar ",
  "la ubicación del producto mejore las ventas reales de RetailAndina.\n",
  sep = ""
)

cat(
  "También se incluyó una promoción simultánea que pudo afectar ",
  "las ventas, por lo que es necesario considerar este factor ",
  "al momento de interpretar los resultados.\n",
  sep = ""
)
