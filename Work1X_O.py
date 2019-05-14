
def inputValid (): #check valid for table
    i = input("enter a number between 1 to 9 ")
    while i<"1" or i>"9" or len(i)!=1: 
        i = input("The number you enter is not between 1 to 9 ") 
    else:
        return int(i)

def wonChek(arr): #winnig check
    for rc in range (0,3):
        if arr[0][rc]==arr[1][rc]:       #row+colum
            if arr[0][rc]==arr[2][rc]: 
                return True
        if arr[rc][0]==arr[rc][1]:       #row+colum
            if  arr[rc][0]==arr[rc][2]:
                return True
    if   arr[1][1]==arr[0][0]:          # seconderay diagonal
        if arr[0][0]==arr[2][2] :
            return True
    if   arr[0][2]==arr[1][1]:     #mainl diagonal
        if arr[2][0]==arr[1][1]:
            return True
    return False

wons = [0,0]
tie=0
while True:            
                # input a array.
    arr=[
    ["1","2","3"],
    ["4","5","6"],
    ["7","8","9"]
    ]
    print("player x",wons[0],"player o",wons[1],"ties",tie)
    input("Press enter to starta new game")
    for turn in range(1,10): #choose turns
    
        print("-------------")      #draw table
        for i in range(0,3):
            for j in range (0,3):
                print("|",arr[i][j] , end = " ")
            print ("|")
            print("-------------")

        temp=inputValid()-1
        
        while(arr[(int)((temp)/3)][temp%3]=="o" or arr[(int)((temp)/3)][temp%3]=="x"): 
            print("the place has already used") #case for used place
            temp=inputValid()-1   
        else:
            if turn%2 != 0:
                arr[(int)((temp)/3)][temp%3]="x" #location x
            else:
                arr[(int)((temp)/3)][temp%3]="o" #location 0

        if wonChek(arr): #restart by case of winning
            break 
                      
    else:
        tie+=1 #there has been a tie
        print("The game ended with tie") 
        continue

    if turn%2!=0: # "x" win
        wons[0]+=1
        print("The game ended with a win for player x")
    else:           #"o" win
        wons[1]+=1
        print("The game ended with win for player o")