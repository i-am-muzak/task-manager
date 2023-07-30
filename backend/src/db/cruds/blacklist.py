from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from db.models.blacklist import Blacklist

# Logging
from lib.logger import logger


def put(db: Session, data: dict, record: Blacklist = None) -> Blacklist:
    try:
        record = record if record else Blacklist()

        for var, value in data.items():
            setattr(record, var, value)

        db.add(record)
        db.commit()
        db.refresh(record)

        return record
    except Exception as error:
        logger.exception(str(error), stack_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An error occured while creating a new user.")