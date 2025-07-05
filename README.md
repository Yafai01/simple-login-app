
# 🔐 Simple Login App

A minimal login + registration system built with:
- ⚛️ React (frontend)
- 🐍 Flask (backend)

### Features
✅ Login / Register  
👁️ Toggle password visibility  
🔐 Lock after 3 failed login attempts  
🗂️ Saves login state using `localStorage`

### How to Run

**Backend**
```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install flask flask-cors
python app.py
Frontend

bash
Copy
Edit
cd frontend
npm install
npm start
🌐 Access From Other Devices
Replace localhost with your local IP (e.g., 192.168.166.137) in App.js:

js
Copy
Edit
const API_BASE = "http://192.168.166.137:5000";
Make sure:

Your device is on the same Wi-Fi.

Windows Firewall allows access.
