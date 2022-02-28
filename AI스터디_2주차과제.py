#Q3

import csv #csv 파일을 읽어들이기 위해 라이브러리를 import

def read_file(file_path):
    file_path = "./data-01-test-score.csv" #오픈할 파일의 경로 설정 
    file = open(file_path,'r') #open 함수를 사용해서 오픈할 파일 오브젝트를 생성하기 위해 파일의 경로를 인자로 건넨다
    csv_r= csv.reader(file) #open을 통해 생성한 파일 오브젝트(file)을 csv.reader라는 함수로 읽어들인 값을 csv_r에 저장한다
    for line in csv_r: #for문을 통해 저장된 값을 반복해서 돌며 한개씩 출력해준다.
        print(line)
    f.close() #열었던 파일을 닫아준다.

print(read_file(read_csv))


#Q4
import csv

class ReadCSV():
    def __init__(self, file_path):
        self.file_path = file_path
    
    def read_file(self):
        file_path = "./data-01-test-score.csv" #오픈할 파일의 경로 설정 
        file = open(file_path,'r') #open 함수를 사용해서 오픈할 파일 오브젝트를 생성하기 위해 파일의 경로를 인자로 건넨다
        csv_r= csv.reader(file) #open을 통해 생성한 파일 오브젝트(file)을 csv.reader라는 함수로 읽어들인 값을 csv_r에 저장한다
        for line in csv_r: #for문을 통해 저장된 값을 반복해서 돌며 한개씩 출력해준다.
            print(line)
        f.close() #열었던 파일을 닫아준다.
       
    
    def merge_list(self):
        file_path = "./data-01-test-score.csv" #오픈할 파일의 경로 설정 
        file = open(file_path,'r') #open 함수를 사용해서 오픈할 파일 오브젝트를 생성하기 위해 파일의 경로를 인자로 건넨다
        csv_r= csv.reader(file) #open을 통해 생성한 파일 오브젝트(file)을 csv.reader라는 함수로 읽어들인 값을 csv_r에 저장한다
        merge_list = [] #merge한 리스트를 저장할 공간 생성
        for line in csv_r: #for문을 통해 저장된 값을 반복해서 돌며 한개씩 출력해준다.
            intList = [int(x) for x in line] #str으로 되어있는 리스트의 요소를 int로 변경
            sum1 = sum(intList) #int로 변경한 리스트의 요소를 sum 함수를 통해 합산해준다
            merge_list.append(sum1) #합산한 값을 리스트에 저장해준다
        
        print(merge_list) #merge된 리스트 출력하기
        f.close() #파일 사용 종료 후 닫아주기
    
file_path = "./data-01-test-score.csv"
read_csv = ReadCSV(file_path) 
print(read_csv.read_file())
print(read_csv.merge_list())


#Q5

import csv

class ReadCSV():
    def __init__(self, file_path):
        self.file_path = file_path
    
    def read_file(self):
        file_path = "./data-01-test-score.csv" #오픈할 파일의 경로 설정 
        file = open(file_path,'r') #open 함수를 사용해서 오픈할 파일 오브젝트를 생성하기 위해 파일의 경로를 인자로 건넨다
        csv_r= csv.reader(file) #open을 통해 생성한 파일 오브젝트(file)을 csv.reader라는 함수로 읽어들인 값을 csv_r에 저장한다
        for line in csv_r: #for문을 통해 저장된 값을 반복해서 돌며 한개씩 출력해준다.
            print(line)
        f.close() #열었던 파일을 닫아준
        
    def merge_list(self): #평균값을 구하는 함수 만들기
        file_path = "./data-01-test-score.csv" #오픈할 파일의 경로 설정 
        file = open(file_path,'r') #open 함수를 사용해서 오픈할 파일 오브젝트를 생성하기 위해 파일의 경로를 인자로 건넨다
        csv_r= csv.reader(file) #open을 통해 생성한 파일 오브젝트(file)을 csv.reader라는 함수로 읽어들인 값을 csv_r에 저장한다
        merge_list = [] #merge한 리스트를 저장할 공간 생성
        for line in csv_r: #for문을 통해 저장된 값을 반복해서 돌며 한개씩 출력해준다.
            intList = [int(x) for x in line] #str으로 되어있는 리스트의 요소를 int로 변경
            sum1 = sum(intList) #int로 변경한 리스트의 요소를 sum 함수를 통해 합산해준다
            avg1 = sum1/4
            merge_list.append(avg1) #평균값을 리스트에 저장해준다
            merge_list.sort() #오름차순 정렬
        
        print(merge_list) #merge된 리스트 출력하기
        f.close() #파일 사용 종료 후 닫아주기
    
file_path = "./data-01-test-score.csv"
read_csv = ReadCSV(file_path) 
print(read_csv.merge_list())
