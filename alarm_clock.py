class Alarm_Clock:
    def __init__(self):
        self.current_time = "9:00 am"
        self.alarm_on = True
        self.alarm_time = "7:00 am"

    def alarm_switch(self):
        if self.alarm_on == True:
            self.alarm_on = False
            print("You have turned off your alarm clock! ")
        elif self. alarm_on == False:
            print("You have turned on your alarm clock!")

    def change_time(self):
        self.current_time = input("What time would you like to change the alarm clock to? ")
        print("The current time is:", self.current_time)
