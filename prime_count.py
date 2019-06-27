def count_primes(num):
    if (num < 2):
        total_prime =0
    
    elif (num ==2):
        total_prime =1
    
    else:
        total_prime = 1
        for i in range (2,num+1):
            for k in range (2,i):
                if (i%k == 0):
                    break
                else:
                    if(k == i-1):
                        total_prime += 1
                    else:
                        pass
                    
    return total_prime            
    
