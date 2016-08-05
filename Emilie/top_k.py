import heapq
# from heapq_showtree import show_tree

#get clothes index
#def get_index(path):
#   image_name = path.split('/')[-1]
#   return image_name.split('_')[0]

# top-k clothes not top-k image!!
def top_k_dists(dists, k):        
    a=5
    top_ak_dists = heapq.nsmallest(k*a, dists, key=lambda t:t[1])
    top_k_clothes=[]
    knn_dic={}                              #there K = ak in KNN , knn_dic to count frequency
    
    for path,dist in top_ak_dists:
        image_name = path.split('/')[-1]    #so image_path has to use '/'   
        clothes_index=image_name.split('_')[0]

        if clothes_index not in knn_dic.keys():
            knn_dic[clothes_index]=0
        #++knn_dic[clothes_index]           #++ != +=1
        knn_dic[clothes_index]+=1

    knn_list=sorted(knn_dic.items(), key=lambda item:item[1], reverse=True)    
    print("clothes account in "+str(a*k)+" : "+str(len(knn_list))+"\n")    
    print("the nearest neighbor's frequency : "+str(knn_list[0][1])+"\n")

    if len(knn_list)>=k:
        knn_list=knn_list[0:k]

    for item in knn_list:
        clothes_index=item[0]
        for path,dist in top_ak_dists:
            image_name = path.split('/')[-1]
            if clothes_index==image_name.split('_')[0]:
                top_k_clothes.append(image_name)
                break;

        # repeat=False         
        # for clothes in top_k_clothes:
        #     if clothes.split('_')[0]==image_name.split('_')[0]:     #if the same clothes , then discard it
        #         repeat=True
        # if(not repeat):
        #     top_k_clothes.append(image_name)
        #     if len(top_k_clothes)==k:
        #         print("hit!!!")
        #         break
    ak=a*k
    while len(top_k_clothes)!=k:
        image_name=top_ak_dists[--ak][0].split('/')[-1]
        top_k_clothes.append(image_name)

    return top_k_clothes

# # top-k
# def top_k(data, k):
#     heap = data[:k]
#     # print 'random :'
#     # show_tree(heap)
#     heapq.heapify(heap)
#     # print 'heapified :'
#     # show_tree(heap)
# 
#     for i in range(k, len(data)):
# 
#         # if the dist is small than the current biggest dist, replace the biggest dist with this one
#         if data[i].dist < heap[0].dist:
#             biggest = heapq.heapreplace(heap, data[i])
#             # print 'replace %s with %s' % (biggest, data[i])
#         # else :
#             # print 'abondom :', data[i]
#         # show_tree(heap)
#     # for i, n in enumerate(heap):
#     #   print n
#     # print 'k smallest: '
#     result = sorted(heap, key=lambda x:x.dist)
#     # for i, n in enumerate(result):
#     #     print n
#     return result
        


# data = [Image('a', 5), Image('b', 4), Image('c', 0), Image('d', 2), Image('e', 9), Image('e', 3), Image('e', 1), Image('e', 19), Image('e', 109), Image('e', 58)]
# heap = 
# print 'random :', data

# for n in data:
#     # print 'add %3d:' % n
#     print n
#     heapq.heappush(heap, n)
    # show_tree(heap)


        

# swap value of different places in list
# def swap(l, i, j):
#   tmp  = l[i]
#   l[i] = l[j]
#   l[j] = tmp

# initialize heap, max heap in this case
# def init_heap(heap):

#   # important !!!
#   start = len(heap)/2 - 1

#   # adjust the heap, from the half to the root
#   for i in xrange(start, -1, -1):
#       big_child_index = 2*i+1
#       if 2*i+2 < len(heap) and heap[2*i+2] > heap[2*i+1]:
#           big_child_index = 2*i+2
#       if heap[big_child_index] > heap[i]:
#           swap(heap, big_child_index, i)




