1. Получить все заметки:
powershell
Invoke-RestMethod -Uri "http://localhost:5000/api/notes" -Method Get
2. Получить конкретную заметку:
powershell
Invoke-RestMethod -Uri "http://localhost:5000/api/get/0" -Method Get
3. Добавить заметку:
powershell
Invoke-RestMethod -Uri "http://localhost:5000/api/task" -Method Post -ContentType "application/json" -Body '{"title":"New Note"}'
4. Изменить заметку:
powershell
Invoke-RestMethod -Uri "http://localhost:5000/api/put/0" -Method Put -ContentType "application/json" -Body '{"topic":"Updated Topic"}'
5. Удалить заметку:
powershell
Invoke-RestMethod -Uri "http://localhost:5000/api/delete/1" -Method Delete