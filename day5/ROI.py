import re

class roi_calc():
    
    def __init__(self):
        self.name = ''
        self.program = 'off'
        self.utilities = 'off'
        self.lawn = 'off'
        self.snow = 'off'
        self.calc = 'off'
    
    def __str__(self):
        return self.name.title()
    
    def __repr__(self):
        return f'< Roi | {self} >'

    def welcome(self):
        print ("""
        --------------------------------------------------------
                 That Annoying Wine Real State Agency
        --------------------------------------------------------
        """)
        name = input('What is your name? ')
        self.name = name
        
        print(f'\nHi, {self}! I hope you had a great time at our shop, and casino!\
        \n\nNow, let\'s see your Real State Owned Investment on that property you want to buy.\n')
        
        print('-'*60)
        address = input('What is the address of the property you would like to buy? ')
        global prop
        prop = Property(address)
        print('-'*60)
        
        self.program = 'off'

    def income(self):
            
        prop.rental_income = self.question('rental income')

        prop.laundry_income = self.question('laundry income')
        prop.storage_income = self.question('storage income')
        prop.miscellaneous_income = self.question('miscellaneous income')

        prop.total_monthly_income = int(prop.rental_income) + int(prop.laundry_income) + \
        int(prop.storage_income) + int(prop.miscellaneous_income)
        
        print('-'*60)
        print(f'Total income: ${prop.total_monthly_income:,.2f}')
        print('-'*60)
        
        return prop.total_monthly_income
        
    def expenses(self):

        lawn = input('Are you paying for lawn care? y/n ')
        while lawn not in {'y', 'n'}:
            lawn = input('Select a valid option. y/n ')
        if lawn == 'y':
            self.lawn = 'on'
        
        snow = input('Are you paying for snow care? y/n ')
        while snow not in {'y', 'n'}:
            snow = input('Select a valid option. y/n ')
        if snow == 'y':
            self.snow = 'on'
        
        utilities = input('Are you paying for utilities? y/n ')
        while utilities not in {'y', 'n'}:
            utilities = input('Select a valid option. y/n ')
        if utilities == 'y':
            self.utilities = 'on' 
        
        prop.tax = self.question('tax')
        prop.insurance = self.question('insurance')
        if self.utilities == 'on':
            prop.electric = self.question('electric bill')
            prop.water = self.question('water bill')
            prop.garbage = self.question('garbage bill')
            prop.gas = self.question('gas bill')
        
        if self.lawn == 'on':
            prop.lawn_care = self.question('lawn care')
        if self.utilities == 'on':
            prop.snow_care = self.question('snow care')
            
        prop.hoa = self.question('hoa')
        prop.vacancy = self.question('vacancy')
        prop.repairs = self.question('repairs')
        prop.capex = self.question('capex')
        prop.property_management = self.question('property_management')
        prop.mortgage = self.question('mortgage')

        prop.total_monthly_expenses = int(prop.tax) + int(prop.insurance) + int(prop.electric)\
        + int(prop.water) + int(prop.garbage) + int(prop.gas) + int(prop.hoa) + int(prop.lawn_care)\
        + int(prop.snow_care) + int(prop.vacancy) + int(prop.repairs) + int(prop.capex) + \
        int(prop.property_management) + int(prop.mortgage)

        print('-'*60)
        print(f'Total expenses: ${prop.total_monthly_expenses:,.2f}')
        print('-'*60)
        
        return prop.total_monthly_expenses

    def investment(self):
        prop.down_payment = self.question('down payment', '')
        prop.closing_costs = self.question('closing costs', '')
        prop.rehab_budget = self.question('rehab budget', '')
        prop.miscellaneous = self.question('miscellaneous', '')

        prop.total_investment = int(prop.down_payment) + int(prop.closing_costs)\
        + int(prop.rehab_budget) + int(prop.miscellaneous)
        print('-'*60)
        print(f'\nTotal investment: ${prop.total_investment:,.2f}')
        return prop.total_investment
    
    def calculate_roi(self):    
        prop.total_monthly_cash_flow = prop.total_monthly_income - prop.total_monthly_expenses      
        prop.annual_cash_flow = prop.total_monthly_cash_flow * 12
        prop.roi = (prop.annual_cash_flow / prop.total_investment) * 100
        self.calc = 'on'    
        print('-'*60)
        print(f'Annual Cash Flow: {prop.annual_cash_flow:,.2f}')
        print('-'*60)
        print(f'Total income: ${prop.total_monthly_income:,.2f}')
        print('-'*60)
        print(f'Total expenses: ${prop.total_monthly_expenses:,.2f}')
        print('-'*60)
        print(f'Total investment: ${prop.total_investment:,.2f}')
        print('-'*60)
        print(f'ROI: {prop.roi:,.2f}%')
        print('-'*60)
        
        return prop.roi
    
    def view_form(self):
        print(f"""
************************************************************
Form for: {self} / {prop.address}
************************************************************

------------------------------------------------------------
Income
------------------------------------------------------------

Rental Income: ${prop.rental_income}
Laundry Income: ${prop.laundry_income}
Storage Income: ${prop.storage_income}
Miscellaneous Income: ${prop.miscellaneous_income}

------------------------------------------------------------
Expenses
------------------------------------------------------------

Tax: ${prop.tax}
Insurance: ${prop.insurance}

Total Utilities: ${prop.electric + prop.water + prop.garbage + prop.gas}
    - Electric: ${prop.electric}
    - Water: ${prop.water}
    - Garbage: ${prop.garbage}
    - Gas: ${prop.gas}
   
Lawn Care: ${prop.lawn_care}
Snow Care: ${prop.snow_care}
            
HOA: ${prop.hoa}
Vacancy: ${prop.vacancy}
Repairs: ${prop.repairs}
Capital Expenditure: ${prop.capex}
Property Management: ${prop.property_management}
Mortgage: ${prop.mortgage }

------------------------------------------------------------
Investments
------------------------------------------------------------

Down Payment: ${prop.down_payment}
Closing Costs: ${prop.closing_costs}
Rehab Budget: ${prop.rehab_budget}
Miscellaneous: ${prop.miscellaneous}""")

    def question(self, field, monthly = 'monthly'):
        question = (input(f'What is your {monthly} {field}? '))
        while not re.match('^[\d]*$', question):
            question = input(f'Please, input a valid number for your {field}: ')
        return question

