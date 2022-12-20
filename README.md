<div align=center>
	<img src="https://capsule-render.vercel.app/api?type=waving&color=auto&height=200&section=header&text=Book_Web_Dashboard&fontSize=60" />
</div>	

<div align=center> 
	<h3> 📌프로젝트 명📌 <h3>
	<h4> Book Web dashboard 개발 <h4>
	<h6> 우리나라 도서관 평균 독서량을 월별, 연령대별, 지역별로 분석하여 통계하고
	<h6> 전국에 위치한 도서관의 갯수와 각 지역별 도서관 위치를 분리하여 검색할 수 있는 웹대시보드를 개발 <h6>
	<br>
	<img src= 'https://user-images.githubusercontent.com/120348555/207815612-b6d738ba-c375-4798-8e60-934770e686d5.gif'>

👉웹대시보드 주소 <http://ec2-3-38-117-95.ap-northeast-2.compute.amazonaws.com:8501/>
	<br>	
</div>	
<div align=center> 
	<br>
	<br>
	<h3> 프로젝트 메뉴 구성📋 <h3>
	<h4> 도서관 평균 독서율 : 우리나라 평균 독서량을 월별, 연령대별, 지역별로 분석하여 통계한 데이터를 차트로 표현
	<h4> 도서관 정보 : 전국에 위치한 도서관의 갯수와 각 지역별로 도서관 위치를 검색 가능
	<br>
	<br>
	<br>
	<br>
	<h3> 사용한 데이터📂 <h3>
	<h4> 국립중앙도서관 연간 독서량(2020) <h4>
	<h4> 국립중앙도서관 도서관 정보(202211) <h4>

<https://www.bigdata-culture.kr/bigdata/user/data_market/detail.do?id=7461f23e-8958-417b-be03-7ede86ab760b>
</div>	
<div align=center>
	<br>
	<br>
	<h3> 사용한 컬럼📑 <h3>
	<h4> 국립중앙도서관 연간 독서량(2020)의 월, 지역, 연령, 성벼르 회원수, 대출건수, 독서량 <h4>
	<h4> 국립중앙도서관 도서관 정보(202211)의 도서관명, 주소, 위도, 경도, 지역, 세부지역, 분류 <h4>	
	<br>
	<br>
	<h3> 사용한 라이브러리✏️ <h3>	
	<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=Streamlit&logoColor=white" />
	<img src="https://img.shields.io/badge/NumPy-013243?style=flat&logo=NumPy&logoColor=white" />
	<img src="https://img.shields.io/badge/pandas-150458?style=flat&logo=pandas&logoColor=white" />
	<img src="https://img.shields.io/badge/Plotly-3F4F75?style=flat&logo=Plotly&logoColor=white" />
	<br>
	<br>
</div>	

		
---


##진행과정

Jupyter Notebook에서 데이터 분석
1. 데이터파일을 가져와서 사용할 컬럼만 엑세스한 후 컬럼명 변경
2. Nan데이터 값이 있으면 지도를 만들 때 에러가 발생하므로 Nan값 제거
3. 차트로 보여줄 데이터 분석(월, 연령, 지역별 데이터)
4. 입력받은 값으로 지도를 표시할 수 있게 데이터 엑세스

Visual Studio Code에서 Streamlit 라이브러리로 작업

1. 메인 앱 화면 생성
		
2. 파일을 새로 만들어 분석한 독서량 파일 작업
		
-데이터 분석한 도서관 평균 독서율을 월별, 연령대별 평균으로 streamlit차트로 표시
		
-각 월별로 해당 월의 연령대 독서율을 볼 수 있게 plotly차트로 표시
		
-전국 연령대별 회원수와 대출건수를 비교하여 볼 수 있게 plotly차트로 표시
		
-지역별 평균독서량, 회원수, 대출건수를 한번에 볼 수 있게 plotly차트로 표시
		
-지역별로 세부데이터(연령, 회원수, 대출건수)를 볼 수 있게 입력받은 지역의 데이터프레임 표시

3. 파일을 새로 만들어 분석한 도서관정보 파일로 작업
		
-전국에 위치한 도서관의 갯수를 plotly bar차트와 데이터프레임으로 표시
		
-도서관명으로 검색할 수 있는 검색기능 설정(검색시 데이터프레임으로 표시)
		
-지역과 세부지역을 선택하여 그 지역의 도서관 정보를 볼 수 있는 지도와
		
-선택한 지역에 있는 도서관의 총 갯수를 나타낸 plotly bar차트 표시

---
		
![1](https://user-images.githubusercontent.com/120348555/208594875-455afcf5-4d5c-43d1-98f7-456af492d932.PNG)
![2](https://user-images.githubusercontent.com/120348555/208594950-50b6cb16-e6ad-462f-9f06-9fd2fa1ba4b0.PNG)
