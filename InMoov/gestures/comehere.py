def comehere():
  fullspeed()
  rest()
  inMoov.setNeopixelAnimation("Larson Scanner", 0, 200, 0, 1)
  inMoov.startedGesture()
##look around
  inMoov.setHeadVelocity(36, 36, 50, 50, -1)
  inMoov.moveHead(80,66,7,85,52)
  sleep(3)
  inMoov.moveHead(80,110,175,85,52)
  sleep(3)
##raise arm point finger
  inMoov.setHandVelocity("left", 43.0, 43.0, 43.0, 43.0, 43.0, -1)
  inMoov.setHandVelocity("right", -1, 43.0, -1, -1, -1, -1)
  inMoov.setArmVelocity("left", -1.0, -1.0, -1.0, -1.0)
  inMoov.setArmVelocity("right", 50, -1, -1, -1)
  inMoov.setHeadVelocity(-1, 50)
  inMoov.setTorsoVelocity(-1, -1, -1)
  inMoov.moveHead(80,86,85,85,52)
  inMoov.moveArm("left",5,94,30,10)
  inMoov.moveArm("right",7,74,92,10)
  inMoov.moveHand("left",180,180,180,180,180,90)
  inMoov.moveHand("right",180,2,175,160,165,180)
  inMoov.moveTorso(90,90,90)
  sleep(4.5)
##move finger
  inMoov.setHandVelocity("left", -1, -1, -1, -1, -1, -1)
  inMoov.setHandVelocity("right", -1, -1, -1, -1, -1, -1)
  inMoov.setArmVelocity("left", -1.0, -1.0, -1.0, -1.0)
  inMoov.setArmVelocity("right", -1.0, -1.0, -1.0, -1.0)
  inMoov.setHeadVelocity(-1, -1)
  inMoov.setTorsoVelocity(-1, -1, -1)
  inMoov.moveHead(80,86)
  inMoov.moveArm("left",5,94,30,10)
  inMoov.moveArm("right",48,74,92,10)
  inMoov.moveHand("left",180,180,180,180,180,90)
  inMoov.moveHand("right",180,2,175,160,165,20)
  inMoov.moveTorso(90,90,90)
  sleep(2)
  inMoov.setHeadVelocity(36, 36)
  inMoov.moveHead(80,80)
  inMoov.moveHand("right",180,164,175,160,165,20)
  sleep(1)
  inMoov.moveHead(80,80)
  inMoov.moveHand("right",180,2,175,160,165,20)
  sleep(1)
  inMoov.moveHead(118,80)
  inMoov.moveHand("right",180,164,175,160,165,20)
  sleep(1)
  inMoov.mouth.speak("come closer")
  inMoov.moveHead(60,80)
  inMoov.moveHand("right",180,2,175,160,165,20)
  sleep(1)
  inMoov.moveHead(118,80)
  inMoov.moveHand("right",180,164,175,160,165,20)
  sleep(1)
  inMoov.moveHead(60,80)
  inMoov.moveArm("right",90,65,10,25)
  sleep(3)
  fullspeed()
  rest()
  sleep(0.3)
  relax()
  sleep(3)
  inMoov.finishedGesture()
