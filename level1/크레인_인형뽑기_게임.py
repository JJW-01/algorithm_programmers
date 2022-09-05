# -*- coding: utf-8 -*-
"""크레인 인형뽑기 게임.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XMxGzQzuPEiqsfLm79arvy1EBXxk6ULW
"""

def solution(id_list, report, k):
    report_set=set(report)
    report=list(report_set)
    report1=[]
    report2=[]
    reported_number=[]
    reported_person=[]
    mailed_person=[]
    answer=[]
    pos=[]
    for number in range(len(report)):
        divided_report=report[number].split(' ')
        report1.append(divided_report[0])
        report2.append(divided_report[1])
    for t in range(len(id_list)):
        reported_number.append(report2.count(id_list[t]))
    for x in range(len(id_list)):
        if reported_number[x] >=k:
            reported_person.append(id_list[x])
    for z in range(len(reported_person)):
        for i in range(len(report2)):
            if report2[i] == reported_person[z]:
                pos.append(i)
    for i in range(len(pos)):
        mailed_person.append(report1[pos[i]])
    for i in range(len(id_list)):
        answer.append(mailed_person.count(id_list[i]))
    return answer

solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2)

from collections import defaultdict

def solution(id_list, report, k):
    answer=[]
    report=list(set(report)) # 중복제거
    report_user=defaultdict[set]
    reportednumber_user=defaultdict[int]

    for r in report:
        a,b= r.split()
        report_user[a].add(b)
        reportednumber_user[b] += 1
    
    for i in id_list:
        result = 0
        for u in user[i]:
            if reportednumber_user[u]>=k:
                result +=1
        answer.append(result)
    return answer

def solution(arr):
    answer = []
    answer.append(arr[0])
    
    for i in range(1, len(arr)):
        if arr[i-1] != arr[i]:
            answer.append(arr[i])
    return answer

solution([1,1,3,3,0,1,1])

def solution(lottos, win_nums):
    answer = []
    
    damaged=lottos.count(0)
    
    intact=set(lottos)
    if damaged >0:
        intact.remove(0)
    win_nums=set(win_nums)
    print(intact, win_nums)
    print(intact & win_nums)
    price=len(intact&win_nums)
    
    if price >=1:
        answer=[7-damaged-price,7-price]
    elif price ==0:
        answer=[7-damaged,6]
    
    return answer

solution([17,15,3,4,45,0],[20, 9, 3, 45, 4, 35])

k=[44, 1, 0, 0, 31, 25]
k.remove(0)
print(k)

def solution(sizes):
    
    hor=[]
    ver=[]
    size=[]
    
    for i in range(len(sizes)):
        hor.append(sizes[i][0])
        ver.append(sizes[i][1])
    for k in range(len(sizes)):
        if hor[k]>=ver[k]:
            size.append(ver[k])
        elif hor[k]<ver[k]:
            size.append(hor[k])
    if max(hor) >= max(ver):
        b=max(hor)
    elif max(hor) < max(ver):
        b=max(ver)
    a=max(size)
    answer=a*b
    return answer

solution([[60, 50], [30, 70], [60, 30], [80, 40]])

def solution(left, right):
    num_yak=[]
    answer=0
    for i in range(left, right):
        for k in range(i):
            if i%k==0:
                num_yak.append(i)
        if len(num_yak)%2 ==0:
            answer+=i
        elif len(num_yak)%2 == 1:
            answer-=i
    
    return answer

solution(13,17)

def solution(board, moves):
    lst=[]
    for i in range(len(board)):
        globals()['ver_board_{}'.format(i+1)]=[]
        for k in range(len(board)):
            if board[k][i] != 0:
                globals()['ver_board_{}'.format(i+1)].append(board[k][i])
        print(globals()['ver_board_{}'.format(i+1)])
    
    for i in range(len(moves)):
        k=moves[i]
        if not globals()['ver_board_{}'.format(k)] == []:
            lst.append(globals()['ver_board_{}'.format(k)][0])
            del globals()['ver_board_{}'.format(k)][0]
    
    print(lst)
    answer = 0
    return answer

solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4])

def solution(N, stages):
    count_stage=[]
    for i in range(1, N+2):
        count_stage.append(stages.count(i))
    print(count_stage)
    answer = []
    return answer

solution(5,[2, 1, 2, 6, 2, 4, 3, 3])

lst=[]

if not lst ==[]:
  print("안빔")
else:
  print("비어있음")

lst=[3,4,5]
del lst[2]
print(lst)

integral_list = [1,2,3]
dictionary = {integral : i for i, integral in integral_list}
print(dictionary)

def solution(N, stages):
    count_stage=[]
    fail_ratio=[]
    for i in range(1, N+2):
        count_stage.append(stages.count(i))

    count=0
    all_count=len(stages)
    for i in range(N):
      if (all_count-count) != 0:
        fail_ratio.append(count_stage[i]/(all_count-count))
        count += count_stage[i]
      else :
        fail_ratio.append(0)
        count += count_stage[i]

    dictionary = {i : ratio for i,ratio in enumerate(fail_ratio)}
    
    sort_dict=sorted(dictionary,reverse=True,key=lambda x:dictionary[x])
    
    answer=[]
    for i in range(len(sort_dict)):
      answer.append(sort_dict[i]+1)
    return answer

solution(5,[2, 1, 2, 6, 2, 4, 3, 3])

