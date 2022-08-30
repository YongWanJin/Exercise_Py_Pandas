
# Q1. pandas 버전 확인

import pandas as pd
print(pd.__version__)


# Q2. 다음의 list, ndarray, dict를  pandas의 Series 객체로 생성하시오
import numpy as np
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))

mylist_sr = pd.Series(mylist)
myarr_sr = pd.Series(myarr)
mydict_sr = pd.Series(mydict)

print(mylist_sr, type(mylist_sr))
print(myarr_sr, type(myarr_sr))
print(mydict_sr, type(mydict_sr))


# Q3. 시리즈의 인덱스를 데이터 프레임의 열로 변환하시오
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))
ser = pd.Series(mydict)

mylist_df = pd.DataFrame([mylist])
myarr_df = pd.DataFrame([myarr])
mydict_df = pd.DataFrame([mydict])
ser_df = pd.DataFrame([ser])

print(mylist_df, type(mylist_df))
print(myarr_df, type(myarr_df))
print(mydict_df, type(mydict_df))
print(ser_df, type(ser_df))


# Q4. ser1과 ser2를 결합하여 데이터 프레임을 생성하시오
import numpy as np
ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))

ser1_df, ser2_df = pd.DataFrame(ser1), pd.DataFrame(ser2)
result = pd.merge(ser1_df, ser2_df,
                  left_index=True, right_index=True)
print(result)


# Q5. Series에 '알파벳'이라고 부르는 이름을 지정하시오
ser = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))

result = pd.DataFrame({"알파벳":ser})
print(result, result.columns)


# **Q6. Series ser1에서 Series ser2에 있는 항목을 제거하시오
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])

result = set.difference(set(ser1),  set(ser2))

print(result)
# => Series타입과 set타입이 서로 호환된다는 사실을 알고,
# set 타입으로 변환시켜서 파이썬 기본 내장함수를 이용하였다.
# 판다스에서는 sql의 join이 아니라 집합연산만을 위한 메서드가 없는걸까??


# **Q7. ser1과 ser2에서 공통적이지 않은 모든 항목을 가져오시오 
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])

result = set.symmetric_difference(set(ser1), set(ser2))

print(result)
# => 6번과 마찬가지. 
# 판다스에서는 sql의 join이 아니라 집합연산만을 위한 메서드가 없는걸까??


# Q8. 숫자 계열의 최소값, 25번째 백분위수, 중앙값,
# 75번째 및 최대값을 출력하시오
ser = pd.Series(np.random.normal(10, 5, 25))

result = pd.DataFrame(ser.describe()).iloc[3:]

for i in result[0] :
    print(round(i, 2)) # 숫자만 출력
    
    
# Q9. 시리즈의 고유한 항목의 수를 출력하시오    
ser = pd.Series(np.take(list('abcdefgh'),
                        np.random.randint(8, size=30)))

result = ser.drop_duplicates()

print(result.value_counts())


# Q10. 가장 빈번한 상위 2 개 값 만 그대로 유지하고
# 다른 모든 값을 '기타'로 대체하라
import numpy as np
import pandas as pd
np.random.RandomState(100)
ser = pd.Series(np.random.randint(1, 5, [12]))

ser_df = pd.DataFrame(ser)
ser_cnt = pd.DataFrame(ser.value_counts())

print(ser_df)
# ==> 안된다. loc 안에 조건문 넣는것을 모르겠다.
# TypeError: 'int' object is not iterable






