from Searcher import Searcher


class DFS(Searcher):

    name = '2.B_dfs.txt'

    def merge_list(self, list1, list2):
        list1 =  list2 + list1
        return list1