class Admition(object):
       
        
    def ageVal(age):
    # Validates the patrons age and returns age
        if int(age) < 18:
            print("you are " + age + ": Denied access")
            
        elif int(age) == 90:
            print ('Admited but no assistance')
            return age
        
        else:
            print("you are " + age +": Granted access")
            return age
        
    # Validates if the attendant was in the queue
    def queueVal(pos):
        if queue.__contains__(pos):
            print('You were in the queue.')
        else:
            print("You must join the queue.")

    # Get the oldest in queue
    def elders(y):
        oldest = max(y)
        return oldest

    # Admition list
    def allowIn(age, pos):
        if pos in str(queue):
            myList = [age], [pos]
            return myList
        
    # Verify attendents age
    #def ageVer(age, pos):
        

    def menu (pos, queue, age):
        optn  = None
        
        while optn != '3':
            
            print(
                '''
                    Welcome

                    0 - Admition
                    1 - View Queue
                    2 - Age Verification
                    3 - Qiut

                '''
                )
            optn = input("Select action: ")

            if optn == '0':
                Admition.ageVal(age)
                Admition.queueVal(pos)
                enter = Admition.elders(Admition.allowIn(age, pos))
                print('The be below attendant is alagible for admition:')
                print(enter)
                optn2 = input('Enter another? Y/N :')

                while optn2 != 'N':
                    age = input("Enter age:")
                    pos = input("Enter position: ")
                    Admition.ageVal(age)
                    Admition.queueVal(pos)
                    enter = Admition.elders(Admition.allowIn(age, pos))
                    print('The be below attendant is alagible for admition:')
                    print(enter)
                
            elif optn == '1':
                attendants = Admition.allowIn(age, pos)
                print (attendants)
                
                
                

        

        


age = input("Enter age:")
pos = input("Enter position: ")
queue = ['A19', 'B28', 'C23', 'D4', 'E78', 'F90', 'G32', 'H54', 'I32', 'J12', 'J67', 'L90', 'M87', 'N6', 'O38', 'P12', 'Q24']

app = Admition
app.menu(pos, queue, age)



input("\n\nPress any key to exit.")
