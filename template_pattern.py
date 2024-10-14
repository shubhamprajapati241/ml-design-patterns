from abc import ABC, abstractmethod 

# Step1: Create an abstract base class
class DinnerTemplate(ABC):
    # The template method defining the skeleton of the dinning experience 
    def serve_dinner(self):
        self.serve_appetizer()
        self.serve_main_course()
        self.serve_dessert()
        self.serve_bevarage()

    # Abstract methods
    @abstractmethod
    def serve_appetizer(self):
        pass 

    @abstractmethod 
    def serve_main_course(self):
        pass 
    
    @abstractmethod 
    def serve_dessert(self):
        pass 

    @abstractmethod 
    def serve_bevarage(self):
        pass 

# Step2 : Create concreate classes that implements the template steps 
class ItaianDinner(DinnerTemplate):
    def serve_appetizer(self):
        print("Serving bruschetta as appetizer")

    def serve_main_course(self):
        print("Serving pasta as the main course")

    def serve_dessert(self):
        print("Serving tiramisu as dessert")
    
    def serve_bevarage(self):
        print("Serving wine as the bevarage") 
    

class IndianDinner(DinnerTemplate):
    def serve_appetizer(self):
        print("Serving Paneer Tikka")
    
    def serve_main_course(self):
        print("Serving Dal Makhani with Naan") 
    
    def serve_dessert(self):
        print("Serving Gulaab Jamun")
    
    def serve_bevarage(self):
        print("Serving Lemon Soda")

# Step3 : Client code 
if __name__ == "__main__":
    print("******** Italian Dinner ********")
    italian_dinner = ItaianDinner()
    italian_dinner.serve_dinner()

    print("******** Indian Dinner ********")
    indian_dinner = IndianDinner()
    indian_dinner.serve_dinner()