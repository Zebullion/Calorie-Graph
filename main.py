from tabulate import tabulate
from tkinter import *
from tkinter.font import Font
from pygal import Bar

foods = []
calories = []



def main():
  wn = Tk()
  wn.title('Food Tracker')
  

  front = Font(family = 'Nyala', size = 25)

  Food = Entry(master = wn, width = 8, font=front)
  Foodlabel = Label(master = wn, text = 'Food', font = front)
  Calories = Entry(master = wn, width = 8, font=front)
  Calorieslabel = Label(master = wn, text = 'Calories', font = front)
  logTime = Button(master = wn, text = 'log info', font = front,command = lambda: add(Food, Calories))
  printTime = Button(master = wn, text ='Create Table', font = front,command=lambda: pTable())
  makeGraph = Button(master = wn,text = 'Make Graph',font = front,command = lambda:mGraph())
  
 


  Food.grid(row = 0, column = 1)
  Foodlabel.grid(row = 0, column = 2)
  Calories.grid(row = 2, column = 1)
  Calorieslabel.grid(row = 2, column = 2)
  logTime.grid(row = 3, column = 1)
  printTime.grid(row = 5, column = 1)
  makeGraph.grid(row = 7, column = 1)


  wn.mainloop()


def add(food,cal):
  temp = []
  f = food.get()
  c = cal.get()
  foods.append(f)
  calories.append(c)
 
  

def pTable():
  print(tabulate(calories))

def mergeSort(values):
  if len(values)<=1:
    return values

  sortedValues = []

  mid = len(values)//2

  low = mergeSort(values[:mid])
  upper = mergeSort(values[mid:])

  while len(low)>0 and len(upper)>0:
    if low[0]<upper[0]:
      sortedValues.append(low.pop(0))
    else:
      sortedValues.append(upper.pop(0))
  if len(low)>0:
    sortedValues.extend(low)
  elif len(upper)>0:
    sortedValues.extend(upper)
  return sortedValues
  print(sortedValues)



def mGraph():
  
  temp = []

  graph = Bar();

  graph.title=('Food and Calories')

 
  print(calories)
  print(foods)

  graph.x_labels=[]
  for i in foods:
    graph.x_labels.append(str(i))


  for x in calories:
    temp.append(int(x))


  graph.add('calories', temp)
  graph.render_to_file('fod.svg')

 

 







  






main()

