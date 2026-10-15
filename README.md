# ✈️ WanderLust AI - Smart Travel Agent & Booking Platform

An interactive, AI-inspired travel planning and booking web application built with **Python** and **Streamlit**. It dynamically recommends tailored holiday and getaway destinations across India, estimates exact spend breakdowns for any selected place, and provides a full end-to-end trip booking workflow with instant digital boarding passes.

---

## 🌟 Key Features

1. **🌴 Explore Destinations Engine**
   - Filter by *Total Group Budget* or *Per-Person Budget* with automatic mathematical split.
   - 12+ curated destinations across India (Hill stations, Tropical beaches, Heritage sites, and Adventure spots).
   - Expandable day-by-day itineraries and downloadable text plans.
   - Instant search bar for activities, places, and states.

2. **🧮 Single Place Spend & Cost Estimator**
   - Pick any one destination to calculate exact trip spending.
   - Customize **Hotel Tier** (Budget Homestay / 3-Star Comfort / Luxury Resort).
   - Customize **Transit Mode** (Sleeper Train & Bus / Express / Flight & Private Cab).
   - Customize **Daily Dining** (Local Dhabas / Cafes / Fine Dining).
   - Customize **Sightseeing** (Standard Passes / Adventure & Water Sports).
   - Instant real-time itemized cost breakdown with tax estimation.

3. **🎫 Instant Travel Booking & Boarding Pass Generator**
   - Direct booking form with lead passenger information, dates, and party size.
   - Add-on services: Travel Insurance, Airport Pickup, Complimentary Breakfast.
   - Promo discount coupon codes:
     - `WANDER10` → 10% Discount
     - `STUDENT500` → ₹500 OFF
   - Generates a verified **Digital Boarding Pass & Official E-Ticket** with unique Reference ID (`WL-XXXX-DEST`).
   - One-click downloadable official booking receipt (`.txt`).

4. **📋 My Bookings Management**
   - Live dashboard tracking all active and confirmed trip bookings in `st.session_state`.
   - View complete trip details or cancel any booking in real time.

5. **🧳 Smart Travel Packing Checklist**
   - Interactive checklist for documents, clothing, and travel essentials.

---

## 📂 Project Structure

```text
travel-agent/
├── app.py                # Main Streamlit web application
├── requirements.txt      # Python dependencies (streamlit)
├── README.md             # Complete documentation and deployment guide
├── .gitignore            # Git ignore file
└── .streamlit/
    └── config.toml       # Custom visual theme and server settings
```

---

## 🚀 How to Run Locally

### 1. Open Terminal in this folder
Ensure you are in the folder containing `app.py`:
```powershell
cd "c:\Users\Tallada Gopi\Downloads\travel-agent\travel-agent"
```

### 2. Install Dependencies
```powershell
py -m pip install -r requirements.txt
```

### 3. Launch the Application
```powershell
py -m streamlit run app.py
```
Your default web browser will automatically open:
👉 **`http://localhost:8501`**

---

## 🌐 How to Upload to GitHub and Get Live Host Link

### Step 1: Upload to GitHub (Easy Web UI Method)
1. Go to [github.com](https://github.com) and log into your account.
2. Click the **+** (plus icon) at top-right ➔ **New repository**.
3. Name your repository (e.g., `travel-agent`), select **Public**, and click **Create repository**.
4. On the new repository page, click **uploading an existing file**.
5. Drag and drop all the files from this folder:
   - `app.py`
   - `requirements.txt`
   - `README.md`
   - `.gitignore`
   - `.streamlit` folder (with `config.toml`)
6. Click the green **Commit changes** button.

### Step 2: Deploy to Streamlit Community Cloud (Free Live Web Link)
1. Go to [share.streamlit.io](https://share.streamlit.io) and click **Continue with GitHub**.
2. Click **Create app** (or **New app**).
3. Select your repository: `your-username/travel-agent`.
4. Set Main file path: `app.py`.
5. Click **Deploy!**
6. Within 1–2 minutes, your website will be live with a permanent URL like:
   👉 `https://travel-agent-yourname.streamlit.app`
