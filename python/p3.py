# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?


'''

'''
def is_prime( num ): #---------------------------
    prime = True

    for i in range( 2, num ):
        if num % i == 0:
            prime = False

        if not prime:
            return prime

    return prime
# -----------------------------------------------




if __name__ == "__main__": #---------------------
    num = 600851475143
    i = num
    done = False

    while not done:
        i -= 1
        if num % i == 0:
            if is_prime( i ):
                print(i)
                done = True

# -----------------------------------------------



# Answer: 6857
