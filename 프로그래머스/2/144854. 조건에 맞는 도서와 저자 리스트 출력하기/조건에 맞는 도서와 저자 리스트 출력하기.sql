-- 코드를 입력하세요
SELECT B.BOOK_ID, A.AUTHOR_NAME, DATE_FORMAT(B.PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE
FROM BOOK B, AUTHOR A
WHERE B.CATEGORY = '경제' AND B.AUTHOR_ID = A.AUTHOR_ID
ORDER BY B.PUBLISHED_DATE