from fastapi import FastAPI
from fastapi import FastAPI, Response, status
from fastapi import FastAPI, HTTPException
from datetime import date, datetime, time, timedelta
from pydantic import BaseModel

class Person(BaseModel):
    name: str
    surname: str

class Counter():
    id = 0


app = FastAPI()


@app.post("/register")
def register_post(person: Person):
    
    register_date = date.today()
    print(register_date)
    #print(type(register_date))
    name_len = len(person.name)
    surname_len = len(person.surname)
    
    vaccination_date = register_date + timedelta(name_len) + timedelta(surname_len)

    Counter.id += 1


    dict_new = {
        "id": Counter.id,
        "name": person.name,
        "surname": person.surname,
        "register_date": register_date,
        "vaccination_date": vaccination_date
    }


    return dict_new

        