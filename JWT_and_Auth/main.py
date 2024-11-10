from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Mock database of crew members with nested equipment data
crew = [
    {
        "id": 1,
        "name": "Cosmo", "role": "Captain", "experience": 10,
        "equipment": [
            {"name": "Helmet", "status": "Good"},
            {"name": "Suit", "status": "Needs Repair"}
        ]
    },
    {
        "id": 2,
        "name": "Alice", "role": "Engineer", "experience": 8,
        "equipment": [
            {"name": "Toolkit", "status": "Good"}
        ]
    },
]


# Define a Pydantic model for equipment
class Equipment(BaseModel):
    name: str
    status: str


# Define a Pydantic model for the crew member, which includes a list of equipment
class CrewMember(BaseModel):
    name: str
    role: str
    experience: int
    equipment: list[Equipment]


# Endpoint to read a crew member details by name using GET method, including nested equipment data
@app.get("/crew/{id}", response_model=CrewMember)
async def read_crew_member(id: int):
    for member in crew:
        if member["id"] == id:
            return member
    return {"message": "Crew member not found"}


# Endpoint to add a new crew member with nested equipment using POST method
@app.post("/crew/")
async def add_crew_member(member: CrewMember):
    member_id = max(c["id"] for c in crew) + 1 if crew else 1
    new_member = {"id": member_id, **member.dict()}
    crew.append(new_member)
    return {"message": "Crew member added successfully", "member": new_member}