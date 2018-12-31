# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 x 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers

def is_palindrome(x) :
  # Cast the number as a string.
  string = str(x)

  # Get the lengths of the string so we can get our parts.
  max_length = len(string)
  halfway = int(max_length / 2)
  first = string[0: halfway]
  second = string[halfway: max_length]

  # Check to see if both parts are equal
  if first == second[::-1] :
    return True

  return False
# end def isPalnidrome

largest = 0;

for x in range(999) :
  for y in range(999) :
    temp = x * y

    # Check to see if the product is a palindrome
    if is_palindrome(temp) :
      # If it is, check to see if it's the largest thusfar.
      if temp > largest :
        largest = temp
      # end if.
    # end if
  # end for x loop
# end for y loop

print largest;


