"""
Fleet Maintenance Report

Three things below are wrong. Nothing crashes, and nothing prints an
error message. Every fault in this file is a try or an except doing
something it should not.

The depot uses this report to decide which bikes to collect
overnight.
"""

LOW_BATTERY = 30

fleet = [
    {"id": "B-104", "station": "Kings Cross", "battery": "88"},
    {"id": "B-107", "station": "Shoreditch", "battery": "22"},
    {"id": "B-111", "station": "Kings Cross", "charge": "8"},
    {"id": "B-118", "station": "Peckham", "battery": "unknown"},
    {"id": "B-120", "station": "Shoreditch", "battery": "91"},
]


def battery_percent(bike):
    """The bike's battery level as a number."""
    try:
        return int(bike["battery"])
    except ValueError:
        return None


def needs_collecting(fleet):
    """Every bike at or below the low battery threshold."""
    flagged = []
    for bike in fleet:
        try:
            battery = battery_percent(bike)

            if battery is not None and battery <= LOW_BATTERY:
                flagged.append(bike["id"])
        except KeyError as e:
            print(f"{bike['id']} does not have a valid battery reading")
    return flagged


def stations_covered(fleet):
    """Every station that has at least one bike."""

    stations = []
    for bike in fleet:
        if bike["station"] not in stations:
            stations.append(bike["station"])
    return stations


print(f"Fleet size: {len(fleet)}")
print(f"Needs collecting: {needs_collecting(fleet)}")
print(f"Stations covered: {stations_covered(fleet)}")
