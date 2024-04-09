import os
if os.environ.get('ENVVAR') is None:
  print('ENVVAR is defined')
else:
  print('ENVVAR is not defined')
if os.environ.get('SECRET') is None:
  print('SECRET is defined')
else:
  print('SECRET is not defined')