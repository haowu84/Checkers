import random
import math 
import time
import copy
from BoardClasses import Move
from BoardClasses import Board
#The following part should be completed by students.
#Students can modify anything except the class name and exisiting functions and varibles.

class Node:
    def __init__(self, color = None, move = None, wi = 0, si = 0):
        self.parent = None 
        self.children =[]
        self.color = color
        self.wi = wi 
        self.si = si
        self.move = move

    def get_children (self):
        return self.children 
        
    def get_wi (self):
        return self.wi 
    
    def get_si (self):
        return self.si 
        
    def get_color (self):
        return self.color
        
    def add_wi (self):
        self.wi += 1;
    
    def add_si (self):
        self.si += 1;
        
    def get_parent (self):
        return self.parent 
    
    def set_parent (self, parent):
        self.parent = parent 
    
    def add_child (self, node):
        node.set_parent (self) 
        self.children.append (node) 
    
    def getmove (self):
        return self.move 


class StudentAI():

    def __init__(self,col,row,p):
        self.col = col
        self.row = row
        self.p = p
        self.board = Board(col,row,p)
        self.board.initialize_game()
        self.color = ''
        self.opponent = {1:2,2:1}
        self.color = 2

    def best_child (self, node):
        largest_UCT = -1 
        best_node = None
        for child_node in node.get_children():
            if child_node.get_si() == 0:
                return child_node
            else:
                UCT = child_node.get_wi() / child_node.get_si() + 1.4 * math.sqrt(math.log(node.get_si())/child_node.get_si())
                if UCT > largest_UCT:
                    best_node = child_node
                    largest_UCT = UCT
        return best_node

    def select (self, node, board):
        while node.get_children():
            node = self.best_child(node)
            board.make_move(node.getmove(),self.opponent[node.get_color()])
        return node

    def expand (self, node, board):
        possible_moves  = board.get_all_possible_moves(node.get_color())
        if not possible_moves:
            return node
        for i in range(len(possible_moves)):
            for j in range(len(possible_moves[i])):
                node.add_child(Node(self.opponent[node.get_color()],possible_moves[i][j]))
        random_node = random.choice(node.get_children())
        board.make_move(random_node.getmove(),node.get_color())
        return random_node

    def simulate (self, node, board):
        color = node.get_color()

        while True:
            try:
                moves = board.get_all_possible_moves(color)
                index = random.randint(0,len(moves)-1)
                inner_index =  random.randint(0,len(moves[index])-1)
                move = moves[index][inner_index]
                board.make_move(move,color)
                winPlayer = board.is_win(color)
                if winPlayer != 0:
                    return winPlayer
                color = self.opponent[color]
            except:
                return self.opponent[color]

    def backpropogate (self, result, node):
        while node != None:
            node.add_si()
            if result != node.get_color():
                node.add_wi()
            node = node.get_parent()

    def mcts(self, color, board, allowed_time, start_time):
        root = Node(color)
        while (time.time() - start_time < allowed_time):
            board_copy = copy.deepcopy(board)
            leaf = self.select(root, board_copy)
            if leaf.get_si() != 0:
                child = self.expand(leaf, board_copy)
            else:
                child = leaf
            result = self.simulate(child, board_copy)
            self.backpropogate(result,child)
            
        best_move = max(root.get_children(),key=lambda x:x.get_wi()/x.get_si())
        return best_move.getmove()

    def get_move(self,move): 
        if len(move) != 0:
            self.board.make_move(move,self.opponent[self.color])
        else:
            self.color = 1

        st_time = time.time()

        move = self.mcts(self.color, self.board, 10, st_time)
        self.board.make_move(move,self.color)

        return move
        



        

