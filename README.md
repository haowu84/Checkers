# Checkers

In this project, implement a Checkers AI agent that can solve a Checkers game. 

## Classes

### Board Class:  
#### Summary  
This part describes the structure of Board class under BoardClasses.py.     
You can import/include this class into your AI file to use this class.  

#### Variables (in the init function)   
col: The number of columns.  
row: The number of rows.  
p: Number of rows filled with Checker pieces at the start.  

#### Functions   
show_board: Prints out the current board to the console.  
get_all_possible_moves: Returns all moves possible in the current state of the board.  
is_win: Check if there is a winner. Return which player wins.   

### Move Class:
#### Summary  
This part describes the structure of Move class under Move.py.  
This class already imported to your StudentAI.  
Your AI must return a ‘Move’ object to describe the move.  

#### Variables (in the init function)   
l: list describing the move.  

#### Functions   
from_str: Makes a move object from a str describing the move.   

### Checker Class:
#### Summary  
This part describes the structure of Board class under Checker.py.     
You can import/include this class into your AI file to use this class.  

#### Variables (in the init function)   
color: color of the checker piece.  
location: a tuple describing the location of the checker piece.    

#### Functions   
get_color: Returns the color of this piece.  
get_location: Returns the location of this piece.  
get_possible_moves: Returns all moves possible for this checker piece in the current state of the board.  


## Running your AI: 
### Manual Mode
After you compile your AI, use the following commands to run your AI in manual mode:   
```bash
python3 main.py {col} {row} {p} m {start_player (0 or 1)}
```

### Play Against Other AI’s
The shell also supports playing against other local AI shells written in different programming languages or against other AI’s. Navigate to Tools/AI_Runner.py shell and run the following commands:  

```bash
python3 AI_Runner.py {col} {row} {p} l {AI_1_path} {AI_2_path}
```





