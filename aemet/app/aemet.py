import json
import os
import urllib3

# Diccionario de municipios y sus códigos postales correspondientes
municipios = {
    "Barcelona": "08019",
    "Madrid": "28079",
    "Valencia": "46250",
    "Girona": "17079",
    # Agrega más municipios y códigos según sea necesario
}

# Función para obtener los datos diarios de predicción meteorológica según el nombre del municipio.
def get_daily_city_by_name(city_name):
    # Convertimos el nombre del municipio en su código postal correspondiente usando el diccionario.
    if city_name in municipios:
        city_code = municipios[city_name]
    else:
        raise ValueError(f"No se ha encontrado el código postal para el municipio '{city_name}'.")

    return get_daily_city(city_code)

# Función para obtener los datos diarios de predicción meteorológica de una ciudad en función del código postal.
def get_daily_city(city_code):
    path = f"data/{city_code}.json"
    if os.path.isfile(path):
        with open(path, "r") as file:
            data = file.read()
    else:
        data = get_data_city(city_code)
        if not os.path.isdir("data"):
            os.makedirs("data")
        with open(path, "w") as file:
            file.write(data)
    return json.loads(data)

# Función para obtener los datos de predicción meteorológica desde la API de AEMET en función del código postal.
def get_data_city(city_code):
    key = get_key()
    url = f"https://opendata.aemet.es/opendata/api/prediccion/especifica/municipio/diaria/{city_code}/?api_key={key}"
    response = urllib3.request("GET", url)
    if response.status == 200:
        datos = response.json()["datos"]
    else:
        raise Exception(f"Error {response.status}: {url}")
    
    response = urllib3.request("GET", datos)
    if response.status == 200:
        data = response.data.decode("latin-1")
        return data
    else:
        raise Exception(f"Error {response.status}: {url}")

# Función para obtener la clave de API desde un archivo de configuración.
def get_key():
    file = "config.json"
    if not os.path.isfile(file):
        raise Exception(f"Config file not found: {config.json}")
    with open(file, "r") as file:
        config = json.load(file)
        return config["key"]


# Función para obtener los datos diarios de predicción meteorológica de una ciudad en función del código postal.
def get_daily_municipio(municipio):
    path = f"data/{municipio}.json"
    if os.path.isfile(path):
        with open(path, "r") as file:
            data = file.read()
    else:
        data = get_data_municipios(municipio)
        if not os.path.isdir("data"):
            os.makedirs("data")
        with open(path, "w") as file:
            file.write(data)
    return json.loads(data)

# Función para obtener los datos de predicción meteorológica desde la API de AEMET en función del código postal.
def get_data_municipios(municipio):
    key = get_key_mun()
    
    url = f"https://opendata.aemet.es/opendata/api/prediccion/especifica/municipio/diaria/{municipio}?api_key={key}"
    
    response = urllib3.request("GET", url)
    print(response.json())
    if response.status == 200:
        print(response.json())
        datos = response.json()["datos"]
    else:
        raise Exception(f"Error {response.status}: {url}")
    
    response = urllib3.request("GET", datos)
    if response.status == 200:
        data = response.data.decode("latin-1")
        return data
    else:
        raise Exception(f"Error {response.status}: {url}")



# Función para obtener la clave de API desde un archivo de configuración.
def get_key_mun():
    file = "config.json"
    if not os.path.isfile(file):
        raise Exception(f"Config file not found: {config.json}")
    with open(file, "r") as file:
        config = json.load(file)
        return config["key"]