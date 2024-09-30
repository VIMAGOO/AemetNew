import aemet
from tabulate import tabulate

# Solicitamos al usuario el código de la ciudad
#city = input("City: (08017) ")
city = "08017"
# Obtenemos los datos diarios de AEMET
#data = aemet.get_daily_city(city)[0]
#data = aemet.get_daily_city_by_name(municipio)[0]
value = 0
municipio = "Abrera"
#data = aemet.get_data_city(city)

data = aemet.get_data_municipios(municipio)
print(data)

if (value != 0):
    # Mostramos el nombre de la ciudad y la provincia
    print(f"{data['nombre']} : {data['provincia']}")

    # Menú de opciones para el usuario
    print("\n¿Qué dato meteorológico deseas obtener?")
    print("1. Probabilidad de precipitación")
    print("2. Temperatura")
    print("3. Humedad")
    print("4. Velocidad del viento")

    # Capturamos la opción elegida por el usuario
    opcion = input("\nSelecciona una opción (1-4): ")

    # Mostramos la información en función de la opción seleccionada
    if opcion == "1":
        print("\nProbabilidad de precipitación:")
        print(tabulate(data["prediccion"]["dia"][0]["probPrecipitacion"], headers="keys"))
    elif opcion == "2":
        print("\nTemperatura:")
        print("Temperatura máxima: ", data["prediccion"]["dia"][0]["temperatura"]["maxima"])
        print("Temperatura mínima: ", data["prediccion"]["dia"][0]["temperatura"]["minima"])
        print("\n", tabulate(data["prediccion"]["dia"][0]["temperatura"]["dato"], headers="keys"))
    elif opcion == "3":
        print("\nHumedad relativa:")
        print("Humedad máxima: ", data["prediccion"]["dia"][0]["humedadRelativa"]["maxima"])
        print("Humedad mínima: ", data["prediccion"]["dia"][0]["humedadRelativa"]["minima"])
        print("\n", tabulate(data["prediccion"]["dia"][0]["humedadRelativa"]["dato"], headers="keys"))
    elif opcion == "4":
        print("\nVelocidad del viento:")
        print(tabulate(data["prediccion"]["dia"][0]["viento"], headers="keys"))
    else:
        print("Opción no válida. Por favor, selecciona una opción entre 1 y 4.")
