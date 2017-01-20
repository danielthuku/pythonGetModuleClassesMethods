#  
# from getdrivers import GetDrivers
#  
# class PageObjects(GetDrivers):
#      
#     #def get_current_drivers(self):
#         return GetDrivers.get_current_drivers(self) 

''''
Instead of doing all above just use below code to 
import all modules classes and method from multiple .py   
'''
      
import inspect      
import sys
from types import FunctionType
import pkgutil

class PageObjects():
    pass
 
 
classes = list()
 
from os.path import dirname, join, isdir, abspath, basename
from glob import glob
pwd = dirname(__file__)
for x in glob(join(pwd, '*.py')):

    
    if not x.startswith('__'):
        mod = __import__(basename(x)[:-3], globals(), locals())
    
        classes = [getattr(mod, x) for x in dir(mod) if isinstance(getattr(mod, x), type)]
         
        for cls in classes:

             
            funList = [x for x, y in cls.__dict__.items() if type(y) == FunctionType and callable(y) and not (y.__name__).startswith('__')]
             
            for fun in funList:

                __fun = fun
                __funt__ = cls.__dict__[fun]
                
                def __fun(__funt__):
                    def fun(self):
                        return __funt__.__call__(self)  
                    return fun
                test_funcRun =  __fun(__funt__)   

                setattr(PageObjects, fun, test_funcRun)
