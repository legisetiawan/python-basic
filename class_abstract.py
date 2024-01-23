from abc import ABC, abstractmethod
# mewarisi method abstact class import dari abc, dan ABC class abtract, abstractmethod decorator methodnya. penggunaan abstractclass dengan decorator lain
class Button(ABC):
    def __init__(self,set_link):
        self.link = set_link # setter
    def click(self):
        pass
    
    @property
    @abstractmethod
    def link(self):
        pass
    
class PressButton(Button):
    
    def click(self):
        print("Got to link:{}".format(self.link)) # getter
        
    @Button.link.setter # urutan setter di perhatikan
    def link(self,input):
        self.__link = input
        
    @link.getter # getter
    def link(self):
        return self.__link
        
        
        
button = PressButton("www.google.com")
button.click()
# help(button)