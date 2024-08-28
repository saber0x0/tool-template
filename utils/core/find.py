from os import walk
from multiprocessing.dummy import Pool


class Find:

    def __init__(self):
        self.search_key = None

    def search(self, word):
        self.search_key = word
        my_list = []
        for path, dirs, files in walk('modules'):
            for f in files:
                # 排除特殊文件（以 "__" 开头）和私有文件（以 "_" 开头）
                if not "__" in path + '/' + f and not f.startswith("_"):
                    my_list.append(path + '/' + f)
        pool = Pool(2)
        results = pool.map(self.is_in_module, my_list)
        pool.close()
        pool.join()
        return self._clean_results(results)

    def is_in_module(self, arg):
        try:
            fr = open(arg, 'r')
            if self.search_key in fr.read().lower():
                return arg.replace(".py", "").replace("modules/", "")
            fr.close()
        except:
            return None

    @staticmethod
    def _clean_results(results):
        while None in results:
            results.remove(None)
        return results
