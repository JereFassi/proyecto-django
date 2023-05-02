import logging
import requests

logger = logging.getLogger(__name__)

def consulta_geodecode(domicilio_datos):

    BASE_URL = 'https://geocode.maps.co/search?'
    BASE_URL = 'https://nominatim.openstreetmap.org/search?format=json'

    request = f"{BASE_URL}&street={domicilio_datos['street']}&city={domicilio_datos['city']}&state={domicilio_datos['state']}&postalcode={domicilio_datos['postalcode']}&country={domicilio_datos['country']}"
    request = request.replace(" ", "+")
    
    data = None
    try:
        response = requests.get(request)
        data = response.json()
    except requests.exceptions.HTTPError as err:
        logger.error(err)
    except requests.exceptions.ConnectionError as err:
        logger.error(err)
    except requests.exceptions.Timeout as err:
        logger.error(err)
    except requests.exceptions.RequestException as err:
        logger.error(err)

    return data