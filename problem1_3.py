#problem1
#@author Anis Harbi

from sys import argv
import numpy



class perceptron:
    w0 = 0
    w1 = 1
    w2 = 2
    #reads input file in nested array 
    #such that calling arr[2][1] is 
    #refers to 2nd feature of the 3rd example
    script, filename_1, filename_2= argv
    input_file = open(filename_1)
    file = input_file.read()
    file = file.replace('\n',' ')
    file = file.replace(',', ' ')
    file = file.split(' ')
    file = map(int, file)
    file = zip(*[iter(file)]*3) 
    #cleans out output file
    #so that we use append mode when we write to output
    with open(filename_2, "w") as fp: 
        fp.write('')

    training_data=file 
    convergence = False
    while (convergence == False):
        
        #prev weights save copies for purposes of determining convergence
        prev_w0 = w0
        prev_w1 = w1
        prev_w2 = w2

        j = 0
        while  (j < len(training_data)):  
            x1 = training_data[j][0]
            x2 = training_data[j][1]
            d = training_data[j][2]        
            dot_product=  w0*1+ w1*x1 + w2*x2
            if (d*dot_product <= 0):
                w0 = w0 + d*1
                w1 =w1 + d*x1
                w2 = w2 + d*x2

            j = j+1
        
        condition = w1 - prev_w1 + w2 - prev_w2 
        if (condition == 0):
            convergence = True
        #print w1,w2
       
        #writes w1,w2,b to output1.csv
        with open(filename_2, "a") as fp: 
            
            s1 = str(w1)
            s2 = str(w2)
            s3 = str(w0)
            fp.write(s1)
            fp.write(",")
            fp.write(s2)
            fp.write(",")
            fp.write(s3)
            fp.write("\n")

      





    
    




