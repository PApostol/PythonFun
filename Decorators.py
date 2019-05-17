import time

def timing(func):
    def wrapper(*arg, **kw):
        start = time.time()
        func(*arg, **kw)
        stop = time.time()
        print('Time taken: {:0.2f} s\n'.format(stop - start))
    return wrapper



def plus(n=0):
  def mydec(func):
    def wrapper(*arg, **kwarg):
      result = func(*arg, **kwarg) + n
      print('Plus decorator used')
      return result
    return wrapper
  return mydec


def minus(n=0):
  def mydec(func):
    def wrapper(*arg, **kwarg):
      result = func(*arg, **kwarg) - n
      print('Minus decorator used')
      return result
    return wrapper
  return mydec


@plus(2)
@minus(10)
def add(*arg):
  return sum(arg)


print(add(1,2))