from category import load_categories
from spirit import load_spirits, Spirits, Spirit
import json


"""
同種合体で作成される精霊を検索
"""
def same_fusion(name):
    categories = load_categories()
    target = categories.get_category(name)
    spirits = load_spirits()
    if target:
        result = spirits.search_by_stuff(name)
        if result:
            return result.name
    return False


def main():
    spirits = load_spirits()
    categories = load_categories()
    result = spirits.get_up_by('魔獣')
    for category in categories.categories:
        up_list = spirits.get_up_by(category.name)
        if up_list:
            print("{:<4}{}".format(category.name, up_list))




if __name__ == '__main__':
    main()
