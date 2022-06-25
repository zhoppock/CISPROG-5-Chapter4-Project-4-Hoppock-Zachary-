"""
Converts an octal integer to a decimal integer.
"""

def octaltodecimal():
  octal = input("\nEnter an octal integer: ")
  exponent = 0
  while exponent >= 0:
    decimal = 0
    exponent = len(octal) - 1
    for digit in octal:
      if int(digit) >= 8:
        octal = input("Enter an octal integer (no digits of 8 or 9 allowed): ")
        break
      decimal += int(digit) * (8 ** exponent)
      exponent = exponent - 1
  print("The decimal integer value is", decimal)
  return