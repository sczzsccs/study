# 프로젝트 폴더 초기화
git init

# 원격 저장소 설
git remote add origin https://github.com/sczzsccs/study.git

# 원격 저장소 연결 확인
git remote -v

# 현재 디렉토리의 모든 파일을 add
git add .

# 커밋 메시지 함께 작성
git commit -m "Message 내용" 

# 커밋 변경사항 추적
git log

# Master -> Main 이름 변경
git branch -M main 

# 원격 저장소로 Push
git push -u origin main
