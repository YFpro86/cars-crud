from app import database
from app.schemas import CarInput

def test_saved_car_can_be_read_from_sqlite(database_path):
 database.initialize(database_path)
 saved = database.create_car(
     database_path,
     CarInput(make="Toyota", model="Yaris", year=2020, color="Blue"),
 )
 loaded = database.get_car(database_path, saved.id)
 assert loaded is not None
 assert loaded.id == saved.id
 assert loaded.make == "Toyota"
 # assert loaded.year == 2020
 assert loaded.year == 2021  # deliberately wrong

def test_deleting_one_car_keeps_the_other(database_path):
    database.initialize(database_path)
    database.create_car(make ="xiaomi",model="su7",year = 2023,color="blank")
    CarInput(make ="xiaomi",model="yu7",year = 2023,color="green")
    database.delete_car(database_path, 2)
    assert database.get_car(car_id=2)
    assert database.list_cars(database_path)