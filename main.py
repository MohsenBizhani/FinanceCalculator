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


def main() -> None:
    monthly_income: float = float(input('Enter monthly income: '))
    tax_rate: float = float(input('Enter tax rate (%): '))
    currency: str = input('Enter currency: ')

    calculate_financial_data(monthly_income, tax_rate, currency)


if __name__ == '__main__':
    main()
