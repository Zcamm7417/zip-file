import logging
logging.basicConfig(level = logging.DEBUG, format= '%(asctime)s - %(levelname)s %(message)s')
#this hides all logging
#logging.disable(logging.CRITICAL)
logging.debug('Start of program')
def factorial(n):
    logging.debug('Start of factorial(%s%%)' % (n))
    total = 1
#this is where d error is so I will replace it with line 9 fix d bug
#    for i in range(n+ 1):
    for i in range(1, n +1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s%%)' % (n))
    return total
print(factorial(5))
logging.debug('End of programl')