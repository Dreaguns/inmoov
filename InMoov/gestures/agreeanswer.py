def agreeanswer():
  i01.startedGesture()
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(1.0, 0.90)
  i01.setTorsoSpeed(1.0, 1.0, 1.0)
  i01.moveHead(120,90)
  sleep(0.5)
  i01.moveHead(20,90)
  sleep(0.5)
  i01.moveArm("left",20,93,42,16)
  i01.moveArm("right",20,93,37,18)
  i01.moveHand("left",180,180,65,81,41,143)
  i01.moveHand("right",180,180,18,61,36,21)
  i01.moveTorso(90,90,90)
  sleep(0.5)
  i01.moveHead(90,90)
  sleep(0.2)
  i01.finishedGesture()
  relax()
