print("_________________________________________________________________________________________________________________________________________________________")
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

origins = [
    "http://localhost:5173",
    "localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Task(BaseModel):
    id: int
    title: str
    description: str
    complete: bool = False

class UpdateTask(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

Tasks = {}
TotalTask = 0



@app.post("/create-task/{taskID}")
def createTask(task: Task):

    global TotalTask
    TotalTask += 1
    Tasks[TotalTask] = task
    Tasks[TotalTask].id = TotalTask
    return Tasks[TotalTask]



@app.put("/update-task-details/{taskID}")
def updateTaskDetails(taskID: int, task: UpdateTask):

    if taskID in Tasks:
        if task.title != None:
            Tasks[taskID].title = task.title
        if task.description != None:
            Tasks[taskID].description = task.description
        return Tasks[taskID]
    else:
        raise HTTPException(status_code=404, detail=f"Task ID {taskID} Doesn't Exist")



@app.put("/switch-task-state/{taskID}")
def switchTaskState(taskID: int):

    if taskID in Tasks:
        Tasks[taskID].complete = not Tasks[taskID].complete
        return Tasks[taskID]
    else:
        raise HTTPException(status_code=404, detail=f"Task ID {taskID} Doesn't Exist")



@app.get("/get-all-tasks")
def getAll():
    return list(Tasks.values())



@app.get("/get-tasks-by-title/{title}")
def getTitle(title: str):

    TempTask = []
    for taskID in Tasks:
        if Tasks[taskID].title == title:
            TempTask.append(Tasks[taskID])
    if TempTask:
        return TempTask
    else:
        raise HTTPException(status_code=404, detail=f"Task Titled '{title}' Doesn't Exist")



@app.get("/get-tasks-by-state/{title}")
def getState(complete: bool):

    TempTask = []
    for taskID in Tasks:
        if Tasks[taskID].complete == complete:
            TempTask.append(Tasks[taskID])
    if TempTask:
        return TempTask
    else:
        raise HTTPException(status_code=404, detail=f"Task Doesn't Exist")



@app.delete("/delete-task/{taskID}")
def deleteTask(taskID: int):
    if taskID in Tasks:    
        del Tasks[taskID]
        return {"Message" : "Task deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail=f"Task ID {taskID} Doesn't Exist")
    
