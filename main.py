#Author: Eric Zhang ecz5032@psu.edu

def digit_sum(n):

  if n == 0:
    return 0
  else:
    z = n % 10
    return z + digit_sum(n//10)

def run():
  value = int(input("Enter an int: "))
  print(f"sum of digits of {value} is {digit_sum(value)}.")
 
if __name__ == "__main__":
  run() 
