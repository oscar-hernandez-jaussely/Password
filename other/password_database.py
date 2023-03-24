
def password1 ():

    password_correct = False

    while password_correct == False: 
        
        password = input ("Veuillez choisir un mot de passe : ")

        for x in password :

            res = any(ele.isupper() for ele in password)
            if res == False:
                print ("Votre mot de passe est invalide, veuillez réessayer")
                break
            else:
                res = any(ele.islower() for ele in password)
                if res == False:
                    print("Votre mot de passe est invalide, veuillez réessayer")
                    break
                else:
                    res = any(ele.isnumeric() for ele in password)
                    if res == False:
                        print("Votre mot de passe est invalide, veuillez réessayer")
                        break
                    else:
                        l = ["!", "@", "#", "$", "%", "^", "&", "*"]
                        found = False
                        found_item = ""
                        for item in l:
                            found = item in password
                            if found:
                                found_item = item
                                break
                        if found == False:
                            print("Votre mot de passe est invalide, veuillez réessayer")
                            break
                        else:
                                if (len(password)) < 8 :
                                    print("Votre mot de passe est invalide, veuillez réessayer")
                                    break
                                else :
                                    print("Votre mot de passe est valide")
                                    password_correct = True
                                    global final_password
                                    final_password = password
                                    break


def crypt():

    import hashlib
    global crypted_password
    global final_password
    crypted_password = hashlib.sha256(final_password.encode()).hexdigest()


def database():

    import json

    print ()

    global pass_list

    pass_list = {
    "passwords":    {
        "password": (final_password),
        }
    }

    with open("password_data.json", 'w') as write_object:  
        json.dump(pass_list, write_object, indent=1)

    a_s = 0


def database_menu():
    print("Votre mot de passe a bien été enregistré")
    print("Voulez vous en définir un autre ?")
    a1 = input("Tapez 'oui' pour écrire un nouveau mot de passe. Tapez 'non' pour quitter le programme.")

    if a1 == "oui":
        password1()
        crypt()
        database()

    elif a1 == "non":
        return
    


def data_enter():
    
    import json

    global a_s 
    global pass_list

    a_s = a_s + 1

    final_password_2 = final_password

    with open("password_data.json", 'r') as read_object:  
        json.load(pass_list) 

    for pass_list in pass_list:
        pass_list["new_password_"+str(a_s)] = (final_password_2)

    with open("password_data.json", 'w') as write_object:  
        json.dump(pass_list, write_object, indent=1) 


password1()

crypt()

database()

database_menu()

data_enter()

