from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/fullname")
def get_fullname(firstname: str, lastname: str):
    if not firstname or not lastname:
        raise HTTPException(status_code=400,
                            detail="Имя и фамилия не могут быть пустыми")

    fullname = firstname + " " + lastname
    return {
        "firstname": firstname,
        "lastname": lastname,
        "fullname": fullname
    }