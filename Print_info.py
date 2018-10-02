import Main

# path for the docs
path = '/people/cs/s/sanda/cs6322/Cranfield/'
# path = 'D:\\Classes\\Information Retrival\\HW1\Token\\data\\'


# print answers for Problem1
def print_info_token():
    c = Main.Collect(path)
    c.cal_all()
    print()
    print("It took " + str(c.seconds_elapsed) + " seconds for token the collection")
    print("The number of tokens in the collection: " + str(c.collection.sum_token_book))
    print("The number of distinct tokens in the Cranfield text collection is: " + str(len(c.collection.collection_dic)))
    print("The number of words only appear once in the collection: " + str(c.single_appear))
    print("The average token per book " + str(round(c.avg_word_doc, 2)))
    print("The 30 most frequent words in the collection: ")
    print("Index  Word      Frequency")
    for index, item in enumerate(c.sorted_dict):
        print('{0:<6} {1:<9} {2:<8}'.format(index, item[0], item[1]))

    print()


# print answers for Problem2
def print_info_stemming():
    c = Main.Collect(path)
    c.run_stemming()
    c.cal_all()
    print("After Stemming")
    print("The number of tokens in the collection: " + str(c.collection.sum_token_book))
    print("The number of distinct stems in the Cranfield text collection is: " + str(len(c.collection.collection_dic)))
    print("The number of stems that occur only once in the Cranfield text collection: " + str(c.single_appear))
    print("The average token per book " + str(round(c.avg_word_doc, 2)))
    print("The 30 most frequent stems in the Cranfield text collection: ")
    print("Index  Word      Frequency")
    for index, item in enumerate(c.sorted_dict):
        print('{0:<6} {1:<9} {2:<8}'.format(index, item[0], item[1]))

    print()


print_info_token()
print_info_stemming()

