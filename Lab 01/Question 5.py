def calavg (numbers):
  sum = 0.0
  count = 0
  for nums in numbers:
    sum = sum + nums
    count = count + 1
  avg = sum/count
  return avg

marks = [70,80,90]
result = calavg (marks)
print ("Marks:",marks)
print("Average marks:",result)
