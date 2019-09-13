class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """
        # Fill this out
        def sort_right(): 
            ''' assumes you can't move left ''' 
            self.move_right()
            if self.compare_item() == 1: ## will return 1 if carried_item > current_item 
                self.swap_item() 
        
        def sort_left(): 
            ''' assumes you can't move right ''' 
            self.move_left()
            if self.compare_item() == -1: 
                self.swap_item()
        
        
        if self.can_move_right() == True: 
            sort_left()
        elif self.can_move_left() == True: 
            sort_right() 
        
        return self
        
### OK the idea is that i want to have it so that you can move on. 
## What i did is strip all these methods out of the class and made them functions and the attributes and made them variables, then I popped it all into python tutor and played around with ordering: 
 ## THIS IS WHAT I TRIED 
    # list_to_sort = l            # The list the robot is tasked with sorting
    # item = None                 # The item the robot is holding
    # position = 0                # The list position the robot is at
    # light = "OFF"               # The state of the robot's light
    # time = 0
       
    # def can_move_right():
    #         """
    #         Returns True if the robot can move right or False if it's
    #         at the end of the list.
    #         """
    #     return position < len(list_to_sort) - 1
    
    # def can_move_left():
    #         """
    #         Returns True if the robot can move left or False if it's
    #         at the start of the list.
    #         """
    #     return position > 0
    
    # def move_right():
    #         """
    #         If the robot can move to the right, it moves to the right and
    #         returns True. Otherwise, it stays in place and returns False.
    #         This will increment the time counter by 1.
    #         """
    #     time += 1
    #     if position < len(list_to_sort) - 1:
    #         position += 1
    #         return True
    #     else:
    #         return False
    
    # def move_left():
    #         """
    #         If the robot can move to the left, it moves to the left and
    #         returns True. Otherwise, it stays in place and returns False.
    #         This will increment the time counter by 1.
    #         """
    #     time += 1
    #     if position > 0:
    #         position -= 1
    #         return True
    #     else:
    #         return False
    
    # def swap_item():
    #         """
    #         The robot swaps its currently held item with the list item in front
    #         of it.
    #         This will increment the time counter by 1.
    #         """
    #     time += 1
    #         # Swap the held item with the list item at the robot's position
    #     item, list_to_sort[position] = list_to_sort[position], item
    
    # def compare_item():
    #         """
    #         Compare the held item with the item in front of the robot:
    #         If the held item's value is greater, return 1.
    #         If the held item's value is less, return -1.
    #         If the held item's value is equal, return 0.
    #         If either item is None, return None.
    #         """
    #     if item is None or list_to_sort[position] is None:
    #         return None
    #     elif item > list_to_sort[position]:
    #         return 1
    #     elif item < list_to_sort[position]:
    #         return -1
    #     else:
    #         return 0
    
    # def set_light_on():
    #         """
    #         Turn on the robot's light
    #         """
    #     self._light = "ON"
    # def set_light_off():
    #         """
    #         Turn off the robot's light
    #         """
    #     return light = "OFF"
        
    # def light_is_on():
    #         """
    #         Returns True if the robot's light is on and False otherwise.
    #         """
    #     return light == "ON"
    
    # def sort():
    #         """
    #         Sort the robot's list.
    #         """
    #     for i in len(list_to_sort): 
    #     # robot starts at position 0 
    #         for item in list_to_sort: 
    #             if compare_item() == -1: ## will return 1 if carried_item > current_item 
    #             ### do stuff
    #             if compare_item() == 1: 
    #             ### do other stuff 
    ''' if can_move_left: move_left. 
        if cannot move left: move_right. 
        compare items. 
            if compare_items == 1, 
                swap() 
            if compare items == -1, 
                move_whichever_way_you_have_to_here 
                Rinse and Repeat. 
    
    ''' 

            
            

            



if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)