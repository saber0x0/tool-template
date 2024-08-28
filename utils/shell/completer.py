from prompt_toolkit.completion import Completion, Completer


class CustomCompleter(Completer):

    def __init__(self, words_dic=None):
        """自定义类，用于扩展 prompt_toolkit 的自动补全功能

        Args:
            words_dic (dict, optional): 要添加到自动补全器中的选项字典。默认为空字典 {}。
        """
        if words_dic is None:
            words_dic = {}
        self.words_dic = words_dic

    @staticmethod
    def _word_matches(word, last_words):
        return word.lower().startswith(last_words)

    def get_completions(self, document, complete_event):
        text_before_cursor = document.text_before_cursor.lower()
        text_before_cursor = str(text_before_cursor)
        text_arr = text_before_cursor.split(' ')
        last_words = text_arr[-1]
        words = self.__get_current_words(text_arr[:-1])
        for word in words:
            try:
                if type(word) == type([]):
                    for w in word:
                        if self._word_matches(w, last_words):
                            w = w + " "
                            yield Completion(w, -len(last_words))
                else:
                    if self._word_matches(word, last_words):
                        word = word + " "
                        yield Completion(word, -len(last_words))
            except:
                pass

    def __get_current_words(self, text_arr):
        current_dic = self.words_dic
        for tmp in text_arr:
            if tmp == ' ' or tmp == '':
                continue
            try:
                if tmp in current_dic.keys():
                    current_dic = current_dic[tmp]
                else:
                    return []
            except:
                return []
            if not current_dic:
                current_dic = ""
        return list(current_dic)
