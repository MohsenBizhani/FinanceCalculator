def calculate_financial_data(monthly_income: float, tax_rate: float, currency: str) -> None:
    monthly_tax: float = monthly_income * (tax_rate / 100)
    monthly_net_income: float = monthly_income - monthly_tax
    yearly_income: float = monthly_income * 12
    yearly_tax: float = monthly_tax * 12
    yearly_net_income: float = yearly_income - yearly_tax

    print('------------------------------------')
    print(f'Monthly income: {currency}{monthly_income:.2f}')
    print(f'Tax rate: {tax_rate:.0f}%')
    print(f'Monthly tax: {currency}{monthly_tax:.2f}')
    print(f'Monthly net income: {currency}{monthly_net_income:.2f}')
    print(f'Yearly income: {currency}{yearly_income:.2f}')
    print(f'Yearly tax paid: {currency}{yearly_tax:.2f}')
    print(f'Yearly net income: {currency}{yearly_net_income:.2f}')
    print('------------------------------------')


def main() -> int:
    try:
        monthly_income: float = float(input('Enter monthly income: '))
    except ValueError:
        return -1
    try:
        tax_rate: float = float(input('Enter tax rate (%): '))
    except ValueError:
        return -2
    try:
        currency: str = input('Enter currency: ')
    except ValueError:
        return -3

    calculate_financial_data(monthly_income, tax_rate, currency)
    return 0


if __name__ == '__main__':
    while True:
        res = main()
        if res == -1:
            print('Please enter a valid income.')
        elif res == -2:
            print('Please enter a valid rate (%).')
        elif res == -3:
            print('Please enter a valid currency.')
