def lookaroundyou(data):
  inMoov.setHeadVelocity(36.0, 36.0, 19.0, 19.0, -1)
  for y in range(0, 3):
    if (data == "can i have your attention"):
      inMoov.mouth.speak("ok you have my attention")
      stopit()
      x = (random.randint(1, 6))
      if x == 1:
        inMoov.head.neck.moveTo(90)
        eyeslooking(data)
      if x == 2:
        inMoov.head.rothead.moveTo(80)
        eyeslooking(data)
      if x == 3:
        headdown()
        eyeslooking(data)
      if x == 4:
        headupp()
        eyeslooking(data)
      if x == 5:
        headright()
        eyeslooking(data)
      if x == 6:
        headleft()
        eyeslooking(data)
      sleep(1)
    x = (random.randint(1, 4))
    if x == 1:
      inMoov.mouth.speak("looking nice")
    if x == 2:
      inMoov.mouth.speak("i like it here")
    if x == 3:
      inMoov.mouth.speak("time just flies away")
    if x == 4:
      inMoov.mouth.speak("ok let's do something")
      sleep(2)
      x = (random.randint(1, 4))
      if x == 1:
        comehere()
      if x == 2:
        perfect()
        sleep(2)
        rest()
        sleep(1)
        relax()
      if x == 3:
        rest()
      if x == 4:
        fingerleft()
        sleep(3)
        relax()

