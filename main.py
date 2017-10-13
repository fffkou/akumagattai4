from category import Category, Categories, load_categories
import argparse


"""
悪魔合体
"""
def union(args):
	categories = load_categories()
	pic_category = set(args.category)


"""
"""
def pos(args):
	pass


def main():
	parser = argparse.ArgumentParser(description='合体検索')
	subparser = parser.add_subparsers()

	union_parser = subparser.add_parser('union', help='2身合体')
	union_parser.add_argument('category', nargs=2, help='種族')
	union_parser.set_defaults(func=union)

	possible_parser = subparser.add_parser('pos', help='合体可能な種族を検索します')
	possible_parser.add_argument('category', type=str, help='対象の種族')
	possible_parser.set_defaults(func=pos)

	args = parser.parse_args()
	args.func(args)

if __name__ == '__main__':
	main()
