# words = ["round" , "dream", "magnet" , "tweet" , "tweet", "trick", "kiwi"]
# for i in range(len(words)):
#     if words[i] == 'done':
#         break

#     if words[i][-1]==words[i+1][0] and words.count(words[i])=1:
#         continue
#     else:
#         print('i+1')

words = ["round" , "dream", "magnet" , "tweet" , "tweet", "trick", "kiwi"]
if words[0]=='done':
    print('done')
else:
    for i in range(1,len(words)):
        if words[i] == 'done':
            break
        if words[i-1][-1]!=words[i][0] or words[i] in words[:i]:
            print(f'{i+1}fail')
            break
        else:
            print('성공')



