import npyscreen as np
import os

class myPop(np.NPSAppManaged):

    def setname(self, name):
        self.name = name

    def setrank(self, rank, rank_list):
        self.rank = rank
        self.options = rank_list

    def setbearings(self, bearing1, bearing2, bearing3):
        self.bearing1 = bearing1
        self.bearing2 = bearing2
        self.bearing3 = bearing3

    def setdistances(self, distance1,distance2,distance3):
        self.distance1= distance1
        self.distance2= distance2
        self.distance3= distance3

    def main(self):
        #First page of Form
        F1 = np.Popup(name="Welcome to the Orienteering Calculator")
        NAME = F1.add(np.TitleText, name='Name')
        RANK = F1.add(np.TitleSelectOne, name='Rank', max_height=len(self.options), values=self.options, scroll_exit=True)
        F1.edit()
        self.return_name = NAME.value
        self.return_rank = RANK.get_selected_objects()

        #Second page of Form
        F2 = np.Popup()
        STARTPOINT = F2.add(np.TitleText,name="What is your starting point? >")
        F2.edit()
        self.return_startpoint = STARTPOINT.value

        #Third page of Form
        F3 = np.Popup()
        BEARING1 = F3.add(np.TitleText,name="bearing  1 >")   
        DISTANCE1= F3.add(np.TitleText,name="distance 1 >")
        F3.edit()
        self.return_bearing1 = BEARING1.value
        self.return_distance1=DISTANCE1.value


        #Fourth page of Form
        F4 = np.Popup()
        BEARING2 = F4.add(np.TitleText,name="bearing  2 >")   
        DISTANCE2= F4.add(np.TitleText,name="distance 2 >")
        F4.edit()
        self.return_bearing2 = BEARING2.value
        self.return_distance2=DISTANCE2.value


        #Fifth page of Form
        F5 = np.Popup()
        BEARING3 = F5.add(np.TitleText,name="bearing  3 >")   
        DISTANCE3= F5.add(np.TitleText,name="distance 3 >")
        F5.edit()
        self.return_bearing3 = BEARING3.value
        self.return_distance3=DISTANCE3.value

def ChooseRank(name,rank,rank_list,startpoint,bearing1,bearing2,bearing3,distance1,distance2,distance3):
    a = myPop()

    a.setname(name)
    a.setrank(rank, rank_list)
    a.setbearings(bearing1,bearing2,bearing3)
    a.setdistances(distance1,distance2,distance3)

    a.run()
    return a.return_rank, a.return_name, a.return_startpoint, \
           a.return_bearing1, a.return_bearing2, a.return_bearing3, \
           a.return_distance1,a.return_distance2,a.return_distance3

#print ChooseRank('name','rank', ['Scout', 'Tenderfoot', 'Second Class'],'startpoint','bearing1','bearing2','bearing3','distance1','distance2','distance3')
name,rank,sp,b1,b2,b3,d1,d2,d3=ChooseRank('name','rank', ['Scout', 'Tenderfoot', 'Second Class'],'startpoint','bearing1','bearing2','bearing3','distance1','distance2','distance3')
name,rank,sp,b1,b2,b3,d1,d2,d3=name,rank,sp,b1,b2,b3,d1,d2,d3

bs=b1+" "+b2+" "+b3
ds=d1+" "+d2+" "+d3

print(bs,ds,sp,name,rank)
os.system("cd /Users/donaldlippi/GitHub/troop35/orienteering && python orienteering_calculator.py" + \
          " -s "+sp+ \
          " -b "+bs+ \
          " -d "+ds+ \
          " -g " \
          )
