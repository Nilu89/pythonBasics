print(f'\n9.2 Three restaurants')


class Restaurant:
    in_county = Restaurant("Tandir", "Uzbek")
    cafe = Restaurant("Athens", "Greek")
    in_county.describe_rest()
    in_county.open_rest()
    cafe.describe_rest()
    cafe.open_rest()