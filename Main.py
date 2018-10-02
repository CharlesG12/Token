import Token
import time


class Collect:
    def __init__(self, p):
        self.path = p
        self.total_words = 0
        self.single_appear = 0
        self.unique_words = 0
        self.top30_words = 0
        self.avg_word_doc = 0
        self.seconds_elapsed = 0
        self.collection = Token.Token(p)
        self.sorted_dict = {}

    # turn on stemming on the process
    def run_stemming(self):
        self.collection.apply_stemming()

    # time to process the collection
    def run(self):
        start_time = time.time()
        self.collection.run()
        end_time = time.time()

        self.seconds_elapsed = end_time - start_time

    # calculate average words per document
    def cal_avg_word_doc(self):
        self.avg_word_doc = self.collection.sum_token_book / self.collection.num_book

    # calculate number of distinct tokens in the collection
    def cal_unique_word_doc(self):
        self.unique_words = len(self.collection.collection_dic)

    #
    def cal_all(self):
        self.run()
        self.cal_avg_word_doc()
        self.cal_unique_word_doc()

        sum_token_dict = {}
        # find each unique token words in collection dictionary
        for key, value in sorted(self.collection.collection_dic.items()):
            _sum = 0
            for v in value:
                _sum += v[1]
                # unique word only have one index and value is one
                if v[1] == 1 and len(value) == 1:
                        self.single_appear += 1
            sum_token_dict[key] = _sum
        # sort the dictionary and select the top 30 item
        self.sorted_dict = sorted(sum_token_dict.items(), key=lambda x: -x[1])[:30]

