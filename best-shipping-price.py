weight = input("Weight of the package: ")

try:
    float(weight)
except ValueError:
    weight = input("Please input numeric value for weight of the package: ")

weight = float(weight)

# ground shipping

if weight <= 2:
  gs_cost = 20 + 1.5 * weight
elif weight <= 6:
  gs_cost = 20 + 3 * weight
elif weight <= 10:
  gs_cost = 20 + 4 * weight
else:
  gs_cost = 20 + 4.75 * weight

ground_shipping_premium = 125

# drone shipping

if weight <= 2:
  ds_cost = 4.5 * weight
elif weight <= 6:
  ds_cost = 9 * weight
elif weight <= 10:
  ds_cost = 12 * weight
else:
  ds_cost = 14.25 * weight

cost = min(gs_cost, ground_shipping_premium, ds_cost)

if cost == gs_cost:
    shipping_method = "ground shipping"
elif cost == ds_cost:
    shipping_method = "drone shipping"
else:
    shipping_method = "ground shipping premium"

print("We recommend the", shipping_method, "for the cost of", cost)
