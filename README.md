# Takeoff Helper

A small Python tool that automates a calculation I do in my estimation work.

At my job (Junior Estimation Assistant), I measure materials from project drawings. Lengths come off the drawings in **millimetres**, but ordering and pricing need **metres** and **feet/inches**, plus a **waste allowance** on top. This script does the conversions in one pass and prints a clean costing summary.

> Built as a hands-on Python refresher — automating a repetitive, real task from my own job.

## What it does

- Converts millimetres → metres and → feet/inches
- Adds a waste allowance (10% by default — a common estimating allowance)
- Calculates a cost per line item from a price per metre
- Prints a formatted summary with a grand total

## Sample output

```
TAKEOFF SUMMARY
--------------------------------------------------------------
Skirting board:
  Measured : 12,400 mm = 12.40 m (40 ft 8.2 in)
  Order qty: 13.64 m (incl. 10% waste)
  Cost     : 13.64 m x $3.50 = $47.74

Door frame timber:
  Measured : 8,600 mm = 8.60 m (28 ft 2.6 in)
  Order qty: 9.46 m (incl. 10% waste)
  Cost     : 9.46 m x $5.25 = $49.67

Ceiling batten:
  Measured : 21,300 mm = 21.30 m (69 ft 10.6 in)
  Order qty: 23.43 m (incl. 10% waste)
  Cost     : 23.43 m x $2.80 = $65.60

--------------------------------------------------------------
GRAND TOTAL: $163.01
```

## Run it

```bash
python takeoff.py
```

## Concepts used

Functions · unit conversion · f-strings and number formatting · lists of tuples · loops · constants

---

Mohamed Idris — Computer Programming graduate (Sheridan College) · [Portfolio](https://mohame67tech.github.io/) · [LinkedIn](https://www.linkedin.com/in/mohamed-idris-ds)
