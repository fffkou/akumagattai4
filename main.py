from category import Category, Categories, load_categories
import argparse


"""
悪魔合体
"""
def union(args):
    categories = load_categories()
    pic_category = args.categories
    result = categories.search_by_stuff(pic_category)
    if result:
        print(result)
    else:
        print('この組み合わせでは合体できません')


"""
必要な素材を検索
"""
def need(args):
    categories = load_categories()
    category = categories.get_category(args.target)
    if category.stuffs:
        for stuff in category.stuffs:
            print("{} × {}".format(stuff[0], stuff[1]))
    else:
        print('合体候補が見つかりませんでした')


def main():
    parser = argparse.ArgumentParser(description='合体検索')
    subparser = parser.add_subparsers()

    union_parser = subparser.add_parser('union', help='2身合体')
    union_parser.add_argument('categories', nargs=2, help='種族')
    union_parser.set_defaults(func=union)

    need_parser = subparser.add_parser('need', help='合体に必要な素材を検索します')
    need_parser.add_argument('target', type=str, help='作成したい種族')
    need_parser.set_defaults(func=need)

    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()
