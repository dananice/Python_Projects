def is_prime(num):
    if num == 2:
        return True
    if num == 1:
        return False
        
        # loop through the numbers between 2 and the numbers
        
    for i in range(2, num):
        
        #  if num can be divided by the potential prime number
        if num % i == 0:
            return False
        
        # this return outside the for loop which will run once the loop finishes 
    return True        