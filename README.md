<div align=center>
	<img src="https://capsule-render.vercel.app/api?type=waving&color=0:66CC33,100:a82da&height=200&section=header&fontColor=FFFFFF&text=Book%20Web%20Dashboard&fontSize=60&animation=twinkling" />
</div>	

<div align=center>
	<a href="mailto:yunwltn98@gmail.com"><img src="https://img.shields.io/badge/Gmail-EA4335?style=flat&logo=Gmail&logoColor=white&link="mailto:yunwltn98@gmail.com" />
	<a href="https://coding-jisu.tistory.com/"><img src="https://img.shields.io/badge/Tistory-000000?style=flat&logo=Tistory&logoColor=white&link="https://coding-jisu.tistory.com" />
	<br>
	<br>
</div>	
	
<div align=center> 
	<h3> 📌프로젝트 명📌 <h3>
	<h4> Book Web dashboard 개발 <h4>
	<h6> 우리나라 도서관 평균 독서량을 월별, 연령대별, 지역별로 분석하여 통계하고
	<h6> 전국에 위치한 도서관의 갯수와 각 지역별 도서관 위치를 분리하여 검색할 수 있는 웹대시보드를 개발 <h6>
	<br>
	<h4>
		
![literature-3327172_960_720](https://user-images.githubusercontent.com/120348555/209486459-cd740167-eeec-4f98-b492-841446f5a6cc.jpg)


👇 웹 대시보드 주소 👇
		
<http://ec2-3-38-117-95.ap-northeast-2.compute.amazonaws.com:8501/>

</div>	
<div align=center> 
	<br>
	<br>
	<h3> 프로젝트 메뉴 구성📋 <h3>
	<h4> 메인화면 : 앱소개와 사용한 데이터프레임 
	<h4> 도서관 평균 독서량 : 우리나라 평균 독서량을 월별, 연령대별, 지역별로 분석하여 통계한 데이터를 차트로 표현
	<h4> 도서관 정보 : 전국에 위치한 도서관의 갯수와 각 지역별로 도서관 위치를 검색 가능
	<br>
	<br>
	<br>
	<br>
	<h3> 사용한 데이터📂
	<h4> 국립중앙도서관 연간 독서량(2020) <h4>
	<h4> 국립중앙도서관 도서관 정보(202211) <h4>
		
<https://www.bigdata-culture.kr/bigdata/user/data_market/agency/detail.do?id=center_nl_org>
		
</div>	
<div align=center>
	<br>
	<br>
	<h3> 사용한 컬럼📑 <h3>
	<h4> 국립중앙도서관 연간 독서량(2020)의 월, 지역, 연령, 성별, 회원수, 대출건수, 독서량 <h4>
	<h4> 국립중앙도서관 도서관 정보(202211)의 도서관명, 주소, 위도, 경도, 지역, 세부지역, 분류 <h4>	
	<br>
	<br>
	<h3> 사용한 라이브러리✏️ <h3>	
	<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=Streamlit&logoColor=white" />
	<img src="https://img.shields.io/badge/NumPy-013243?style=flat&logo=NumPy&logoColor=white" />
	<img src="https://img.shields.io/badge/pandas-150458?style=flat&logo=pandas&logoColor=white" />
	<img src="https://img.shields.io/badge/Plotly-3F4F75?style=flat&logo=Plotly&logoColor=white" />
	<h3> 사용한 Tools🔨 <h3>
	<img src="https://img.shields.io/badge/Jupyter-F37626?style=flat&logo=Jupyter&logoColor=white" />
	<img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=flat&logo=Visual Studio Code&logoColor=white" />
	<img src="https://img.shields.io/badge/GitHub-181717?style=flat&logo=GitHub&logoColor=white" />
	<br>
	<br>
</div>	

		
---


<h3>진행과정💬<h3>

<h4>▶️ Jupyter Notebook에서 데이터 분석<h4>
	
<h5>  <h5>
	
- 데이터 파일을 가져와서 사용할 컬럼만 엑세스한 후 컬럼명 변경
- Nan데이터 값이 있으면 지도를 만들 때 에러가 발생하므로 Nan값 제거
- 차트로 보여줄 데이터 분석(월, 연령, 지역별 데이터)
- 입력받은 값으로 지도를 표시할 수 있게 데이터 엑세스


<h4>▶️ Visual Studio Code에서 Streamlit 라이브러리로 작업<h4>

<h5>1. 메인 앱 화면 생성<h5>
	
- 앱 소개와 대표이미지 삽입
- 앱에 사용된 데이터를 데이터프레임으로 표시
- 데이터를 가져온 사이트url 삽입
- 사이드바에 전국 도서관 회원수를 연령대별로 차트 표시
- 사이드바에 도서관명을 입력하면 해당 도서관의 주소가 데이터프레임으로 나오는 기능 설정
		
<h5>2. 독서량 파일 작업<h5>
	
- 데이터 소개와 관련 이미지, 사용한 데이터 프레임 삽입	
- 데이터 분석한 도서관 평균 독서량을 라디오 버튼으로 월별, 연령대별 평균으로 볼 수 있게 streamlit 차트 입력
- 셀렉트박스로 각 월별 해당 월의 연령대 독서율을 볼 수 있게 plotly 차트 입력
- 전국 연령대별 회원수와 대출건수를 비교하여 볼 수 있게 plotly 차트와 데이터프레임 입력
- 라디오 버튼으로 지역별 평균독서량, 회원수, 대출건수를 한눈에 볼 수 있게 plotly차트로 표시
- 선택한 데이터의 최대값을 바로 알 수 있게 info로 해당 값을 입력
- 지역별로 세부데이터(연령, 회원수, 대출건수)를 볼 수 있게 입력받은 지역의 데이터프레임 표시
- 선택한 지역의 총 회원수를 바로 알 수 있게 info로 입력

<h5>3. 도서관정보 파일로 작업<h5>
		
- 데이터 소개와 관련 이미지, 사용한 데이터 프레임 삽입
- 전국에 위치한 도서관의 갯수를 plotly bar차트와 데이터프레임으로 표시
- 전국 도서관의 총 갯수를 파악할 수 있도록 차트 제목에 갯수 표시
- 도서관명으로 주소를 검색할 수 있는 검색기능 설정(검색시 데이터프레임으로 표시)	
- 지역과 세부지역을 선택하여 그 지역의 도서관 정보를 볼 수 있는 데이터 프레임과 지도 삽입
- 선택한 지역의 세부지역에 있는 도서관의 갯수를 나타낸 plotly bar차트 표시
- 그 지역 전체에 있는 도서관 총 갯수를 파악할 수 있도록 차트 제목에 갯수 표시

	
<h4>▶️ github를 이용해 ec2서버로 전송하여 백그라운드 실행, 자동 배포<h4>
	
<h5><h5>
		
- 새로운 repository를 생성해 Visual Studio Code에서 Streamlit 라이브러리로 작업하는 내용을 commit, pull하여 저장
- ec2 서버에 작업한 repository의 HTTP 주소를 ec2 서버에 클론(Clone)
- ec2 서버에 자동 배포하기 위한 Github Actions 셋팅(https://coding-jisu.tistory.com/139)
- PuTTY를 실행해 ec2서버에 접속해 클론한 파일이 있는 경로로 들어가 터미널에 아래 코드 실행
	
```
nohup streamlit run app.py --server.port 8501 --server.runOnSave true &
```

<h4> ▶️ AWS 포트 설정 <h4>
	
<h5>

- AWS사이트에 접속해 ec2보안그룹 인바운드규칙 설정에서 해당 사이트 포트를 사용 가능하게 지정
	
---


![1](https://user-images.githubusercontent.com/120348555/209073474-22e7b49e-749e-47a7-9886-89b6f8ebf59b.PNG)
![2](https://user-images.githubusercontent.com/120348555/209073481-cfffbc13-052f-45ff-ade9-062c5d8d3ff5.PNG)
![3](https://user-images.githubusercontent.com/120348555/209073483-fc529b3c-1597-4eb0-91af-71637132dd36.PNG)
![4](https://user-images.githubusercontent.com/120348555/209073486-99f3482d-cb61-4016-aa13-bfaaf682990f.PNG)
![5](https://user-images.githubusercontent.com/120348555/209073489-ed5faeaa-df56-46c0-bb71-918361d0f683.PNG)

<div align=center>
	<img src="https://capsule-render.vercel.app/api?type=waving&color=0:66CC33,100:a82da&height=100&section=footer&text=Thank%20you&fontSize=50&animation=twinkling" />
</div>	
