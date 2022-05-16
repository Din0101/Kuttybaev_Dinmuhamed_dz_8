
def val_checker(func):
   def chek(arg):
      return arg
   return chek





@val_checker(lambda x: x > 0)
def calc_cube(x):
   if x > 0:
      return x ** 3
   else:
      raise ValueError(f'wrong val {x}')

print(calc_cube(-5))