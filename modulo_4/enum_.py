from enum import Enum

class Direction(Enum):
    rigth = 1
    left = 2
    up = 3
    down = 4
    
def move(direction):
    return f'Moving {direction.name}'
    
if __name__ == "__main__":
    print(move(Direction.down))
    print(move(Direction.left))
    print(move(Direction.down))