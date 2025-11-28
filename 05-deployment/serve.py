import pickle
import numpy as np

from fastapi import FastAPI
from pydantic import BaseModel

def predict_single(customer, dv, model):
    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[:, 1]
    return y_pred[0]


with open('pipeline_v1.bin', 'rb') as f_in:
    dv, model = pickle.load(f_in)


app = FastAPI(title='churn')


class Customer(BaseModel):
    class Config:
        extra = "allow"


@app.post('/predict')
def predict(customer: Customer):
    customer_dict = customer.dict()
    prediction = predict_single(customer_dict, dv, model)
    
    result = {
        'score': float(prediction)
    }

    return result


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=9696)