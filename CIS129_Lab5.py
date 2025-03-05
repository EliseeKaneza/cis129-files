# Lab 5: The Bottle Return Program
# Name: [Elisee Kaneza]
# Date: [03-03-2025]
# Description: This program calculates the total number of bottles collected
#              and the total payout for a grocery store over 7 days.

def get_bottles():
    """Function to collect bottle count for 7 days"""
    NBR_OF_DAYS = 7
    total_bottles = 0
    counter = 1
    
    while counter <= NBR_OF_DAYS:
        today_bottles = int(input(f"Enter number of bottles returned for day #{counter}: "))
        total_bottles += today_bottles
        counter += 1
    
    return total_bottles

def calc_payout(total_bottles):
    """Function to calculate total payout"""
    PAYOUT_PER_BOTTLE = 0.10
    total_payout = total_bottles * PAYOUT_PER_BOTTLE
    return total_payout

def print_info(total_bottles, total_payout):
    """Function to print results"""
    print("\nThe total number of bottles collected is", total_bottles)
    print(f"The total paid out is ${total_payout:.2f}\n")

def main():
    """Main function to run the bottle return program"""
    keep_going = 'y'

    while keep_going.lower() == 'y':
        total_bottles = get_bottles()
        total_payout = calc_payout(total_bottles)
        print_info(total_bottles, total_payout)

        keep_going = input("Do you want to enter another week’s worth of data? (Enter y or n): ")

if __name__ == "__main__":
    main()
