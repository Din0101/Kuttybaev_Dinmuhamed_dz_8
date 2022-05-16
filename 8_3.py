def type_logger(func):



   def log(arg):
      print(str(func).split(" ")[1])
      return (f'{arg}: {type(arg)}')
   return log



@type_logger
def calc_cube(x):
   return x ** 3

print(calc_cube(5))