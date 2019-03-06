#coding:utf-8
import sys
class Event:
    """
    class Event has 2 members
    There are sensor_values and action_No.

    sensor_values is a list of integers
    action_No is an integer
    """
    def __init__(self, sensor_values, action_No):
        if(type(sensor_values) is list and type(sensor_values[0]) is int):
            self.sensor_values = sensor_values
        else:
            print("""
            Error from class "Event"
            sensor_values must be a list of integers
            """)
            sys.exit()
        if(type(action_No) is int):
            self.action_No = action_No
        else:
            print("""
            Error from class "Event"
            action_No must be an integer
            """)
            sys.exit()
