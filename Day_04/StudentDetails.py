class Student:
    def __init__(self, roll, name, marks):
        self._roll = roll
        self._name = name
        self._marks = marks

    @property
    def roll(self):
        return self._roll

    @property
    def marks(self):
        return self._marks

    @property
    def name(self):
        return self._name

    def __str__(self):
        return f'Roll No :- {self._roll} | Name :- {self._name} | Marks :- {self._marks}'