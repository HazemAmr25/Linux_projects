import webbrowser


def Firefox(input_link):
    if (input_link=='youtupe'):
        webbrowser.open('https://www.youtube.com/')
    elif(input_link=='Facebook'):    
        webbrowser.open('https://www.facebook.com/') 
    elif(input_link=='twitter'):
        webbrowser.open('https://twitter.com/') 
    elif(input_link=='Linkedin'):  
        webbrowser.open('https://www.linkedin.com/')
    else:
        print("the input link does not exist")

