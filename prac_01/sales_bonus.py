LOW_BONUS = 0.1
HIGH_BONUS = 0.15
SALES_LIMIT = 1000

sales = float(input("Enter sales: $"))
while sales > 0:
    if sales < SALES_LIMIT:
        bonus = sales*LOW_BONUS
    else:
        bonus = sales*HIGH_BONUS
    print(f"Your bonus is {bonus:.2f}")
    sales = float(input("Enter sales: $"))


# sales = float(input("Enter sales: $"))
# while sales >= 0:
#     if sales < 1000:
#         bonus = sales * 0.1
#     else:
#         bonus = sales * 0.15
#     print(f"Your bonus is {bonus:.2f}")
#     sales = float(input("Enter sales: $"))
#

