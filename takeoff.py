"""
Takeoff Helper — a small Python tool from my estimation work.

At my job I measure materials from project drawings: lengths come off the
drawings in millimetres, but pricing often needs metres and feet/inches,
plus a waste allowance on top. I used to do these conversions by hand in a
calculator. This script does them in one pass and prints a clean summary.

Built as a hands-on Python refresher, automating a calculation I do at work.
"""

# Waste allowance added on top of measured quantities (10% is a common allowance)
WASTE_PERCENT = 10


def mm_to_metres(mm):
    """Convert millimetres to metres."""
    return mm / 1000


def mm_to_feet_inches(mm):
    """Convert millimetres to (feet, inches), inches rounded to 1 decimal."""
    total_inches = mm / 25.4
    feet = int(total_inches // 12)
    inches = round(total_inches - feet * 12, 1)
    return feet, inches


def add_waste(quantity, waste_percent=WASTE_PERCENT):
    """Return the quantity with the waste allowance added."""
    return quantity * (1 + waste_percent / 100)


def line_total(quantity_with_waste, unit_price):
    """Cost of one line item."""
    return quantity_with_waste * unit_price


# Sample takeoff: (item name, measured length in mm, price per metre)
takeoff_items = [
    ("Skirting board", 12400, 3.50),
    ("Door frame timber", 8600, 5.25),
    ("Ceiling batten", 21300, 2.80),
]


def main():
    print("TAKEOFF SUMMARY")
    print("-" * 62)
    grand_total = 0.0

    for name, length_mm, price_per_m in takeoff_items:
        metres = mm_to_metres(length_mm)
        feet, inches = mm_to_feet_inches(length_mm)
        order_metres = add_waste(metres)
        cost = line_total(order_metres, price_per_m)
        grand_total += cost

        print(f"{name}:")
        print(f"  Measured : {length_mm:,.0f} mm = {metres:.2f} m ({feet} ft {inches} in)")
        print(f"  Order qty: {order_metres:.2f} m (incl. {WASTE_PERCENT}% waste)")
        print(f"  Cost     : {order_metres:.2f} m x ${price_per_m:.2f} = ${cost:,.2f}")
        print()

    print("-" * 62)
    print(f"GRAND TOTAL: ${grand_total:,.2f}")


if __name__ == "__main__":
    main()
