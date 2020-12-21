#!/usr/bin/env python
# coding: utf-8

# In[46]:


from tkinter import *
import time
import random


# In[47]:


root = Tk()
root.title('Aplikasi Visualisasi Bubble Sort & Heap Sort')
root.geometry("880x640")
root.config (bg='white')

arr1 = []
arr2 = []
time_start = time.time()


# In[48]:


def arrayVisual(arr, color, canvas):
    canvas.delete("all")
    c_width = 340
    c_height = 240
    x_width = c_width / (len(arr) + 1)
    offset = 10
    space = 5
    normalizedarr = [ i / max(arr) for i in arr]
    for i, height in enumerate(normalizedarr):
        
        x0 = i * x_width + offset + space
        y0 = c_height - height * 210
       
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=color[i])

    root.update_idletasks()


# In[49]:


def randomArray():
    global arr1
    global arr2
    arr1 = []  
    arr2 = []
    
    length = int(inputN.get())
    for _ in range(length):
        arr1.append(random.randrange(1, 100))
    arr2[:] = arr1[:]
    arrayVisual(arr1,['red' for x in range(len(arr1))],canvas1)
    arrayVisual(arr2,['red' for x in range(len(arr2))],canvas2)


# In[50]:


def bubbleSort(arr,arrayVisual,canvas):
    global time_start

    n = len(arr)
    
    for i in range(n-1):
        for j in range(n-1):
            if(arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                arrayVisual(arr, ['yellow' if x == j or x == j+1 else 'blue' for x in range(len(arr))], canvas)
                updateTime(runTime2,time_start)
                
        


# In[51]:



def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
  
    if l < n and arr[i] < arr[l]:
        largest = l
  
    if r < n and arr[largest] < arr[r]:
        largest = r
  
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


# In[52]:


def heapSort(arr,arrayVisual,canvas):
    global time_start
    time_start = time.time()

    n = len(arr)
  
    for i in range(n//2, -1, -1):
        heapify(arr, n, i)
        arrayVisual(arr, ['yellow' if x == i or x == i+1 else 'blue' for x in range(len(arr))], canvas)
        updateTime(runTime1,time_start)
        
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
        arrayVisual(arr, ['yellow' if x == i or x == i+1 else 'blue' for x in range(len(arr))], canvas)
        updateTime(runTime1,time_start)


# In[53]:


def run():
    global arr1
    global arr2

    heapSort(arr1, arrayVisual, canvas1)
    bubbleSort(arr2, arrayVisual, canvas2)

def updateTime(timeLabel,startTime):
    timeLabel.config(text=time.time() - time_start)


# In[54]:


frameTombol = Frame(root, width = 720, height = 50, bg ='white')
frameTombol.grid(row = 0, column=0, padx =10, pady=10)

Label(frameTombol, text="Banyak elemen array:", bg= 'white').grid(row=0, column=0, padx=5,pady=5)
inputN = Entry(frameTombol)
inputN.grid(row=1, column=0, padx=5,pady=5)

tombolRandm =Button(frameTombol, text="Random Array", command=randomArray)
tombolRandm.grid(row=1, column=3, padx=5, pady=5)

tombolMulai = Button(frameTombol, text="Start", command=run)
tombolMulai.grid(row=1, column=5, padx=5, pady=5)

canvas1 = Canvas(root, width=340, height=240, bg = 'grey')
canvas1.grid(row=1, column=0, padx=10, pady=10)

canvas2 = Canvas(root, width=340, height=240, bg = 'grey')
canvas2.grid(row=2, column=0, padx=10, pady=10)

frameText1 = Frame(root, width = 720, height = 50, bg='white')
frameText1.grid(row= 1,column=1, padx=100,pady=100,sticky=W)
Label(frameText1,text="Heap Sort\n\nRunning Time (detik):\n\n",bg='white').grid(row=1,column=0)
runTime1 = Label(frameText1, text="",bg = "white")
runTime1.grid(row=1, column=1,pady=20,padx=40)

frameText2 = Frame(root, width = 720, height = 50, bg='white')
frameText2.grid(row= 2,column=1, padx=100,pady=100,sticky=W)
Label(frameText2,text="Bubble Sort\n\nRunning Time (detik):\n\n",bg='white').grid(row=2,column=0)
runTime2 = Label(frameText2, text="", bg = "white")
runTime2.grid(row=2, column=1,pady=20,padx=40)


root.mainloop()

