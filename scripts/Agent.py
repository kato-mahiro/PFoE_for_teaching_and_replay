#coding:utf-8
from Event import Event
from Particles import Particles
from likelihood import likelihood
import sys

class Agent:
    def __init__(self):
        self.event_list = []
        self.particle = None

    def setEvent(self,sensor_values,action_No):
        """
        append new event to a self.event_list
        """
        e = Event(sensor_values,action_No)
        self.event_list.append(e)

    def getAction(self,sensor_values):
        for i in range(self.particles.num_of_p):
            self.particles.particle_list[i].weight =  \
            likelihood(sensor_values, self.event_list[self.particles.particle_list[i].position ].sensor_values)
        self.particles.normalize()
        self.particles.resampling()
        action_No = self.event_list[self.particles.decision_making()].action_No
        self.particles.slide()
        return action_No

    def writeData(self, file_name):
        with open(file_name,'w') as f:
            for i in range(len(self.event_list)):
                string = ''
                for n in self.event_list[i].sensor_values:
                    string += str(n)
                    string += ','
                string += str(self.event_list[i].action_No)
                string += '\n'
                f.write(string)

    def addData(self,file_name):
        with open(file_name,'a') as f:
            for i in range(len(self.event_list)):
                string = ''
                for n in self.event_list[i].sensor_values:
                    string += str(n)
                    string += ','
                string += str(self.event_list[i].action_No)
                string += '\n'
                f.write(string)

    def readData(self,file_name):
        with open(file_name,'r') as f:
            for line in f:
                l = line.split(',')
                l_i = [int(l_s) for l_s in l]
                self.setEvent(l_i[:-1],l_i[-1])

        self.particles = Particles(1000, len(self.event_list))
