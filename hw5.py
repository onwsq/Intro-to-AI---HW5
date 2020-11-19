import math
import random
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from math import pow

class hw5:

 
    bag = []
    bag1 = []
    bag2 = []
    bag3 = []
    bag4 = []
    bag5 = []

    ##create the bags in relation to proportion of limes and cherries
    for x in range(25):
        bag1.append(1)
        bag2.append(1)
        bag3.append(1)
        bag4.append(1)
        bag5.append(0)

    for x in range(25):
        bag1.append(1)
        bag2.append(1)
        bag3.append(1)
        bag4.append(0)
        bag5.append(0)
    
    for x in range(25):
        bag1.append(1)
        bag2.append(1)
        bag3.append(0)
        bag4.append(0)
        bag5.append(0)

    for x in range(25):
        bag1.append(1)
        bag2.append(0)
        bag3.append(0)
        bag4.append(0)
        bag5.append(0)

    ##creates 4 more bags for each type for question 2c
    bag12 = bag1.copy()
    bag13 = bag1.copy()
    bag14 = bag1.copy()
    bag15 = bag1.copy()

    bag22 = bag2.copy()
    bag23 = bag2.copy()
    bag24 = bag2.copy()
    bag25 = bag2.copy()

    bag32 = bag3.copy()
    bag33 = bag3.copy()
    bag34 = bag3.copy()
    bag35 = bag3.copy()

    bag42 = bag4.copy()
    bag43 = bag4.copy()
    bag44 = bag4.copy()
    bag45 = bag4.copy()
    
    bag52 = bag5.copy()
    bag53 = bag5.copy()
    bag54 = bag5.copy()
    bag55 = bag5.copy()
    
    #shuffle bags
    random.shuffle(bag1)
    random.shuffle(bag2)
    random.shuffle(bag3)
    random.shuffle(bag4)
    random.shuffle(bag5)

    random.shuffle(bag12)
    random.shuffle(bag13)
    random.shuffle(bag14)
    random.shuffle(bag15)

    random.shuffle(bag22)
    random.shuffle(bag23)
    random.shuffle(bag24)
    random.shuffle(bag25)

    random.shuffle(bag32)
    random.shuffle(bag33)
    random.shuffle(bag34)
    random.shuffle(bag35)
    
    random.shuffle(bag42)
    random.shuffle(bag43)
    random.shuffle(bag44)
    random.shuffle(bag45)
    
    random.shuffle(bag52)
    random.shuffle(bag53)
    random.shuffle(bag54)
    random.shuffle(bag55)
    
    h1_arr = []
    h2_arr = []
    h3_arr = []
    h4_arr = []
    h5_arr = []
    bayes_arr = []

    x_axis = []

    index = 0
    for x in range(0,101):
        x_axis.append(index)
        index = index+1

    #for each graph
    for graph in range(5):
        cherry = 0
        lime = 0
        bag = []
        h1 = 0
        h2 = 0
        h3 = 0
        h4 = 0
        h5 = 0
        bayes = 0
        h1_arr = []
        h2_arr = []
        h3_arr = []
        h4_arr = []
        h5_arr = []
        bayes_arr = []
        
        if graph == 0:
            bag = bag1.copy()
        elif graph == 1:
            bag = bag2.copy()
        elif graph == 2:
            bag = bag3.copy()
        elif graph == 3:
            bag = bag4.copy()
        elif graph == 4:
            bag = bag5.copy()

        #print(str(len(bag)))

        #for each candy
        for x in range(-1, 100):

            if x != -1:
                if len(bag) == 1:
                    index1 = 0
                else:
                    index1 = random.randint(0, len(bag)-1)
                #cherry is picked
                if bag[index1] == 1:
                    cherry = cherry+1
                    bag.pop(index1)
                #lime is picked
                elif bag[index1] == 0:
                    lime = lime + 1
                    bag.pop(index1)
           
            if x == -1:
                h1 = 0.1
                h2 = 0.2
                h3 = 0.4
                h4 = 0.2
                h5 = 0.1
                bayes = 0.25*h2 + 0.5*h3 + 0.75*h4 + 1*h5
            else:
                h1 = 0**lime * 1**cherry * 0.1
                h2 = 0.25**lime * 0.75**cherry * 0.2
                h3 = 0.5**lime * 0.5**cherry * 0.4
                h4 = 0.75**lime * 0.25**cherry * 0.2
                h5 = 1**lime * 0**cherry * 0.1
                a = 1 / (h1 + h2 + h3 + h4 + h5)

                h1 = h1 * a
                h2 = h2 * a
                h3 = h3 * a
                h4 = h4 * a
                h5 = h5 * a
                bayes = 0.25*h2 + 0.5*h3 + 0.75*h4 + 1*h5
                
            h1_arr.append(h1)
            h2_arr.append(h2)
            h3_arr.append(h3)
            h4_arr.append(h4)
            h5_arr.append(h5)
            bayes_arr.append(bayes)

        proportion = lime / (lime+cherry)

        h1_arr = np.array(h1_arr)
        h2_arr = np.array(h2_arr)
        h3_arr = np.array(h3_arr)
        h4_arr = np.array(h4_arr)
        h5_arr = np.array(h5_arr)
        bayes_arr = np.array(bayes_arr)
        x_axis1 = np.array(x_axis)

        if graph == 0:
            title = 'Bag of 1.0 cherry'
        elif graph == 1:
            title = 'Bag of 0.75 cherry, 0.25 lime'
        elif graph == 2:
            title = 'Bag of 0.5 cherry, 0.5 lime'
        elif graph == 3:
            title = 'Bag of 0.25 cherry, 0.75 lime'
        elif graph == 4:
            title = 'Bag of 1.0 lime'

        plt.figure(graph)
        h1, = plt.plot(x_axis1, h1_arr, 'bo-', linewidth = 1.0, label = 'P(h1 | d)')
        h2, = plt.plot(x_axis1, h2_arr, 'gD-', linewidth = 1.0, label = 'P(h2 | d)')
        h3, = plt.plot(x_axis1, h3_arr, 'rs-', linewidth = 1.0, label = 'P(h3 | d)')
        h4, = plt.plot(x_axis1, h4_arr, 'y^-', linewidth = 1.0, label = 'P(h4 | d)')
        h5, = plt.plot(x_axis1, h5_arr, 'k*-', linewidth = 1.0, label = 'P(h5 | d)')
        plt.title(title)
        plt.xlabel('Number of observations in d')
        plt.ylabel('Posterior probability of hypothesis')
        plt.legend()
        plt.axis([0,100,0,1])

        plt.figure(graph+5)
        bayes, = plt.plot(x_axis1, bayes_arr, 'c+-', linewidth = 1.0, label = 'Bayesian prediction')
        plt.title(title)
        plt.xlabel('Number of observations in d')
        plt.ylabel('Probability that next candy is lime')
        plt.legend()
        plt.axis([0,100,0,1])




    # print("averages: ")

    cherry1 = 0
    cherry2 = 0
    cherry3 = 0
    cherry4 = 0
    cherry5 = 0
    lime1 = 0
    lime2 = 0
    lime3 = 0
    lime4 = 0
    lime5 = 0




    h1 = 0
    h2 = 0
    h3 = 0
    h4 = 0
    h5 = 0

    for graph in range(5):

        cherry1 = 0
        cherry2 = 0
        cherry3 = 0
        cherry4 = 0
        cherry5 = 0

        lime1 = 0
        lime2 = 0
        lime3 = 0
        lime4 = 0
        lime5 = 0
    

        h1_arr = []
        h2_arr = []
        h3_arr = []
        h4_arr = []
        h5_arr = []
        


        for x in range(-1, 100):
            h1_total = 0
            h2_total = 0
            h3_total = 0
            h4_total = 0
            h5_total = 0
            for y in range(5):
                currCherry = 0
                currLime = 0
                h1 = 0
                h2 = 0
                h3 = 0
                h4 = 0
                h5 = 0
                bag = []

                if y == 0:
                    if graph == 0:
                        bag = bag1
                    elif graph == 1:
                        bag = bag2
                    elif graph == 2:
                        bag = bag3
                    elif graph == 3:
                        bag = bag4
                    elif graph == 4:
                        bag = bag5
                elif y == 1:
                    if graph == 0:
                        bag = bag12
                    elif graph == 1:
                        bag = bag22
                    elif graph == 2:
                        bag = bag32
                    elif graph == 3:
                        bag = bag42
                    elif graph == 4:
                        bag = bag52
                elif y == 2:
                    if graph == 0:
                        bag = bag13
                    elif graph == 1:
                        bag = bag23
                    elif graph == 2:
                        bag = bag33
                    elif graph == 3:
                        bag = bag43
                    elif graph == 4:
                        bag = bag53
                elif y == 3:
                    if graph == 0:
                        bag = bag14
                    elif graph == 1:
                        bag = bag24
                    elif graph == 2:
                        bag = bag34
                    elif graph == 3:
                        bag = bag44
                    elif graph == 4:
                        bag = bag54
                elif y == 4:
                    if graph == 0:
                        bag = bag15
                    elif graph == 1:
                        bag = bag25
                    elif graph == 2:
                        bag = bag35
                    elif graph == 3:
                        bag = bag45
                    elif graph == 4:
                        bag = bag55


                if x != -1:
                    if len(bag) == 1:
                        index1 = 0
                    else:
                        index1 = random.randint(0, len(bag)-1)
                    if bag[index1] == 1:
                        if y == 0:
                            cherry1 = cherry1+1
                            currCherry = cherry1
                            currLime = lime1
                        if y == 1:
                            cherry2 = cherry2+1
                            currCherry = cherry2
                            currLime = lime2 
                        if y == 2:
                            cherry3 = cherry3+1
                            currCherry = cherry3
                            currLime =  lime3
                        if y == 3:
                            cherry4 = cherry4+1
                            currCherry = cherry4
                            currLime =  lime4
                        if y == 4:
                            cherry5 = cherry5+1
                            currCherry = cherry5
                            currLime =  lime5
                        bag.pop(index1)
                    elif bag[index1] == 0:
                        if y == 0:
                            lime1 = lime1+1
                            currCherry = cherry1
                            currLime = lime1
                        if y == 1:
                            lime2 = lime2+1
                            currCherry = cherry2
                            currLime = lime2             
                        if y == 2:
                            lime3 = lime3+1
                            currCherry = cherry3
                            currLime =  lime3
                        if y == 3:
                            lime4 = lime4+1
                            currCherry = cherry4
                            currLime =  lime4
                        if y == 4:
                            lime5 = lime5+1
                            currCherry = cherry5
                            currLime =  lime5
                        bag.pop(index1)
                    
                if x == -1:
                    h1 = 0.1
                    h2 = 0.2
                    h3 = 0.4
                    h4 = 0.2
                    h5 = 0.1
                else:
                    h1 = 0**currLime * 1**currCherry * 0.1
                    h2 = 0.25**currLime * 0.75**currCherry * 0.2
                    h3 = 0.5**currLime * 0.5**currCherry * 0.4
                    h4 = 0.75**currLime * 0.25**currCherry * 0.2
                    h5 = 1**currLime * 0**currCherry * 0.1
                    a = 1 / (h1 + h2 + h3 + h4 + h5)

                    h1 = h1 * a
                    h2 = h2 * a
                    h3 = h3 * a
                    h4 = h4 * a
                    h5 = h5 * a
                    
                    # print("graph #: "+str(graph))
                    # print("bag #: "+str(y+1))
                    # print("# limes: "+str(currLime))
                    # print("# cherries: "+str(currCherry))
                    # print("candies so far: "+str(x+1))
                    # print("h1: "+ str(h1))
                    # print("h2: "+ str(h2))
                    # print("h3: "+ str(h3))
                    # print("h4: "+ str(h4))
                    # print("h5: "+ str(h5)+"\n")
 
                h1_total = h1_total + h1
                h2_total = h2_total + h2
                h3_total = h3_total + h3
                h4_total = h4_total + h4
                h5_total = h5_total + h5

                # print("total h1: "+str(h1_total))
                # print("total h2: "+str(h2_total))
                # print("total h3: "+str(h3_total))
                # print("total h4: "+str(h4_total))
                # print("total h5: "+str(h5_total))

            h1_total = h1_total / 5
            h2_total = h2_total / 5
            h3_total = h3_total / 5
            h4_total = h4_total / 5
            h5_total = h5_total / 5

            h1_arr.append(h1_total)
            h2_arr.append(h2_total)
            h3_arr.append(h3_total)
            h4_arr.append(h4_total)
            h5_arr.append(h5_total)
            

        h1_arr = np.array(h1_arr)
        h2_arr = np.array(h2_arr)
        h3_arr = np.array(h3_arr)
        h4_arr = np.array(h4_arr)
        h5_arr = np.array(h5_arr)
        x_axis1 = np.array(x_axis)

        if graph == 0:
            title = 'Bag of 1.0 cherry averaged across 5 data sets'
        elif graph == 1:
            title = 'Bag of 0.75 cherry, 0.25 lime averaged across 5 data sets'
        elif graph == 2:
            title = 'Bag of 0.5 cherry, 0.5 lime averaged across 5 data sets'
        elif graph == 3:
            title = 'Bag of 0.25 cherry, 0.75 lime averaged across 5 data sets'
        elif graph == 4:
            title = 'Bag of 1.0 lime averaged across 5 data sets'

        plt.figure(graph+10)
        h1, = plt.plot(x_axis1, h1_arr, 'bo-', linewidth = 1.0, label = 'P(h1 | d)')
        h2, = plt.plot(x_axis1, h2_arr, 'gD-', linewidth = 1.0, label = 'P(h2 | d)')
        h3, = plt.plot(x_axis1, h3_arr, 'rs-', linewidth = 1.0, label = 'P(h3 | d)')
        h4, = plt.plot(x_axis1, h4_arr, 'y^-', linewidth = 1.0, label = 'P(h4 | d)')
        h5, = plt.plot(x_axis1, h5_arr, 'k*-', linewidth = 1.0, label = 'P(h5 | d)')
        plt.title(title)
        plt.xlabel('Number of observations in d ')
        plt.ylabel('Posterior probability of hypothesis')
        plt.legend()
        plt.axis([0,100,0,1])


    y_vals = []
    x_vals = []
    
    for x in range(0,5):
        # print("y value: "+str(x))
        val = math.factorial(int(4)) / math.factorial(int(x)) / math.factorial(int(4-x))*0.75**x*0.25**(4-x)
        # print("value at "+str(y)+": "+str(val)+"\n\n")
        y_vals.append(val)
        x_vals.append(x)

    y_vals1 = np.array(y_vals)
    x_vals1 = np.array(x_vals)

    plt.figure(15)
    width = 1
    plt.bar(x_vals1, y_vals1, width=width, align='edge')
    plt.xlabel('y')
    plt.ylabel('likelihood')
    plt.axis([0,5,0,1])


    
    fig, axs = plt.subplots(2,2)
    n = 0
    y = 0

    for k in range(4):
        x_axis = []
        y_axis = []
        theta = 0
        for x in range(11):
            if k == 0:
                n = 1
                y = 1
            elif k == 1:
                n = 2
                y = 2
            elif k == 2:
                n = 3
                y = 2
            elif k == 3:
                n = 4
                y = 3

            val = math.factorial(int(n)) / math.factorial(int(y)) / math.factorial(int(n-y))*theta**y*(1-theta)**(n-y)
            y_axis.append(val)
            x_axis.append(theta)
            theta = theta + 0.1

        # print("graph # "+str(k+1))
        # print("n flips: "+str(n))
        # print("y heads: "+str(y))
        # print("theta values")
        # print(x_axis)
        # print("posterior distribution values")
        # print(y_axis)

        y_axis1 = np.array(y_axis)
        x_axis1 = np.array(x_axis)

        if k == 0:
            axs[0,0].plot(x_axis,y_axis)
            axs[0,0].set_title('1 flip, 1 heads')
        elif k == 1:
            axs[0,1].plot(x_axis,y_axis)
            axs[0,1].set_title('2 flips, 2 heads')
        elif k == 2:
            axs[1,0].plot(x_axis,y_axis)
            axs[1,0].set_title('3 flips, 2 heads')
        elif k == 3:
            axs[1,1].plot(x_axis,y_axis)
            axs[1,1].set_title('4 flips, 3 heads')

        for ax in axs.flat:
            ax.set(xlabel = 'theta', ylabel = 'posterior distribution of theta')
        #for ax in axs.flat:
            #ax.label_outer()

    plt.show()







    


