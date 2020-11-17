# 일 잘하는 직장인을 위한 엑셀 자동화 with 파이썬

- 책 소개: https://wikibook.co.kr/pyexcel/

![book_cover_image](/book_cover_image.png)

**아래의 방법을 이용해 소스코드와 데이터를 내려받고 활용하세요. 그 밖의 자세한 사용법은 책의 『책 사용 설명서』 부분을 참고하세요.**

1. 압축 파일(zip 파일) 다운로드
    - 아래 URL을 통해 압축 파일을 다운로드합니다.
        - https://github.com/wikibook/pyexcel/archive/master.zip

2. 압축 풀기
    - 다운로드한 압축 파일을 임의의 폴더에 풉니다.
    - 압축을 풀면 `data`, `figures`, `modules`, `notebooks` 폴더가 있습니다.

3. 폴더 복사
    - 윈도우 탐색기로 작업 폴더인 `C:\myPyExcel`을 생성합니다.
    - 압축을 푼 폴더에서 `data`, `figures`, `modules`, `notebooks` 폴더를 모두 작업 폴더(여기서는 `C:\myPyExcel`)에 복사합니다.

4. 작업 폴더 구조
    - `data`: 이 책에서 사용하는 데이터 파일이 있는 폴더
    - `modules`: 이 책에서 사용하는 모듈의 예제를 위한 폴더
    - `figures`: 이 책에서 사용하는 이미지 파일이 담긴  폴더
    - `notebooks`: 이 책의 예제 코드가 담긴 주피터 노트북 파일(`\*.ipynb`)이 있는 폴더
        - 각 장별로 있는 노트북의 코드 셀 위에는 `[2장: 50페이지]`처럼 예제 코드가 있는 책의 장과 페이지가 표시돼 있습니다.

5. 노트북 실행 방법
    - 주피터 노트북이 실행되지 않은 상태라면 아나콘다 메뉴에서 `[Anaconda Prompt]`를 클릭해 아나콘다 프롬프트를 실행합니다.
    - 아나콘다 프롬프트에 명령어를 입력해서 작업 폴더로 이동합니다(만약 작업 폴더가 `C:\myPyExcel`이라면 `cd C:\myPyExcel`을 입력).
    - 아나콘다 프롬프트에 `jupyter notebook`을 입력합니다.
    - 주피터 노트북이 실행되면 브라우저의 홈 화면(Home page)에 보이는 `notebooks` 폴더를 클릭한 후 원하는 노트북 파일(`\*.ipynb`)을 클릭합니다.
    - 예제 코드를 실행하려면 주피터 노트북의 `[셀 실행]` 아이콘을 클릭하거나 키보드의 `Shift + Enter` 키를 입력합니다. 
