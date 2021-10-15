from logger import LOG
from flask import Blueprint, request, Response
import tachometer_service as service

tachometer_api = Blueprint('tachometer', __name__, url_prefix='/tachometer')


@tachometer_api.route('/', methods=['POST'])
def create_route_record():
    # Parse Input
    LOG.debug(f'{__name__} Request Received: {request.get_json()}')
    data = request.get_json()
    # Validate Input
    if 'driver' not in data or 'vehicle' not in data or 'start' not in data or 'speed' not in data:
        LOG.error(f'Bad Request: {data}')
        return Response('Problem', status=400)

    # Call Service
    result = service.record_route(data['driver'], data['vehicle'], data['start'], data['speed'])

    # Serialize Result
    return Response(result, status=200)

@tachometer_api.route('/drivers', methods=['GET'])
def read_drivers():
    return {
        'drivers': service.read_drivers()
    }

@tachometer_api.route('/drivers/<driver>')
def read_vechiles_of_driver(driver: str):
    return {
        'vehicles': service.read_vehicles_of_driver(driver)
    }
