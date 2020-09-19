#Author: Eric Zhang ecz5032@psu.edu

def digit_sum(n):

  if n != 1:
    z = n % 10
    return z + digit_sum(n//10)
  else:
    return 0

def run():
  value = int(input("Enter an int: "))
  print(f"sum of digits of {value} is {digit_sum(value)}.")
 
if __name__ == "__main__":
  run() 
