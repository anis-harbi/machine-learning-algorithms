
from sys import argv
import numpy as np
from numpy import genfromtxt

script, inputfile, outputfile = argv
with open(outputfile, "w") as fp: 
    fp.write('')

data0 = genfromtxt(inputfile, delimiter = ",")

n_examples = len(data0)

data = np.insert(data0, 0, 1, axis=1)

#normalizing data

av_age= np.mean(data[:,1])
sd_age= np.mean(data[:,1])

av_weight= np.mean(data[:,2])
sd_weight= np.mean(data[:,2])

av_height= np.mean(data[:,3])
sd_height= np.mean(data[:,3])

normalized_data = np.insert(data0, 0, 1,axis = 1)
normalized_data[:,1] = (data[:,1]-av_age)/sd_age
normalized_data[:,2] = (data[:,2]-av_weight)/sd_weight

nd = normalized_data

alpha = [0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1, 5, 10]
iterations = 100

def GradientDescent(alpha, iterations,nd):
    
    betas = [[0,0,0]]
    beta = [0,0,0]

    for i in range(iterations):
        errors = []

        for j in range(3):
            errors.append(np.sum((beta[0]+beta[1]*nd[:,1]+beta[2]*nd[:,2]-nd[:,3])*nd[:,j]))
        for j in range(3):
            beta[j] = beta[j] - alpha*errors[j]/len(nd)
        betas.append(beta[:])
    return np.array(betas)

for a in range(len(alpha)):
    
    beta = GradientDescent(alpha[a], iterations,nd)[iterations]
    #print beta[1], beta[2], beta[0]
    with open(outputfile, "a") as fp: 
        s1 = str(alpha[a])
        s2 = str(iterations)    
        s3 = str(beta[1])
        s4 = str(beta[2])
        s5 = str(beta[0])
        fp.write(s1)
        fp.write(",")
        fp.write(s2)
        fp.write(",")
        fp.write(s3)
        fp.write(",")
        fp.write(s4)
        fp.write(",")
        fp.write(s5)
        fp.write("\n")


betas = GradientDescent(1.92,280,nd)
arr = betas[280]
#print betas[100]
#for i in xrange(280):
#    print betas[i]

with open(outputfile, "a") as fp: 
        s1 = str(1.92)
        s2 = str(280)    
        s3 = str(arr[1])
        s4 = str(arr[2])
        s5 = str(arr[0])
        fp.write(s1)
        fp.write(",")
        fp.write(s2)
        fp.write(",")
        fp.write(s3)
        fp.write(",")
        fp.write(s4)
        fp.write(",")
        fp.write(s5)
        fp.write("\n")


#the following was used only for intuition in search of optimal parameters
#and is not used in the actual program
risk_beta=[]
for i in xrange(100):
    risk_beta.append(np.sum((betas[i,0] + betas[i,1]*nd[:,1] + betas[i,2]*nd[:,2] - nd[:,3])**2)/(2*len(nd)))

#we set a precision criteria
#and calculate the slope of the tanget
#or the rate of convergence

precision = 0.00001
n_iterations_needed = []
for i in range(len(risk_beta)-1):
    dif = risk_beta[i+1]-risk_beta[i]
    
   
    if abs(dif) > precision:
        n_iterations_needed.append(dif)
        #print dif, len(n_iterations_needed)



