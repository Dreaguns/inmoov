def notTrue():
  x = (random.randint(1, 3))
  inMoov.mouth.speak("oh")
  #inMoov.mouth.speak(u"Ох")
  sleep(0.2)
  inMoov.mouth.speak("really")
  #inMoov.mouth.speak(u"действительно")
  fullspeed()
  inMoov.moveHead(16,11)
  inMoov.moveArm("left",60,67,67,40)
  inMoov.moveArm("right",5,116,10,28)
  inMoov.moveHand("left",143,69,48,2,2,23)
  inMoov.moveHand("right",89,60,78,43,68,163)
  inMoov.moveTorso(161,62,92)
  sleep(3)
  rest()
  sleep(1)
  relax()
  if x == 1:
    inMoov.mouth.speak("okay then, as you please")
    #inMoov.mouth.speak(u"Тогда, как вам угодно")
    inMoov.moveHead(90,90)
  if x == 2:
    inMoov.mouth.speak("oh, yes I forgot")
    #inMoov.mouth.speak(u"О, да, я забыл")
    inMoov.moveHead(90,90)
  if x == 3:
    inMoov.mouth.speak("oh, I will turn around")
    #inMoov.mouth.speak(u"О, я обернусь")
    inMoov.moveHead(90,90)
