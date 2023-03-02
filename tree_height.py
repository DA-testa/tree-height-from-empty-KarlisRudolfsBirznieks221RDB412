import sys
import threading

def calculate_height(n, parents):
    heights = [-1] * n

    def get_height(node):
        if heights[node] != -1:
            return heights[node]
        if parents[node] == -1:
            heights[node] = 1
        else:
            heights[node] = get_height(parents[node]) + 1
        return heights[node]

    max_height = 0
    for i in range(n):
        max_height = max(max_height, get_height(i))

    return max_height

def main():
    user_input = str(input())
    if "I" in user_input:
        n = int(input())
        parents = list(map(int, input().split()))
        print(calculate_height(n, parents))
    elif "F" in user_input:
        filename = str(input())
        filepath = "test/" + filename
        with open(filepath, 'r') as file:
            n = int(file.readline())
            parents = list(map(int, file.readline().split()))
        print(calculate_height(n, parents))
        
sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()
