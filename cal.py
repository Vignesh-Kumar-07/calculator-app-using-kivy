from kivy.app import App 
from  kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang import Builder


Window.size = (500,700)
Builder.load_file("my.kv")


class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = '0'
        
    #create a button press function
    def button_press(self,button):
        
        #creating a variavble that contain whatever in the text box
        pre  = self.ids.calc_input.text

    #    test for error
     
        if "ERROR" in pre:
            pre = ""


        if pre == "0":
            self.ids.calc_input.text = ''
            self.ids.calc_input.text  = f'{button}'
        else:
            self.ids.calc_input.text = f'{pre}{button}'

    def math_sign(self,sign):
        pre = self.ids.calc_input.text
        self.ids.calc_input.text = f'{pre}{sign}'

        
    #create remove function
    def remove(self):
        pre = self.ids.calc_input.text

        pre = pre[:-1]

        self.ids.calc_input.text = pre

        

    # create decimal function
    def dot(self):
        pre = self.ids.calc_input.text
        num_list = pre.split("+")
        


        if "+" in pre and "." not in num_list[:-1]:
            pre = f"{pre}."
            self.ids.calc_input.text = pre 


        elif  "." in pre:
            pass
        else:
            pre = f"{pre}."
            self.ids.calc_input.text = pre 

    # #create pos_neg function
    # def pos_neg(self):
    #     pre = self.ids.calc_input.text

    #     if "-" in pre:
    #         self.ids.calc_input.text = f'{pre.replace("-","")}' 
    #     else:
    #         self.ids.calc_input.text = f"-{pre}"






    def equalto(self):
        
        pre = self.ids.calc_input.text
        try:

            answer  = eval(pre)
            self.ids.calc_input.text = str(answer) 

        except:
            self.ids.calc_input.text ="ERROR"

             

            #Addition 
            # if '+' in pre:
            #     num_list  = pre.split("+")
            #     # print(num_list)
            #     answer = 0.0

            #     for number  in num_list:
            #         answer +=float(number)
                       

            #     self.ids.calc_input.text = int(answer)



         
         
             





class Calculatorapp(App):
    def build(self):
        
        return MyLayout()

if __name__ == "__main__":
    Calculatorapp().run()  
        

