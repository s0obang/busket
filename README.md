앱 별 기능

-----ACCOUNTS-------


회원가입

로그인

로그아웃

프로필 수정


--------BUKET--------


새 버스켓 추가하기

이미 있는 버스켓 조회하기

카테고리별로 비스켓 보여주기

누적 버스켓 구하기

버스켓 리포트

버켓 고르기 팝업->버켓조회 및 선택


* 프로젝트 생성시 기본으로 생기는 폴더는 busket, 위 기능의 BUCKET에 해당하는 부분은 buket폴더 내부에서 작업 될 예정이니 혼동 X
* 앱별로  templates 폴더 생성해놓음
* static내부에 js, css, img폴더링 해놓음
* .gitkeep 파일은 빈 폴더들 깃허브에 push하기 위한 임시 파일일 뿐 지워도 상관 없음
* 파트별로 상의 후 브랜치 나눠서 작업하기


<------------------------------------------------------------------------------------->
수진
깃허브 초기세팅하기!


vs코드 열고 터미널에서 
git clone https://github.com/s0obang/busket.git

클론된 폴더 경로에서
git branch 내브랜치명
git checkout 내브랜치명
git add .
git commit -m "first commit"


장고 세팅하기

python -m venv venv
-> 옆에 venv 폴더 생성된 거 확인

.\venv\Scripts\activate 또는 source venv/scripts/activate
-> 가상환경 실행, 실행되면 앞에 괄호로 (venv) 가 떠요

pip install django
python manage.py migrate
python manage.py runserver
-> 하면 밑에 127.0.0.1:8000 이라는 url이 뜹니다. 컨트롤 + url 클릭하면 접속됩니다~

장고 실행하기
python manage.py runserver 

생성한 가상환경 폴더는 깃허브에 올리지 않는 게 좋기때문에 이름을 venv 또는 myvenv로 해주세요
