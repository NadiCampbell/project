import pdb
from models.country import Country
from models.city import City
from models.attraction import Attraction
from repositories import attraction_repository

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



attraction1 = Attraction('Amstel Bridge', city1, 'amazing view into the heart of the city') 
attraction_repository.save(attraction1)

attraction2 = Attraction('Royal Ontario Musem', city3, 'recommend it highly, the World exhibit is fantastic!')
attraction_repository.save(attraction2)

attraction3 = Attraction('The Louvre Guided tour', city4, 'this was an amazing experience')
attraction_repository.save(attraction3)

attraction4 = Attraction('Street Food Tasting Tour', city2, 'would highly recommend if you love good hearty food')
attraction_repository.save(attraction4)

attraction5 = Attraction('Pub Crawl Tour with a Guide', city8, 'if you love to drink and bar hop this is the tour for you')
attraction_repository.save(attraction5)

attraction6 = Attraction('Pirates Route Sea Kayaking Tour', city7, 'just amazing! best day of my life')
attraction_repository.save(attraction6)

attraction7 = Attraction('Capilano Suspension Bridge', city6, 'the view was spectacular')
attraction_repository.save(attraction7)

attraction8 = Attraction('Rotterdam Zoo', city5, 'had a great day out here with the family!')
attraction_repository.save(attraction8)

# pdb.set_trace()
