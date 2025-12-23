



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
        while months < 36:
            months+=1
            return_on_investment = current_savings * (return_on_investment_rate / 12)
            monthly_saved = (annual_salary / 12) * saving_rate
            current_savings+= monthly_saved + return_on_investment
            if not months % 6:
                annual_salary+= (semi_annual_raise * annual_salary)

        return current_savings
    
    def binary_search(annual_salary):
        if test_saving_rate(1, 0, 1000000, annual_salary) < down_payment - 100:
            print("It is not possible to pay the down payment in three years.")
            return
        l,r = 0,10000
        steps = 0
        while l<r:
            mid = (l + r) // 2
            test_savings = test_saving_rate(mid / 10000, 0, 1000000, annual_salary)
            if test_savings < down_payment - 100:
                l = mid + 1
            else:
                r = mid
            steps+=1
       
        print("Best savings rate:", l / 10000)
        print("Steps in bisection search:", steps)
    binary_search(annual_salary)
        
            



if __name__ == "__main__":
    main()


        
    


  
   

    
   
    

