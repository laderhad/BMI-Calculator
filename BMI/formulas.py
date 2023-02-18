#Below are the equations used for calculating BMI in the International System of Units (SI)
# and the US customary system (USC) using a 5'10", 160-pound
#x=lbs,y=in
import webbrowser
import time


def calculate_BMI_USC(lbs,inch):
    BMI=703*lbs/inch**2
    if BMI <=18.5:
        print("You are UNDERWEIGHT")
        print("Useful article")
        time.sleep(3)
        webbrowser.open("https://www.nhs.uk/live-well/healthy-weight/managing-your-weight/advice-for-underweight-adults/")
    elif BMI<=24.9:
        print("CONGRATS You are NORMALWEIGHT ")
        
    elif BMI<=29.9:
        print("You are OVERWEIGHT")
        print("Useful article")
        time.sleep(3)
        webbrowser.open("https://www.nhsinform.scot/illnesses-and-conditions/nutritional/obesity")
    elif BMI<=40:
        print("OBESITY!")
        #coded by laderhad
        print("Useful article")
        time.sleep(3)
        webbrowser.open("https://www.nhsinform.scot/illnesses-and-conditions/nutritional/obesity")
    else:
        print("EXTREME OBESITY!!!!!")
        print("Useful article")
        time.sleep(3)
        webbrowser.open("https://www.nhsinform.scot/illnesses-and-conditions/nutritional/obesity")
    return f"your BMI:{BMI}"
    



def calculate_BMI_SI(kg,m):
    BMI=kg/m**2
    if BMI <=18.5:
        print("You are UNDERWEIGHT")
        print("Useful article")
        time.sleep(3)
        webbrowser.open("https://www.nhs.uk/live-well/healthy-weight/managing-your-weight/advice-for-underweight-adults/")
    elif BMI<=24.9:
        print("CONGRATS You are NORMALWEIGHT ")
        
    elif BMI<=29.9:
        print("You are OVERWEIGHT")
        print("Useful article")
        time.sleep(3)
        webbrowser.open("https://www.nhsinform.scot/illnesses-and-conditions/nutritional/obesity")
    elif BMI<=40:
        print("OBESITY!")
        print("Useful article")
        time.sleep(3)
        webbrowser.open("https://www.nhsinform.scot/illnesses-and-conditions/nutritional/obesity")
    else:
        print("EXTREME OBESITY!!!!!")
        print("Useful article")
        time.sleep(3)
        webbrowser.open("https://www.nhsinform.scot/illnesses-and-conditions/nutritional/obesity")
    return f"your BMI:{BMI}"
    
    
