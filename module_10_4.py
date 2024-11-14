import threading
import random
import time
from queue import Queue

class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):

        time.sleep(random.randint(3, 10))

class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.queue = Queue()

    def guest_arrival(self, *guests):
        for guest in guests:

            table = self.find_free_table()
            if table is not None:
                table.guest = guest
                guest.start()
                print(f"{guest.name} сел(-а) за стол номер {table.number}")
            else:
                self.queue.put(guest)
                print(f"{guest.name} в очереди")

    def find_free_table(self):
        for table in self.tables:
            if table.guest is None:
                return table
        return None

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest and not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None


                    if not self.queue.empty():
                        next_guest = self.queue.get()
                        table.guest = next_guest
                        next_guest.start()
                        print(f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")

            time.sleep(1)

tables = [Table(number) for number in range(1, 6)]

guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]


guests = [Guest(name) for name in guests_names]


cafe = Cafe(*tables)


cafe.guest_arrival(*guests)


cafe.discuss_guests()