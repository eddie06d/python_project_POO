from models.Route import Route
from models.Plane import Plane

class Flight:
    def __init__(self, route: Route, plane: Plane, departure_time: str):
        self.route: Route = route
        self.plane: Plane = plane
        self.departure_time: str = departure_time