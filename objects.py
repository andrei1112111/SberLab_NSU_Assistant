class Gitlab:
    proj_repo: str
    username: str


class Kimai:
    pass


class BookStack:
    pass


class Plane:
    pass


class Student(Gitlab, Plane, BookStack, Kimai):
    def __init__(self):
        git = Gitlab
        plane = Plane
        bookstack = BookStack
        kimai = Kimai
