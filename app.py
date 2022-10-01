from typing import Dict, List
from models.FlightDetail import FlightDetail
from models.Flight import Flight
from utils.functions import get_currency_format, get_dict_planes_by_tickets, create_list_flights, list_details_flight
from utils.config import CURRENCY_SYMBOL

# lista de vuelos
flights: List[Flight] = create_list_flights()
 
# list del detalle de los vuelos
list_detail_flights: List[FlightDetail] = []

for k, flight in enumerate(flights):
    code_flight: str = f"{flight.route.code}-{flight.plane.code}"
    list_detail_flights.append(FlightDetail(code_flight, flight))

# cantidad total de pasajes vendidos en todos los vuelos    
quantity_tickets_sold: int = sum([detail_flight.number_economic_seats + detail_flight.number_premium_seats for detail_flight in list_detail_flights])

# ganancia total de pasajes vendidos en clase económica
total_economic_tickets_sold: float = sum([detail_flight.total_economic_seat_sales for detail_flight in list_detail_flights])

# ganancia total de pasajes vendidos en clase premium
total_premium_tickets_sold: float = sum([detail_flight.total_premium_seat_sales for detail_flight in list_detail_flights])

# cantidad total de pasajes vendidos en clase económica
quantity_economic_tickets_sold: int = sum([detail_flight.number_economic_seats for detail_flight in list_detail_flights])

# cantidad total de pasajes vendidos en clase premium
quantity_premium_tickets_sold: int = sum([detail_flight.number_premium_seats for detail_flight in list_detail_flights])

# total de IGV de los pasajes vendidos
total_igv: float = sum([detail_flight.igv for detail_flight in list_detail_flights])

# diccionario con la cantidad de pasajes vendidos por avión
quantity_tickets_by_plane: Dict[str, int] = get_dict_planes_by_tickets(list_detail_flights)

# costo promedio de los pasajes vendidos en clase económica
economic_ticket_avg: float = round(total_economic_tickets_sold / quantity_economic_tickets_sold, 2)

# costo promedio de los pasajes vendidos en clase premium
premium_ticket_avg: float = round(total_premium_tickets_sold / quantity_premium_tickets_sold, 2)

# lista de vuelos ordenada por cantidad de pasajes vendidos
sorted_flights_by_number_seats: List[FlightDetail] = sorted(list_detail_flights, key=lambda x: x.number_economic_seats + x.number_premium_seats)

# lista de vuelos ordenada por ganancia total
sorted_flights_by_total_sales: List[FlightDetail] = sorted(list_detail_flights, key=lambda x: x.total_economic_seat_sales + x.total_premium_seat_sales, reverse=True)

# lista de aviones ordenada por cantidad de pasajes vendidos
planes_higher_passengers: List[Dict[str, int]] = [{ "code": plane_code, "quantity": quantity } for plane_code, quantity in quantity_tickets_by_plane.items() if quantity == max(quantity_tickets_by_plane.values())]

# dar formato a la lista de aviones ordenada por cantidad de pasajes vendidos
format_higher_passengers: str = ", ".join([f"{plane['code']} ({plane['quantity']})" for plane in planes_higher_passengers])

# función para mostrar el menú de opciones
def show_menu() -> (None):
    print("*"*55)
    print("\tPROYECTO AEROLÍNEA EN PYTHON CON POO")
    print("*"*55)
    print("1. Listar detalle de los vuelos programados")
    print("2. Cantidad total de pasajes vendidos en todos los vuelos")
    print("3. Ganancia total de pasajes vendidos en clase económica")
    print("4. Ganancia total de pasajes vendidos en clase premium")
    print("5. Importe total de IGV cobrado por la venta de pasajes")
    print("6. Valor promedio de los pasajes vendidos en clase económica")
    print("7. Valor promedio de los pasajes vendidos en clase premium")
    print("8. Vuelo con la mayor cantidad de pasajeros")
    print("9. Vuelo con la menor cantidad de pasajeros")
    print("10. Tres primeros vuelos con mayores ingresos por la venta de asientos")
    print("11. Avión que transportó la mayor cantidad de pasajeros")
    print("12. Listar todos los parámetros anteriores")
    print("13. Salir")

