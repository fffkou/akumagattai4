import json
import os


"""
種族オブジェクト

name: 種族名
stuffs: 合体に必要な素材
"""
class Category:
    def __init__(self, ID, name, stuffs):
        self.ID = ID
        self.name = name
        self.stuffs = stuffs

    """
    指定素材と一致する場合、組み合わせを返す
    """
    def match_stuff(self, target):
        match_stuffs = []
        if isinstance(target, str):
            target = [target]
        for stuff in self.stuffs:
            if set(target) <= set(stuff):
                match_stuffs.append(stuff)
        if match_stuffs:
            return match_stuffs
        else:
            return False


"""
種族情報操作クラス
"""
class Categories:
    def __init__(self, categories):
        self.categories = categories

    """
    種族名からオブジェクトを返す
    """
    def get_category(self, name):
        for category in self.categories:
            if category.name == name:
                return category
        return False

    """
    指定素材にマッチする種族と素材リストを返す

    >>> ['a']
    {category1: [{'a', 'b'}, {'a', 'd'}], category2: [{'a', 'y'}]}
    >>> ['a', 'b']
    {category1: [{'a', 'b'}]}
    """
    def search_by_stuff(self, stuffs):
        match_categories = {}
        for category in self.categories:
            if category.match_stuff(stuffs):
                match_categories[category.name] = category.match_stuff(stuffs)
        return match_categories

    """
    種族情報更新
    """
    def update(self):
        categories_list = []
        # カテゴリーオブジェクトをjsonに変換できる形式に変換
        for category in self.categories:
            category_dict = {}
            category_dict['ID'] = category.ID
            category_dict['name'] = category.name
            category_dict['stuffs'] = []
            for stuff in category.stuffs:
                category_dict['stuffs'].append(stuff)
            categories_list.append(category_dict)
        with open('data/category.json', mode='w', encoding='utf-8') as f:
            json.dump(categories_list, f, ensure_ascii=False, indent="\t")

    """
    合体素材情報登録
    """
    def add_stuffs(self, name, stuffs):
        categories = load_categories()
        target_category = categories.get_category(name)
        if target_category:
            # 重複している場合は、追加処理をスキップ
            if not target_category.match_stuff(stuffs):
                target_category.stuffs.append(stuffs)
                categories.update()
                return True
        return False


"""
種族情報を読み込み
"""
def load_categories():
    category_list = []
    with open('data/category.json', encoding='utf-8') as f:
        # Json形式を読み込み
        json_data = json.load(f)
        for line in json_data:
            # ID
            ID = line['ID']
            # 種族名
            name = line['name']
            # 必要素材
            stuffs = []
            if line.setdefault('stuffs'):
                stuffs = line['stuffs']

            category = Category(ID, name, stuffs)
            category_list.append(category)
    categories = Categories(category_list)
    return categories


if __name__ == '__main__':
    pass
