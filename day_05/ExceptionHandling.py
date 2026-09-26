import sys
import traceback as tb

try :
    dividend = int(input('Enter Dividend: '))
    divisor = int(input('Enter Divisor: '))
    result = dividend / divisor
    print(f'Result :- {result:.2f}')
except  ValueError as e:
    print(e)
    e_type,cause,tb = sys.exc_info()
    print(f'{cause} , {e_type}')

except ZeroDivisionError as e:
    print(e)
    tb.print_exc()

else:
    print('if try execute successfully')

finally:
    print('Finally Execute Always')