
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
    







if __name__ == "__main__"":
    main()
