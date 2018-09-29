import Token
import time

# path for the docs
path = 'data/'
cranefill = Token.Token(path)

cranefill.apply_stemming()

start_time = time.time()
cranefill.run()
end_time = time.time()

seconds_elapsed = end_time - start_time

single_appear = 0
unique = 0
avg_token_dict = cranefill.sum_token_book / cranefill.num_book
sum_token_dict = {}

for key, value in sorted(cranefill.collection_dic.items()):
    # print(str(key) + " " + str(value))
    _sum = 0
    for v in value:
        _sum += v[1]
        if v[1] == 1:
            single_appear += 1
            if len(value) == 1:
                unique += 1

    sum_token_dict[key] = _sum

sorted_dict = sorted(sum_token_dict.items(), key=lambda x: -x[1])[:30]


def print_info_token():
    print()
    print("It took " + str(seconds_elapsed) + " seconds for token the collection")
    print("The number of tokens in the collection: " + str(len(cranefill.collection_dic)))
    print("The number of unique words in the collection: " + str(unique))
    print("The number of words only appear once in the collection: " + str(single_appear))
    print("The 30 most frequent words in the collection: ", end="", flush=True)

    for key, value in sorted_dict:
        print(str(key) + " " + str(value) + ", ", end="", flush=True)

    print()
    print("The average token per book " + str(avg_token_dict))


print_info_token()
