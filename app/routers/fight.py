from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter,  Depends, HTTPException
from app.utils.utils import get_db
from app import actions, schemas


router = APIRouter()

@router.get("/{trainer_id}/{trainer2_id}", response_model=schemas.BattleResult)
def fight_trainers(trainer_id: int, trainer2_id: int, database: Session = Depends(get_db)):
    """
        Make a fight between 2 trainers
    """
    db_trainer = actions.get_trainer(database, trainer_id=trainer_id)
    db_trainer2 = actions.get_trainer(database, trainer_id=trainer2_id)
    
    if db_trainer is None or db_trainer2 is None:
        raise HTTPException(status_code=404, detail="One of trainer is not found")
    return actions.fight_pokemon(database=database, trainer=db_trainer, trainer2=db_trainer2)

