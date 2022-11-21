
import math

k = 2.0     # shape parameter
c = 6.0     # scale parameter
bin = 2.0   # histogram bin size 
locn = 1.0  # location or offset value
pdir = 12.4 # wind direction probability (%)
mindiff = 1000.0 # 

w = [0.0]*6                     # initialise weibull array
u = [1.0,3.0,5.0,7.0,9.0,11.0]  # (imported) wind speed values (***at centre of bins***)
f = [0.1,2.4,5.7,3.2,0.8,0.2]   # (imported) wind frequency values

for i in range(0,len(u)):
  f[i] = f[i]/(pdir*bin) # normalise by pdir and bin size

print("check data")
print(len(u))

for i in range(0,len(u)):
  print("%.4f" % f[i])
 
for kk in range(400):   # k=2 (1 -> 5)
  for cc in range(400): # c=6 (4 -> 8)

    k = 1.0 + float(kk)/100.0
    c = 4.0 + float(cc)/100.0

    diff = 0

    for i in range(len(u)):
      w[i] = (k/c)*(((u[i]-locn)/c)**(k-1))*math.exp(-(((u[i]-locn)/c)**k))
      diff = diff + abs(w[i]-f[i])

    if (diff < mindiff):
      mindiff = diff
      k_save = k
      c_save = c

print("k = %.2f" % k_save)
print("c = %.2f" % c_save)



