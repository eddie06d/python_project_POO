from typing import Dict, List

ROUTES: List[Dict[str, str | float | int | Dict[str, int]]] = [
    {
        "code": "LIM-AYA",
        "name": "Lima - Ayacucho",
        "price_base": 55.19,
        "price_economic_seat": 8,
        "price_premium_seat": 16,
        "range_economic_ticket_sales": {
                "min": 120,
                "max": 130
        },
        "range_premium_ticket_sales": {
            "min": 10,
            "max": 20
        }
    },
    {
        "code": "LIM-CUS",
        "name": "Lima - Cusco",
        "price_base": 136.51,
        "price_economic_seat": 8,
        "price_premium_seat": 16,
        "range_economic_ticket_sales": {
                "min": 130,
                "max": 144
        },
        "range_premium_ticket_sales": {
            "min": 15,
            "max": 24
        }
    },
    {
        "code": "LIM-ARE",
        "name": "Lima - Arequipa",
        "price_base": 90.59,
        "price_economic_seat": 8,
        "price_premium_seat": 16,
        "range_economic_ticket_sales": {
                "min": 115,
                "max": 138
        },
        "range_premium_ticket_sales": {
            "min": 16,
            "max": 22
        }
    },
    {
        "code": "LIM-TAR",
        "name": "Lima - Tarapoto",
        "price_base": 71.89,
        "price_economic_seat": 8,
        "price_premium_seat": 16,
        "range_economic_ticket_sales": {
                "min": 100,
                "max": 120
        },
        "range_premium_ticket_sales": {
            "min": 12,
            "max": 18
        }
    },
    {
        "code": "AYA-LIM",
        "name": "Ayacucho - Lima",
        "price_base": 40.42,
        "price_economic_seat": 7,
        "price_premium_seat": 16,
        "range_economic_ticket_sales": {
                "min": 100,
                "max": 115
        },
        "range_premium_ticket_sales": {
            "min": 10,
            "max": 15
        }
    },
    {
        "code": "CUS-LIM",
        "name": "Cusco - Lima",
        "price_base": 124.32,
        "price_economic_seat": 7,
        "price_premium_seat": 16,
        "range_economic_ticket_sales": {
                "min": 105,
                "max": 120
        },
        "range_premium_ticket_sales": {
            "min": 14,
            "max": 20
        }
    },
    {
        "code": "ARE-LIM",
        "name": "Arequipa - Lima",
        "price_base": 86.59,
        "price_economic_seat": 7,
        "price_premium_seat": 16,
        "range_economic_ticket_sales": {
                "min": 100,
                "max": 110
        },
        "range_premium_ticket_sales": {
            "min": 13,
            "max": 18
        }
    },
    {
        "code": "TAR-LIM",
        "name": "Tarapoto - Lima",
        "price_base": 68.42,
        "price_economic_seat": 7,
        "price_premium_seat": 16,
        "range_economic_ticket_sales": {
                "min": 90,
                "max": 105
        },
        "range_premium_ticket_sales": {
            "min": 10,
            "max": 15
        }
    }
]

FLIGHTS: List[Dict[str, str]] = [
    {
        "route": "LIMA - AYACUCHO",
        "plane": "A001",
        "departure_time": "06:30 AM"
    },
    {
        "route": "LIMA - CUSCO",
        "plane": "A002",
        "departure_time": "07:25 AM"
    },
    {
        "route": "LIMA - AREQUIPA",
        "plane": "A003",
        "departure_time": "08:10 AM"
    },
    {
        "route": "LIMA - TARAPOTO",
        "plane": "A004",
        "departure_time": "08:50 AM"
    },
    {
        "route": "AYACUCHO - LIMA",
        "plane": "A001",
        "departure_time": "15:45 PM"
    },
    {
        "route": "CUSCO - LIMA",
        "plane": "A002",
        "departure_time": "16:25 PM"
    },
    {
        "route": "AREQUIPA - LIMA",
        "plane": "A003",
        "departure_time": "17:15 PM"
    },
    {
        "route": "TARAPOTO - LIMA",
        "plane": "A004",
        "departure_time": "17:50 PM"
    }
]
