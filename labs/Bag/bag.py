from linearbag import Bag

mybag = Bag()

mybag.add( 19 )
mybag.add( 74 ) 
mybag.add( 23 )
mybag.add( 19 )
mybag.add( 12 )

value = int( input("Gues a value contained in the bag. "))

if value in mybag:
    print("The bag contains the value ", value)
else:
    print("The bag does not contain the value ", value)    