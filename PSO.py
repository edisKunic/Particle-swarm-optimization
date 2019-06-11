import random
import math
from math import *
from numpy import array
import numpy as np
class cestica:
    def __init__(self):
        self.brzina=[] #brzina cestice
        self.najbolja_pozicija = []  #najbolja pozicija ikad
        self.pozicija= []  #trenutna pozicija tacke
        self.fitnes = 0     #vrijednsot funkcije u tacki/ pozicija

class PSO(object):
    def __init__(self):
        self.brojac=0
        self.granica=700
        #self.kazna_po_koordinati=0.5
        self.M = 1000000
        self.delta_1 = 0
        self.delta_2 = 0
        self.velicina_roja=500
        self.max_br_iteracija=500
        self.c1= 0.8                 # Preporucena vrijednost 0,7 ili 0,8
        self.c2= 0.8                 # Slucajan broj iz opsega [0,Cmax], Cmax- 1,42 ili 1,62
        self.c3= 1.62                # Slucajan broj iz opsega [0,Cmax], Cmax- 1,42 ili 1,62
        self.K=5                     # Broj informanata
        self.cestice = []            # Niz cestica
        self.informanti= []          # Niz informanata
        self.funkcija=0              # Funkcija za trazenje rjesenja
    def inicial(self):
        for i in range(self.velicina_roja):
            p = cestica()
            x= random.uniform((-1)*self.granica,self.granica) #svoju najbolju, najbolju svih informanata, i trenutna
            y= random.uniform((-1)*self.granica,self.granica)
            p.pozicija.append(x)
            p.pozicija.append(y)
            p.najbolja_pozicija.append(x)
            p.najbolja_pozicija.append(y)
            p.brzina.append(x)
            p.brzina.append(y)
            self.cestice.append(p)
        for i in range(self.K):
            a=random.randint(0,self.velicina_roja-1)
            self.informanti.append(a)

    def postavi_funkciju(self,f):   # Dodavanje funkcije algoritmu
        self.funkcija=f


    def pronadi_rjesenje(self):
        i=0
        for c in self.cestice:
            c.fitnes=self.funkcija(c.pozicija)
            c.najbolja_pozicija

        while i < self.max_br_iteracija:
            for c in self.cestice:

                for inf in self.informanti:
                    inf = random.randint(0,self.velicina_roja-1) # Generisanje 5 informanata

                j=0
                najbolji_informant=self.informanti[0]    # ovde idem koz petlju i trazim najmanjeg infroamnta tj. njegovu poziciju unutar problemskog prostora
                for info in self.informanti: # jer trazimo minimum
                    if self.funkcija(self.cestice[info].najbolja_pozicija) < self.funkcija(self.cestice[najbolji_informant].najbolja_pozicija):
                        najbolji_informant=info

                informant = self.cestice[najbolji_informant]
                # Racunamo brzinu sa novim podacima


                v = self.c1 * np.array(c.brzina) + self.c2 * (np.array(c.najbolja_pozicija) - np.array(c.pozicija)) + self.c3 * (np.array(informant.najbolja_pozicija) - np.array(c.pozicija))
                c.brzina = v

                c.pozicija = c.pozicija + v

                self.delta_1=0
                self.delta_2=0
                if fabs(c.pozicija[0]) > self.granica:
                    self.delta_1 = 1
                    self.brojac= self.brojac+ 1
                if fabs(c.pozicija[1]) > self.granica:
                    self.delta_2 = 1
                    self.brojac= self.brojac+ 1


                if  (self.funkcija(c.pozicija) + self.M * self.delta_1 + self.M * self.delta_2) < self.funkcija(c.najbolja_pozicija):  # cestice i ukoliko je manja od tekuce azuriramo je
                    c.najbolja_pozicija = c.pozicija
            i=i+1

        rjesenje=self.funkcija(self.cestice[0].najbolja_pozicija)
        pozicija=self.cestice[0].najbolja_pozicija

        for c in self.cestice:
            if rjesenje < self.funkcija(c.najbolja_pozicija):
                rjesenje = self.funkcija(c.najbolja_pozicija)
                pozicija = c.najbolja_pozicija

        print("--------")
        print 'minimum:' , rjesenje
        print 'koordinate: ',pozicija
        print 'kazne: ',self.brojac



def Booth_s_fuction(koordinate):  # f(1,3)=0
    x=koordinate[0]
    y=koordinate[1]
    a=(x+2*y-7)
    b=(2*x+y-5)
    f=pow(a,2) + pow(b,2)
    return f

def Matyas_function(koordinate): # f(0,0)=0
    x=koordinate[0]
    y=koordinate[1]
    a=pow(x,2)
    b=pow(y,2)
    f=0.26 * (a+b) - 0.48*x*y
    return f

def McCormick(koordinate): # van granica x,y E (-2,2) ima minimum negdje
    x=koordinate[0]
    y=koordinate[1]
    a= pow((x-y),2)
    f=math.sin(x+y)+ pow((x-y),2)  -1.5 * x + 2.5*y+1
    return f

def Ackley_s_function(koordinate): # f(0,0)=0
    x=koordinate[0]
    y=koordinate[1]
    f=-20 * math.exp(-0.2*math.sqrt(0.5*(pow(x,2)+pow(y,2)))) - math.exp(0.5 *(math.cos(2*x*math.pi) +  math.cos(2*y*math.pi))) + math.e + 20
    return f

def Eggholder_function(koordinate): # f(512, 404.2319)= - 959.6407
    x=koordinate[0]
    y=koordinate[1]
    f= - (y + 47)* math.sin(math.sqrt(math.fabs((x / 2) + (y + 47)))) - x * math.sin(math.sqrt(math.fabs(x - (y + 47))))
    return f # zapada u lokalni minimum -66.8437173295, [  8.45693466  15.65091794]

    # -929.581914998  [ 507.2525757   396.92107997] 199770 kazni


def Schaffer_function_N2(koordinate): # f(0,0)=0
    x=koordinate[0]
    y=koordinate[1]
    f = 0.5 + (math.sin(pow(x,2) - pow(y,2)) * math.sin(pow(x,2) - pow(y,2))- 0.5) / ((1 + 0.001*(pow(x,2) + pow(y,2))) * (1 + 0.001*(pow(x,2) + pow(y,2))))
    return f # racuna priblizno 0,0x previse lokalnih minimuma na maloj povrsini


p= PSO()
p.postavi_funkciju(Eggholder_function)
p.inicial()
p.pronadi_rjesenje()
