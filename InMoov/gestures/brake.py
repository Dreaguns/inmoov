
def brake():
  #neopixel.write(9)
  inMoov.startedGesture()
  inMoov.moveHead(80,86)
  inMoov.moveArm("left",5,90,30,10)
  inMoov.moveArm("right",5,90,30,10)
  inMoov.moveHand("left",45,40,30,25,35,90)
  inMoov.moveHand("right",55,2,50,48,30,90)
  inMoov.moveTorso(90,90,90)
  sleep(3)
  inMoov.moveHead(20,86)
  inMoov.moveArm("left",21,92,49,22)
  inMoov.moveArm("right",38,91,43,10)
  inMoov.moveHand("left",45,40,30,25,35,90)
  inMoov.moveHand("right",89,127,123,48,30,90)
  inMoov.moveTorso(90,90,90)
  sleep(3)
  inMoov.moveHead(20,106)
  inMoov.moveArm("left",75,69,49,22)
  inMoov.moveArm("right",38,91,43,10)
  inMoov.moveHand("left",120,80,74,106,35,90)
  inMoov.moveHand("right",89,127,123,48,30,90)
  inMoov.moveTorso(90,90,90)
  sleep(3)
  inMoov.moveHead(20,93)
  inMoov.moveArm("left",75,69,49,22)
  inMoov.moveArm("right",71,66,60,10)
  inMoov.moveHand("left",120,80,74,106,35,90)
  inMoov.moveHand("right",89,127,123,48,30,146)
  inMoov.moveTorso(90,90,90)
  sleep(3)
  inMoov.moveHead(110,93)
  inMoov.moveArm("left",75,69,49,22)
  inMoov.moveArm("right",71,66,60,10)
  inMoov.moveHand("left",120,80,74,106,35,90)
  inMoov.moveHand("right",89,127,123,48,30,146)
  inMoov.moveTorso(90,90,90)
  sleep(3)
  inMoov.mouth.speakBlocking("Should I brake that")
  #inMoov.mouth.speakBlocking(u"Должен ли я тормозить")
  inMoov.moveHead(110,93)
  inMoov.moveArm("left",90,69,84,22)
  inMoov.moveArm("right",71,66,60,10)
  inMoov.moveHand("left",138,134,168,168,120,90)
  inMoov.moveHand("right",124,142,151,48,30,146)
  inMoov.moveTorso(90,90,90)
  inMoov.finishedGesture()

