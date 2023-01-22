import os

# Set environment variables
os.environ['API_USER'] = 'username'
os.environ['API_PASSWORD'] = 'secret'

# Get environment variables
USER = os.getenv('API_USER')
PASSWORD = os.environ.get('API_PASSWORD')

BASENAME = os.environ.get('BASENAME')

def print_env(env):
  try:
    print(env, ": ", os.environ[env])
  except Exception as e:
    print ("Unknown environment variable: ", env)
                                            # print (e)   
                                                
  print ("Command line arguments\n")
  print_env('PATH')
  print_env('HOME')
  print_env('API_USER')
  print_env('API_PASSWORD')
  print_env('BASENAME')
