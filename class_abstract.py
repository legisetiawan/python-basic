from abc import ABC, abstractmethod
# mewarisi method abstact class import dari abc, dan ABC class abtract, abstractmethod decorator methodnya.
class Button(ABC):
    @abstractmethod
    def click(self):
        pass
    
class PressButton(Button):
    
    def click(self):
        print("Press Button click")
        
button = PressButton()
button.click()
help(button)