# bucle infinito para mostrar el menú de opciones
while True:
    # mostrar el menú de opciones
    show_menu()
    # capturar la opción del usuario
    opt: str = input("Ingrese una opción: ")
    print("*"*55)
    print("\n")
    # validar si la opción ingresada es un valor numérico
    if opt.isnumeric():
        # convertir la opción a entero
        option: int = int(opt)
        # validar si la opción ingresada está entre el rango permitido
        if option not in [x for x in range(1, 14)]:
            print("La opción ingresada no es válida, intente nuevamente")
        else:
            # mostrando el resultado de la opción seleccionada
            if option == 1:
                list_details_flight(list_detail_flights)
            elif option == 2:
                print(f"La cantidad total de pasajes vendidos en todos los vuelos es de {quantity_tickets_sold}")
            elif option == 3:
                print(f"La ganancia total de pasajes vendidos en clase económica es de {get_currency_format( CURRENCY_SYMBOL, total_economic_tickets_sold)}")
            elif option == 4:
                print(f"La ganancia total de pasajes vendidos en clase premium es de {get_currency_format( CURRENCY_SYMBOL, total_premium_tickets_sold)}")
            elif option == 5:
                print(f"El importe total de IGV cobrado por la venta de pasajes es de {get_currency_format(CURRENCY_SYMBOL,total_igv)}")
            elif option == 6:
                print(f"El valor promedio de los pasajes vendidos en clase económica es de {get_currency_format(CURRENCY_SYMBOL,economic_ticket_avg)}")
            elif option == 7:
                print(f"El valor promedio de los pasajes vendidos en clase premium es de {get_currency_format(CURRENCY_SYMBOL,premium_ticket_avg)}")
            elif option == 8:
                print(f"El vuelo con la mayor cantidad de pasajeros es el {sorted_flights_by_number_seats[-1].code}")
            elif option == 9:
                print(f"El vuelo con la menor cantidad de pasajeros es el {sorted_flights_by_number_seats[0].code}")
            elif option == 10:
                print("Los tres primeros vuelos con mayores ingresos por la venta de asientos son: {', '.join([x.code for x in sorted_flights_by_total_sales[:3]])}")
            elif option == 11:
                print(f"El avión que transportó la mayor cantidad de pasajeros es el {', '.join(planes_higher_passengers)}")
            elif option == 12:
                print(f"Cantidad total de pasajes vendidos en todos los vuelos: {quantity_tickets_sold}")
                print(f"Ganancia total de pasajes vendidos en clase económica: {get_currency_format( CURRENCY_SYMBOL, total_economic_tickets_sold)}")
                print(f"Ganancia total de pasajes vendidos en clase premium: {get_currency_format( CURRENCY_SYMBOL, total_premium_tickets_sold)}")
                print(f"Importe total de IGV cobrado por la venta de pasajes: {get_currency_format(CURRENCY_SYMBOL,total_igv)}")
                print(f"Valor promedio de los pasajes vendidos en clase económica: {get_currency_format(CURRENCY_SYMBOL,economic_ticket_avg)}")
                print(f"Valor promedio de los pasajes vendidos en clase premium: {get_currency_format(CURRENCY_SYMBOL,premium_ticket_avg)}")
                print(f"Vuelo con la mayor cantidad de pasajeros: {sorted_flights_by_number_seats[-1].code} ({sorted_flights_by_number_seats[-1].number_economic_seats + sorted_flights_by_number_seats[-1].number_premium_seats})")
                print(f"Vuelo con la menor cantidad de pasajeros: {sorted_flights_by_number_seats[0].code} ({sorted_flights_by_number_seats[0].number_economic_seats + sorted_flights_by_number_seats[0].number_premium_seats})")
                print(f"Tres primeros vuelos con mayores ingresos por la venta de asientos: \n{', '.join([f'{x.code} ({get_currency_format(CURRENCY_SYMBOL, x.total)})' for x in sorted_flights_by_total_sales[:3]])}")
                print(f"Avión que transportó la mayor cantidad de pasajeros: {format_higher_passengers}")
            else:
                print("Gracias por utilizar el programa, hasta luego")
                break
    else:
        print("Por favor ingrese un valor numérico, intente nuevamente")
    print("\n")