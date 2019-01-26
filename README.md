# 사용법

※ 기본적으로 파이썬이 설치되어 있어야 합니다.

1. 문제에서 요구하는 입력 데이터의 확인
  ex) int_array, int_matrix, str_array, trees, graphs

2. 입력 데이터에 적합한 파일(testcaseMaker.py) 선택

3. 예시 코드(exCode.py) 작성(exCode.py는 반드시 testcaseMaker.py와 같은 폴더에 있어야 함)
  ex) 정답 코드가 아래와 같을 때,
    
    n=int(input())
    sum=0
    l=list(input().split())
    for i in l:
        sum+=int(i)
    print(sum)
        
    아래와 같이 함수 형태로 변경한 후에 저장(파일명 : exCode.py)
    
    def F(n,s):
        sum=0
        l=list(s.split())
        for i in l:
            sum+=int(i)
        return(sum)
    
4. testcaseFiles에 있는 .in .out 파일을 적당한 곳에 저장(가급적 경로가 짧은 곳에 저장)

5. testcaseMaker.py 실행 

6. 문제의 조건에 맞는 수치나 문자를 입력하고, .in .out 파일이 있는 곳의 경로를 입력

7. 입력 데이터 생성 -> 출력 데이터 생성

8. .in .out 파일 확인 후 이상 없으면, 총 100개의 파일을 압축

9. 압축 파일을 OnlineJudge 사이트에 업로드
