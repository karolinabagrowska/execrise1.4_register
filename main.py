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
def register_post(response: Response, person: Person):
    
    register_date = date.today()
    print(register_date)
    #print(type(register_date))
    new_name = []
    new_surname = []
    for x in person.name:
        if x.isalpha():
            new_name.append(x)
        else:
            continue
    
    for y in person.surname:
        if y.isalpha():
            new_surname.append(y)
        else:
            continue

    name_len = len(new_name)
    surname_len = len(new_surname)
    

    vaccination_date = register_date + timedelta(name_len) + timedelta(surname_len)

    Counter.id += 1


    dict_new = {
        "id": Counter.id,
        "name": person.name,
        "surname": person.surname,
        "register_date": register_date,
        "vaccination_date": vaccination_date
    }

    response.status_code = status.HTTP_201_CREATED

    return dict_new

        