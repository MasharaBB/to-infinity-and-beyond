def evaluate(value_input):
    TotalSum = 0
    TotalCount = 0
    value_input = 0
    while value_input != 'done':
        value_input = input('Enter a number:')
        if value_input != 'done':
            try: 
                value_int = float(value_input)
                TotalSum = TotalSum + value_int
                TotalCount = TotalCount + 1
            except:
                print('Invalid input')
    print('Total: ',TotalSum)
    print('Count: ', TotalCount)
    print('Average: ', TotalSum/TotalCount)
external_value = 0
evaluate(external_value)