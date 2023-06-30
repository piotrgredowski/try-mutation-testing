
def calculate_net_salary(gross_salary):
    TAX_RATES = {
        'income_tax_rate': 0.18,     # 18% income tax rate in Poland
        'social_security_rate': 0.0976,   # 9.76% social security contribution rate in Poland
        'health_insurance_rate': 0.09,    # 9% health insurance contribution rate in Poland
        
    }
    # Dead code
    my_salary = 2000
    print(my_salary)
    income_tax = gross_salary * TAX_RATES['income_tax_rate']
    social_security = gross_salary * TAX_RATES['social_security_rate']
    health_insurance = gross_salary * TAX_RATES['health_insurance_rate']

    net_salary = gross_salary - income_tax - social_security + health_insurance
    return net_salary
