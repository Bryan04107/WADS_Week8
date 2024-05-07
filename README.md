# Todo FastAPI
| Endpoint | Method | Description | Body Request | Body Response | Error Response |
| -------- | ------ | ----------- | ------------ | ------------- | ----------- |
| /create-task/{taskID} | POST | Create a Task with a Title, Description, and ID. | `{ "title": "{title}", "description": "{description}", "completed": false }` | `{ "id": {id}, "title": "{title}", "description": "{description}", "completed": false }` | - |
| /update-task-details/{taskID} | PUT | Change and Update the Title and/or Description of specified Task by ID. | `{ "title": "{title}", "description": "{description}" }` | `{ "id": {id}, "title": "{title}", "description": "{description}", "completed": false }` | `{"error": "Task ID {taskID} Doesn't Exist"}` |
| /switch-task-state/{taskID} | PUT | Switches the completion of specified Task by ID. | - | `{ "id": {id}, "title": "{title}", "description": "{description}", "completed": false }` | `{"error": "Task ID {taskID} Doesn't Exist"}` |
| /get-all-tasks | GET | Get all available Tasks. | - | `{ "id": {id}, "title": "{title}", "description": "{description}", "completed": false }` | - |
| /get-tasks-by-title/{title} | GET | Gets all Tasks with the specified Title. | - | `{ "id": {id}, "title": "{title}", "description": "{description}", "completed": false }` | `{"error": "Task Titled '{title}' Doesn't Exist"}` |
| /get-tasks-by-state/{title} | GET | Gets all Tasks with the specified Completion. | - | `{ "id": {id}, "title": "{title}", "description": "{description}", "completed": false }` | `{"error": "Task Doesn't Exist"}` |
| /delete-task/{taskID} | DELETE | Delete a Task specified by ID. | - | `"Message" : "Task deleted successfully"` | `{"error": "Task ID {taskID} Doesn't Exist"}` |
