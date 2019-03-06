#coding:utf-8
import random
import collections

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
        self.weight_of_episodes = [0.0 for i in range(self.num_of_e)]
        for i in range(self.num_of_p):
            s += self.particle_list[i].weight
        for i in range(self.num_of_p):
            self.particle_list[i].weight /= s
            self.weight_of_episodes[self.particle_list[i].position] += self.particle_list[i].weight

    def resampling(self):
        """
        update positions of particles 
        according to their normalized weights
        """
        for n in range(self.num_of_p):
            r = random.uniform(0.0,1.0)
            for e in range(self.num_of_e):
                r -= self.weight_of_episodes[e]
                if r <= 0.0:
                    self.particle_list[n].position = e
                    break
                else:
                    self.particle_list[n].position = random.randint(0,self.num_of_e - 1)

    def decision_making(self):
        l = [n.position for n in self.particle_list]
        n = collections.Counter(l).most_common()[0][0]
        return n
            

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
