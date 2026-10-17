# enumerate function is a built-in function in python that allows you to loop over a sequence (such as a list , tuple or string) and get the index and the value of each element  in the sequence at the same time. 
# enumerate() yields pairs containing (counter, item). In the loop statement (for index, fruit in ...), Python unpacks this pair into the two distinct variables you provide.

mark = [10,20,30,40,50]
# for i, v in enumerate(mark):
#     print(f"Index : {i} , Value : {v}")

for i, v in enumerate(mark, start=1):  # By default the index is at 0 but here we specify the starting index to be 1 . But mark[0] will still print 10 . 
    print(f"Box : {i} , Value : {v}")