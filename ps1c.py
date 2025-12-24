
def get_float(prompt, error_message):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(error_message)




def main():
    semi_annual_raise = .07
    annual_return = 0.04
    down_payment = 0.25 
    cost = 1000000 

    annual_salary = get_float("Enter the starting salary: ","Annual salary needs to be a number")



    def check_savings_rate(saving_rate):
    
        months = 0

        while current_savings < portion_down_payment:
            months+=1
            return_on_investment = current_savings * (saving_rate / 12)
            monthly_saved = (annual_salary / 12) * portion_saved
            current_savings+= monthly_saved + return_on_investment
            if not months % 6:
                annual_salary+= (semi_annual_raise * annual_salary)
        
        return current_savings







if __name__ == "__main__"":
    main()
