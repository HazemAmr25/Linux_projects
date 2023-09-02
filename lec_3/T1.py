#Lec_3   task1
#Write python code to generate Init function of GPIO for AVR


def GPIO_Init():
    
    
    print("- GPIOA\n- GPIOB\n- GPIOC")
    
    GPIOx=input(str("Enter GPIO that need to be init from the list :"))


    GPIO_init_regester = []
    
    print("enter the mode 'in or out' for the input bits  ")

 
    for bit_position in range(8):

        mode = input(f"Please enter Bit {bit_position} mode : ")

        if mode.lower() == "in":

            GPIO_init_regester.append("0")

        elif mode.lower() == "out":

            GPIO_init_regester.append("1")
        else:

            print("Invalid ")
            GPIO_init_regester = "error"
            break
        
    GPIO_init_regester = ''.join(GPIO_init_regester)    

    print(GPIOx + "   =   {}".format(GPIO_init_regester))


#call the function to init the GPIO register
GPIO_Init()

