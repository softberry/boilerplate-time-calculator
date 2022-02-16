from  TimeCalculator import TimeCalculator

def am_pm(ampm):
    if ampm=="AM":
        return 0
    else:
        return 12

def is_next_day(sh,dh):
    return 24 - sh <= dh and dh < 48 - sh



def add_time(start, duration,dayName=""):
    
    return TimeCalculator(start, duration,dayName).calculatedTime()