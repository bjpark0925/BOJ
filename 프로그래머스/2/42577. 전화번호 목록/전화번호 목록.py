def solution(phone_book):
    phone_dict = {}
    
    for num in phone_book:
        phone_dict[num] = True
    
    for num in phone_book:
        temp = ""
        for digit in num[:-1]:
            temp += digit
            if temp in phone_dict:
                return False
    
    return True