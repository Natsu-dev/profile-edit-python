class Date:
    def __init__(self, year, month, day) -> None:
        self.year = year
        self.month = month
        self.day = day


class Profile:
    def __init__(self, id, name, year, month, day, address, note) -> None:
        self.id = id
        self.name = name
        self.date = Date(year, month, day)
        self.address = address
        self.note = note
