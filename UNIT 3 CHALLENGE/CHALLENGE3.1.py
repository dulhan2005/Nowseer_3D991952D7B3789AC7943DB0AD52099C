

def linearSearchProduct(productList, targetProduct):
  indices = []
  
  for index, product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)
      
      return indices

#Example usuage:
products = [ "boot", "loafer", "shoes", "sandal"]
target = "loafer"
target2 = 'apple'
result = linearSearchProduct(products, target)
print(result)
      