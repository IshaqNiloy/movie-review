import csv
import random
from faker import Faker

fake = Faker()

headers = [
    "title", "rating", "director", "writer", "stars", "storyline", "genres",
    "release_date", "countries_of_origin", "language", "filming_locations",
    "production_companies", "budget", "gross_worldwide", "runtime"
]

data = []

available_names = [fake.name() for _ in range(10)]
available_genres = [
    "Action",
    "Adventure",
    "Animation",
    "Comedy",
    "Crime",
    "Documentary",
    "Drama",
    "Fantasy",
    "Historical",
    "Horror",
    "Musical",
    "Mystery",
    "Romance",
    "Science Fiction (Sci-Fi)",
    "Thriller",
    "War",
    "Western",
    "Biographical",
    "Family",
    "Sport",
    "Superhero"
]

for _ in range(100):
    row = [
        fake.word(),  # title
        round(random.uniform(0, 10), 1),  # rating
        fake.random_elements(elements=available_names, length=random.randint(1, 5)),  # director
        fake.random_elements(elements=available_names, length=random.randint(1, 5)),  # writer
        fake.random_elements(elements=available_names, length=random.randint(1, 5)),  # stars
        fake.sentence(),  # storyline
        fake.random_elements(elements=available_genres, length=random.randint(1, 5)),  # genres
        fake.date(),  # release_date
        [fake.country() for _ in range(random.randint(1, 5))],  # countries_of_origin
        [fake.language_name() for _ in range(random.randint(1, 5))],  # languages
        [fake.city() for _ in range(random.randint(1, 5))],  # filming_locations
        fake.company(),  # production_companies
        fake.random_int(min=100000, max=10000000),  # budget
        fake.random_int(min=100000, max=10000000),  # gross_worldwide
        fake.random_int(min=60, max=180),  # runtime
    ]
    data.append(row)

filename = "../movie_data.csv"

with open(filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(data)

print(f"CSV file '{filename}' has been created.")
