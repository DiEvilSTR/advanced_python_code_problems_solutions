def solution(l):
    divisor_counter = [0 for x in l]
    triple_counter = 0
    
    for num_index in range(len(l)):
    
        for previous_num_index in range(num_index):
            if l[num_index] % l[previous_num_index] == 0:
                # Counting number of divisors for every num in l
                divisor_counter[num_index] += 1
                # If second number have divisors count them as "lucky triples" 
                triple_counter += divisor_counter[previous_num_index]
    
    return triple_counter


res = solution([1, 2, 3, 4, 5, 6])
print(res)