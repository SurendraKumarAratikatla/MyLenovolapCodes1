def logging(fun):
  def log_function_called():
    print(f'{fun} called.')
    fun()
  return log_function_called


@logging
def my_name():
  print('chris')

@logging
def friends_name():
  print('naruto')

my_name()
friends_name()