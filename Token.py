from xml.dom import minidom
import os
import TokenRules
import Stemming


class Token:
    def __init__(self, path):
        self.collection_dic = {}
        self.num_book = 0
        self.sum_token_book = 0
        self.path = path
        self.stemming = 0

    def apply_stemming(self):
        self.stemming = 1

    # process in stream of text based on token rules
    # store token in dictionary
    def process_string(self, stream, doc_no):
        # create token dictionary for the book
        book_dict = {}

        words = stream.split()
        for w in words:
            # return processed word, 0 is not a word
            processed_word = TokenRules.apply(w)
            # filter empty word after tokenization
            if processed_word != 0:
                # apply stemming
                if self.stemming == 1:
                    processed_word = Stemming.apply_stemming(processed_word)

                # add new key to dictionary
                if w not in book_dict:
                    book_dict[processed_word] = [doc_no, 1]
                # increment value by 1 if key exist
                else:
                    book_dict[processed_word] = [doc_no, book_dict[processed_word][1] + 1]
        return book_dict

    # load individual xml file to Doc NO and Text
    def load_file(self, url):
        # parse xml doc from the url
        mydoc = minidom.parse(url)

        # read doc NO
        doc = mydoc.getElementsByTagName('DOCNO')[0]
        doc_no = int(doc.firstChild.data)

        # read doc text file
        text = mydoc.getElementsByTagName('TEXT')[0]
        data = text.firstChild.data

        return self.process_string(data, doc_no)

    # build a collection of dictionary for all the files under the path
    # apply stemming is boolean is 1, no stemming otherwise
    def run(self):
        # loop through files under path
        for filename in os.listdir(self.path):
            book_dic = self.load_file(self.path + filename)
            print(self.path + filename)
            # for average token per book
            self.num_book += 1
            self.sum_token_book += len(book_dic)
            # merge books dict to a collection dict
            for key, value in book_dic.items():
                print(str(key) + " " + str(value))
                # add token to dictionary if not exist
                if key not in self.collection_dic:
                    self.collection_dic[key] = [value]
                # increase the frequency by one if exist in the dictionary
                elif key in self.collection_dic:
                    self.collection_dic[key].append(value)

