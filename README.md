# Todo with discordbOt(feat.python)

# DB - SQLITE3

## **todo.db**

```sql
CREATE TABLE "todo_list" (
	"todo_id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"pwd"	TEXT,
	"todo"	TEXT NOT NULL,
	"data_time"	TEXT
);
```

## TODO
1. discord.py 개발 필요
2. argparse 개선 필요
3. 기능 개선 필요
4. bin에 추가 하여 todo로 작동 하게 하는 방법 연구 필요
5. DB 구조 개선 필요
