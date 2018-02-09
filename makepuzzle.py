import argparse
import random
import json

def makePuzzle(args):
	puzzle = {'width': args.width, 'height': args.height, 'puzzles': []}

	#grid = [[0 for y in range(args.height)] for x in range(args.width)]

	for i in range(args.numPuzzles):
		minesGenerated = 0
		puzzle['puzzles'].append([])
		while minesGenerated < args.mines:
			x = random.randint(0, args.width-1)
			y = random.randint(0, args.height-1)
			if [x, y] not in puzzle['puzzles'][i]:
				puzzle['puzzles'][i].append([x, y])
				minesGenerated+=1

	f = open(args.filename, 'w')
	f.write(json.dumps(puzzle))
	f.close()

parser = argparse.ArgumentParser(description='Generate games of minesweeper.')

parser.add_argument('--num-puzzles', metavar='-n', default=1, type=int, help='Number of of puzzles to generate. >= 1.', dest='numPuzzles')
parser.add_argument('--location', metavar='-l', default='puzzle.txt', help='Location to gnerate puzzles.', dest='filename')
parser.add_argument('--width', metavar='-w', default=16, type=int, help='Width of puzzle.', dest='width')
parser.add_argument('--height', metavar='-h', default=16, type=int, help='Height of puzzle.', dest='height')
parser.add_argument('--mines', metavar='-m', default=40, type=int, help='Number of of mines.', dest='mines')
parser.add_argument('--seed', default=None, metavar='-s', help='Seed for puzzle generation.', dest='seed')

args = parser.parse_args()
random.seed(a=args.seed)

if args.mines > args.width * args.height:
	raise 'You have created more mines than you have room for'

makePuzzle(args)
