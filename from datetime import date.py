from datetime import date  # Importing date for age calculation

class Person(object):
    def __init__(self, name):
        """
        Abstraction: The constructor abstracts the creation of a Person object.
        It takes a name (a string) and initializes the object, hiding the details
        of how the name is split and stored (e.g., into last_name).
        """
        self._name = name  # Private attribute to store the full name
        try:
            last_blank = name.rindex(' ')  # Find the last space to split the name
            self._last_name = name[last_blank + 1:]  # Extract the last name
        except:
            self._last_name = name  # If no space, the whole name is the last name
        self._birthday = None  # Initialize birthday as None

    def get_name(self):
        """
        Abstraction: This method provides access to the person's full name.
        It hides the internal storage (self._name) and lets the user interact
        with the Person object at a higher level ("get the name") without
        worrying about how it's stored.
        """
        return self._name

    def get_last_name(self):
        """
        Abstraction: This method abstracts the retrieval of the last name.
        The user doesn't need to know how the last name was extracted from
        the full name (via rindex) — they just call this method.
        """
        return self._last_name

    def set_birthday(self, birthdate: date):
        """
        Abstraction: This method abstracts the process of setting a birthday.
        It takes a date object and stores it, hiding the internal representation
        (self._birthday) from the user.
        """
        self._birthday = birthdate

    def get_age(self):
        """
        Abstraction: This method abstracts the age calculation.
        The user doesn't need to know how the age is computed (using today's date
        and the birthday) — they just call get_age() and get the result in days.
        If no birthday is set, it raises an error, enforcing the ADT's rules.
        """
        if self._birthday == None:
            raise ValueError
        return (date.today() - self._birthday).days

    def __lt__(self, other):
        """
        Abstraction: This method abstracts the comparison of two Person objects.
        It defines "less than" based on last names (and full names if last names
        are the same), so the user can compare people without knowing the
        comparison logic. This makes sorting or ordering people intuitive.
        """
        if self._last_name == other._last_name:
            return self._name < other._name
        return self._last_name < other._last_name

    def __str__(self):
        """
        Abstraction: This method abstracts the string representation of a Person.
        It allows the user to print a Person object and get the name, without
        needing to access the internal self._name attribute directly.
        """
        return self._name