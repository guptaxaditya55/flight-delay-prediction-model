from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import joblib

# 1. Initialize FastAPI App
app = FastAPI(title="Flight Delay API", version="1.0")

# Allow frontend to communicate with backend (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, put your frontend domain here
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. Load the trained model and encoders
try:
    model = joblib.load('flight_delay_xgboost_model.pkl')
    encoders = joblib.load('label_encoders.pkl')
    print("✅ Models loaded successfully!")
except Exception as e:
    print(f"❌ Error loading models: {e}")

# 3. Define Input Data Schema (Data Validation - The SDE Way!)
class FlightData(BaseModel):
    month: int
    day_of_week: int
    airline: str
    origin: str
    dest: str
    distance: float
    dep_hour: int
# lets start the prediction function 

# 4. Create the Prediction Endpoint
@app.post("/predict")
def predict_delay(data: FlightData):
    try:
        # Edge Case checking
        if data.origin == data.dest:
            raise HTTPException(status_code=400, detail="Origin and Destination cannot be the same!")

        # A. Encode Categorical Data
        encoded_airline = encoders['Marketing_Airline_Network'].transform([data.airline])[0]
        encoded_origin = encoders['Origin'].transform([data.origin])[0]
        encoded_dest = encoders['Dest'].transform([data.dest])[0]

        # B. Prepare DataFrame exactly as the model expects
        input_df = pd.DataFrame({
            'Month': [data.month],
            'DayOfWeek': [data.day_of_week],
            'Marketing_Airline_Network': [encoded_airline],
            'Origin': [encoded_origin],
            'Dest': [encoded_dest],
            'Distance': [data.distance],
            'DepHour': [data.dep_hour]
        })

        # C. Make Prediction
        prediction = int(model.predict(input_df)[0])
        probability = float(model.predict_proba(input_df)[0][1]) * 100

        # D. Return JSON Response
        return {
            "status": "success",
            "is_delayed": bool(prediction == 1),
            "delay_probability": round(probability, 2),
            "message": "High Chances of Delay 🚨" if prediction == 1 else "Flight is On-Time ✅"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))