def menu():
  print('''Choose an option:
  1) Calculate double a number
  2) Multiply two numbers
  3) Convert a string to uppercase
  4) Count characters in a user input
  5) Exit
  ''')
  
def option_from_the_user():
  option = input('Choose an option: ')
  return option

menu()

while True:
  option_ = option_from_the_user()
  
  match option_:
    case '1':
      num = float(input('Enter a number: '))
      double = num * 2
      print(f'The double from the {num} is {double}')
    case '2':
      num_1 = float(input('Enter the first number: '))
      num_2 = float(input('Enter the second number: '))
      multi = num_1 * num_2
      print(f'{num_1}*{num_2} = {multi}')
    case '3':
      quote = input('Enter a quote: ')
      Uppercase_quote = quote.upper()
      print(Uppercase_quote)
    case '4':
      quote = input('Enter a quote: ')
      quote_length = len(quote)
      print(quote_length)
    case '6':
      print('Leaving...')
      exit(0)
    case _:
      print('Invalid Option. Try again')