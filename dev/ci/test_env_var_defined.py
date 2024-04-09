import os
if 'ENVVAR' in os.environ:
  print('ENVVAR is defined')
else:
  print('ENVVAR is not defined')
if 'SECRET' in os.environ:
  print('SECRET is defined')
else:
  print('SECRET is not defined')