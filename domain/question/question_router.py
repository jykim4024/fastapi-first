from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

# from database.database import SessionLocal
from database.database import get_db
from domain.question import question_schema, question_crud

from starlette import status

router = APIRouter(
    prefix="/api/question",
)

@router.get("/list", response_model=question_schema.QuestionList)
def question_list(db:Session = Depends(get_db),
                  page: int = 0, size: int = 10):
    # FastAPI의 Depends는 매재 변수로 전달 받은 함수를 실행시킨 결과를 리턴한다. 따라서 db:Session = Depends(get_db) 의 db객체에는
    # get_db 제너레이터에 의해 생성된 세션 객체가 주입된다. 이 때 get_db 함수에 자동으로 contextmanager가 적용되기 때문에
    # (Depends에서 contextmanager를 적용하게끔 설계되어 있음) database.py 의 get_db 함수에 contextlib.contextmanager 어노테이션을
    # 제거해야 함.

    total, _question_list = question_crud.get_question_list(
        db, skip=page*size, limit=size)
    return {
        'total': total,
        'question_list': _question_list
    }

    # _question_list = question_crud.get_question_list(db)
    # return _question_list
    
@router.get("/detail/{question_id}",response_model=question_schema.Question)
def question_detail(question_id: int, db: Session = Depends(get_db)):
    question = question_crud.get_question(db, question_id=question_id)
    return question

@router.post("/create",status_code=status.HTTP_204_NO_CONTENT)
def question_create(_question_create: question_schema.QuestionCreate,
                    db:Session=Depends(get_db)):
    question_crud.create_question(db=db, question_create=_question_create)