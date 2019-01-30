def food_tax(price):
    return 0.1 * price

def tobacco_tax(price):
    return 10 + 0.02 * price

def entertainment_tax(price):
    return 0 if price <= 100 else 0.01 * (price - 100)

TAX_CODES = [
    {
        "type": "Food",
        "refundable": True,
        "value": food_tax
    },
    {
        "type": "Tobacco",
        "refundable": False,
        "value": tobacco_tax
    },
    {
        "type": "Entertainment",
        "refundable": False,
        "value": entertainment_tax
    }
]