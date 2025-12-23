
def get_float(prompt, error_message):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(error_message)


def main():
  
    annual_salary = get_float("Enter your starting annual salary: ","Annual salary needs to be a number")
    portion_saved = get_float("Enter the percent of your salary to save, as a decimal: ","Portion Saved needs to be a number")
    total_cost = get_float("Enter the cost of your dream home: ","Total cost needs to be a number")
    semi_annual_raise = get_float("Enter the semi-annual raise, as a decimal: ", "Your semi-annual raise needs to be a number")
    portion_down_payment = .25 * total_cost
    current_savings = 0.0
    