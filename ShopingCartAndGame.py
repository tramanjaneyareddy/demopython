import sys
def dis():
    for val in cart:
        print("{} :{}".format(val,cart[val]))


print('''welcome to shoping 
          1)to add item enter 1
          2)to remove item enter 2
          3)to view item enter 3
          4) to exit enter 0  
          5) total cost 4 ''')
cart={}
while True:

     no = int(input('enter your option:'))

     if no == 1:
      item=input('please enter item name:')
      if item in cart:
         print('item is allready taken please add quanty')
         quant=int(input('please enter  qunt:'))
         cart[item]=cart[item]+quant
      else:
          quant=int(input('enter quanty:'))
          cart[item]=quant

     elif no ==2:
        item = input('please enter item name:')
        quant=int(input('no of delete :'))
        if quant<1:
          del (cart[item])
        else:
              cart[item] = cart[item]-quant

     elif no == 3:
         dis()



     elif no !=  0:
         print('please enter valid no')
         no=int(input('enter no:'))
     else:
         sys.exit()


