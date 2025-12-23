



def main():
    annual_salary = get_float("Enter your starting annual salary: ","Annual salary needs to be a number")
    portion_saved = get_float("Enter the percent of your salary to save, as a decimal: ","Portion Saved needs to be a number")
    total_cost = 1000000
    semi_annual_raise = .07
    portion_down_payment = .25 * total_cost
    current_savings = 0

    def get_float(prompt, error_message):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print(error_message)

    
    months = 0
    def test_saving_rate(saving_rate):
        while current_savings < portion_down_payment:
            months+=1
            return_on_investment = current_savings * (saving_rate / 12)
            monthly_saved = (annual_salary / 12) * portion_saved
            current_savings+= monthly_saved + return_on_investment
            if not months % 6:
                annual_salary+= (semi_annual_raise * annual_salary)

        return months

        

  
   

    
   
    

