import json
import argparse

UNKNOWN_SQUARE = '?'
MINE_SQUARE = '+'
FLAG_SQUARE = '*'

IS_MINE = -1

VALID_START_LOC = 'y'
INVALID_START_LOC = 'n'

def printSol(puzzle):
	output = ''
	for i in range(puzzle['width']):
		for j in range(puzzle['height']):
			if [i, j] in puzzle['mines']:
				output += MINE_SQUARE
			else:
				output += str(getNearMines(puzzle, i, j))
		output += '\n'
	print(output)

def printStage(puzzle):
	output = ''
	for i in range(puzzle['width']):
		for j in range(puzzle['height']):
			output += str(puzzle['knownMat'][i][j])
		output += '\n'
	print(output)

def getNearMines(puzzle, x, y):
	if [x, y] in puzzle['mines']:
		return IS_MINE #Hit a mine :(
	near = 0
	for k in [-1, 0, 1]:
		for l in [-1, 0, 1]:
			if [x+k, y+l] in puzzle['mines']:
				near += 1
	return near

def getNewBlankKnownMat():
	return [[UNKNOWN_SQUARE for y in range(height)] for x in range(width)]

def initPuzzle(mineList, width, height):
	puzzle = {'mines': mineList}
	puzzle['knownMat'] = getNewBlankKnownMat()
	puzzle['startingLocs'] = [[VALID_START_LOC for y in range(height)] for x in range(width)]
	puzzle['width'] = width
	puzzle['height'] = height
	return puzzle

def _solvePuzzle(puzzle, x, y):
	if [x, y] in puzzle['mines']:
		print('There was a big error...')
		sys.exit(0)
	getStartingPoints(puzzle)
	print(puzzle['startingLocs'])

def solvePuzzle(puzzle):
	for i in range(puzzle['width']):
		for j in range(puzzle['height']):
			if [i, j] in puzzle['mines']:
				puzzle['startingLocs'][i][j] = INVALID_START_LOC
			else:
				_solvePuzzle(puzzle)


parser = argparse.ArgumentParser(description='Generate games of minesweeper.')

parser.add_argument('--filename', metavar='-f', default='puzzle.txt', help='.', dest='filename')

args = parser.parse_args()

f = open(args.filename, mode='r')
filedata = json.load(f)

width = filedata['width']
height = filedata['height']
puzzles = filedata['puzzles']

for mineList in puzzles:
	puzzle = initPuzzle(mineList, width, height)
	printSol(puzzle)
	print('\n\n')
	solvePuzzle(puzzle)

f.close()
