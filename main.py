from octalToDecimal import octaltodecimal
from decimalToOctal import decimaltooctal

option = "y"

print("Welcome to the decimal/octal conversion program.")
while option != "n":
  octaltodecimal()
  decimaltooctal()
  option = input("\nKeep going? (y/n): ")
print("Goodbye.")