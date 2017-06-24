import json
import argparse

def printSol(puzzle, width, height):
    output = ''
    for i in range(width):
        for j in range(height):
            if [i, j] in puzzle:
                output += '*'
            else:
                output += str(getNearMines(puzzle, i, j))
        output += '\n'
    print(output)

def printStage(puzzle, width, height):
    output = ''
    for i in range(width):
        for j in range(height):
            if [i, j] in puzzle:
                output += '*'
            else:
                output += str(getNearMines(puzzle, i, j))
        output += '\n'
    print(output)

def getNearMines(puzzle, x, y):
    near = 0
    for k in [-1, 0, 1]:
        for l in [-1, 0, 1]:
            #print([x+k, y+l])
            if [x+k, y+l] in puzzle:
                near += 1
    return near


def solvePuzzle(puzzle, width, height):
    puzzle['knwonMat'] = [['_' for y in range(height)] for x in range(width)]
    #for i in range(width):
    #    for j in range(height):
    #        print(i, j, getNearMines(puzzle, i, j))


parser = argparse.ArgumentParser(description='Generate games of minesweeper.')

parser.add_argument('--filename', metavar='-f', default='puzzle.txt', help='.', dest='filename')

args = parser.parse_args()

f = open(args.filename, mode='r')
filedata = json.load(f)

width = filedata['width']
height = filedata['height']
puzzles = filedata['puzzles']



for puzzle in puzzles:
    printPuzzle(puzzle, width, height)
    print('\n\n')
    #solvePuzzle(puzzle, width, height)

f.close()
