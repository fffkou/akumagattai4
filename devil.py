from category import load_categories
import json



"""
悪魔情報クラス
"""
class Devil:
    def __init__(self, name, category, level):
        self.name = name
        self.category = category
        self.level = level


"""
悪魔情報操作クラス
"""


class Devils:
    def __init__(self, devils):
        self.devils = devils

    """
    """
    def update(self):
        devils_list = self.devils
        with open('data/devil.json', mode='w', encoding='utf-8') as f:
            json.dump(devils_list, f, ensure_ascii=False, indent=4)


    """
    悪魔情報新規追加
    """
    def add_devil(self, name, category_name, level):
        devil_data = {}
        categories = load_categories()
        for category in categories.categories:
            if category.name == category_name:
                category_number = str(categories.categories.index(category))
        devil_data['name'] = name
        devil_data['level'] = level
        if not self.devils.setdefault(category_number):
            self.devils[category_number] = []
        self.devils[category_number].append(devil_data)
        self.update()


"""
悪魔情報読み込み関数
"""


def load_devils():
    with open('data/devil.json', encoding='utf-8') as f:
        json_data = json.load(f)
        devils = Devils(json_data)
        return devils
            


def main():
    devils = load_devils()
    devils.add_devil('ハトホル', '女神', 18)


if __name__ == '__main__':
    main()