class Property():
        
    def __init__(self, address):
        self.address = address

        self.rental_income = 0
        self.laundry_income = 0
        self.storage_income = 0
        self.miscellaneous_income = 0

        self.total_monthly_income = 0
        self.total_monthly_expenses = 0
        self.total_investment = 0
        self.total_monthly_cash_flow = 0
        self.annual_cash_flow = 0
        self.roi = 0
        
        self.tax = 0
        self.insurance = 0
        self.utilities_total = 0
        self.electric = 0
        self.water = 0
        self.sewage = 0
        self.garbage = 0
        self.gas = 0
        self.hoa = 0
        self.lawn_care = 0
        self.snow_care = 0
        self.vacancy = 0
        self.repairs = 0
        self.capex = 0
        self.property_management = 0
        self.mortgage = 0

        self.down_payment = 0
        self.closing_costs = 0
        self.rehab_budget = 0
        self.miscellaneous = 0
        
    def __str__(self):
        return f'{self.address}'
    
    def __repr__(self):
        return f'< Property | {self} >'
        
def main():
    roi = roi_calc()
    roi.welcome()
    roi.program = 'on'
    
    while roi.program == 'on':
        user_action = input('What would you like to do?\n\
        1. Calculate ROI\n\
        2. Edit Form\n\
        3. View Form\n\
        4. Exit ').lower()

        if user_action in '1 calculate roi':
            roi.income()
            roi.expenses()
            roi.investment()
            roi.calculate_roi()
        elif user_action in '2 Edit Form':
            if roi.calc == 'off':
                print('-'*60)
                print('You have not completed the form yet!')
                print('-'*60)
            else:
                roi.view_form()
                edit_action = input('What would you like to edit?\n\
                1. Income\n\
                2. Expenses\n\
                3. Investment\n\
                4. Exit ').lower()
                # while edit not in {1}:
                while edit_action not in '4 exit':
                    if edit_action in '1 income':
                        roi.income()
                    elif edit_action in '2 expenses':
                        roi.expenses()
                    elif edit_action in '3 investment':
                        roi.investment()
                    elif edit_action in '4 exit':
                        pass
                    print('\n' + '*'*60)
                    print('This is your new ROI after editing your form')
                    print('*'*60 + '\n')
                    roi.calculate_roi()

                    if edit_action not in '4 exit':
                        edit_action = input('\nWhat would you like to edit?\n\
                        1. Income\n\
                        2. Expenses\n\
                        3. Investment\n\
                        4. Exit ')

        elif user_action in '3 View Form':
            if roi.calc == 'off':
                print('-'*60)
                print('You have not completed the form yet!')
                print('-'*60)
            else:
                roi.view_form()
                roi.calculate_roi()
        elif user_action in '4 exit':
            program = 'off'
            break

main()
