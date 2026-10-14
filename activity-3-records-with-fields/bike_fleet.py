"""
Bike Hire Fleet

A working program. Each bike in the fleet is a dictionary with the
same set of fields, and the fleet is a list of those dictionaries.

This is what two-level data almost always looks like in real code:
not a grid of numbers, but a list of records that each have named
fields.
"""

LOW_BATTERY = 30

fleet = [
    {"id": "B-104", "station": "Kings Cross", "battery": 88, "available": True},
    {"id": "B-107", "station": "Shoreditch", "battery": 22, "available": True},
    {"id": "B-111", "station": "Kings Cross", "battery": 64, "available": False},
    {"id": "B-118", "station": "Peckham", "battery": 15, "available": True},
    {"id": "B-120", "station": "Shoreditch", "battery": 91, "available": False},
    {"id": "B-123", "station": "Birmingham", "battery": 70, "available": False},
]


def ready_to_hire(fleet):
    """Bikes that are available and have enough charge."""
    ready = []
    for bike in fleet:
        if bike["available"] and bike["battery"] > LOW_BATTERY:
            ready.append(bike["id"])
    return ready


def needs_charging(fleet):
    """Bikes at or below the low battery threshold, wherever they are."""
    flagged = []
    for bike in fleet:
        if bike["battery"] <= LOW_BATTERY:
            flagged.append(bike["id"])
    return flagged


def bikes_at(fleet, station):
    """Every bike currently at one station."""
    found = []
    for bike in fleet:
        if bike["station"] == station:
            found.append(bike["id"])
    return found


def average_battery(fleet):
    total = 0
    for bike in fleet:
        total = total + bike["battery"]
    return total / len(fleet)

def battery_availability(fleet):
    total = 0
    count = 0
    for bike in fleet:
        if bike["available"] == True:
            total += bike["battery"]
            count += 1
    return total/count
    

    


print(f"{len(fleet)} bikes in the fleet")
print(f"Fields on each bike: {list(fleet[0].keys())}")
print("---")
print(f"Ready to hire: {ready_to_hire(fleet)}")
print(f"Needs charging: {needs_charging(fleet)}")
print(f"At Kings Cross: {bikes_at(fleet, 'Kings Cross')}")
print(f"At Shoreditch: {bikes_at(fleet, 'Shoreditch')}")

print(f"Average battery: {average_battery(fleet):.1f}%")

print(fleet[0]["battery"])
print(list(fleet[0].keys()))
print(f"Average battery of available bikes: {battery_availability(fleet):.1f}%")


