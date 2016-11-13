import time;
import webbrowser;

current = time.localtime(time.time())

time_hours = input('Enter the hour that you would like the alarm to go off at.\n')
time_minutes = input('Enter the minute that you would like the alarm to go off at.\n')
noon = raw_input('AM or PM?\n')

print "The alarm will go off at %d:%d %s" %(time_hours, time_minutes, noon)

if noon == 'PM':
    time_hours += 12

sleep_minutes = time_minutes - current.tm_min
sleep_time = ((time_hours - current.tm_hour)*60 + sleep_minutes)*60

print "Alarm initiated..."
time.sleep(sleep_time)

print "Let's get jiggy with it"
webbrowser.open('https://www.youtube.com/watch?v=izGwDsrQ1eQ', new=1, autoraise = True)

