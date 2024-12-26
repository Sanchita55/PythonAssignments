# A machine is purchased which will produce earning of Rs. 1000 per year while it lasts. The machine costs Rs. 6000 and will have a salvage of Rs. 2000 when it is condemned. If 12 percent per annum can be earned on alternative investments what would be the minimumlife of the machine to make it a more attractive investment compared to alternative investment?
'''earnings_per_year = 1000
machine_cost = 6000
salvage_value = 2000
alternate_rate = 0.12

years = 1
while True:
    total_earnings = earnings_per_year * years + salvage_value
    alternative_investment = machine_cost * ((1 + alternate_rate) ** years)
    if total_earnings > alternative_investment:
        print('Minimum life of machine:',years, 'years')
        break
    years += 1  '''

machine_cost = 6000
salvage_value = 2000
annual_earnings = 1000
alternate_rate = 0.12

machine_life = 1

while True:
    npv_machine = -machine_cost + salvage_value / (1 + alternate_rate) ** machine_life
    for year in range(1, machine_life + 1):
        npv_machine += annual_earnings / (1 + alternate_rate) ** year

    npv_alternate = machine_cost * (1+alternate_rate)**year

    if npv_machine > npv_alternate:
        print('The minimum life of the machine to make it more attractive is:',machine_life, 'years')
        break
    machine_life += 1
