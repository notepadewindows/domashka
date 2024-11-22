class gen:
   def __init__(self, data):
       self.data = data
   def __iter__(self):
       for item in self.data:
           yield item
iter = gen([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
for item in iter:
   print(item)