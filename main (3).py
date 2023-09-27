class player:
  def play(self):
    print("The player is playing cricket.")

class Batsman(player):
   def play(self):
     print("The Batsman is Batting.")

class Bowler:
  def play(self):
    print("The Bowler is Bowling.")

#create objects of Batsman and Bowler classes and call the play() method for each object.
if_name=="main"
batsman=Batsman()
bowler=Bowler()

batsman.play()
bowler.play()
