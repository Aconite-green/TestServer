from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class TMList(BaseModel):
    start_station: str
    end_station: str
    desired_departure: str
    current_members: int

class TeamInfo(BaseModel):
    start_station: str
    end_station: str
    start_time: str
    current_population: int
    member_info: List[int]
    comments: Optional[str]

class Rating(BaseModel):
    team_no: int
    rating: float

@app.get(
    "/tm_list/{station}",
    response_model=List[TMList],
)
async def get_tm_list(station: str):
    return [{"start_station": "A", "end_station": "B", "desired_departure": "12:00", "current_members": 4}]

@app.get("/team/{team_no}", response_model=TeamInfo)
async def get_team_info(team_no: int):
    return {
        "start_station": "A", 
        "end_station": "B", 
        "start_time": "12:00", 
        "current_population": 4, 
        "member_info": [1, 2, 3], 
        "comments": "Hello"
    }

@app.delete("/team/{team_no}")
async def delete_team(team_no: int):
    return {"message": f"Team {team_no} deleted successfully"}

@app.put("/team/", response_model=TeamInfo)
async def put_team_info(team: TeamInfo):
    return team

@app.post("/rating/")
async def post_rating(rating: Rating):
    return {"message": "Post request received", "rating": rating}

# Kakao 인증 부분도 단순화
@app.get("/kakao")
def get_kakao_token(code: Optional[str] = None):
    # 실제 Kakao API를 호출하는 대신에 테스트용 응답을 반환
    return {"access_token": "fake_token", "user_info": {"id": 12345, "name": "John Doe"}}
