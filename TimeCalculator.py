class TimeCalculator:
    wholeDayAsMinute = 24 * 60
    weekDays = ("monday","tuesday","wednesday","thursday","friday","saturday","sunday")

    def __init__(self,start,duration,day_name=""):
        self.__start_time = start.split(" ")[0]
        self.__start_meridiem = start.split(" ")[1]
        self.__day_name=day_name.lower()

        self.__duration=duration
        self.__to_24Hour=0
        if self.__start_meridiem == "PM":
            self.__to_24Hour = 12

        self.startHour=int(self.__start_time.split(":")[0]) + self.__to_24Hour
        self.startMinute=int(self.__start_time.split(":")[1])
        self.durationHour=int(self.__duration.split(":")[0])
        self.durationMinute=int(self.__duration.split(":")[1])

        self.startAsMinutes = (self.startHour  * 60) + self.startMinute
        self.durationAsMinutes = (self.durationHour * 60) + self.durationMinute
        self.sumWithDuration = self.startAsMinutes + self.durationAsMinutes
        
    
    def calculatedDayDiff(self):
        rest =  self.sumWithDuration % self.wholeDayAsMinute
        if self.sumWithDuration == rest:
            return int(0)        
        return int((self.sumWithDuration - (self.sumWithDuration % self.wholeDayAsMinute)) / self.wholeDayAsMinute)
    
    def daysDiffString(self):
        days = self.calculatedDayDiff()
        if days == 0:
            return ""
        elif days == 1:
            return " (next day)" 
        else:
            return " ("+ str(days) +" days later)"

    def dayName(self):
        if self.__day_name == "":
            return ""
        days = self.calculatedDayDiff()
        if days == 0:
            return ", " + self.__day_name.capitalize()
        todayIndex = int(self.weekDays.index(self.__day_name))

        return ", " + self.weekDays[(todayIndex + days)%7].capitalize() 

    def calculatedTime(self):
        meridiem = " AM"
        days = self.calculatedDayDiff()

        time = self.sumWithDuration - (days * self.wholeDayAsMinute)

        minutes = int(time % 60)
        hours = int((time - minutes) / 60)
        
        if(hours > 12):
            hours -= 12
            meridiem = " PM"  
        
        if hours == 12 and minutes > 0:
                meridiem = " PM"    
        
        if hours == 0:
            hours = 12
        
        return  str(hours) + ":" +("0" + str(minutes))[-2:] + meridiem +self.dayName()+ self.daysDiffString()