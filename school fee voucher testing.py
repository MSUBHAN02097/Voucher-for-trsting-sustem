def main():
    tuition = 8000.00
    tuition_list = []
    total = 0

    for i in range(5):

        tuition += tuition*0.03
        tuition_list.append(tuition)

    for i, x in enumerate(tuition_list[:4]):
        print(f'Year {i+1}\tTuition ${round(x)}')

    print(f'Total for 4 years ${round(sum(tuition_list[:4]) * 2)}')


main()
>>> Year 1  Tuition $8240
>>> Year 2  Tuition $8487
>>> Year 3  Tuition $8742
>>> Year 4  Tuition $9004
>>> Total for 4 years $68946
def main():
    tuition = 8000.00
    tuition_list = []

    tuition_yr1 = tuition * 1.03
    tuition_yr2 = tuition_yr1 * 1.03
    tuition_yr3 = tuition_yr2 * 1.03
    tuition_yr4 = tuition_yr3 * 1.03

    total_cost_over_4yrs = (tuition_yr1 + tuition_yr2 + tuition_yr3 + tuition_yr4) * 2

    print('Year 1', tuition_yr1)
    print('Year 2', tuition_yr2)
    print('Year 3', tuition_yr3)
    print('Year 4', tuition_yr4)
    print('Total over 4 years', total_cost_over_4yrs)

main()
