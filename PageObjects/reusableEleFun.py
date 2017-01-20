 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
class ReusableEleFun(object):
     
    def get_click_Element_Fun(self,driver,myXpath):
        element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "myXpath")));
 
        element.click();