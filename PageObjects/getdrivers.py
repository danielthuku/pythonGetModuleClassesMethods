from robot.libraries.BuiltIn import BuiltIn


class GetDrivers(object):
    def get_current_drivers(self):
        print("some body called me")
        se2lib = BuiltIn().get_library_instance('Selenium2Library')
        return se2lib._current_browser()
    
    
    
# from robot.libraries.BuiltIn import BuiltIn
# 
# 
# class GetDrivers(object):
#     def get_current_drivers(self):
#         print("some body called me")
#         se2lib = BuiltIn().get_library_instance('Selenium2Library')
#         return se2lib._current_browser()