
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
    goal = cost * down_payment

    annual_salary = get_float("Enter the starting salary: ","Annual salary needs to be a number")



    def check_savings_rate(saving_rate, annual_salary):
    
        months = 0
        current_savings = 0 

        while months < 36:
            months+=1
            return_on_investment = current_savings * (annual_return / 12)
            monthly_saved = (annual_salary / 12) * saving_rate
            current_savings+= monthly_saved + return_on_investment
            if not months % 6:
                annual_salary+= (semi_annual_raise * annual_salary)
        
        return current_savings



    def binary_search(annual_salary):

        test_savings = check_savings_rate(1, annual_salary)
        if test_savings < goal - 100:
            print("It is not possible to pay the down payment in three years.")
            return



        l,r = 0, 10000
        steps = 0

        while l < r:
            mid = (l + r) // 2

            savings = check_savings_rate(mid / 10000 , annual_salary)

            if savings < goal - 100:
                l = mid + 1
            else:
                r  = mid 
            steps+=1
        print("Best savings rate:", l / 10000)
        print("Steps in bisection search:", steps)
        






    binary_search(annual_salary)






if __name__ == "__main__":
    main()
