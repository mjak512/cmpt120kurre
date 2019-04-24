from random import random
def main():
            print("Hello AI Mike. What is your emotion?\n")
            AIstates = ["angry", "disgusted", "fearful", "happy", "sad", "suprised"]
            AINMikeEmotion = int(random() * 6);
            C = [[1,0,4,3,3,3],
                 [2,0,2,4,4,4],
                 [0,1,2,4,4,2],
                 [1,0,4,3,4,3]]


            def getInteraction():
                cmd = input('AI Mike is ' + AIstates[AINMikeEmotion] + ', change its emotion to be in a good mood or a bad mood: ')
                if cmd == "reward":
                    return 0
                elif cmd == "punish":
                    return 1
                elif cmd == "threaten":
                    return 2
                elif cmd == "joke":
                    return 3
                else:
                    return -1

                def lookupEmotion(currEmotion, userAction):
                    return C[userAction][currEmotion]
                while True:
                    interact = getInteraction()
                    if interact != -1:
                        AIMikeEmotion = lookupEmotion(AIMikeEmotion, interact)
                    else:
                        print("That is not a valid command, type again")

main()
