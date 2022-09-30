from typing import Dict, List
from models.FlightDetail import FlightDetail
from models.Route import Route
from models.Plane import Plane
from models.Flight import Flight
from utils.config import CURRENCY_SYMBOL
from utils.data import ROUTES, FLIGHTS

def get_currency_format(currency_symbol: str, amount: float) -> (str):
    """
    Función para formatear una variable numérica en string con formato de moneda
    """
    return "{}{:,.2f}".format(currency_symbol, amount)

def list_details_flight(list_detail_flights: List[FlightDetail]) -> (None):
    """
    Función para listar los detalles de cada vuelo
    """
    for k, detailFlight in enumerate(list_detail_flights):
        # extrayendo los objetos de ruta y avion del detalle del vuelo
        route: Route = detailFlight.flight.route
        plane: Plane = detailFlight.flight.plane
        
        print("#"*30)
        print(f"Flight {k+1}")
        print("#"*15)
        print(f"Código de la Ruta: {route.code}")
        print(f"Nombre de la Ruta: {route.name}")
        print(f"Hora de salida: {detailFlight.flight.departure_time}")
        print(f"Número de asientos económicos vendidos: {detailFlight.number_economic_seats}")
        print(f"Ganancias total por la venta de asientos económicos: {get_currency_format(CURRENCY_SYMBOL, detailFlight.total_economic_seat_sales)}")
        print(f"Número de asientos premium vendidos: {detailFlight.number_premium_seats}")
        print(f"Ganancias total por la venta de asientos premium: {get_currency_format(CURRENCY_SYMBOL, detailFlight.total_premium_seat_sales)}")
        print(f"Subtotal: {get_currency_format(CURRENCY_SYMBOL, detailFlight.subtotal)}")
        print(f"IGV: {get_currency_format(CURRENCY_SYMBOL, detailFlight.igv)}")
        print(f"Total: {get_currency_format(CURRENCY_SYMBOL, detailFlight.total)}")
        print(f"Código del Avión: {plane.code}")
        print()

def get_dict_planes_by_tickets(list_detail_flights: List[FlightDetail]) -> (Dict[str, int]):
    """
    Función para armar un diccionario con la cantidad de asientos vendidos por cada avión
    """
    quantity_tickets_by_plane: Dict[str, int] = {}
    
    for k, detailFlight in enumerate(list_detail_flights):
        # extrayendo el objeto avion del detalle del vuelo
        plane: Plane = detailFlight.flight.plane
    
        # armando el diccionario con la cantidad de pasajes vendidos por avión
        if plane.code in quantity_tickets_by_plane:
            quantity_tickets_by_plane[plane.code] += detailFlight.number_economic_seats + detailFlight.number_premium_seats
        else:
            quantity_tickets_by_plane[plane.code] = detailFlight.number_economic_seats + detailFlight.number_premium_seats
    
    return quantity_tickets_by_plane

def create_list_routes() -> (List[Route]):
    """
    Función que crea una lista de objetos Route a partir de la lista de diccionarios ROUTES
    """
    routes: List[Route] = []
    
    for k, route in enumerate(ROUTES):
        obj_route: Route = Route(route['code'], route['name'], route['price_base'], route['price_economic_seat'], route['price_premium_seat'], route['range_economic_ticket_sales'], route['range_premium_ticket_sales'])
        routes.append(obj_route)
    
    return routes

def create_list_planes() -> (List[Plane]):
    """
    Función que crea una lista de objetos Plane a partir de una lista de código de aviones
    """
    planes: List[Plane] = [Plane(f"A00{i+1}") for i in range(4)]
    return planes

def create_list_flights() -> (List[Flight]):
    """ 
    Función que crea una lista de objetos Flight a partir de la lista de diccionarios FLIGHTS
    """
    flights: List[Flight] = []
    routes: List[Route] = create_list_routes()
    planes: List[Plane] = create_list_planes()
    
    for k, flight in enumerate(FLIGHTS):
        obj_route: Route = [route for route in routes if route.name.upper() == flight['route']][0]
        obj_plane: Plane = [plane for plane in planes if plane.code == flight['plane']][0]
        flights.append(Flight(obj_route, obj_plane, flight['departure_time']))
    
    return flights