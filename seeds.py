import pdb

from models.country import Country
from models.destination import Destination
from models.user import User
from models.visit import Visit

import repositories.country_repository as country_repo
import repositories.destination_respository as destination_repo
import repositories.user_repository as user_repo
import repositories.visit_repository as visit_repo

destination_1 = Destination('Rome', 'Home of the Romans')
destination_2 = Destination('Florence', 'Home of the Medici')
destination_3 = Destination('Paris', 'Capital of France')
destination_4 = Destination('Walt Disney World', 'Disney park in Orlando')

country_1 = Country('Italy',[destination_1, destination_2])
country_2 = Country('France', destination_3)
country_3 = Country('America', destination_4)

user_1 = User('Dave')
user_2 = User('John')
user_3 = User('Simon')
user_4 = User('Jack')
user_5 = User('Steve')
user_6 = User('Luke')

visit_1 = Visit(user_1,destination_3,'15/01/2023', 5,'We visited Notre Dame')
visit_2 = Visit(user_3,destination_1,'05/02/2023', 4,'The Vatican was huge')
visit_3 = Visit(user_1,destination_2,'23/01/2023',5,'Florence was amazing')
visit_4 = Visit(user_4,destination_4,'09/02/2023',3,'The magic kingdom was great')

# DROP tables
destination_repo.delete_all() # working


# TEST Destination

destination_repo.save(destination_1)  # working
destination_repo.save(destination_2)  
destination_repo.save(destination_4)  

dest1 = destination_repo.select_all() # working
print(dest1[0].__dict__)  

dest2 = destination_repo.select(3) # working
print(dest2.__dict__) 

destination_repo.delete(1) # working




# TEST Country

country_repo.save()
country_repo.save()
country_repo.save()





pdb.set_trace()


