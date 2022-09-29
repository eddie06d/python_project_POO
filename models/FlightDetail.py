from models.Flight import Flight
from utils.config import IGV_PERCENT
import random

class FlightDetail:
    def __init__(self, code: str, flight: Flight):
        # código del detalle del vuelo
        self.code: str = code
        # vuelo al que pertenece el ticket
        self.flight: Flight = flight
        # cantidad de asientos económicos asociados al ticket
        self.number_economic_seats: int = random.randint(flight.route.min_economic_ticket_sales, flight.route.max_economic_ticket_sales)
        # cantidad de asientos premium asociados al ticket
        self.number_premium_seats: int = random.randint(flight.route.min_premium_ticket_sales, flight.route.max_premium_ticket_sales)
        # precio total de los asientos económicos
        self.total_economic_seat_sales: float = round(self.number_economic_seats * (flight.route.price_base + flight.route.price_economic_seat), 2)
        # precio total de los asientos premium
        self.total_premium_seat_sales: float = round(self.number_premium_seats * (flight.route.price_base + flight.route.price_premium_seat), 2)
        # subtotal del ticket
        self.subtotal: float = round(self.total_economic_seat_sales + self.total_premium_seat_sales, 2)
        # igv del ticket
        self.igv: float = round(self.subtotal * IGV_PERCENT / 100, 2)
        # total del ticket
        self.total: float = round(self.subtotal + self.igv, 2)