
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
                                    break


password1()

