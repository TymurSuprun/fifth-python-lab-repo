"""importing module enum"""
import enum


class Type(enum.Enum):
    """
    Creating class for clothing's types
    """
    SHIRT = 1
    JEANS = 2
    JACKET = 3
    DRESS = 4


class Clothing:
    """
    Creating class Clothing for clothing elements
    """

    def __init__(self, name, description, location, colour, size, types):  # pylint: disable=too-many-arguments
        self.name = name
        self.description = description
        self.location = location
        self.colour = colour
        self.size = size
        self.type = types

    def get_name(self):
        """
        Getter for name
        :return self.name
        """
        return self.name

    def get_description(self):
        """
        Getter for description
        :return self.description
        """
        return self.description

    def get_location(self):
        """
        Getter for location
        :return self.location
        """
        return self.location

    def get_colour(self):
        """
        Getter for colour
        :return self.colour
        """
        return self.colour

    def get_size(self):
        """
        Getter for size
        :return self.size
        """
        return self.size

    def get_type(self):
        """
        Getter for type
        :return self.type
        """
        return self.type


class Wardrobe:
    """ Creating class Wardrobe for list of clothing"""

    def __init__(self):
        self.list_clothing = []

    def add_clothing(self, cloth):
        """
        Adding cloth to list
        :return None
        """
        self.list_clothing.append(cloth)

    def go_out(self):
        """
        Whether you can go out or not
        :return number, out
        """
        temp_set = set()
        out = False
        for cloth in self.list_clothing:
            temp_set.add(cloth.get_type())
        number = len(temp_set)
        if number > 3:
            print(f'Number of clothing: {number}. You can go out')
            out = True
        else:
            print(f'Number of clothing: {number}. You can\'t go out')
        return number, out

    def sort(self):
        """
        Func for sorting by size
        :return sorted_list
        """
        sorted_list = []
        sorted_list = [cloth.name for cloth in sorted(self.list_clothing,
                                                      key=lambda c: c.size, reverse=True)]
        return sorted_list

    def ward_info(self):
        """
        Getter for wardrobe info
        :return None
        """
        print('Clothing in wardrobe:')
        for clothing in self.list_clothing:
            print(clothing.get_name())


if __name__ == '__main__':
    cloth1 = Clothing("Grandfathers skirt", 'Holed Soviet Union', 'Ukraine', 'Gray', 46, Type.SHIRT)
    cloth2 = Clothing('Dress', 'Are you a child?', 'Milan', 'Purple', 35, Type.DRESS)
    cloth3 = Clothing('Jacket', 'Not fashion, not stylish', 'Trash can', 'Jeans', 44, Type.JACKET)
    cloth4 = Clothing('Pants', 'My belly is big(((', 'The back of a chair', 'Black', 48, Type.JEANS)
    cloth5 = Clothing('Jeans jacket', 'One more?!?!', 'Trash can again', 'Jeans', 40, Type.JACKET)
    wardrobe = Wardrobe()

    wardrobe.add_clothing(cloth1)
    wardrobe.add_clothing(cloth2)
    wardrobe.add_clothing(cloth3)
    wardrobe.add_clothing(cloth4)
    wardrobe.add_clothing(cloth5)
    wardrobe.ward_info()
    wardrobe.go_out()
    print(f'Sorted clothing: {wardrobe.sort()}')

    del cloth1, cloth2, cloth3, cloth4, cloth5, wardrobe
