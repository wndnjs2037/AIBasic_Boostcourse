import pandas as pd

#df1 생성
df1 = pd.DataFrame({"Name":["cherry","mango","potato","onion"],
      "Type":["Fruit","Fruit","Vegetable","Vegetable"],
      "Price":[100,110,60,80]})

#df2 생성
df2 = pd.DataFrame({"Name":["pepper","carrot","banana","kiwi"],
      "Type":["Vegetable","Vegetable","Fruit","Fruit"],
      "Price":[50,70,90,120]})

#df1과 df2를 concat을 이용해 결합한 데이터프레임 df3 생성
df3 = pd.concat([df1,df2])

#Fruit와 Vegetavle의 type에 따라 정렬하고, 가격을 내림차순으로 정리
df_Fruit = df3[df3['Type'].str.contains('Fruit')] #Fruit이 포함된 데이터만 추출
df_Fruit = df_Fruit.sort_values('Price', ascending=False) #Price를 기준으로 내림차순 정렬
df_Veg = df3[df3['Type'].str.contains('Vegetable')] #Vegetable이 포함된 데이터만 추출
df_Veg = df_Veg.sort_values('Price', ascending=False) #Price를 기준으로 내림차순 정렬

#Fruit와 Vegetable 상위 2개의 가격의 합 출력
print("Sum of Top 2 Fruit Price :", df_Fruit.iloc[0]['Price'] + df_Fruit.iloc[1]['Price']) #0번째 값과 1번째 값 추출
print("Sum of Top 2 Vegetable Price :", df_Veg.iloc[0]['Price'] + df_Veg.iloc[1]['Price']) #0번째 값과 1번째 값 추출
