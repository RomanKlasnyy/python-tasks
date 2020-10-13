"""Define abstract class Human with:
  first_name, last_name fields (private)
  full_name property
  and a do_hobby abstract method
- Define a new class Student which is derived from Human and has:
  grade field.
  do_hobby - print 'dancing' or some another hobby
- Define class Worker derived from Human with:
  week_salary, work_hours_per_day properties
  money_per_hour() method, returns money earned per hour by the worker
  do_hobby - print 'reading' or some another hobby
- Initialize a list of 5 students and sort them by grade.
- Initialize a list of 5 workers and sort them by money per hour.
- Concatenate the lists and call do_hobby on each object."""

from abc import ABC, abstractmethod
import operator


class Human(ABC):
    """Human abstract class"""
    def __init__(self, first_name, last_name):
        self.__first_name, self.__last_name = first_name, last_name

    @property
    def full_name(self):
        return f'{self.__first_name} {self.__last_name}'

    @abstractmethod
    def do_hobby(self):
        """Abstract method that does hobby"""
        print("I'm going to do human things!")


class Student(Human):
    def __init__(self, first_name, last_name, grade):
        super(Student, self).__init__(first_name, last_name)
        self.grade = grade

    def do_hobby(self):
        print("I'm going to dance!")


class Worker(Human):
    def __init__(self, first_name, last_name, p):
        super(Worker, self).__init__(first_name, last_name)
        self.ws, self.hpd = p

    @property
    def week_salary(self):
        return self.ws

    @property
    def work_hours_per_day(self):
        return self.hpd

    def money_per_hour(self):
        return self.week_salary / (self.work_hours_per_day * 5)

    def do_hobby(self):
        print("I'm going to read a book!")


def sort_by_mph(self):
    return self.money_per_hour()


students = [Student('Kate', 'Anderson', 91),
            Student('Jake', 'Paulus', 61),
            Student('Joe', 'Wagner', 76),
            Student('Winston', 'Churchill', 85),
            Student('Julius', 'Caesar', 99)]
students.sort(key=operator.attrgetter('grade'))
for student in students:
    print(f'{student.full_name} has grade {student.grade}')  # students sort by grade

workers = [Worker('James', 'Smith', (100, 2)),
           Worker('Bill', 'Gates', (76613000, 8)),
           Worker('John', 'Doe', (500, 8)),
           Worker('Earl', 'Grey', (600, 6)),
           Worker('Michael', 'Hopkins', (1500, 4))]

workers.sort(key=sort_by_mph)

for worker in workers:
    print(f'{worker.full_name} earns ${worker.money_per_hour()} per hour')  # workers sort by mph

students.extend(workers)

for person in students:
    person.do_hobby()
