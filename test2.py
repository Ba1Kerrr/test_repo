import itertools 

def check(code, masks, sums): 
    for mask, sum_value in zip(masks, sums): 
        current_sum = sum(code[i] for i in range(len(code)) if mask[i] == '1') 
        if current_sum != sum_value: 
            return False 
    return True 

def count(b, n, masks, sums): 
    valid_codes = 0 
    all_codes = itertools.product(range(b), repeat=n) 
    
    for code in all_codes: 
        if check(code, masks, sums): 
            valid_codes += 1 

    return valid_codes 

def main(): 
    b = int(input()) 
    n = int(input()) 
    t = int(input()) 
    
    masks = [] 
    sums = [] 
    
    for _ in range(t): 
        mask = input().strip() 
        s = int(input()) 
        masks.append(mask) 
        sums.append(s) 
    
    # Подсчет количества валидных кодов 
    result = count(b, n, masks, sums) 
    print(result) 

if __name__ == "__main__": 
    main()