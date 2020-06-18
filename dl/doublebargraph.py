import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import random


x_axis_dataset=[['yellow','blue','red','green'],
            ['Google','IBM','Facebook'],
            ['Jodhpur','Pune','Mumbai','Delhi'],
            ['Arpit','Raghav','Aditya','Tanuj','Akash'],
            ['Cake','Sandwich','Pizza','Burger','Chips','Chocolate'],
            ['Python','C++','Java','Ruby','C','Javascript','R'],
            ['Html','Css','Javascript'],
            ['Maharashtra','Rajasthan','UP','Kerala','Assam','MP'],
            ['Mi','Realme','Apple','Samsung'],
            ['Android','Iphone'],
            ['Dell','HP','Apple','Asus'],
            ['India','USA','UK','China']
            ]
color1=["red","yellow","pink"]
color2=["blue","green","brown"]
label1=["local","overseas","sale","profit"]
label2=["profit","loss","price","value"]
os.mkdir("Doublebargraphfordl")

numberOfGraphs=1000
plt.figure(figsize=(10,6))
for i in range(numberOfGraphs):
    xx=random.choice(x_axis_dataset)
    bars1=[]
    bars2=[]
    # width of the bars
    barWidth = 0.3

    for _ in range(len(xx)):
        bars1.append(random.randint(1,100))
        bars2.append(random.randint(1,100))


    # The x position of bars
    r1 = np.arange(len(bars1))
    r2 = [x + barWidth for x in r1]

    # Create blue bars
    plt.bar(r1, bars1, width = barWidth, color = random.choice(color1), capsize=7, label=random.choice(label1))

    # Create cyan bars
    plt.bar(r2, bars2, width = barWidth, color = random.choice(color2),  capsize=7, label=random.choice(label2))

    # general layout
    plt.xticks([r + barWidth for r in range(len(bars1))], xx)
    plt.ylabel('height')
    plt.legend()
    k=str(i+1)
    var="image"+k+".png"
    image_filepath=os.path.join("Doublebargraphfordl/",var)
    # Show graphic
    plt.savefig(image_filepath)
    plt.cla()
