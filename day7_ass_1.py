class player:
    plyerno = 0
    name = " "
    number_of_matches = 0
    match_goal = []

    def getdata(self):
        self.plyerno=int(input("enter player number : "))
        self.name = input("enter the name : ")
        self.number_of_matches=int(input("enter the number of matches : "))
        for i in range(0,self.number_of_matches):
            self.match_goal.append(int(input("enter number of goal : ")))

    def desplaydata(self):
        print("player number : ",self.plyerno,"player name : ",self.name,"number of matches : ",self.number_of_matches,"number of goals : ",self.match_goal)

obj = player()

obj.getdata()
obj.desplaydata()

