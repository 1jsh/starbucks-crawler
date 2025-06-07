# 스타벅스 크롤러
언제부터인가 소상공인시장진흥공단의 상가(상권)정보에서 프렌차이즈 직영점이 보이지 않습니다. 따라서 직접 스타벅스 홈페이지에서 웹크롤링을 통해 점포의 위치를 얻어야 합니다.

이 코드는 `selenium`, `BeautifulSoup4`, `pandas` 모듈을 활용하고 있어 해당 모듈에 대한 설치가 필요합니다.

```{bash}
pip install selenium
pip install bs4
pip install pandas
```

코드 작성에는 [access.log](https://velog.io/@song-_-/python-%ED%81%AC%EB%A1%A4%EB%A7%81-%EC%8A%A4%ED%83%80%EB%B2%85%EC%8A%A4-%EB%A7%A4%EC%9E%A5-%EC%A0%95%EB%B3%B4-%EA%B0%80%EC%A0%B8%EC%98%A4%EA%B8%B0)의 Song님의 코드를 활용하였습니다.

세종시의 경우 하위 행정구역이 없어 하위 메뉴에 '전체' 버튼이 없습니다. 이 부분을 if문으로 처리하였습니다.

✅ 2025년 6월 7일 기준 스타벅스 홈페이지에서 정상작동함을 확인하였습니다. 이 코드를 활용하여 얻은 해당 날짜 기준의 점포 데이터도 동봉합니다.
