class Cart():
  """
  The Cart class will wheels, capacity, and items to place inside

  Attributes for the class:
  -wheels expected to be an integer
  -volum expected to be an integer
  -items expected to be a list
  """
  def __init__(self,wheels,items = [], capacity = 10):
    #what ever someone hands in handle saving it to the value 2
    #self.wheels is like putting it on the cload
    #items is an empty list
    self.wheels = wheels
    self.items = items
    self.capacity = capacity

  def show(self):
      if len(self.items) == 0:
        print("you have no items")
      else:
        print("you have items in your Cart. ") #to do conditional if no items in bag
        for item in self.items:
          #the self word is kinda you want to bring it down from the cload
          print(item)

  def showCapacity(self):
    print(f"your capacity is ,{self.cacapcity-len(self.items())}" )

  def addcart(self):
    if len(self.items) == self.capacity:
      print("you have no more room")
      #self is to access the cart, its a magic word to use
    else:
      product = input("what would like to add")
      self.items.append(product)

  def changecart(self, capacity):
      self.capacity = capacity


def run():
  my_cart= Cart(4)
  while True:
    responce = input("what would you like to do \n -you may \n add \n-show \n-quit \n ")

    if responce.lower()=="quit":
      my_cart.showCapacity()
      print("Thanks for shopping")
      break
    elif responce.lower() == "add":
        my_cart.addcart()

    elif responce.lower() == "show":
        showChoice = input("what would you like to see \n-capacity \n-wheels \n Cart")
        if responce.lower == "capacity":
              my_cart.showCapacity()
        elif responce.lower() == "wheels":
              my_cart.wheels()
        else:
              my_cart.showcart()
    else:
        print("That is not a valid option, please enter add, show, or quit")


run()