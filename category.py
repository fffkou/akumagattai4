import json
import os


"""
種族オブジェクト

name: 種族名

stuffs: 合体に必要な素材
集合のリスト形式なので、
片方のみ or 両方の素材に対してマッチング検索がおこなえます。
"""
class Category:
	def __init__(self, name, stuffs):
		self.name = name
		self.stuffs = self.convert_stuffs(stuffs)

	"""
	指定素材と一致する場合、組み合わせを返す
	"""
	def match_stuff(self, search):
		match_stuffs = []
		for stuff in self.stuffs:
			if set(search) <= stuff:
				match_stuffs.append(stuff)
		return match_stuffs

	"""
	素材リストの組み合わせを集合に変換
	>>> [['a', 'b'], ['c', 'd'], ['a', 'e']]
	[{'a', 'b'}, {'c', 'd'}, {'a', 'e'}]
	"""
	def convert_stuffs(self, stuffs):
		stuffs_set = []
		if stuffs:
			for stuff in stuffs:
				stuffs_set.append(set(stuff))
		return stuffs_set



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
	def search_by_stuff(self, *stuffs):
		match_categories = {}
		for category in self.categories:
			if category.match_stuff(stuffs):
				match_categories[category.name] = category.match_stuff(stuffs)
		return match_categories


"""
種族情報を読み込み
"""
def load_categories():
	category_list = []
	with open('data/category.json', encoding='utf-8') as f:
		# Json形式を読み込み
		json_data = json.load(f)
		for line in json_data:
			# 種族名
			name = line['name']
			# 必要素材
			stuffs = []
			if line.setdefault('stuffs'):
				stuffs = line['stuffs']

			category = Category(name, stuffs)
			category_list.append(category)
	categories = Categories(category_list)
	return categories


if __name__ == '__main__':
	pass
