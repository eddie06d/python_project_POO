from typing import Dict, List
from models.Route import Route
from models.Plane import Plane
from models.FlightDetail import FlightDetail
from models.Flight import Flight
from utils.data import ROUTES, FLIGHTS
from utils.functions import get_currency_format
from utils.config import CURRENCY_SYMBOL

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

# lista de vuelos
flights: List[Flight] = create_list_flights()
 
# list del detalle de los vuelos
list_detail_flights: List[FlightDetail] = []

for k, flight in enumerate(flights):
    code_flight: str = f"{flight.route.code}-{flight.plane.code}"
    list_detail_flights.append(FlightDetail(code_flight, flight))

# cantidad total de pasajes vendidos    
quantity_tickets_sold: int = 0

# ganancia total de pasajes vendidos en clase económica
total_economic_tickets_sold: float = 0

# ganancia total de pasajes vendidos en clase premium
total_premium_tickets_sold: float = 0

# cantidad total de pasajes vendidos en clase económica
quantity_economic_tickets_sold: int = 0

# cantidad total de pasajes vendidos en clase premium
quantity_premium_tickets_sold: int = 0

# total de IGV de los pasajes vendidos
total_igv: float = 0

# diccionario con la cantidad de pasajes vendidos por avión
quantity_tickets_by_plane: Dict[str, int] = {}

for k, detailFlight in enumerate(list_detail_flights):
    route: Route = detailFlight.flight.route
    plane: Plane = detailFlight.flight.plane
    total_economic_tickets_sold += detailFlight.total_economic_seat_sales
    total_premium_tickets_sold += detailFlight.total_premium_seat_sales
    quantity_economic_tickets_sold += detailFlight.number_economic_seats
    quantity_premium_tickets_sold += detailFlight.number_premium_seats
    total_igv += detailFlight.igv
    
    if detailFlight.flight.plane.code in quantity_tickets_by_plane:
        quantity_tickets_by_plane[detailFlight.flight.plane.code] += detailFlight.number_economic_seats + detailFlight.number_premium_seats
    else:
        quantity_tickets_by_plane[detailFlight.flight.plane.code] = detailFlight.number_economic_seats + detailFlight.number_premium_seats
    
    print("*"*30)
    print(f"Flight {k+1}")
    print("*"*15)
    print(f"Route code: {route.code}")
    print(f"Route name: {route.name}")
    print(f"Departure time: {detailFlight.flight.departure_time}")
    print(f"Number of economic seats: {detailFlight.number_economic_seats}")
    print(f"Total economic ticket sales: {get_currency_format(CURRENCY_SYMBOL, detailFlight.total_economic_seat_sales)}")
    print(f"Number of premium seats: {detailFlight.number_premium_seats}")
    print(f"Total premium ticket sales: {get_currency_format(CURRENCY_SYMBOL, detailFlight.total_premium_seat_sales)}")
    print(f"Subtotal: {get_currency_format(CURRENCY_SYMBOL, detailFlight.subtotal)}")
    print(f"IGV: {get_currency_format(CURRENCY_SYMBOL, detailFlight.igv)}")
    print(f"Total: {get_currency_format(CURRENCY_SYMBOL, detailFlight.total)}")
    print(f"Plane code: {plane.code}")
    print()

quantity_tickets_sold = quantity_economic_tickets_sold + quantity_premium_tickets_sold

# costo promedio de los pasajes vendidos en clase económica
economic_ticket_avg: float = round(total_economic_tickets_sold / quantity_economic_tickets_sold, 2)

# costo promedio de los pasajes vendidos en clase premium
premium_ticket_avg: float = round(total_premium_tickets_sold / quantity_premium_tickets_sold, 2)

# lista de vuelos ordenada por cantidad de pasajes vendidos
sorted_flights_by_number_seats: List[FlightDetail] = sorted(list_detail_flights, key=lambda x: x.number_economic_seats + x.number_premium_seats)

# lista de vuelos ordenada por ganancia total
sorted_flights_by_total_sales: List[FlightDetail] = sorted(list_detail_flights, key=lambda x: x.total_economic_seat_sales + x.total_premium_seat_sales)

print("#"*30)
print(f"Total pasajes vendidos: {quantity_tickets_sold}")
print(f"Total ingresos por pasajes económicos: {get_currency_format(CURRENCY_SYMBOL,total_economic_tickets_sold)}")
print(f"Total ingresos por pasajes premium: {get_currency_format(CURRENCY_SYMBOL,total_premium_tickets_sold)}")
print(f"Importe total de IGV: {get_currency_format(CURRENCY_SYMBOL,total_igv)}")
print(f"Valor promedio de un pasaje económico: {get_currency_format(CURRENCY_SYMBOL,economic_ticket_avg)}")
print(f"Valor promedio de un pasaje premium: {get_currency_format(CURRENCY_SYMBOL,premium_ticket_avg)}")
print(f"Vuelo con la mayor cantidad de pasajeros: {sorted_flights_by_number_seats[-1].code}")
print(f"Vuelo con la menor cantidad de pasajeros: {sorted_flights_by_number_seats[0].code}")
print(f"3 primeros vuelos con la mayor cantidad de ingresos: {sorted_flights_by_total_sales[-1].code}, {sorted_flights_by_total_sales[-2].code}, {sorted_flights_by_total_sales[-3].code}")

# lista de aviones ordenada por cantidad de pasajes vendidos
planes_higher_passengers: List[str] = [plane_code for plane_code, quantity in quantity_tickets_by_plane.items() if quantity == max(quantity_tickets_by_plane.values())]

print(f"Avión(es) que transportó la mayor cantidad de pasajeros: {', '.join(planes_higher_passengers)}")

print(quantity_tickets_by_plane)