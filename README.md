---
title: README
---

## Necessary codes for SQL

```sql

SELECT
	chapter_id,
	voc_id,
	title,
	spelling,
	`order`
FROM
	VOC_TB
	INNER JOIN (
	SELECT
		title,
		voc_origin_id voc_id,
		chapter_origin_id chapter_id,
		`order`
	FROM
		BK_VOC_TB V
	INNER JOIN BK_CHAPTER_TB C ON V.chapter_origin_id = C.id 
	AND V.book_origin_id IN ( SELECT origin_id FROM BK_TB WHERE name = '2024恋练有词考研英语词汇' )) AS tmp ON VOC_TB.origin_id = tmp.voc_id

```
