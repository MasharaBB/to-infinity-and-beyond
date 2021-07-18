def computepay(hours, rate):
    overtime_reach = 40
    overtime_rate = 1.5
    try:
        hours = float(hours)
        rate = float(rate)
        if hours > overtime_reach:
            extra = hours - overtime_reach
            print("Regular Pay: ", overtime_reach*rate)
            print("Overtime Pay: ", overtime_rate*extra*rate)
            print("Total: ", overtime_reach*rate+overtime_rate*extra*rate)
        else:
            print("Regular Pay: ", hours*rate)
    except:
        print("You have not entered numbers")
hours_in = input("Enter the hours: ")
rate_in = input("Enter the rate: ")
computepay(hours_in, rate_in)