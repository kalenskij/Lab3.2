import json
import uuid
from abc import abstractmethod, ABC

LOCATION = "Poltava c., Heroiv Krut st., 11's h."


class ITeacher(ABC):

    @property
    @abstractmethod
    def teacher_id_(self):
        pass

    @teacher_id_.setter
    @abstractmethod
    def teacher_id_(self, id_):
        pass

    @property
    @abstractmethod
    def teacher_name_(self):
        pass

    @teacher_name_.setter
    @abstractmethod
    def teacher_name_(self, name):
        pass

    @property
    @abstractmethod
    def teacher_surname_(self):
        pass

    @teacher_surname_.setter
    @abstractmethod
    def teacher_surname_(self, surname):
        pass

    @property
    @abstractmethod
    def get_teacher(self):
        pass

    @get_teacher.setter
    def get_teacher(self, info):
        pass

    @property
    @abstractmethod
    def teacher_info_(self):
        pass

    @teacher_info_.setter
    def teacher_info_(self, info):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass


class ICourse(ABC):

    @property
    @abstractmethod
    def id_course_(self):
        pass

    @id_course_.setter
    @abstractmethod
    def id_course_(self, id_):
        pass

    @property
    @abstractmethod
    def name_course_(self):
        pass

    @name_course_.setter
    @abstractmethod
    def name_course_(self, name):
        pass

    @property
    @abstractmethod
    def duration_(self):
        pass

    @duration_.setter
    @abstractmethod
    def duration_(self, time):
        pass

    @property
    @abstractmethod
    def program_(self):
        pass

    @program_.setter
    @abstractmethod
    def program_(self, program):
        pass

    @property
    @abstractmethod
    def capacity_(self):
        pass

    @capacity_.setter
    @abstractmethod
    def capacity_(self, num):
        pass

    @property
    @abstractmethod
    def price_(self):
        pass

    @price_.setter
    @abstractmethod
    def price_(self, cost):
        pass

    @property
    @abstractmethod
    def teacher_(self):
        pass

    @teacher_.setter
    @abstractmethod
    def teacher_(self, teacher):
        pass

    @property
    @abstractmethod
    def teacher_id_(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class ILocalCourse(ABC):

    @property
    @abstractmethod
    def course_type_(self):
        pass

    @course_type_.setter
    @abstractmethod
    def course_type_(self, type_):
        pass


class IOffsiteCourse(ABC):

    @property
    @abstractmethod
    def address_(self):
        pass

    @address_.setter
    @abstractmethod
    def address_(self, address):
        pass


class ICourseFactory(ABC):

    @abstractmethod
    def add_teacher(self, teacher):
        pass

    @abstractmethod
    def add_local_course(self, course_):
        pass

    @abstractmethod
    def add_offset_course(self, course_):
        pass

    @abstractmethod
    def show_courses(self):
        pass

    @abstractmethod
    def show_teachers(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Program:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name_):
        if not isinstance(name_, str):
            raise TypeError("Wrong name type")
        self._name = name_


class Teacher(ITeacher):

    def __init__(self, name, surname, *args):
        self._teacher_id = uuid.uuid1()
        self._name = name
        self._surname = surname
        self._programs = []
        for program in args:
            self.add_program(program)

    @property
    def teacher_id_(self):
        return self._teacher_id

    @teacher_id_.setter
    def teacher_id_(self, id_):
        self._teacher_id = id_

    @property
    def teacher_name_(self):
        return self._name

    @teacher_name_.setter
    def teacher_name_(self, name):
        if not isinstance(name, str):
            raise TypeError("Wrong name type")
        self._name = name

    @property
    def teacher_surname_(self):
        return self._surname

    @teacher_surname_.setter
    def teacher_surname_(self, surname):
        if not isinstance(self, surname):
            raise TypeError("Wrong surname type")
        self._surname = surname

    def add_program(self, program):
        if not isinstance(program, Program):
            raise TypeError("Wrong program Type")
        self._programs.append(program)

    def add_program_to_db(self, *programs):
        if not all(isinstance(program, Program) for program in programs):
            raise TypeError("Wrong program type")
        with open("Teachers.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        for teacher in data:
            if str(self._teacher_id) == teacher:
                for program in programs:
                    teacher["programs"].append(program)
        with open("Teachers.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    @property
    def get_teacher(self):
        return self._name, self._surname

    @get_teacher.setter
    def get_teacher(self, info):
        self._name = info[0]
        self._surname = info[1]

    @property
    def teacher_info_(self):
        return f'{self._name} {self._surname}', f'{self._teacher_id}'

    @teacher_info_.setter
    def teacher_info_(self, info):
        self._name = info.get[0]
        self._surname = info.get[1]
        self._programs = info.get[2]

    def __str__(self):
        return f'{self._name} {self._surname}\n'

    def __repr__(self):
        return f'{self._name} {self._surname} -- {self._programs}'


class Course(ICourse):

    def __init__(self, name, duration, teacher, program, capacity, price):
        if self.check_course_exist(name):
            raise ValueError(f'course with the {name} exist')
        self._id_course = uuid.uuid1()
        self._name = name
        self._duration = duration
        self._teacher = teacher
        self._program = program
        self._capacity = capacity
        self._price = price
        self._teacher = teacher[0]
        self._teacher_id = teacher[1]

    @property
    def id_course_(self):
        return self._id_course

    @id_course_.setter
    def id_course_(self, id_):
        self._id_course = id_

    @property
    def name_course_(self):
        return self._name

    @name_course_.setter
    def name_course_(self, name):
        if not isinstance(name, str):
            raise TypeError("Wrong name type")
        self._name = name

    @property
    def duration_(self):
        return self._duration

    @duration_.setter
    def duration_(self, duration):
        if not isinstance(duration, int):
            raise TypeError("Wrong duration type")
        if not duration > 0:
            raise ValueError("Wrong duration value")
        self._duration = duration

    @property
    def teacher_(self):
        return self._teacher

    @teacher_.setter
    def teacher_(self, teacher):
        if not isinstance(teacher, Teacher):
            raise TypeError("Wrong teacher type")
        self._teacher = teacher

    @property
    def program_(self):
        return self._program

    @program_.setter
    def program_(self, program):
        if not isinstance(program, Program):
            raise TypeError("Wrong program type")
        if program not in self.teacher_.programs:
            raise ValueError("This teacher doesn't have this program")
        self._program = program

    @staticmethod
    def check_course_exist(name):
        with open("Courses.json", "r", encoding="utf-8") as file:
            data_courses = json.load(file)
        return any(j == name for j in [i["name"] for i in (data_courses['Local'] | data_courses['OffSet']).values()])

    @property
    def capacity_(self):
        return self._capacity

    @capacity_.setter
    def capacity_(self, num):
        if not isinstance(num, int):
            raise TypeError("Wrong capacity type")
        if not num > 0:
            raise ValueError("Wrong capacity value")
        self._capacity = num

    @property
    def price_(self):
        return self._price

    @price_.setter
    def price_(self, cost):
        if not isinstance(cost, int):
            raise TypeError("Wrong price type")
        if not cost > 0:
            raise ValueError("Wrong price value")
        self._price = cost

    @property
    def teacher_id_(self):
        return self._teacher_id

    def __str__(self):
        return f'{self._name}\nProgram:{self._program}\nTeacher: {self._teacher}\n' \
               f'Time:{self._duration} hours Places: {self._capacity} Price: {self._price} UAH'


class LocalCourse(Course, ILocalCourse):

    def __init__(self, name, duration, teacher, program, capacity, price, type_):
        if self.check_course_exist(name):
            raise ValueError(f"Course {name} exist")
        super().__init__(name, duration, teacher, program, capacity, price)
        self._type = type_

    @staticmethod
    def check_course_exist(course):
        with open("Courses.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        data = data["Local"]
        return any(data[i]["name"] == course for i in data)

    @property
    def course_type_(self):
        return self._type

    @course_type_.setter
    def course_type_(self, type_):
        if not (type_ == 'offline' or type_ == 'online'):
            raise ValueError('invalid input')
        self._type = type_

    def __str__(self):
        return f'{self._name}\nProgram:{self._program}\nTeacher: {self._teacher}\n' \
               f'Time:{self._duration} hours\tType: {self._type}\tPrice: {self._price} UAH'


class OffSetCourse(Course, IOffsiteCourse):

    def __init__(self, name, duration, teacher, program, capacity, price, address):
        if self.check_course_exist(name):
            raise ValueError(f'course {name} exist')
        super().__init__(name, duration, teacher, program, capacity, price)
        self._address = address

    @staticmethod
    def check_course_exist(course):
        data = json.load(open('Courses.json'))['OffSet']
        return any(data[i]['name'] == course for i in data)

    @property
    def address_(self):
        return self._address

    @address_.setter
    def address_(self, address):
        if not isinstance(address, str):
            raise TypeError("Wrong address value")
        self._address = address

    def __str__(self):
        return f'{self._name}\nProgram:{self._program}\nTeacher: {self._teacher}\n' \
               f'Time:{self._duration} hours\tPlace: {self._address}\tPrice: {self._price} UAH'


class CourseFactory(ICourseFactory):

    def __init__(self):
        self._location = LOCATION

    def add_teacher(self, teacher):
        if not isinstance(teacher, Teacher):
            raise TypeError("Wrong teacher type")
        self.file_teacher_write(teacher)

    def file_teacher_write(self, teacher):
        with open("Teachers.json", "r", encoding="utf-8") as file:
            database = json.load(file)
            id_of_teacher = str(teacher.teacher_id_)
        if self.check_teacher_exist(teacher):
            raise ValueError("Teacher already exists")
        database[id_of_teacher] = {
            "name": teacher.teacher_name_,
            "surname": teacher.teacher_surname_,
            "programs": []
        }
        for program in teacher._programs:
            database[id_of_teacher]["programs"].append(program.name)
        with open("Teachers.json", "w", encoding="utf-8") as file:
            json.dump(database, file, indent=4)

    @staticmethod
    def check_teacher_exist(teacher):
        database = json.load(open('Teachers.json'))
        return str(teacher.teacher_id_) in database and \
            any(i['name'] + i['surname'] == teacher.teacher_name_ + teacher.teacher_surname_ for i in database)

    def add_local_course(self, course_):
        if not isinstance(course_, LocalCourse):
            raise TypeError("Wrong LocalCourse type")
        self.file_course_write("Local", course_)

    def add_offset_course(self, course_):
        if not isinstance(course_, OffSetCourse):
            raise TypeError("Wrong OffsetCourse type")
        self.file_course_write("OffSet", course_)

    @staticmethod
    def file_course_write(type_of_course, course):
        with open("Courses.json", "r", encoding="utf-8") as file:
            database = json.load(file)
        course_id = str(course.id_course_)
        if type_of_course not in database:
            database[type_of_course] = {}
        if course_id in database[type_of_course] and \
                any(database[i]['name'] == course.name_course_ for i in database):
            raise ValueError('course exist')
        if type_of_course == 'Local':
            database[type_of_course][course_id] = {
                'name': course.name_course_,
                'duration': course.duration_,
                'program': course.program_.name,
                'capacity': course.capacity_,
                'price': course.price_,
                'type': course.course_type_,
                'teacher': course.teacher_,
            }
        if type_of_course == 'OffSet':
            database[type_of_course][course_id] = {
                'name': course.name_course_,
                'duration': course.duration_,
                'program': course.program_.name,
                'capacity': course.capacity_,
                'price': course.price_,
                'address': course.address_,
                'teacher': course.teacher_,
            }
        with open("Courses.json", "w", encoding="utf-8") as file:
            json.dump(database, file, indent=4)

    @staticmethod
    def delete_teacher(teacher_id):
        with open("Teachers.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        if teacher_id not in data:
            raise ValueError('teacher don`t exist')
        data.pop(teacher_id)
        with open("Teachers.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def delete_course(id_course):
        with open("Courses.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        if id_course in data["Local"]:
            data["Local"].pop(id_course)
            with open("Courses.json", "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)
        elif id_course in data["OffSet"]:
            data["OffSet"].pop(id_course)
            with open("Courses.json", "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)
        else:
            raise ValueError('Invalid input')

    def show_courses(self):
        with open("Courses.json", "r", encoding="utf-8") as file:
            database = json.load(file)
        return '\n'.join([''.join([f'{j}: {i[j]}\n' for j in i.keys()])
                          for i in (database["Local"] | database['OffSet']).values()])

    def show_teachers(self):
        with open("Teachers.json", "r", encoding="utf-8") as file:
            teachers_data = json.load(file)
        return '\n\n'.join([f'{teachers_data[i]["name"]} {teachers_data[i]["surname"]}\n'
                            f'Programs:\n{teachers_data[i]["programs"]}' for i in teachers_data])

    def __str__(self):
        return f'Courses: {self.show_courses()}\n\nTeachers: {self.show_teachers()}'


course_factory = CourseFactory()
program1 = Program("History")
program2 = Program("Chemistry")
teacher1 = Teacher("Vladimir", "Vladimirov", program1, program2)
teacher2 = Teacher("Oleksandr", "Kalenskyi", program2)
course_factory.add_teacher(teacher1)
course_factory.add_teacher(teacher2)
local_course1 = LocalCourse("History of ancient egypt", 45, teacher1.teacher_info_, program1, 99, 149, "offline")
offset_course1 = OffSetCourse("Oil refinement", 60, teacher2.teacher_info_, program2, 50, 249, "St. Nicolas st.")
course_factory.add_local_course(local_course1)
course_factory.add_offset_course(offset_course1)
print(course_factory)
