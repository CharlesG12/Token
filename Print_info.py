import Main

# path for the docs
# path = 'data/'
path = 'D:\\Classes\\Information Retrival\\HW1\Token\\data\\'


# print answers for Problem1
def print_info_token():
    c = Main.Collect(path)
    c.cal_all()
    print()
    print("It took " + str(c.seconds_elapsed) + " seconds for token the collection")
    print("The number of tokens in the collection: " + str(len(c.collection.collection_dic)))
    print("The number of unique words in the collection: " + str(c.unique_words))
    print("The number of words only appear once in the collection: " + str(c.single_appear))
    print("The 30 most frequent words in the collection: ", end="", flush=True)

    for key, value in c.sorted_dict:
        print(str(key) + " " + str(value) + ", ", end="", flush=True)

    print()
    print("The average token per book " + str(round(c.avg_word_doc, 2)))


# print answers for Problem2
def print_info_stemming():
    c = Main.Collect(path)
    c.run_stemming()
    c.cal_all()
    print()
    print("The number of tokens in the collection: " + str(len(c.collection.collection_dic)))
    print("The number of distinct stems in the Cranfield text collection is: " + str(c.unique_words))
    print("The number of stems that occur only once in the Cranfield text collection: " + str(c.single_appear))
    print("The 30 most frequent stems in the Cranfield text collection: ", end="", flush=True)
    for key, value in c.sorted_dict:
        print(str(key) + " " + str(value) + ", ", end="", flush=True)

    print()
    print("The average token per book " + str(round(c.avg_word_doc, 2)))


print_info_token()
print_info_stemming()

