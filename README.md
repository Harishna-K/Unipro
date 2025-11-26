# Master Transaction Management System

## 📌 Project Description
This application demonstrates Master Data Management, Transaction Entry, and Reporting using
Python FastAPI as backend and ReactJS as frontend.

It supports:
- Master Creation (Customer / Supplier)
- Transaction Entry
- Auto reference number generation
- Inventory balance logic
- Summary and Ledger reports
- Filtering by Date, Type and Entity

---

## 🛠 Technology Stack
- Backend: Python 3.11, FastAPI, SQLAlchemy
- Frontend: ReactJS
- Database: SQLite
- Styling: CSS
- Tools: VS Code, Node.js, PowerShell

---

## ✅ Prerequisites

Install the following:

### 1. Python 3.11+
Download: https://www.python.org/downloads/

Verify:
python --version

### 2. Node.js + npm
Download: https://nodejs.org/

Verify:
node -v
npm -v

### 3. Visual Studio Code (Recommended)
Download: https://code.visualstudio.com/

---

## 📂 Project Structure
master-transaction-app/
├── backend/
│ ├── main.py
│ ├── database.py
│ ├── models.py
│ ├── crud.py
│ ├── schemas.py
│ └── routers.py
├── frontend/
│ ├── src/
│ ├── public/
│ └── package.json

---

## ▶ BACKEND SETUP (FastAPI)

### Step 1: Open Project in VS Code
Open the main folder using VS Code.

---

### Step 2: Open Terminal and Move to Backend

---

### Step 3: Install Backend Libraries
pip install fastapi uvicorn sqlalchemy

---

### Step 4: Run Backend Server
uvicorn main:app --reload

---

### ✅ Backend Running At
http://127.0.0.1:8000

### ✅ API Docs
http://127.0.0.1:8000/docs

---

## ▶ FRONTEND SETUP (React)

### Step 1: Open a New Terminal

---

### Step 2: Move to Frontend Directory
cd frontend

---

### Step 3: Install Frontend Packages
npm install

---

### Step 4: Start React App
npm start

---

### ✅ App Runs At
http://localhost:3000

---

## 💡 Features
- CRUD operations for master records
- Auto pickup entity details in transactions
- Auto Ref number generation
- Customer adds balance
- Supplier reduces balance
- Reports with filters
- Clean UI
- Validation for mandatory fields

---

## ❗ Troubleshooting

### If `uvicorn` not found:
pip install uvicorn

### If `npm` not recognized:
Install Node.js and restart VS Code.

---

## 🚀 How to Use

1. Create Master (Customer / Supplier)
2. Create Transaction
3. View Daily Report
4. View Ledger


- Data handling
- Real-time reporting
- UI structure & validation

---

