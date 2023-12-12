from typing import Union


class NodeDoubleLinked:
    """"""
    def __init__(self, data, previous_p: Union[int, None], next_p: Union[int, None]):
        """Description:
        Parameters:
        Return"""
        self.data = data
        self.previous = previous_p
        self.next_p = next_p
        self.node = [self.previous, self.data, self.next_p]


class DoubleListOperations:
    """Description:
    Parameters:
    Return"""

    def add_item(self):
        """Description:
        Parameters:
        Return"""
        pass

    def delete_item(self):
        """Description:
        Parameters:
        Return"""
        pass
