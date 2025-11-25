"""A collection of question templates which are used in the app"""

def bond_price_from_ytm(face, coupon_rate, years, y):
    """Price of annual-pay coupon bond with face (par), coupon_rate in % (e.g., 3.0) and annual yield y (decimal)."""
    c = coupon_rate/100.0 * face
    price = 0.0
    for t in range(1, years+1):
        price += c / ((1.0 + y) ** t)
    price += face / ((1.0 + y) ** years)
    return price


def ytm_from_price(face, coupon_rate, years, price, guess=0.03):
    """Solve for annual YTM (decimal) given price using Newton or bisection fallback."""
    # Use bisection in [0, 1] to be robust
    lo, hi = -0.999, 1.0  # allow negative yields a bit
    for _ in range(60):
        mid = (lo + hi) / 2
        p = bond_price_from_ytm(face, coupon_rate, years, mid)
        if p > price:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2

