from pydantic import BaseModel, Field

class UserPageView(BaseModel):
    id: int
    title: str
    created_at: int
    
    class Config:
        from_attributes = True

class UserPageRequestData(BaseModel):
    title: str = Field(..., max_length=30)
    project_id: int
