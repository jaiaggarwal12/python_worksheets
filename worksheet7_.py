import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import heapq


def print_board(board):
    for i in range(3):
        row = board[3*i:3*i+3]
        print(' | '.join([c if c!='' else str(3*i+j+1) for j,c in enumerate(row)]))
        if i < 2:
            print('--+---+--')

def check_winner(board, player):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for comb in wins:
        if all(board[i]==player for i in comb):
            return True
    return False

def check_tie(board):
    return all(cell != '' for cell in board)

def get_player_input(player, board):
    while True:
        pos = input(f"Player {player}, choose position (1-9): ")
        if not pos.isdigit(): 
            print("Enter number.")
            continue
        pos = int(pos)
        if pos < 1 or pos > 9:
            print("Range 1-9.")
            continue
        if board[pos-1] != '':
            print("Already taken.")
            continue
        return pos-1

def play_game():
    board = ['']*9
    current = 'X'
    while True:
        print_board(board)
        idx = get_player_input(current, board)
        board[idx] = current
        if check_winner(board, current):
            print_board(board)
            print(f"Player {current} wins!")
            break
        if check_tie(board):
            print_board(board)
            print("It's a tie.")
            break
        current = 'O' if current == 'X' else 'X'
    if input("Play again? (y/n): ").lower().startswith('y'):
        play_game()


# Project 2: To-Do List App

def add_task(tasks, task):
    tasks.append(task)

def view_tasks(tasks):
    for i,t in enumerate(tasks):
        print(i, t)

def delete_task(tasks, idx):
    if 0 <= idx < len(tasks):
        tasks.pop(idx)
    else:
        print("Invalid index.")

def todo_app():
    tasks = []
    while True:
        print("\n1) Add 2) View 3) Delete 4) Exit")
        cmd = input("Choose: ")
        if cmd == '1':
            t = input("Task: ")
            add_task(tasks, t)
        elif cmd == '2':
            view_tasks(tasks)
        elif cmd == '3':
            i = int(input("Index to delete: "))
            delete_task(tasks, i)
        elif cmd == '4':
            break
        else:
            print("Invalid.")


# Project 3: A* Pathfinding

def astar(grid, start, goal):
    rows, cols = grid.shape
    def neighbors(pos):
        r,c = pos
        for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr,nc]==0:
                yield (nr,nc)
    def h(a,b):
        return abs(a[0]-b[0]) + abs(a[1]-b[1])
    open_heap = []
    heapq.heappush(open_heap, (0+h(start,goal), 0, start, None))
    came_from = {}
    gscore = {start:0}
    while open_heap:
        f, g, current, parent = heapq.heappop(open_heap)
        if current in came_from:
            continue
        came_from[current] = parent
        if current == goal:
            # reconstruct
            path = []
            node = current
            while node:
                path.append(node)
                node = came_from[node]
            return path[::-1]
        for nb in neighbors(current):
            tentative_g = g + 1
            if nb in gscore and tentative_g >= gscore[nb]:
                continue
            gscore[nb] = tentative_g
            heapq.heappush(open_heap, (tentative_g + h(nb,goal), tentative_g, nb, current))
    return None

def visualize_grid(grid, path=None, start=None, goal=None):
    plt.imshow(grid, cmap='gray_r')
    if path:
        ys = [p[0] for p in path]
        xs = [p[1] for p in path]
        plt.plot(xs, ys, marker='o')
    if start:
        plt.scatter([start[1]], [start[0]], c='green', s=100)
    if goal:
        plt.scatter([goal[1]], [goal[0]], c='blue', s=100)
    plt.gca().invert_yaxis()
    plt.show()

def run_astar_demo():
    rows, cols = 10, 10
    grid = np.zeros((rows,cols), dtype=int)
    # place obstacles
    grid[3,1:8] = 1
    grid[6,2:9] = 1
    start = (0,0)
    goal = (9,9)
    path = astar(grid, start, goal)
    print("Path:", path)
    visualize_grid(grid, path, start, goal)

if __name__ == "__main__":
    print("1) Play tic-tac-toe, 2) Run ToDo app, 3) Run A* demo")
    choice = input("Choose (1/2/3): ")
    if choice == '1':
        play_game()
    elif choice == '2':
        todo_app()
    elif choice == '3':
        run_astar_demo()
    else:
        print("Exiting.")
