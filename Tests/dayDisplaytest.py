
import unittest
from Model.day import day
from Model.event import Event

# tests get magic index
class testAddEvent(unittest.TestCase):
    
    j1 = day.Day(2022, 1, 1)
    j1temp = day.Day(2022, 1, 1)
    earliestEvent = event.Event("Earliest event", "this is the earliest event", 6, 0, 7, 0)
    secondEarliestEvent = event.Event("Earliest event", "this is the earliest event", 6, 30, 7, 30)
    thirdEarliestEvent = event.Event("Earliest event", "this is the earliest event", 8, 0, 9, 0)
    
    # tests standard inputs
    def test_input_into_empty_day(self):
        j1temp.events = [earliestEvent]
        j1.addEvent(earliestEvent)
        self.assertEqual(j1temp, j1)


    def test_input_into_sorted(self):
        j1.addEvent(thirdEarliestEvent)
        j1temp.events = [earliestEvent, secondEarliestEvent, thirdEarliestEvent]
        j1.addEvent(secondEarliestEvent)
        self.assertEqual(j1temp, j1)

    # def test_input_into_unsorted(self);





    
    # # tests inputs where the magic index is nonexistent
    # def test_inputs_with_no_magic_index(self):
    #     self.assertEqual(getMagicIndex([1, 2, 3], 0), None)
    #     self.assertEqual(getMagicIndex([1, 2, 3, 4], 0), None)
    
    # # tests a list containing its indices
    # def test_input_with_all_magic_indices(self):
    #     self.assertEqual(getMagicIndex([0, 1, 2], 0), 1)

    # # tests an empty list
    # def test_empty_input(self):
    #     with self.assertRaises(ValueError):
    #         getMagicIndex([], 0)
    
    # # test an input with nonzero shifter
    # def test_shifted_input(self):
    #     self.assertEqual(getMagicIndex([2, 4, 10], 3), 4)
    #     self.assertEqual(getMagicIndex([-12, -6, -1, 4, 10], 1), 4)