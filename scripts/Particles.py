#coding:utf-8
import random

class Particle:
    position = 0
    weight = 0.0

class Particles:
    def __init__(self, num_of_p, num_of_e):
        self.num_of_p = num_of_p
        self.num_of_e = num_of_e
        self.particle_list = []
        for i in range(num_of_p):
            p = Particle()
            p.position = random.randint(0,num_of_e - 1)
            p.weight = (1.0 / num_of_p)
            self.particle_list.append(p)

    def normalize(self):
        """
        summention of weight of particles to be 1.0
        """
        s = 0.0
        for i in range(self.num_of_p):
            s += self.particle_list[i].weight
        for i in range(self.num_of_p):
            self.particle_list[i].weight /= s

    def decision_making(self):
            
    def slide(self):
        """
        slide all particles while adding noise
        """
        for i in range(self.num_of_p):
            r = random.randint(1,10)
            if(1 <= r <= 3):
                self.particle_list[i].position += 1
                if(self.particle_list[i].position >= self.num_of_e):
                    self.particle_list[i].position = random.randint(0,self.num_of_e - 1)

            elif (4 <= r <= 6):
                pass

            elif (7<= r <= 9):
                self.particle_list[i].position -= 1
                if(self.particle_list[i].position < 0):
                    self.particle_list[i].position = random.randint(0,self.num_of_e - 1)
            else:
                self.particle_list[i].position = random.randint(0,self.num_of_e - 1)
