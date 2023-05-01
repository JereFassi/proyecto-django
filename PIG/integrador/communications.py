import requests

def consulta_geodecode(domicilio_datos):

    BASE_URL = 'https://geocode.maps.co/search?'
    BASE_URL = 'https://nominatim.openstreetmap.org/search?format=json'

    req = f"{BASE_URL}&street={domicilio_datos['street']}&city={domicilio_datos['city']}&state={domicilio_datos['state']}&postalcode={domicilio_datos['postalcode']}&country={domicilio_datos['country']}"
    req = req.replace(" ", "+")
    
    response = requests.get(req)
    data = response.json()

    return data