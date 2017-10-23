from category import Category, Categories, load_categories
from fusion import same_fusion, normal_fusion
from devil import load_devils, Devils, Devil
import argparse


"""
悪魔合体
"""


def fusion(args):
    result = normal_fusion(args.devil_name1, args.devil_name2)
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


"""
素材を追加
"""
def add_stuff(args):
    categories = load_categories()
    result = categories.add_stuffs(args.name, args.stuffs)
    if result:
        print('追加しました')
    else:
        print('エラー: 追加できませんでした')


"""
悪魔の追加
"""


def add_devil(args):
    devils = load_devils()
    result = devils.add_devil(args.name, args.category, args.level)
    if result:
        print('登録しました')
    else:
        print('登録失敗')


def main():
    parser = argparse.ArgumentParser(description='合体検索')
    subparser = parser.add_subparsers()

    fusion_parser = subparser.add_parser('fusion', help='2身合体')
    fusion_parser.add_argument('devil_name1', type=str, help='悪魔1')
    fusion_parser.add_argument('devil_name2', type=str, help='悪魔2')
    fusion_parser.set_defaults(func=fusion)

    need_parser = subparser.add_parser('need', help='合体に必要な素材を検索します')
    need_parser.add_argument('target', type=str, help='作成したい種族')
    need_parser.set_defaults(func=need)

    add_stuff_parser = subparser.add_parser('add_stuff', help='種族情報を追加')
    add_stuff_parser.add_argument('name', type=str, help='素材を追加する種族')
    add_stuff_parser.add_argument('stuffs', nargs=2, help='追加する種族')
    add_stuff_parser.set_defaults(func=add_stuff)

    add_devil_parser = subparser.add_parser('add_devil', help='悪魔の追加')
    add_devil_parser.add_argument('name', type=str, help='悪魔の名前')
    add_devil_parser.add_argument('category', type=str, help='種族名')
    add_devil_parser.add_argument('level', type=str, help='初期レベル')
    add_devil_parser.set_defaults(func=add_devil)

    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()
