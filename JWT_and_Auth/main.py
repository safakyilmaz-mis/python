from fastapi import FastAPI
from pydantic import BaseModel, model_validator

app = FastAPI()

# Mock database of crew members
crew = [
    {"id": 1, "name": "Cosmo", "role": "Captain", "experience": 10},
    {"id": 2, "name": "Alice", "role": "Engineer", "experience": 8},
    {"id": 3, "name": "Bob", "role": "Scientist", "experience": 5}
]


# Defining a Pydantic model with custom validation
class CrewMember(BaseModel):
    name: str
    role: str
    experience: int

    # Validating if experience for captain is at least 5
    @model_validator(mode="after")
    def validate_experience_for_captain(cls, values):
        if values.role == 'Captain' and values.experience <= 5:
            raise ValueError('Captain must have more than 5 years of experience')
        return values


# POST endpoint receiving CrewMember model
@app.post("/crew/")
async def add_crew_member(member: CrewMember):
    return {"message": f"{member.name} added as {member.role} with {member.experience} years of experience"}


# PUT endpoint receiving id and CrewMember model
@app.put("/crew/{crew_id}")
async def update_crew_member(crew_id: int, member: CrewMember):
    return {"message": f"{member.name} updated to {member.role} with {member.experience} years of experience"}