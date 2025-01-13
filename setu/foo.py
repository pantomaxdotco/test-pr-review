
def foo1():
  ...

def foo2(*, a: int, b: int):
  ...

def foo3(a: int, *, b: int):
  ...
  
def foo4(a: int, b: int):
  ...

class ABC:
  def sample1(self): 
    ...

  def sample2(self, *, a: int, b: str):
    ...
    

  def sample3(self, a: int, b: str):
    ...

  def sample4(self, a: int, *, b: str):
    ...


from flask import Flask

myapp = Flask(__name__)

@myapp.post('/user/<username>')
def myfooroutes(var1, var2):  
    ...

mycelery = Celery('tasks', broker='pyamqp://guest@localhost//')

@mycelery.task(bind=True, max_retries=3)
def my_task(email, password):
    ...