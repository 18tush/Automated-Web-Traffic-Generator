import robot

logFile = open('mylog.txt', 'w') 
robot.run("trafficgen",stdout=logFile)