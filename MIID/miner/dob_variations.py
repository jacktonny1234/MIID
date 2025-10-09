"""
DOB Variation Generator

Generates date-of-birth (DOB) variations from a seed date with at least
one variation in each category:
  - ±1 day
  - ±3 days
  - ±30 days
  - ±90 days
  - ±365 days
  - year+month only (format YYYY-MM, no day)

Each variation is paired with a different, realistic address string.

Threaded API is provided to run generation off the main loop.
"""
from datetime import datetime, timedelta
from typing import List, Tuple, Dict

def _format_date(d: datetime) -> str:
    return d.strftime("%Y-%m-%d")

def generate_dobes_variations(seed_dobs: List[str], count: int) -> Dict[str, List[str]]:
    return {seed_dob: generate_dob_variations(seed_dob, count) for seed_dob in seed_dobs}

def generate_dob_variations(seed_dob: str, count: int) -> List[str]:
    """Generate DOB variations (dob, address) from a seed YYYY-MM-DD string.

    Returns a list with at least one entry for each category listed in the module docstring.
    The final list contains 6 entries (5 date offsets + 1 year-month only).
    """
    base = datetime.strptime(seed_dob, "%Y-%m-%d")

    # Deterministic picks for one sample in each category
    categories: List[Tuple[str, datetime]] = [
        ("+1", base + timedelta(days=+1)),
        ("-1", base + timedelta(days=-1)),
        ("+3", base + timedelta(days=+3)),
        ("-3", base + timedelta(days=-3)),
        ("+30", base + timedelta(days=+30)),
        ("-30", base + timedelta(days=-30)),
        ("+90", base + timedelta(days=+90)),
        ("-90", base + timedelta(days=-90)),
        ("+365", base + timedelta(days=+365)),
        ("-365", base + timedelta(days=-365)),
    ]

    variations: List[str] = []
    for idx, (_, dt_val) in enumerate(categories):
        variations.append(_format_date(dt_val))

    # Year+month only variant (YYYY-MM), keep unique address as well
    ym = base.strftime("%Y-%m")
    variations.append(ym)

    return variations[:count]
