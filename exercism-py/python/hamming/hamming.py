def distance(strand_a, strand_b):
    cnt=0
    if len(strand_a) != len(strand_b):
        raise ValueError("Length of stands are not same.")
    else:        
        for i in range(len(strand_a)):
            if strand_a[i] != strand_b[i]:
                cnt += 1
    return cnt 
