def solution(today, terms, privacies):
    answer = []
    today_year = int(today[:4])
    today_month = int(today[5:7])
    today_day = int(today[8:])
    #print(today_year, today_month, today_day)
    
    terms_dict = {}
    for term in terms:
        alphabet = term[0]
        limit_month = int(term[1:])
        terms_dict[alphabet] = limit_month
    #print(terms_dict)
    
    for i, privacy in enumerate(privacies):
        p_year = int(privacy[:4])
        p_month = int(privacy[5:7])
        p_day = int(privacy[8:10])
        p_alpha = privacy[-1]
        
        plus_month = terms_dict[p_alpha]
        final_month = p_month + plus_month
        final_year = p_year
        if final_month // 12 > 0:
            final_year += final_month // 12
            final_month %= 12
            if final_month == 0:
                final_year -= 1
                final_month += 12
        
        final_day = p_day - 1
        if final_day == 0:
            final_month -= 1
            final_day += 28
            if final_month == 0:
                final_year -= 1
                final_month += 12
        
        if final_year == today_year :
            if final_month == today_month:
                if final_day < today_day:
                    answer.append(i+1)
            elif final_month < today_month:
                answer.append(i+1)
        elif final_year < today_year:
            answer.append(i+1)
    
    return answer