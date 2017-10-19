from category import load_categories
from spirit import load_spirits, Spirits, Spirit
from devil import load_devils, Devils, Devil
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


"""
2身合体
"""


def normal_fusion(devil_name1, devil_name2):
    devils = load_devils()
    devil1 = devils.get_devil(devil_name1)
    devil2 = devils.get_devil(devil_name2)
    categories = load_categories()
    if devil1 and devil2:
        cat1 = categories.search_by_id(devil1.category)
        cat2 = categories.search_by_id(devil2.category)
        if cat1.name == cat2.name:
            result = same_fusion(cat1.name)
        else:
            pattern = [cat1.name, cat2.name]
            result = categories.search_by_stuff(pattern)
        return result
    return False


def main():
    pass


if __name__ == '__main__':
    main()
