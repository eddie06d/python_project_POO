from typing import Dict

class Route:
    def __init__(self, code: str, name: str, price_base: float, price_economic_seat: float, price_premium_seat: float, range_economic_ticket_sales: Dict[str, int], range_premium_ticket_sales: Dict[str, int]):
        self.code: str = code
        self.name: str = name
        self.price_base: float = price_base
        self.price_economic_seat: float = price_economic_seat
        self.price_premium_seat: float = price_premium_seat
        self.min_economic_ticket_sales: int = range_economic_ticket_sales['min']
        self.max_economic_ticket_sales: int = range_economic_ticket_sales['max']
        self.min_premium_ticket_sales: int = range_premium_ticket_sales['min']
        self.max_premium_ticket_sales: int = range_premium_ticket_sales['max']