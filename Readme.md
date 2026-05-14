🦇🔴 Flight Delay Predictor - The Upside Down Edition
Welcome to the Flight Delay Predictor, a Machine Learning project that not only predicts flight delays but does so with an immersive, Stranger Things-inspired "Vecna" theme.  
+1

Will your flight arrive on time, or will it be dragged into the Upside Down? Seek the truth.

  
+1

🔮 Features
Themed User Interface: A dark, eerie, Stranger Things themed UI featuring custom fonts, glowing red accents, and a "SEEK THE TRUTH" prediction button.  
+1

Machine Learning Powered: Uses a trained classification model to predict the probability of flight delays based on historical data.  
+1

Lightning Fast API: Built with FastAPI for quick and efficient data processing and model inference.  
+1

Ready for Production: Structured for easy deployment on platforms like Railway or Render.  
+1

🛠️ Tech Stack
Frontend: HTML, CSS, JavaScript (Custom styling)  
+1

Backend: FastAPI, Uvicorn, Python  
+1

Machine Learning: scikit-learn, Pandas, NumPy  
+1

Deployment: Railway  
+1

🚀 Local Setup & Installation
Follow these steps to run the gate on your local machine:  

1. Clone the repository:

Bash
git clone https://github.com/yourusername/flight-delay-predictor.git
cd flight-delay-predictor
2. Create a virtual environment:

Bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```[cite: 2]

**3. Install dependencies for the project :**
```bash
pip install -r requirements.txt
```[cite: 2]

**4. Run the FastAPI server:**
```bash
uvicorn main:app --reload
```[cite: 2]

## 📡 API Reference

### `POST /predict`
Sends flight details to the model to get the delay prediction[cite: 1, 2].

**Request Body (JSON):**
```json
{
  "MONTH": 12,
  "DAY_OF_WEEK": "FRIDAY",
  "ORIGIN_CODE": "JFK",
  "DEST_CODE": "LAX",
  "AIRLINE_ID": "B6",
  "DISTANCE": 2475,
  "HOUR": 18
}
```[cite: 1, 2]

