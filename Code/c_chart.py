import pandas as pd
import numpy as np

def p_chart_or_c_chart_analysis(data):
    if(len(data.columns[1:])==1):
        return 'c_chart'
    return 'p_chart'

def points_out_of_contols(x,y,lcl,ucl):
    scv={'x':[],'y':[]}
    for k in range(len(y)):
        if y[k]>ucl or y[k]<lcl:
            scv['x'].append(x[k])
            scv['y'].append(y[k])
    return scv

def check_less_than_value(arr,value):
    for i in arr:
        if(i>=value):return False
    return True

def check_greater_than_value(arr,value):
    for i in arr:
        if(i<=value):return False
    return True

def get_points_with_pattern(x,y,mean):
    scv={'x':[],'y':[]}
    for k in range(len(y)):
        if(k+7<len(y)): 
            if check_less_than_value(y[k:k+8],mean):
                scv['x']+=x[k:k+8]
                scv['y']+=y[k:k+8]
            if check_greater_than_value(y[k:k+8],mean):
                scv['x']+=x[k:k+8]
                scv['y']+=y[k:k+8]
    return scv

def apply_c_chart(data):
    '''
        scv_ool => Special control variations [out of limits]
        scv_pwp => Special control variations [patterns]
        ucl => Lpper control level
        lcl => Lower control level
    '''
    i=data[f'{data.columns[0]}'].tolist()
    c=data[f'{data.columns[1]}'].tolist()
    c_mean=np.mean(c)
    ucl=c_mean+3*np.sqrt(c_mean)
    lcl=c_mean-3*np.sqrt(c_mean)
    if lcl<0: 
        lcl=0
    print(p_chart_or_c_chart_analysis(data))
    
    scv_ool=points_out_of_contols(i,c,lcl,ucl)
    scv_pwp=get_points_with_pattern(i,c,c_mean)
    print(f'Out pf limits: {scv_ool}')
    print(f'Pattern: {scv_pwp}')
    print(f'UCL: {ucl}')
    print(f'LCL: {lcl}')
    print(f'Mean: {c_mean}')

# Goal contribution 
print(apply_c_chart(pd.DataFrame({"Season":["2017/18","2018/19","2019/20","2020/21","2021/22","2022/23","2023/24"],
                                  "Goal contribution":[64,46,35,39,51,54,48]})))