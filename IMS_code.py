#to open the json doc
fd = open("/content/dhanu1.json",'r')
r = fd.read()
fd.close()
import json
dhanu1 = json.loads(r)



#to get new prod_id,name,pr,qn
prod_id = str(input("Enter product id:"))
name = str(input("Enter name:"))
pr = int(input("Enter price:"))
qn = int(input("Enter quantity:"))

manu[prod_id] = {'name': name, 'pr': pr, 'qn': qn}

js = json.dumps(dhanu1)

fd = open("/content/dhanu1.json",'w')
fd.write(js)
fd.close()



#to open the updated doc
import json

fd = open("/content/dhanu1.json",'r')
r = fd.read()
fd.close()

manu = json.loads(r)



#to get prod_id and quantity from to to buy
d_prod  = str(input("Enter the product_Id: "))
d_quant = int(input("Enter the quantity: "))
if dhanu1[d_prod]['qn']<=0:
  print("product is not available in store")
elif d_quant>dhanu1[d_prod]['qn']:
  print("That much quantity is not available")
else:
  print("Product: ", dhanu1[d_prod]['name'])
  print("Price: ", dhanu1[d_prod]['pr'])
  print("Billing Amount: ", dhanu1[d_prod]['pr'] * d_quant)
  dhanu1[d_prod]['qn'] = dhanu1[d_prod]['qn'] - d_quant


#to update the file as per sales
import json

fd = open("/content/dhanu1.json",'r')
r = fd.read()
fd.close()

dhanu1 = json.loads(r)



#to print the receipt
recepit={'prod' : d_prod, 'qn' : d_quant, 'amount': dhanu1[d_prod]['pr'] * d_quant}
receipt


