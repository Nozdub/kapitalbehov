# Universal variabler brukt av flere metoder:
ansatte = 3
omsetning = 1500000
car_antall = 3
car_price_pr = 200000
tool_antall = 3
tool_price = 40000
varekostnad_percent = 0.4
salary = 500000
hours_per_employee = 1500
kreditt_tid = 30
forventet_utgift = 260000


def investering_i_anleggsmidler():
    total = (car_antall * car_price_pr) + (tool_antall * tool_price)
    return total


print(investering_i_anleggsmidler())


def investeringer_i_omløpsmidler():
    yearly_varekostnad = omsetning * ansatte * varekostnad_percent
    return yearly_varekostnad

print(investeringer_i_omløpsmidler())

kapitalbinding_i_lager = investeringer_i_omløpsmidler() * (45/360)

print(kapitalbinding_i_lager)




def påløpte_kostnader_per_dag():
    salary_cost = salary / hours_per_employee
    varekostnad_per_time = (salary * ansatte) * varekostnad_percent / hours_per_employee

    running_cost_per_day = (salary_cost + varekostnad_per_time) * 7 * 3
    return round(running_cost_per_day, -3) # runder av her da foreleser sa dette var greit.

print(påløpte_kostnader_per_dag())

def investering_i_omløpsmidler_varer_i_arbeid():
    total_item_invested_in_labor = round(påløpte_kostnader_per_dag() * 30, -3)
    return total_item_invested_in_labor

print(investering_i_omløpsmidler_varer_i_arbeid())

def investering_i_drift():
    yearly_total_turnover = ansatte * omsetning
    turnover_per_day = yearly_total_turnover / 360
    kapitalbinding_i_arbeid = turnover_per_day * kreditt_tid
    return kapitalbinding_i_arbeid

print(investering_i_drift())


def omløpsmider():
    omlopsmidler = kapitalbinding_i_lager + investering_i_omløpsmidler_varer_i_arbeid() + investering_i_drift()
    total = omlopsmidler - forventet_utgift # I tillegg antas det i eksempelet at man trenger en liten reserve, og at man har
    # noe kortsiktig kreditter til leverandører og det offentlige.
    return total

print(omløpsmider())

def total_kapital_behov():
   total_kap = investering_i_anleggsmidler() + omløpsmider()
   return total_kap

print(f"Totalt kapitalbehov blir derfor {total_kapital_behov()}")