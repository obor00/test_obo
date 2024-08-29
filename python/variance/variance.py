def shifted_data_variance(data):
   if len(data) < 2:
      return 0.0
   K = data[0]
   n = Ex = Ex2 = 0.0
   for x in data:
      n = n + 1
      Ex += x - K
      Ex2 += (x - K) * (x - K)
   variance = (Ex2 - (Ex * Ex)/n)/(n - 1)
   # use n instead of (n-1) if want to compute the exact variance of the given data
   # use (n-1) if data are samples of a larger population
   return variance


adata=[38, 37, 36, 28, 18, 14, 12, 11, 10.7, 9.9]

variance=shifted_data_variance(adata)

print ("variance=", variance)

adata=[38, 37, 36, 28, 28, 34, 42, 41, 40.7, 39.9]
variance=shifted_data_variance(adata)
print ("variance=", variance)
