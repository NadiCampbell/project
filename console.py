import pdb
from models.country import Country
from models.city import City

import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

city_repository.delete_all()
country_repository.delete_all()


country1 = Country('France')
country_repository.save(country1)

country2 = Country('Canada')
country_repository.save(country2)

country3 = Country('Netherlands')
country_repository.save(country3)

country4 = Country('Greece')
country_repository.save(country4)

city1 = City('Amsterdam', country3)
city_repository.save(city1)

city2 = City('Athens', country4)
city_repository.save(city2)

city3 = City('Toronto', country2)
city_repository.save(city3)

city4 = City('Paris', country1)
city_repository.save(city4)

city5 = City('Rotterdam', country3)
city_repository.save(city5)

city6 = City('Vancouver', country2)
city_repository.save(city6)

city7 = City('Rhodes', country4)
city_repository.save(city7)

city8 = City('Toulouse', country1)
city_repository.save(city8)

pdb.set_trace()
