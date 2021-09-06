class Config:
  '''
  General configuration parent class
  '''
  MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/550?api_key=d8e714062bf27229a379a09af8e8a5dd'

class ProdConfig(Config):
  '''
  Production configuration child class
  
  Args:
      Config: The parent configuration class with General configuration settings
  '''
  pass

class DevConfig(Config):
  '''
  Development configuration child class
  
  Args:
      Config: The parent configuration class with General configuration settings
  '''
  DEBUG = True