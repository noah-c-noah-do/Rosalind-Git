# def add(X, Y):
#     Z = []
#     for i in range(len(X)):
#         subZ = []
#         for j in range(len(X[0])):
#             Zval = X[i][j] + Y[i][j]
#             subZ.append(Zval)
#         Z.append(subZ)
#     return Z


# X = [[1, -2], [-3, 4]]
# Y = [[2, -1], [0, -1]]
# # X = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
# # Y = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]

# Z = []
# for i, j in zip(X, Y):
#     sub_list = []
#     for i0, j0 in zip(i, j):
#         sub_value = i0 + j0
#         sub_list.append(sub_value)
#     Z.append(sub_list)
# print(Z)

test = 'When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be'


words = {}
wordlist = test.split(' ')
for word in wordlist:
    word_count = wordlist.count(word)
    words[f"{word}"] = word_count
for key, value in words.items():
    print(key + " " + str(value))
