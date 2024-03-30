from fastapi import FastAPI, HTTPException, Request
from censor import censor_text

app = FastAPI()

@app.get('/predict')
async def predict(request: Request, sent: str):
    if not sent:
        raise HTTPException(status_code=400, detail="Sent field is required")
    # Perform prediction using your model
    prediction = censor_text(sent)
    # prediction = "hllo"
    # Return the prediction as JSON response
    return {'prediction': prediction}


# Example endpoint for health check
@app.get('/')
async def health_check():
    return 'Hello .... API is up and running'
