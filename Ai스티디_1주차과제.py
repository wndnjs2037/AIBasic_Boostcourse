score = [(100, 100), (95, 90), (55,60), (75,80), (70,70)] #각 학생들의 점수(5명)
def get_avg(score): #평균을 구하기 위한 함수 정의
	for i in range (len(score)): #리스트의 길이만큼 반복문 실행
		sum_score = sum(score[i]) #i번째 튜플 안의 점수를 더한 값 계산
		avg_score = sum_score/2 #*더한 값을 점수 개수만큼 나눠서 평균 값 계산
		print(f"%d 번, 평균 : {avg_score:.1f}" % (i+1)) #학생의 점수 출력 (소숫점 조절을 위해 f-string 사용)
		
get_avg(score) #구현한 함수 실행
