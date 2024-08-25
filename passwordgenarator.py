import random
import string

def pass_gen(length):
    lower_case = list(string.ascii_lowercase)
    upper_case = list(string.ascii_uppercase)
    numbers = list(string.digits)
    special_char = ['/','_','-','*','&','^','%','$','#','@','~','<','>']
    password = [random.choice(lower_case),random.choice(upper_case),
                random.choice(numbers),random.choice(special_char)]
    
    all_char = lower_case + upper_case + numbers + special_char
    password += random.choices(all_char,k=length-4)
    random.shuffle(password)

    return ''.join(password)

def main():
    print("Password Generator :")
    length = int(input("Enter the desired length of password :"))
    try :
        if length < 4:
            raise ValueError("Password length must be atleast 4 to make a strong password with all cases, digits and special characters ")        
        else:
            print("The generated password is : ",pass_gen(length))
    except ValueError as ve:
        print(ve)

if __name__ == "__main__":
    main()
    
