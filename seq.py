list1 = [1,2,8,6,3,7,0,-1,-7]
list2 = [2,6,7,-7]

def check_seqence(array: list=[], seqence: list=[]):
    #check if all element contained in seqence are available in the given array
    
    present = False
    for elm in seqence:
        if elm in array:
            present=True
        else:
            present = False
            
    print(present)
    
    # appending the indexes of the element to 
    indexes=[]
    indexes2 = []
    if present:
        for a in seqence:
            indexes.append(array.index(a))
            indexes2.append(array.index(a))
        
        print(indexes)
        in_order = False    
        for b in indexes:
            indexes2.remove(b)
            for c in indexes2:
                print(b,c)
                if b < c:
                    in_order=True
                else:
                    return False
                    
                
        return in_order
    
# run the function    
ans=check_seqence(list1, list2)
print(ans)