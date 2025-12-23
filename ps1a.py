



def main():
    annual_salary = float(input("Enter your annual salary: "))
    portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
    total_cost = float(input("Enter the cost of your dream home: "))
    portion_down_payment = .25 * total_cost
    current_savings = 0.0
    
    
    months = 0

    while current_savings < portion_down_payment:
        return_on_investment =  current_savings * (.04 / 12)
        months+=1
        monthly_saved = (annual_salary / 12) * portion_saved
        current_savings+= monthly_saved + return_on_investment
        
    print (f"Number of months: {months}")




if __name__ == "__main__":
    main()