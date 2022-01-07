from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel
from typing import Optional
import json

app = FastAPI()


class Person(BaseModel):
    id: Optional[int] = None
    name: str
    age: int
    gender: str

def write_json(people):
    with open('people.json','w') as f:
        json.dump(people, f)


def read_json():
    with open('people.json','r') as f:
        people = json.load(f)
    return people

@app.get('/')
def welcome():
    return {'msg': 'Welcome to the people\'s API.'}

@app.get('/people/{p_id}', status_code=200)
def read_person(p_id: int):
    people = read_json()
    person = [p for p in people if p['id'] == p_id]
    return person if len(person)>0 else {}


@app.get('/search', status_code=200)
def search_person(
        age: Optional[int] = Query(None, title="Age", description="The age to filter for"),
        name: Optional[str] = Query(None, title="Name", description="The name to filter  for")):
    people = read_json()
    people_by_age = [p for p in people if p['age'] == age]
    print(f'by age: {people_by_age}')
    print(f'age: {age}')
    print(f'name: {name}')
    if name is None:
        if age is None:
            return people
        else:
            return people_by_age

    else:
        people_by_name = [p for p in people if name.lower() in p['name'].lower()]
        print(f'by name: {people_by_name}')
        if age is None:
            return people_by_name
        else:
            combined = [p for p in people_by_age if p in people_by_name]
            return combined


@app.post('/people', status_code=201)
def add_person(person: Person):
    people = read_json()
    p_id = max([p['id'] for p in people]) + 1
    new_person = {
        "id": p_id,
        "name": person.name,
        "age": person.age,
        "gender": person.gender
    }

    people.append(new_person)
    write_json(people)

    return new_person

@app.put('/people', status_code=204)
def update_person(person: Person):
    new_person = {
        "id": person.id,
        "name": person.name,
        "age": person.age,
        "gender": person.gender
    }

    people = read_json()
    person_list = [p for p in people if p['id'] == person.id]

    if len(person_list) > 0:
        people.remove(person_list[0])
        people.append(new_person)
        write_json(people=people)
        return new_person
    else:
        return HTTPException(status_code=404, detail=f"Person with id {person.id} doesn't not exist!")

@app.delete('/people/{p_id}', status_code=204)
def delete_person(p_id: int):
    people = read_json()
    person_list = [p for p in people if p['id'] == p_id]

    if len(person_list)>0:
        people.remove(person_list[0])
        write_json(people=people)
    else:
        raise HTTPException(status_code=404, detail=f"Person with id {person.id} doesn't not exist!")


