import numpy as np

datapoints = np.arange(15)


times  = np.array(datapoints, dtype='float')
times=times*0.5

#print(times)

height = np.array([], dtype='float')
uncertainty = np.array([], dtype='float')
g = -9.8
h0 = 500.

out_file = open("CadutaLiberaDati.txt", "w") 
out_file.write("Misure esperimento Caduta Libera\n")
out_file.write("Data: 13 Dicembre 2019\n")
out_file.write("\n\n")
out_file.write("       Punto    Tempo(sec)   Altezza(m)   Incertezza(m)\n")

for i in datapoints:
    dist = g*times[i]*times[i]+h0
    height = np.append(height,dist+np.random.randn())
    uncertainty = np.append(uncertainty,10./np.sqrt(dist))
    my_str = "        {:2d}        {:2.1f}          {:6.2f}         {:3.1f}".format(datapoints[i],times[i],height[i],uncertainty[i])
    print(my_str)
    out_file.write(my_str+"\n")

out_file.close()
