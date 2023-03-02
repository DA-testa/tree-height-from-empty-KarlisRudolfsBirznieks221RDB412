import sys
import threading


def calculate_height(n, parents):
    height = [-1] * n

    def get_height(node):
        if height[node] != -1:
            return height[node]
        if parents[node] == -1:
            height[node] = 1
        else:
            height[node] = get_height(parents[node]) + 1
        return height[node]

    max_height = 0
    for i in range(n):
        max_height = max(max_height, get_height(i))

    return max_height


def main():
    input_str = input().strip()

    if "I" in input_str:
        n = int(input())
        parents = list(map(int, input().split()))
        print(calculate_height(n, parents))

    if "F" in input_str:
        filename = input().strip()
        if len(filename) == 1:
            
        filename = "0" + filename
        filepath = "test/" + filename
        
        with open(filepath, 'r') as file:
            n = int(file.readline())
            parents = list(map(int, file.readline().split()))
        print(calculate_height(n, parents))


sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()
