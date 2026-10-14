"""
Three things below are wrong. Nothing crashes.

Two grids and one fleet. Each one produces an answer that looks
entirely reasonable.
"""

# ---------- 1: building a grid ----------

grid = [[0] * 3 for i in range(3)]

print("Grid after setting the top-left corner to 9:")
for row in grid:
    print(row)

grid[0][0] = 9

print("Grid after setting the top-left corner to 9:")
for row in grid:
    print(row)

# ---------- 2: totalling a column ----------

sales = [
    [12, 15, 9],
    [20, 18, 11],
    [7, 14, 22],
]


def column_total(table, column):
    """Add up one column of the table."""
    total = 0
    for row in table:
        total += row[column]
    return total


print("---")
print(f"Column 0 total: {column_total(sales, 0)}")
print(f"Column 1 total: {column_total(sales, 1)}")

# ---------- 3: searching a list of records ----------

fleet = [
    {"id": "B-104", "station": "Kings Cross"},
    {"id": "B-107", "station": "Shoreditch"},
    {"id": "B-111", "station": "Kings Cross"},
]


def is_at_station(fleet, bike_id, station):
    """Return True if that bike is currently at that station."""
    for bike in fleet:
        if bike["id"] == bike_id and bike["station"] == station:
            return True
    return False




print("---")
print(f"B-104 at Kings Cross? {is_at_station(fleet, 'B-104', 'Kings Cross')}")
print(f"B-111 at Kings Cross? {is_at_station(fleet, 'B-111', 'Kings Cross')}")
print(f"B-111 at Kings Cross? {is_at_station(fleet, 'B-107', 'Kings Cross')}")
print(f"B-111 at Kings Cross? {is_at_station(fleet, 'B-107', 'Shoreditch')}")

