
def get_float(prompt, error_message):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(error_message)


def main():
  
    annual_salary = get_float("Enter your starting annual salary: ","Annual salary needs to be a number")
    portion_saved = get_float("Enter the percent of your salary to save, as a decimal: ","Portion Saved needs to be a number")
    total_cost = 1000000
    semi_annual_raise = .07
    portion_down_payment = .25 * total_cost
    current_savings = 0.0
    