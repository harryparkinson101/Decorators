def hello():
  print('hellooooooo')

greet = hello

# greet still works because greet still points to hello in memory when we run del hello greet is still able to run because greet still points to hello
del hello

print(greet())

def hi(func):
  func()

def greeting():
  print('still here')

a = hi(greeting)

print(a)
