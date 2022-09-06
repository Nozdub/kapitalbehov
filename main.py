# ---------------------------------------- Start up capital calculator ------------------------------------------------#


# Universal variabler brukt av flere metoder:
# Company:
employees = 3  # Mengder ansatte / amount of employees.
car_amount = 3  # Antall bedriftsbiler / amount of company cars.
tool_amount = 3  # Antall verktøysett / amount of tool sets.

# Company finances:
turnover_per_employee = 1500000  # Omsetning per ansatt / turnover per employee.
salary = 500000  # Lønn per ansatt / salary per employee per year.
car_price_per = 200000  # Pris per kjøretøy / price per car.
tool_price_per = 40000  # Pris per verkstøysett / price per tool set.
item_cost_percent = 0.4  # Rente på varer / interest on items or services.
hours_worked_per_employee = 1500  # Arbeidstimer per ansatt / working hours employees.
credit_duration = 30  # Nedbetalingsperiode på renter / duration of interest down payment in days.
expected_expenditure = 260000  # Påregnet utgift / expected expenditures for the company.


# -------------------------------------- INVESTMENTS DONE IN FIXED ASSETS ---------------------------------------------#

# iia = Investering i annlegsmidler
# Investeringer gjort i anleggsmidler (langtidsbrukte gjenstander):
def iia():
    total = (car_amount * car_price_per) + (tool_amount * tool_price_per)
    return total


print(f"Investering i anlegsmidler blir / investments done in fixed assets: {iia()}")


# -------------------------------------INVESTMENTS DONE IN CURRENT ASSETS----------------------------------------------#

# iio = Investering i omløpsmidler
# Investeringer gjort i omløpsmidler (kortsiktige utgifter):
def iio():
    yearly_item_cost = turnover_per_employee * employees * item_cost_percent
    return yearly_item_cost


print(f"Investing i omløpsmidler blir / investments done in current assets: {iio()}")


# --------------------------------------------- CAPITAL IN STOCK-------------------------------------------------------#

# Kapitalbinding i lager (varer som bedriften har inne):

capital_in_stock = iio() * (45 / 360)

print(f"Kapitalbinding i lagervarer blir / capital in stock: {capital_in_stock}")


# ----------------------------------------------- COST PER DAY --------------------------------------------------------#

# Utgifter per dag:
def cost_per_day():
    salary_cost = salary / hours_worked_per_employee
    varekostnad_per_time = (salary * employees) * item_cost_percent / hours_worked_per_employee

    running_cost_per_day = (salary_cost + varekostnad_per_time) * 7 * 3
    return round(running_cost_per_day, -3)  # runder av her da foreleser sa dette var greit.


print(f"Daglige kostnader blir: {cost_per_day()}")


# ---------------------------------------- CURRENT ASSETS IN USE ------------------------------------------------------#

# Investeringer i omløpsmidler som er bundet i arbeid.
def current_assets_in_use():
    total_item_invested_in_labor = round(cost_per_day() * 30, -3)
    return total_item_invested_in_labor


print(f"Omløpsmidler i varer i arbeid blir / current assets in use: {current_assets_in_use()}")


# ---------------------------------------------------------------------------------------------------------------------#

def investering_i_drift():
    yearly_total_turnover = employees * turnover_per_employee
    turnover_per_day = yearly_total_turnover / 360
    kapitalbinding_i_arbeid = turnover_per_day * credit_duration
    return kapitalbinding_i_arbeid


print(f"Investering i drift blir: {investering_i_drift()}")


# ------------------------------------------ CURRENT ASSETS -----------------------------------------------------------#

def current_assets():
    omlopsmidler = capital_in_stock + current_assets_in_use() + investering_i_drift()
    total = omlopsmidler - expected_expenditure  # I tillegg antas det i eksempelet at man trenger en liten reserve,
    # og at man har noe kortsiktig kreditter til leverandører og det offentlige.
    return total


print(f"Omløpsmidler / current assets: {current_assets()}")


# ------------------------------------------ TOTAL NEEDED CAPITAL -----------------------------------------------------#

def total_needed_capital():
    total_kap = iia() + current_assets()
    return total_kap


print(f"Totalt kapitalbehov blir derfor / total capital needed: {total_needed_capital()}")
