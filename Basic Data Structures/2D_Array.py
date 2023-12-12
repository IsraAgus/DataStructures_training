
class TwoDArrayOperations:
    """Description: Class created to emulated the principal operations into a array.
    Parameters:
        - Array.
    Return: None."""
    def __init__(self, array):
        """Description: Constructor of the class.
        Parameters:
            - Array.
        Return: None."""
        self.array = array

    def __setitem__(self, key: (int, int), value: int):
        """Description: Add an element into a specific position of the array - Class special method."""
        self.array[key[0]][key[1]] = value

    def __str__(self):
        """Description: Returns formatted - Class special method."""
        return "Item: ".join(self.array)

    def add_element(self, element: int, position: (int, int)):
        """Description: Method to add a new element into the array.
        Parameters:
            - newElement: the new element to add of the same type.
            - position: the position to add the new element into the array.
        Return:
            - array: the array with the new element"""
        if position < len(self.array):  # Validating if the index of the new position exists.
            self.array[position[0]][position[1]] = element
        else:
            raise IndexError("The position is not a valid index in the list, try with other one.")
        return self.array

    def search_element(self, element: int):
        """Description: Method used to look for a item inside the array in a linear way O(n^2).
        Parameters:
            - element: Item to look for.
        Return: index: if values exist index, otherwise an error."""
        for row in range(0, len(self.array), 1):  # Rows
            for column in range(0, len(self.array[row]), 1):  # Columns
                if self.array[row][column] == element:
                    return row, column
        raise ValueError("The element is not in the array.")

    def delete_element(self, element: int):
        """Description: Method used to delete a item inside the array in a linear way O(n).
        Parameters:
            - element: Item to look for.
        Return: index: if values exist index, otherwise an error."""
        index_to_delete = self.search_element(element)
        if type(index_to_delete) == tuple:
            self.array = self.array[index_to_delete[0]][:index_to_delete[1]] +\
                         self.array[index_to_delete[0]][index_to_delete[1]+1:]
        else:
            raise TypeError("The element to delete is not in the list.")
