# 목적
지도에 제로페이 가맹점 위치를 표시

# 과정  
1. 크롤링  
제로페이 홈페이지에 있는 가맹점 주소를 크롤링한다  
2. Upload  
크롤링한 데이터를 csv 나 xlsx 로 업로드 한다  

# 제약사항  
1. 시도와 시군구 코드를 알아야한다  
tryCode(sido) = '01' (서울)  
skkCode(sigungu) = '09' (노원구)  
2. 마지막 페이지 번호를 알아야 한다  
for loop 안의 5590  
![last_page](https://github.com/flapper/zeropay-crawling/blob/master/last_page.png)

# Request Url
https://www.zeropay.or.kr/intro/frncSrchList_json.do

# Form Data (Page 2)
pageIndex=2&recordCountPerPage=10&firstIndex=11&lastIndex=20&searchCondition=&tryCode=01&skkCode=09&pobsAfstrName=&bztypName=&_csrf=9677acdc-21ac-4e53-8c44-c4bf471da6f7

# Response Json
https://github.com/flapper/zeropay-crawling/blob/master/response.json

---


# Purpose
To make pins of zeropay market places on the map.

# Processes
1. Crawling
Crawl all market places of the web
2. Upload
Upload csv or xlsx on Google Map

# Constrains
1. You must know the code of sido and sigungu  
sido = tryCode  
sigungu = skkCode  
2. You must know the last page number  
In this case 5590 in for loop
