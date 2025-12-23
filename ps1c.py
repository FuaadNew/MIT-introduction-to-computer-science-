



def main():

    def get_float(prompt, error_message):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print(error_message)



    annual_salary = get_float("Enter the starting salary: ","Annual salary needs to be a number")
    current_savings = 0
    total_cost = 1000000
    down_payment = .25 * total_cost
    return_on_investment_rate = .04
    semi_annual_raise = .07

    def test_saving_rate(saving_rate,current_savings, total_cost,annual_salary):
        months = 0
        while current_savings < down_payment - 100:
            months+=1
            return_on_investment = current_savings * (return_on_investment_rate / 12)
            monthly_saved = (annual_salary / 12) * saving_rate
            current_savings+= monthly_saved + return_on_investment
            if not months % 6:
                annual_salary+= (semi_annual_raise * annual_salary)

        return months
    
    def binary_search(annual_salary):
        l,r = 0,1000
        steps = 0
        while l<r:
            mid = (l + r) // 2
            months = test_saving_rate(mid / 1000, 0, 1000000, annual_salary)
            if months < 36:
                r = mid
            else:
                l = mid + 1
            steps+=1
        if months > 36:
            print("It is not possible to pay the down payment in three years.")
        else:
            print("Best savings rate:", l / 1000)
            print("Steps in bisection search:", steps)
    binary_search(annual_salary)
        
            



if __name__ == "__main__":
    main()


        
    


  
   

    
   
    

