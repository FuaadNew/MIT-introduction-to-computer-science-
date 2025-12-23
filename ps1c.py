
def get_float(prompt, error_message):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(error_message)


def testSavings(mid):

def binary_search(epsilon,goal,annual_salary):
    
    l,r = 0.0,1.0
    

    while l<r:
        mid = (l + r) / 2
        test_months = testSavings(mid)
        if goal - epsilon <= test_months <= goal + epsilon:
            print("steps")
        else:
            if test_months > goal:
                l = mid + .01
            else:
                r = mid - 1
    print("there is no way to hit the goal")





def main():
  
    annual_salary = get_float("Enter your starting annual salary: ","Annual salary needs to be a number")
    portion_saved = get_float("Enter the percent of your salary to save, as a decimal: ","Portion Saved needs to be a number")
    total_cost = 1000000
    semi_annual_raise = .07
    portion_down_payment = .25 * total_cost
    

