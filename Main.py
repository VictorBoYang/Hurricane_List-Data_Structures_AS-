from Node import *

Storm1 = Storm("Tropical Storm Alberto",60,"MAY",0)
Storm2 = Storm("Tropical Storm Beryl",70,"MAY",0)
Storm3 = Storm("Hurricane Chris",85,"JUNE",1)
Storm4 = Storm("Hurricane Ernesto",100,"AUGUST",2)
Storm5 = Storm("Hurricane Michael",115,"SEPTEMBER",3)
double = DoublyLinkedList()
double.push_front(Storm1)
double.push_back(Storm2)
double.insert(Storm3,1)
double.push_front(Storm4)
double.insert(Storm5,2)
double.print_Forward()
double.print_Reverse()
double.erase(1)
double.print_Forward()
double.print_Reverse()
