from pydantic import BaseModel, Field

class UserProjectView(BaseModel):
    id: int
    title: str
    created_at: int
    
    class Config:
        from_attributes = True

class UserProjectRequestData(BaseModel):
    title: str = Field(..., max_length=30)
