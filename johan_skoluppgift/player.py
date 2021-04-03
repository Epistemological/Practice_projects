#!/usr/bin/env python3
import random

from fishing_game_core.game_tree import Node
from fishing_game_core.player_utils import PlayerController
from fishing_game_core.shared import ACTION_TO_STR


class PlayerControllerHuman(PlayerController):
    def player_loop(self):
        """
        Function that generates the loop of the game. In each iteration
        the human plays through the keyboard and send
        this to the game through the sender. Then it receives an
        update of the game through receiver, with this it computes the
        next movement.
        :return:
        """

        while True:
            # send message to game that you are ready
            msg = self.receiver()
            if msg["game_over"]:
                return


class PlayerControllerMinimax(PlayerController):

    def __init__(self):
        super(PlayerControllerMinimax, self).__init__()

    def player_loop(self):
        """
        Main loop for the minimax next move search.
        :return:
        """

        # Generate game tree object
        first_msg = self.receiver()
        # Initialize your minimax model
        model = self.initialize_model(initial_data=first_msg)

        while True:
            msg = self.receiver()
            # Create the root node of the game tree
            node = Node(message=msg, player=0)

            # Possible next moves: "stay", "left", "right", "up", "down"
            best_move = self.search_best_next_move(
                model=model, initial_tree_node=node)

            # Execute next action
            self.sender({"action": best_move, "search_time": None})

    def initialize_model(self, initial_data):
        return None



    def search_best_next_move(self, model, initial_tree_node):
        mPenalty = [[0,0],[-1,0],[1,0],[0,-1],[0,1]]
        currentPosition = initial_tree_node.state.get_hook_positions().get(0)
        move = self.miniMax(initial_tree_node, int(currentPosition[0]),int(currentPosition[1]), mPenalty)
        """
        Use your minimax model to find best possible next move for player 0 (green boat)
        :param model: Minimax model
        :type model: object
        :param initial_tree_node: Initial game tree node
        :type initial_tree_node: game_tree.Node
            (see the Node class in game_tree.py for more information!)
        :return: either "stay", "left", "right", "up" or "down"
        :rtype: str
        """


        # EDIT THIS METHOD TO RETURN BEST NEXT POSSIBLE MODE FROM MINIMAX MODEL ###

        # NOTE: Don't forget to initialize the children of the current node
        #       with its compute_and_get_children() method!


        # NOTE: Don't forget to initialize the children of the current node
        #       with its compute_and_get_children() method!
        action_to_string = ["stay","left","right","up","down"]
        random_move = random.randrange(5)

        #return "right"
        return action_to_string[move]


    def generateDistance(self,parent,stateX, stateY):
        fish_pos = parent.state.get_fish_positions()
        fish_scores = parent.state.get_fish_scores()
        highScore = -99999999

        for j in fish_pos:
                    fish_score = 4*int(fish_scores[j])
                    fish_posX = int(fish_pos[j][0])

                    fish_posY = int(fish_pos[j][1])
                    currentScore = 2*fish_score-(abs(stateX-int(fish_pos[j][0]))+abs(stateY-int(fish_pos[j][1])))
                    highScore = max(currentScore,highScore)
            # Generate all fish positions and their scores
            # If negative fish set its score to -200
            # Make a function for ways to move count in overlap. See Anders Slides
            # Function that is going to be used currentScore = 2*fish_score - (stateX-fishP[0]) - (stateY-fishP[1])- stateY)
            #
        return highScore


#positionx
#positiony
#visited
#optimal
#penalty
#action_to_string
    def miniMax2(self, parent,aModel,bModel,childPosA,childPosB, player):

        if(parent.depth == 4):
            if (player):
                return self.generateDistance(parent,childPosA[0], childPosB[])
            else:
                return self.generateDistance(parent,childPosA[0], childPosB[])
        elif (player):
            player = False
            currentState = 0
            v = -9999
            children = parent.compute_and_get_children()
            for child in children:
                childPosA[0] += aModel.penalty[currentState][0]
                childPosA[1] += aModel.penalty[currentState][1]
                aModel.visited.append(childPosA)
                v = max(v, child,aModel,bModel,childPosA,childPosB,player)
                aModel.optimal = max(v, aModel.optimal)
                if (bModel.optimal <= aModel.optimal):
                    break
        else:
            player = True
            currentState = 0
            v = -9999
            children = parent.compute_and_get_children()
            for child in children:
                childPosB[0] += bModel.penalty[currentState][0]
                childPosB[1] += bModel.penalty[currentState][1]
                bModel.visited.append(childPosA)
                v = max(v, child,aModel,bModel,childPosA,childPosB,player)
                bModel.optimal = max(v, bModel.optimal)
                if (bModel.optimal <= aModel.optimal):
                    break
        return v

    def miniMax(self, parent, stateX, stateY, mPenalty):
        action_to_string = ["stay","left","right","up","down"]
        # Ways of optimization remember position so that restepping doesn't demand extra counting
        #
        if(parent.depth == 4):
            return self.generateDistance(parent,stateX, stateY)
        else:
            best = -10000000
            currentState = 0
            lastState = -1
            children = parent.compute_and_get_children()
            for child in children:
                #v = self.minimax(child,previousState, currentState,currentPosition[0]-mPenalty[currentState][0], fish, mPenalty)
                v = self.miniMax(child, stateX-mPenalty[currentState][0],stateY-mPenalty[currentState][1], mPenalty)
                if(v>=best):
                    lastState = currentState
                best = max(best,v)
                currentState +=1
            parent.move = lastState
            if(parent.depth == 0):
                return lastState
            else:
                return best
