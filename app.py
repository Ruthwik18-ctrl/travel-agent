import streamlit as st
import datetime
import random

# Page Configuration
st.set_page_config(
    page_title="WanderLust AI - Smart Travel Agent & Booking",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize Session State
if "bookings" not in st.session_state:
    st.session_state.bookings = [
        {
            "booking_id": "WL-8942-HYD",
            "destination": "Hyderabad City & Heritage Break",
            "state": "Telangana",
            "passenger_name": "Gopi Tallada",
            "contact": "gopi@example.com",
            "phone": "+91 98765 43210",
            "travel_date": "2026-11-10",
            "days": 2,
            "travelers": 2,
            "tier": "Standard Comfort (3-Star Hotel)",
            "transport": "AC Sleeper Train / Volvo Bus",
            "addons": ["Daily Buffet Breakfast", "Travel Insurance"],
            "total_amount": 9000,
            "status": "Confirmed 🟢",
            "booked_at": "2026-10-15 22:30"
        }
    ]

if "prefill_dest" not in st.session_state:
    st.session_state.prefill_dest = "Goa Tropical Beaches & Latin Quarter"

if "booking_success_data" not in st.session_state:
    st.session_state.booking_success_data = None

if "last_booked_id" not in st.session_state:
    st.session_state.last_booked_id = None

# Custom Styling (Rich Glassmorphism, Boarding Pass & Modern UI)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap');

    * {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* Main Container & Gradient Header */
    .hero-container {
        background: linear-gradient(135deg, #0f172a 0%, #0d9488 50%, #059669 100%);
        border-radius: 20px;
        padding: 34px 30px;
        color: white;
        margin-bottom: 22px;
        box-shadow: 0 12px 25px -5px rgba(13, 148, 136, 0.25);
        position: relative;
    }
    .hero-title {
        font-size: 2.3rem;
        font-weight: 800;
        letter-spacing: -0.5px;
        margin-bottom: 6px;
        color: #ffffff;
    }
    .hero-subtitle {
        font-size: 1.02rem;
        opacity: 0.94;
        max-width: 760px;
        line-height: 1.5;
        font-weight: 400;
        color: #e2e8f0;
    }
    .hero-badge {
        display: inline-block;
        background: rgba(255, 255, 255, 0.18);
        backdrop-filter: blur(8px);
        padding: 4px 14px;
        border-radius: 50px;
        font-size: 0.82rem;
        font-weight: 600;
        margin-bottom: 12px;
        border: 1px solid rgba(255, 255, 255, 0.25);
    }

    /* Tag styles */
    .tag-badge {
        display: inline-block;
        padding: 4px 10px;
        border-radius: 8px;
        font-size: 0.78rem;
        font-weight: 600;
        margin-right: 6px;
        margin-bottom: 6px;
    }
    .tag-style { background-color: #e0f2fe; color: #0369a1; }
    .tag-season { background-color: #fef3c7; color: #b45309; }
    .tag-duration { background-color: #f3e8ff; color: #7e22ce; }
    .tag-budget { background-color: #dcfce7; color: #15803d; }

    /* Highlights pill */
    .pill-item {
        display: inline-block;
        background: #f1f5f9;
        color: #475569;
        padding: 4px 11px;
        border-radius: 20px;
        font-size: 0.82rem;
        margin: 3px 3px 3px 0;
        font-weight: 500;
    }
    @media (prefers-color-scheme: dark) {
        .pill-item {
            background: #334155;
            color: #cbd5e1;
        }
    }

    /* Summary Box */
    .summary-box {
        background: linear-gradient(135deg, rgba(13, 148, 136, 0.08) 0%, rgba(30, 58, 138, 0.08) 100%);
        border-radius: 12px;
        border: 1px solid rgba(13, 148, 136, 0.2);
        padding: 14px;
        text-align: center;
        margin-bottom: 14px;
    }
    .summary-val {
        font-size: 1.55rem;
        font-weight: 800;
        color: #0d9488;
    }
    .summary-lbl {
        font-size: 0.8rem;
        color: #64748b;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    /* Estimate Banner */
    .estimate-banner {
        background: linear-gradient(135deg, #0d9488 0%, #1e3a8a 100%);
        border-radius: 14px;
        padding: 18px 22px;
        color: white;
        margin: 12px 0;
    }
    .estimate-banner-title {
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        opacity: 0.9;
        font-weight: 600;
    }
    .estimate-banner-price {
        font-size: 2.2rem;
        font-weight: 800;
        margin: 3px 0;
    }
    .estimate-banner-sub {
        font-size: 0.95rem;
        opacity: 0.95;
    }

    /* Boarding Pass / Booking Ticket Style */
    .ticket-card {
        background: #ffffff;
        border-radius: 16px;
        border: 2px dashed #0d9488;
        padding: 24px;
        margin: 18px 0;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.08);
        color: #0f172a;
    }
    .ticket-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1px solid #e2e8f0;
        padding-bottom: 12px;
        margin-bottom: 15px;
    }
    .ticket-code {
        font-family: 'JetBrains Mono', monospace;
        font-weight: 700;
        font-size: 1.15rem;
        color: #0d9488;
        background: #f0fdf4;
        padding: 4px 10px;
        border-radius: 6px;
        border: 1px solid #86efac;
    }
    @media (prefers-color-scheme: dark) {
        .ticket-card {
            background: #1e293b;
            color: #f8fafc;
            border-color: #14b8a6;
        }
        .ticket-code {
            background: #064e3b;
            color: #6ee7b7;
        }
    }
</style>
""", unsafe_allow_html=True)

# Curated Destinations Database
DESTINATIONS = [
    {
        "id": "hyd",
        "name": "Hyderabad City & Heritage Break",
        "state": "Telangana",
        "style": "City & Food",
        "days": 2,
        "base_cost_per_day": 2250,
        "cost": 4500,
        "best_season": "October to March",
        "tagline": "Pearls, Nizami Palaces, and Authentic Biryani",
        "description": "Immerse yourself in centuries of royal history, bustling bazaars around Charminar, and world-famous Hyderabadi culinary delicacies.",
        "highlights": ["Charminar & Laad Bazaar", "Golconda Fort Sound & Light Show", "Chowmahalla Palace", "Authentic Dum Biryani & Irani Chai"],
        "itinerary": [
            "Day 1: Explore Golconda Fort in morning, visit Qutb Shahi Tombs, evening shopping at Laad Bazaar and dinner near Charminar.",
            "Day 2: Morning tour of Chowmahalla Palace, visit Salar Jung Museum, and evening boat ride at Hussain Sagar Lake."
        ],
        "cost_breakdown": {"Stay (3-star)": 2000, "Local Transport": 1000, "Food & Treats": 1100, "Entry Tickets": 400}
    },
    {
        "id": "warangal",
        "name": "Warangal Heritage & Lakes",
        "state": "Telangana",
        "style": "Nature & Heritage",
        "days": 2,
        "base_cost_per_day": 1750,
        "cost": 3500,
        "best_season": "October to February",
        "tagline": "Kakatiya Architecture & Ancient Sacred Temples",
        "description": "A peaceful historic getaway featuring intricately carved stone pillars, ancient lakeside views, and legendary stone gateway arches.",
        "highlights": ["Warangal Fort & Kakatiya Kala Thoranam", "Thousand Pillar Temple", "Ramappa Temple (UNESCO)", "Bhadrakali Lake Sunset"],
        "itinerary": [
            "Day 1: Arrive from Hyderabad, tour the historic Warangal Fort complex, and enjoy sunset walk by Bhadrakali Lake.",
            "Day 2: Morning darshan at Thousand Pillar Temple, excursion to the world-renowned Ramappa UNESCO Temple, return."
        ],
        "cost_breakdown": {"Stay": 1400, "Local Transport": 1100, "Food": 700, "Entry & Guides": 300}
    },
    {
        "id": "araku",
        "name": "Araku Valley & Borra Caves",
        "state": "Andhra Pradesh",
        "style": "Nature & Adventure",
        "days": 3,
        "base_cost_per_day": 2800,
        "cost": 8500,
        "best_season": "September to March",
        "tagline": "Misty Hills, Coffee Plantations & Million-Year Caves",
        "description": "Travel through the picturesque Eastern Ghats by glass-domed Vistadome train into lush organic coffee hills and limestone caverns.",
        "highlights": ["Vistadome Scenic Train Ride", "Borra Caves Stalactites", "Organic Coffee Plantations", "Katiki & Chaparai Waterfalls"],
        "itinerary": [
            "Day 1: Scenic morning train from Vizag to Araku, check-in, visit Araku Tribal Museum and Coffee Museum.",
            "Day 2: Excursion to Borra Caves marvels, explore Katiki Waterfalls, and evening tribal Dhimsa dance.",
            "Day 3: Padmapuram Botanical Gardens, local organic honey & coffee tasting, drive down to Vizag."
        ],
        "cost_breakdown": {"Train & Transport": 2800, "Eco Resort Stay": 3200, "Food & Coffee": 1600, "Activities & Tickets": 900}
    },
    {
        "id": "vizag",
        "name": "Visakhapatnam Coastal Escape",
        "state": "Andhra Pradesh",
        "style": "Beach & Relaxation",
        "days": 3,
        "base_cost_per_day": 2650,
        "cost": 8000,
        "best_season": "October to March",
        "tagline": "Where the Lush Hills Meet the Bay of Bengal",
        "description": "The Jewel of the East Coast offers pristine long shorelines, hill-top ropeway viewpoints, and unique maritime submarine museums.",
        "highlights": ["INS Kursura Submarine Museum", "Kailasagiri Ropeway View", "Rishikonda Beach Water Sports", "Ross Hill Sunset"],
        "itinerary": [
            "Day 1: Stroll RK Beach, tour inside the genuine decommissioned INS Kursura Submarine & TU-142 Aircraft museums.",
            "Day 2: Ropeway ride to Kailasagiri mountain park with panoramic ocean views; afternoon water sports at Rishikonda Beach.",
            "Day 3: Sunrise at Yarada Beach, visit Dolphin's Nose Lighthouse, and taste authentic coastal Andhra seafood."
        ],
        "cost_breakdown": {"Hotel Stay": 3300, "Transport & Cabs": 2200, "Seafood & Food": 1800, "Museums & Activities": 700}
    },
    {
        "id": "goa",
        "name": "Goa Tropical Beaches & Latin Quarter",
        "state": "Goa",
        "style": "Beach & Relaxation",
        "days": 4,
        "base_cost_per_day": 4125,
        "cost": 16500,
        "best_season": "November to April",
        "tagline": "Sun-Kissed Sands, Portuguese Villas & Sunset Cruises",
        "description": "The quintessential Indian holiday hotspot blending vibrant beach shacks, heritage Portuguese churches, and relaxed coastal vibes.",
        "highlights": ["Palolem & Vagator Beaches", "Fontainhas Heritage Walk", "Basilica of Bom Jesus", "Mandovi River Sunset Cruise"],
        "itinerary": [
            "Day 1: Arrive in North Goa, settle in, relax at Anjuna beach shack, and watch sunset at Chapora Fort.",
            "Day 2: Explore historic Old Goa basilicas, stroll through colorful Fontainhas Latin Quarter in Panaji.",
            "Day 3: Drive to South Goa; unwind on white sands of Palolem or Colva, enjoy beachside barbecue dinner.",
            "Day 4: Morning water adventure or spice plantation tour; souvenir shopping in Calangute before departure."
        ],
        "cost_breakdown": {"Stay (Boutique/Resort)": 7500, "Scooter/Cab Rentals": 2800, "Cafes & Dining": 4200, "Activities & Cruise": 2000}
    },
    {
        "id": "munnar",
        "name": "Munnar Tea Hills & Waterfalls",
        "state": "Kerala",
        "style": "Nature & Adventure",
        "days": 4,
        "base_cost_per_day": 3500,
        "cost": 14000,
        "best_season": "September to May",
        "tagline": "Endless Emerald Tea Carpets & Cool Mountain Mist",
        "description": "Perched at 1,600m altitude in God's Own Country, Munnar is famous for rolling tea plantations, exotic flora, and refreshing waterfalls.",
        "highlights": ["Tea Estate Trek & Tea Factory", "Eravikulam National Park (Nilgiri Tahr)", "Mattupetty Dam & Eco Point", "Cheeyappara Waterfalls"],
        "itinerary": [
            "Day 1: Scenic drive up from Kochi via Cheeyappara waterfalls, check into hillside hotel, stroll tea garden.",
            "Day 2: Visit Eravikulam National Park to spot endangered Nilgiri Tahr; tour Lockhart Tea Museum.",
            "Day 3: Excursion to Mattupetty Dam, Echo Point, and Kundala Lake with paddle boating.",
            "Day 4: Top Station sunrise viewpoint, spice garden walk, and traditional Kerala Sadhya lunch."
        ],
        "cost_breakdown": {"Hill Stay": 5800, "Cab/Transfers": 4200, "Local Meals": 2500, "Entry & Safari": 1500}
    },
    {
        "id": "manali",
        "name": "Manali & Solang Valley Snow Trip",
        "state": "Himachal Pradesh",
        "style": "Nature & Adventure",
        "days": 5,
        "base_cost_per_day": 3500,
        "cost": 17500,
        "best_season": "October to June",
        "tagline": "Himalayan Pine Forests, Atal Tunnel & Snow Sports",
        "description": "High altitude adrenaline and tranquility nestled by the Beas River, featuring pine forests, snow activities, and Old Manali cafes.",
        "highlights": ["Atal Tunnel Drive to Sissu", "Solang Valley Paragliding & Skiing", "Hadimba Devi Temple", "Old Manali Riverside Cafes"],
        "itinerary": [
            "Day 1: Arrive, acclimatize with a stroll through cedar woods to Hadimba Temple and Mall Road.",
            "Day 2: Full day excursion to Solang Valley for paragliding, zorbing, and cable car rides.",
            "Day 3: Drive through architectural wonder Atal Tunnel to Lahaul Valley / Sissu waterfall.",
            "Day 4: Explore Jogini Waterfall trek near Vashisht village, unwind in natural hot sulfur springs.",
            "Day 5: Riverside trout tasting, cafe hopping in Old Manali, souvenir shopping for warm shawls."
        ],
        "cost_breakdown": {"Stay": 6500, "Mountain Cabs": 5200, "Food & Cafes": 3300, "Activities & Permits": 2500}
    },
    {
        "id": "jaipur",
        "name": "Jaipur Royal Pink City",
        "state": "Rajasthan",
        "style": "City & Food",
        "days": 3,
        "base_cost_per_day": 3150,
        "cost": 9500,
        "best_season": "October to March",
        "tagline": "Maharaja Forts, Gem Bazaars & Rajasthani Thali",
        "description": "Step into royal splendor with hilltop sandstone fortresses, intricate honeycomb palaces, and rich Rajasthani heritage hospitality.",
        "highlights": ["Amber Fort Elephant/Jeep Ascent", "Hawa Mahal & City Palace", "Nahargarh Sunset over Pink City", "Authentic Dal Baati Churma"],
        "itinerary": [
            "Day 1: Photograph Hawa Mahal, explore City Palace royal courtyards, and visit Jantar Mantar observatory.",
            "Day 2: Grand tour of Amer Fort and Jaigarh Cannon Fort; sunset viewpoint from Nahargarh ramparts.",
            "Day 3: Hand-block printing workshop in Bagru, shopping at Johari Bazaar, traditional Rajasthani dinner."
        ],
        "cost_breakdown": {"Heritage Stay": 4000, "Autos & Cabs": 2200, "Thalis & Sweets": 2100, "Monument Passes": 1200}
    },
    {
        "id": "pondicherry",
        "name": "Pondicherry French Quarter & Auroville",
        "state": "Puducherry",
        "style": "Beach & Relaxation",
        "days": 3,
        "base_cost_per_day": 3000,
        "cost": 9000,
        "best_season": "October to March",
        "tagline": "French Colonial Boulevards, Cafes & Spiritual Peace",
        "description": "A delightful seaside destination lined with mustard-yellow colonial villas, bougainvillea-covered balconies, and peaceful ashrams.",
        "highlights": ["White Town Bicycle Stroll", "Promenade Beach Rock Walk", "Auroville Matrimandir", "French Bakeries & Croissants"],
        "itinerary": [
            "Day 1: Rent a vintage bicycle or pastel scooter, ride through White Town, sunset at Rock Beach.",
            "Day 2: Visit peaceful Auroville and view the golden Matrimandir sphere; relax at Serenity Beach.",
            "Day 3: Morning croissant at Baker's Street cafe, browse boutique ceramic and leather stores, seaside stroll."
        ],
        "cost_breakdown": {"Heritage Guest House": 4200, "Bike Rental & Travel": 1800, "French Cafes & Dining": 2200, "Activities": 800}
    },
    {
        "id": "rishikesh",
        "name": "Rishikesh Yoga & River Rafting",
        "state": "Uttarakhand",
        "style": "Nature & Adventure",
        "days": 3,
        "base_cost_per_day": 2500,
        "cost": 7500,
        "best_season": "September to May",
        "tagline": "Ganga Aarti, White Water Rapids & Himalayan Foothills",
        "description": "The world yoga capital offers heart-pumping Ganga river rafting, cliff jumping, peaceful mountain ashrams, and magical evening aartis.",
        "highlights": ["16km Ganga White Water Rafting", "Triveni Ghat Evening Aarti", "Beatles Ashram Graffiti Walk", "Laxman Jhula & Riverside Cafes"],
        "itinerary": [
            "Day 1: Arrive, check into riverside camp or boutique stay, witness divine Ganga Aarti with floating lamps.",
            "Day 2: Thrilling white-water rafting through Grade 3+ rapids; cliff jumping, and cafe hopping.",
            "Day 3: Sunrise yoga session, explore the iconic Beatles Ashram ruins, and Ayurvedic lunch."
        ],
        "cost_breakdown": {"River Camp / Stay": 2800, "Rafting & Gear": 1800, "Meals & Cafes": 1900, "Local Travel": 1000}
    },
    {
        "id": "bengaluru",
        "name": "Bengaluru & Coorg Weekend",
        "state": "Karnataka",
        "style": "City & Food",
        "days": 3,
        "base_cost_per_day": 3500,
        "cost": 10500,
        "best_season": "All Year Round",
        "tagline": "Garden City Brews to Coorg Coffee Estates",
        "description": "Start with Bengaluru's bustling craft breweries and botanical parks, followed by the fragrant coffee hills of Madikeri.",
        "highlights": ["Lalbagh Botanical Gardens", "Indiranagar Cafe & Microbrewery Culture", "Coorg Coffee Plantation Walk", "Abbey Falls & Raja's Seat"],
        "itinerary": [
            "Day 1: Lalbagh botanical glasshouse, filter coffee at Vidyarthi Bhavan, and evening craft brewery tour.",
            "Day 2: Drive to scenic Coorg, explore sprawling coffee estate with home-stay host, visit Abbey Falls.",
            "Day 3: Sunset panorama at Raja's Seat, Tibetan Golden Temple at Bylakuppe, return trip."
        ],
        "cost_breakdown": {"Stay": 4800, "Intercity Transport": 2900, "Food & Drinks": 2100, "Estate Entry": 700}
    },
    {
        "id": "hampi",
        "name": "Hampi Ancient Ruins & Boulder Valley",
        "state": "Karnataka",
        "style": "Nature & Heritage",
        "days": 3,
        "base_cost_per_day": 2160,
        "cost": 6500,
        "best_season": "October to March",
        "tagline": "Surreal Granite Landscapes & Vijayanagara Empire",
        "description": "A UNESCO World Heritage marvel set amid a surreal landscape of giant boulders, ancient monolithic temples, and Coracle boat rides.",
        "highlights": ["Virupaksha Temple & Bazaar", "Stone Chariot at Vijaya Vittala", "Tungabhadra Coracle Boat Ride", "Sunset from Matanga Hill"],
        "itinerary": [
            "Day 1: Sunrise hike up Matanga Hill, discover sacred Virupaksha Temple, explore river Ghats.",
            "Day 2: Rent a moped to visit Vijaya Vittala temple and musical pillars; coracle boat ride at Sanapur Lake.",
            "Day 3: Royal Enclosure, Queen's Bath, and Lotus Mahal; chill at Hippie Island rooftop cafe."
        ],
        "cost_breakdown": {"Heritage Stay": 2600, "Moped & Coracle Boat": 1400, "Food & Mango Tree Cafe": 1700, "Monument Passes": 800}
    }
]

dest_names = [d["name"] for d in DESTINATIONS]
dest_dict = {d["name"]: d for d in DESTINATIONS}

# Hero Banner Section
st.markdown("""
<div class="hero-container">
    <span class="hero-badge">✈️ Next-Gen AI Trip Recommender & Booking System</span>
    <h1 class="hero-title">Plan, Estimate & Book Your Trips</h1>
    <p class="hero-subtitle">
        Find your ideal travel destinations, calculate exact travel price estimates with itemized breakdowns, and confirm instant bookings with official digital boarding passes!
    </p>
</div>
""", unsafe_allow_html=True)

# Main Navigation Tabs
tab_explore, tab_estimator, tab_booking, tab_my_bookings = st.tabs([
    "🌴 Find My Travel & Explore",
    "🧮 Single Place Cost Estimator",
    "🎫 Book Travel Package",
    f"📋 My Bookings ({len(st.session_state.bookings)})"
])

# =========================================================================
# TAB 1: FIND MY TRAVEL & EXPLORE (WITH DIRECT ESTIMATOR & INSTANT BOOKING)
# =========================================================================
with tab_explore:
    # Sidebar Controls for Find My Travel
    with st.sidebar:
        st.header("🎯 Find My Travel Filters")
        
        calc_mode = st.radio(
            "Budget Calculation Mode",
            ["Total Group Budget", "Per-Person Budget"],
            help="Choose whether your entered budget applies to the whole group or per individual person."
        )
        
        filter_travelers = st.number_input(
            "Number of Travellers 👥",
            min_value=1,
            max_value=12,
            value=2,
            step=1,
            key="filter_trav"
        )
        
        if calc_mode == "Total Group Budget":
            total_budget_input = st.slider(
                "Total Group Budget (INR) 💰",
                min_value=3000,
                max_value=100000,
                value=25000,
                step=1000,
                key="filter_tot_bud"
            )
            effective_per_person_budget = total_budget_input / filter_travelers
            st.info(f"💡 Equivalent to **₹{int(effective_per_person_budget):,}** per person for {filter_travelers} traveller(s).")
        else:
            per_person_budget_input = st.slider(
                "Budget Per Person (INR) 💰",
                min_value=2000,
                max_value=50000,
                value=12000,
                step=1000,
                key="filter_per_bud"
            )
            effective_per_person_budget = per_person_budget_input
            st.info(f"💡 Total estimated group budget: **₹{int(effective_per_person_budget * filter_travelers):,}**.")

        st.divider()

        filter_style = st.selectbox(
            "Travel Style / Vibe 🌴",
            ["Any Style", "Nature & Adventure", "Beach & Relaxation", "City & Food", "Nature & Heritage"],
            key="filter_style_choice"
        )

        filter_days = st.select_slider(
            "Trip Duration (Days) ⏳",
            options=[1, 2, 3, 4, 5, 6, 7],
            value=3,
            key="filter_days_choice"
        )

        search_query = st.text_input("Search destination or activity 🔍", placeholder="e.g. coffee, beach, temple, rafting...", key="filter_search")

        find_btn = st.button("🔍 Find My Travel / Apply Filter", type="primary", use_container_width=True)

        st.markdown("---")
        st.caption("🚀 **Live Streamlit App** • Instant response and no API key needed.")

    # Matching Algorithm
    matches = []
    for d in DESTINATIONS:
        cost_fits = d["cost"] <= effective_per_person_budget
        duration_fits = d["days"] <= filter_days + 1
        style_fits = (filter_style == "Any Style") or (d["style"] == filter_style)
        search_fits = True
        if search_query.strip():
            q = search_query.lower()
            search_fits = (
                q in d["name"].lower()
                or q in d["description"].lower()
                or q in d["state"].lower()
                or any(q in h.lower() for h in d["highlights"])
            )
        if cost_fits and duration_fits and style_fits and search_fits:
            matches.append(d)

    matches.sort(key=lambda d: (abs(d["days"] - filter_days), d["cost"]))

    # Summary Stats Bar
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f"""
        <div class="summary-box">
            <div class="summary-val">{len(matches)}</div>
            <div class="summary-lbl">Matching Trips</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="summary-box">
            <div class="summary-val">₹{int(effective_per_person_budget):,}</div>
            <div class="summary-lbl">Max Budget / Person</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
        <div class="summary-box">
            <div class="summary-val">{filter_days} Days</div>
            <div class="summary-lbl">Target Duration</div>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown(f"""
        <div class="summary-box">
            <div class="summary-val">{filter_travelers}</div>
            <div class="summary-lbl">Travellers</div>
        </div>
        """, unsafe_allow_html=True)

    if not matches:
        st.warning("⚠️ No destinations found matching your exact filter criteria.")
        st.info("💡 **Tips to find destinations:**\n- Increase the budget slider in the sidebar\n- Switch style to **'Any Style'**\n- Increase trip duration")
    else:
        st.subheader(f"🌟 Recommended Trips ({len(matches)} found) — View Estimates & Book Below")
        for idx, dest in enumerate(matches):
            group_cost = dest["cost"] * filter_travelers
            with st.container(border=True):
                head_col, price_col = st.columns([3, 1])
                with head_col:
                    st.markdown(f"### {dest['name']}")
                    st.caption(f"📍 {dest['state']} • *{dest['tagline']}*")
                    st.markdown(f"""
                    <span class="tag-badge tag-style">🏷️ {dest['style']}</span>
                    <span class="tag-badge tag-duration">⏱️ {dest['days']} Days</span>
                    <span class="tag-badge tag-season">🌤️ Best: {dest['best_season']}</span>
                    <span class="tag-badge tag-budget">💰 Base: ₹{dest['cost']:,} / person</span>
                    """, unsafe_allow_html=True)
                
                with price_col:
                    st.metric(
                        label="Group Estimated Total",
                        value=f"₹{group_cost:,}",
                        delta=f"₹{dest['cost']:,} each"
                    )

                st.write(dest["description"])
                st.markdown("**Top Highlights:**")
                pills_html = "".join([f'<span class="pill-item">✨ {h}</span>' for h in dest['highlights']])
                st.markdown(pills_html, unsafe_allow_html=True)

                # SECTION 1: Itinerary
                with st.expander(f"📋 Suggested Itinerary for {dest['name']}"):
                    st.markdown("#### 📅 Day-by-Day Schedule")
                    for day_step in dest["itinerary"]:
                        st.markdown(f"- **{day_step}**")

                # SECTION 2: Dynamic Travel Price & Final Estimate Calculator
                with st.expander(f"🧮 Travel Price Breakdown & Final Estimate for {dest['name']}"):
                    st.markdown(f"#### 💰 Customize Price & Final Estimate for **{dest['name']}**")
                    p_c1, p_c2 = st.columns(2)
                    with p_c1:
                        inline_tier = st.selectbox(
                            "Hotel & Stay Tier",
                            ["Standard Comfort 3-Star (₹2,200/night)", "Budget Homestay (₹1,000/night)", "Luxury Resort (₹5,500/night)"],
                            key=f"in_tier_{dest['id']}_{idx}"
                        )
                        inline_transport = st.selectbox(
                            "Travel Transit Mode",
                            ["Sleeper Train / AC Volvo Bus (₹900/person)", "Express Train / Cabs (₹1,800/person)", "Flight / Private Dedicated Cab (₹5,000/person)"],
                            key=f"in_trans_{dest['id']}_{idx}"
                        )
                    with p_c2:
                        inline_food = st.selectbox(
                            "Dining Preference",
                            ["Standard Restaurants (₹850/person/day)", "Local Dhabas & Cafes (₹400/person/day)", "Fine Dining & Lounges (₹1,800/person/day)"],
                            key=f"in_food_{dest['id']}_{idx}"
                        )
                        inline_act = st.selectbox(
                            "Sightseeing Level",
                            ["Standard Sightseeing Passes (₹300/person/day)", "Guided Tours & Adventure Sports (₹1,200/person/day)"],
                            key=f"in_act_{dest['id']}_{idx}"
                        )

                    # Compute estimate
                    rooms = (filter_travelers + 1) // 2
                    nights = max(1, dest["days"] - 1)
                    h_rate = 5500 if "Luxury" in inline_tier else (1000 if "Budget" in inline_tier else 2200)
                    t_rate = 5000 if "Flight" in inline_transport else (900 if "Sleeper" in inline_transport else 1800)
                    f_rate = 1800 if "Fine" in inline_food else (400 if "Local" in inline_food else 850)
                    a_rate = 1200 if "Adventure" in inline_act else 300

                    calc_hotel = h_rate * rooms * nights
                    calc_transit = t_rate * filter_travelers
                    calc_food = f_rate * dest["days"] * filter_travelers
                    calc_act = a_rate * dest["days"] * filter_travelers
                    subtot = calc_hotel + calc_transit + calc_food + calc_act
                    calc_tax = int(subtot * 0.05)
                    final_estimate = subtot + calc_tax
                    per_head_est = int(final_estimate / filter_travelers)

                    st.markdown(f"""
                    <div class="estimate-banner">
                        <div class="estimate-banner-title">Final Travel Price Estimate ({dest['name']})</div>
                        <div class="estimate-banner-price">₹{final_estimate:,}</div>
                        <div class="estimate-banner-sub">₹{per_head_est:,} per person for {filter_travelers} traveller(s) ({dest['days']} Days / {nights} Nights)</div>
                    </div>
                    """, unsafe_allow_html=True)

                    b_c1, b_c2 = st.columns(2)
                    with b_c1:
                        st.write(f"🏨 **Hotel Stay ({rooms} room(s) × {nights} nights):** ₹{calc_hotel:,}")
                        st.write(f"🚗 **Transit & Travel ({filter_travelers} persons):** ₹{calc_transit:,}")
                    with b_c2:
                        st.write(f"🍽️ **Dining & Food ({dest['days']} days):** ₹{calc_food:,}")
                        st.write(f"🎟️ **Activities & Passes:** ₹{calc_act:,}")
                        st.write(f"🧾 **Taxes & State Permits (5%):** ₹{calc_tax:,}")

                # SECTION 3: Direct Booking & Boarding Pass Form
                with st.expander(f"🎫 Book This Trip Now & Generate Boarding Pass"):
                    st.markdown(f"#### 📝 Book Your Package for **{dest['name']}**")
                    with st.form(f"quick_book_form_{dest['id']}_{idx}"):
                        q_c1, q_c2 = st.columns(2)
                        with q_c1:
                            in_pname = st.text_input("Lead Passenger Full Name *", placeholder="e.g. Rahul Sharma", key=f"q_name_{dest['id']}_{idx}")
                            in_pemail = st.text_input("Email Address *", placeholder="e.g. rahul@gmail.com", key=f"q_email_{dest['id']}_{idx}")
                            in_pphone = st.text_input("Mobile Phone Number *", placeholder="+91 98765 43210", key=f"q_phone_{dest['id']}_{idx}")
                        with q_c2:
                            today = datetime.date.today()
                            in_pdate = st.date_input("Travel Start Date 📅", value=today + datetime.timedelta(days=14), min_value=today, key=f"q_date_{dest['id']}_{idx}")
                            in_ptrav = st.number_input("Number of Passengers 👥", min_value=1, max_value=12, value=filter_travelers, key=f"q_trav_{dest['id']}_{idx}")
                            in_ptier = st.selectbox("Selected Package Tier", ["Standard Comfort (3-Star Hotel)", "Luxury Executive (4/5-Star Resort)", "Backpacker Economy (Homestay)"], key=f"q_tier_{dest['id']}_{idx}")
                            in_ptrans = st.selectbox("Selected Transport", ["AC Sleeper Train / Volvo Bus", "Flight Transfers Included", "Private AC Cab / Self Drive"], key=f"q_trans_{dest['id']}_{idx}")

                        st.markdown("**Add-on Benefits & Promo Code:**")
                        ad_c1, ad_c2 = st.columns(2)
                        with ad_c1:
                            in_ins = st.checkbox("Travel Insurance & Medical Protection (₹250 / person)", value=True, key=f"q_ins_{dest['id']}_{idx}")
                            in_bfast = st.checkbox("Daily Complimentary Breakfast (₹400 / person / day)", value=True, key=f"q_bf_{dest['id']}_{idx}")
                            in_pick = st.checkbox("Airport / Railway Station Dedicated Pickup (₹800)", value=False, key=f"q_pk_{dest['id']}_{idx}")
                        with ad_c2:
                            in_promo = st.text_input("Promo Discount Code 🏷️", placeholder="Try: WANDER10 or STUDENT500", key=f"q_promo_{dest['id']}_{idx}").strip().upper()
                            st.caption("Coupons: **`WANDER10`** (10% OFF) or **`STUDENT500`** (₹500 OFF)")

                        submit_quick_book = st.form_submit_button("💳 Confirm Booking & Generate Boarding Pass", type="primary", use_container_width=True)

                    if submit_quick_book:
                        if not in_pname.strip() or not in_pemail.strip() or not in_pphone.strip():
                            st.error("⚠️ Please fill in all required passenger fields (Name, Email, Phone Number).")
                        else:
                            # Pricing calculation
                            base_rate = dest["cost"]
                            tier_mult = 1.45 if "Luxury" in in_ptier else (0.75 if "Backpacker" in in_ptier else 1.0)
                            trans_addon = (3500 * in_ptrav) if "Flight" in in_ptrans else ((1800 * in_ptrav) if "Private" in in_ptrans else 0)
                            
                            addons = []
                            addon_cost = 0
                            if in_ins:
                                addon_cost += 250 * in_ptrav
                                addons.append("Travel Insurance")
                            if in_bfast:
                                addon_cost += 400 * in_ptrav * dest["days"]
                                addons.append("Daily Breakfast")
                            if in_pick:
                                addon_cost += 800
                                addons.append("Station/Airport Pickup")

                            pre_discount = int((base_rate * tier_mult * in_ptrav) + trans_addon + addon_cost)
                            disc = 0
                            if in_promo == "WANDER10":
                                disc = int(pre_discount * 0.10)
                                st.toast("🎉 Promo Code WANDER10 Applied! 10% Discount saved!")
                            elif in_promo == "STUDENT500":
                                disc = 500
                                st.toast("🎉 Promo Code STUDENT500 Applied! ₹500 Discount saved!")
                            elif in_promo != "":
                                st.warning("Invalid promo code. Proceeding with regular price.")

                            final_cost = max(1000, pre_discount - disc)
                            b_ref = f"WL-{random.randint(1000, 9999)}-{dest['id'].upper()}"

                            new_bk = {
                                "booking_id": b_ref,
                                "destination": dest["name"],
                                "state": dest["state"],
                                "passenger_name": in_pname,
                                "contact": in_pemail,
                                "phone": in_pphone,
                                "travel_date": str(in_pdate),
                                "days": dest["days"],
                                "travelers": in_ptrav,
                                "tier": in_ptier,
                                "transport": in_ptrans,
                                "addons": addons if addons else ["Standard Package"],
                                "total_amount": final_cost,
                                "status": "Confirmed 🟢",
                                "booked_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                            }

                            st.session_state.bookings.insert(0, new_bk)
                            st.session_state.booking_success_data = new_bk
                            st.session_state.last_booked_id = b_ref
                            st.balloons()
                            st.success(f"🎉 Booking Confirmed Successfully! Reference ID: **{b_ref}**")

                # Show Boarding Pass directly if this was the last booked destination
                if st.session_state.booking_success_data and st.session_state.booking_success_data.get("destination") == dest["name"]:
                    bk = st.session_state.booking_success_data
                    st.markdown(f"""
                    <div class="ticket-card">
                        <div class="ticket-header">
                            <div>
                                <span style="font-size: 0.82rem; font-weight: 700; text-transform: uppercase; color: #0d9488;">Official E-Ticket & Confirmation</span>
                                <h3 style="margin: 3px 0 0 0;">✈️ {bk['destination']}</h3>
                                <span style="font-size: 0.88rem; color: #64748b;">State: {bk['state']}</span>
                            </div>
                            <div style="text-align: right;">
                                <div class="ticket-code">{bk['booking_id']}</div>
                                <div style="font-size: 0.85rem; color: #16a34a; font-weight: 700; margin-top: 5px;">STATUS: {bk['status']}</div>
                            </div>
                        </div>
                        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px; margin-top: 12px;">
                            <div>
                                <span style="font-size: 0.78rem; text-transform: uppercase; color: #94a3b8; font-weight: 600;">Lead Passenger</span>
                                <div style="font-weight: 700; font-size: 1.05rem;">{bk['passenger_name']}</div>
                                <div style="font-size: 0.85rem; color: #64748b;">{bk['phone']}</div>
                            </div>
                            <div>
                                <span style="font-size: 0.78rem; text-transform: uppercase; color: #94a3b8; font-weight: 600;">Departure Date</span>
                                <div style="font-weight: 700; font-size: 1.05rem;">{bk['travel_date']}</div>
                                <div style="font-size: 0.85rem; color: #64748b;">Duration: {bk['days']} Days</div>
                            </div>
                            <div>
                                <span style="font-size: 0.78rem; text-transform: uppercase; color: #94a3b8; font-weight: 600;">Party Size</span>
                                <div style="font-weight: 700; font-size: 1.05rem;">{bk['travelers']} Traveller(s)</div>
                                <div style="font-size: 0.85rem; color: #64748b;">Package: {bk['tier'].split('(')[0]}</div>
                            </div>
                            <div>
                                <span style="font-size: 0.78rem; text-transform: uppercase; color: #94a3b8; font-weight: 600;">Total Amount Paid</span>
                                <div style="font-weight: 800; font-size: 1.3rem; color: #0d9488;">₹{bk['total_amount']:,}</div>
                                <div style="font-size: 0.85rem; color: #64748b;">Incl. all taxes & fees</div>
                            </div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

                    ticket_txt = f"""==================================================
WANDERLUST AI - OFFICIAL TRAVEL BOOKING RECEIPT
==================================================
Booking Reference: {bk['booking_id']}
Booking Timestamp: {bk['booked_at']}
Booking Status   : {bk['status']}

PASSENGER DETAILS:
- Lead Passenger : {bk['passenger_name']}
- Contact Email  : {bk['contact']}
- Mobile Phone   : {bk['phone']}

TRIP DETAILS:
- Destination    : {bk['destination']} ({bk['state']})
- Departure Date : {bk['travel_date']}
- Duration       : {bk['days']} Days
- Travellers     : {bk['travelers']} Person(s)
- Package Tier   : {bk['tier']}
- Transit Choice : {bk['transport']}
- Add-on Benefits: {', '.join(bk['addons'])}

PAYMENT SUMMARY:
- Total Paid     : ₹{bk['total_amount']:,} (All Inclusive)

IMPORTANT NOTICE:
Please carry this digital or printed pass along with a valid Government
Photo ID at check-in. Free cancellations available up to 48 hours before travel.
=================================================="""
                    st.download_button(
                        label="📥 Download Official Boarding Pass (.txt)",
                        data=ticket_txt,
                        file_name=f"{bk['booking_id']}_boarding_pass.txt",
                        mime="text/plain",
                        key=f"dl_tkt_inline_{dest['id']}_{idx}"
                    )

                # Quick action buttons row
                btn_col1, btn_col2 = st.columns([1, 1])
                with btn_col1:
                    plan_text = f"""==================================================
WANDERLUST AI - TRAVEL ITINERARY PLAN
==================================================
Destination: {dest['name']} ({dest['state']})
Style: {dest['style']}
Duration: {dest['days']} Days
Best Season: {dest['best_season']}
Travellers: {filter_travelers}
Total Estimated Cost: ₹{group_cost:,} (₹{dest['cost']:,} per person)

HIGHLIGHTS:
{chr(10).join(['- ' + h for h in dest['highlights']])}

ITINERARY:
{chr(10).join(dest['itinerary'])}

COST BREAKDOWN:
{chr(10).join([f'- {k}: ₹{v:,}' for k, v in dest['cost_breakdown'].items()])}
=================================================="""
                    st.download_button(
                        label=f"📥 Download Itinerary Plan (.txt)",
                        data=plan_text,
                        file_name=f"{dest['id']}_itinerary.txt",
                        mime="text/plain",
                        key=f"dl_exp_{dest['id']}_{idx}"
                    )
                with btn_col2:
                    if st.button(f"⚡ Select for Dedicated Booking Tab", key=f"sel_{dest['id']}_{idx}"):
                        st.session_state.prefill_dest = dest["name"]
                        st.success(f"Selected **{dest['name']}**! You can also use the **'Book Travel Package'** tab above.")

# =========================================================================
# TAB 2: SINGLE PLACE COST ESTIMATOR (HOW MUCH PRICE SPEND)
# =========================================================================
with tab_estimator:
    st.header("🧮 Single Place Travel Expense & Spend Estimator")
    st.write("Pick any one destination and customize your hotel tier, transport mode, food style, and duration to see **exactly how much money you will spend**.")

    col_e1, col_e2 = st.columns([1, 1])
    
    with col_e1:
        selected_dest_name = st.selectbox(
            "Select Destination to Estimate Spend 📍",
            dest_names,
            index=dest_names.index(st.session_state.prefill_dest) if st.session_state.prefill_dest in dest_names else 0,
            key="est_dest_select"
        )
        current_dest = dest_dict[selected_dest_name]

        est_days = st.slider("Number of Days 📅", min_value=1, max_value=14, value=current_dest["days"], key="est_days_slider")
        est_travelers = st.number_input("Number of Travellers 👥", min_value=1, max_value=12, value=2, key="est_travelers_input")

        hotel_tier = st.selectbox(
            "Accommodation Type 🏨",
            [
                "Budget Homestay / Hostel (₹1,000 / room / night)",
                "Standard 3-Star Comfort Hotel (₹2,200 / room / night)",
                "Luxury 4/5-Star Resort (₹5,500 / room / night)"
            ],
            index=1,
            key="est_hotel_tier"
        )

        transport_mode = st.selectbox(
            "Travel & Transit Mode 🚗/✈️",
            [
                "Sleeper Train / AC Volvo Bus (₹900 / person round-trip/local)",
                "Express Train / Shared Cabs (₹1,800 / person round-trip/local)",
                "Flight / Private Dedicated Cab (₹5,000 / person round-trip/local)"
            ],
            index=1,
            key="est_transport_mode"
        )

        food_preference = st.selectbox(
            "Daily Food & Dining Style 🍽️",
            [
                "Local Dhabas & Street Food Cafes (₹400 / person / day)",
                "Standard Restaurants & Cafes (₹850 / person / day)",
                "Fine Dining & Beach/Rooftop Lounges (₹1,800 / person / day)"
            ],
            index=1,
            key="est_food_tier"
        )

        activities_level = st.radio(
            "Sightseeing & Adventure Activities 🎟️",
            [
                "Standard Monument & Park Entry Passes (₹300 / person / day)",
                "Guided Tours + Adventure Sports / Water Sports (₹1,200 / person / day)"
            ],
            key="est_act_tier"
        )

    # Cost Calculation Logic
    rooms_needed = (est_travelers + 1) // 2
    nights = max(1, est_days - 1)

    if "Budget" in hotel_tier:
        nightly_room_rate = 1000
    elif "Standard" in hotel_tier:
        nightly_room_rate = 2200
    else:
        nightly_room_rate = 5500
    total_hotel_cost = nightly_room_rate * rooms_needed * nights

    if "Sleeper" in transport_mode:
        transit_per_person = 900
    elif "Express" in transport_mode:
        transit_per_person = 1800
    else:
        transit_per_person = 5000
    total_transit_cost = transit_per_person * est_travelers

    if "Local Dhabas" in food_preference:
        daily_food_rate = 400
    elif "Standard" in food_preference:
        daily_food_rate = 850
    else:
        daily_food_rate = 1800
    total_food_cost = daily_food_rate * est_days * est_travelers

    if "Standard Monument" in activities_level:
        daily_act_rate = 300
    else:
        daily_act_rate = 1200
    total_act_cost = daily_act_rate * est_days * est_travelers

    subtotal_cost = total_hotel_cost + total_transit_cost + total_food_cost + total_act_cost
    taxes_fees = int(subtotal_cost * 0.05)
    grand_total_estimate = subtotal_cost + taxes_fees
    per_person_spend = int(grand_total_estimate / est_travelers)

    with col_e2:
        st.subheader("📊 Estimated Spend Breakdown")
        
        # Grand Total Card
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #0d9488 0%, #1e3a8a 100%); padding: 22px; border-radius: 16px; color: white; margin-bottom: 16px;">
            <div style="font-size: 0.9rem; text-transform: uppercase; letter-spacing: 1px; opacity: 0.9;">Total Estimated Trip Spend</div>
            <div style="font-size: 2.5rem; font-weight: 800; margin: 4px 0;">₹{grand_total_estimate:,}</div>
            <div style="font-size: 1rem; opacity: 0.95;">₹{per_person_spend:,} per person for {est_travelers} traveller(s) ({est_days} Days / {nights} Nights)</div>
        </div>
        """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown(f"#### 📍 Destination: **{selected_dest_name}**")
            st.caption(f"State: {current_dest['state']} • Ideal Travel Season: {current_dest['best_season']}")
            
            st.markdown("**Itemized Spending Breakdown:**")
            
            b1, b2 = st.columns([3, 2])
            with b1:
                st.write(f"🏨 **Hotel & Stay ({rooms_needed} room(s) × {nights} nights):**")
                st.write(f"🚗 **Transport & Transit ({est_travelers} persons):**")
                st.write(f"🍽️ **Food & Dining ({est_days} days):**")
                st.write(f"🎟️ **Activities & Sightseeing:**")
                st.write(f"🧾 **Taxes & State Permits (~5%):**")
            with b2:
                st.write(f"₹{total_hotel_cost:,}")
                st.write(f"₹{total_transit_cost:,}")
                st.write(f"₹{total_food_cost:,}")
                st.write(f"₹{total_act_cost:,}")
                st.write(f"₹{taxes_fees:,}")
            
            st.divider()
            tot_c1, tot_c2 = st.columns([3, 2])
            with tot_c1:
                st.markdown("### **Final Estimated Spend:**")
            with tot_c2:
                st.markdown(f"### **₹{grand_total_estimate:,}**")

        st.write("")
        if st.button("👉 Proceed to Book This Trip With This Estimate", type="primary", use_container_width=True):
            st.session_state.prefill_dest = selected_dest_name
            st.success("Configuration loaded! Go to the **'Book Travel Package'** tab to complete your booking.")

# =========================================================================
# TAB 3: BOOK TRAVEL PACKAGE
# =========================================================================
with tab_booking:
    st.header("🎫 Instant Travel Booking & Boarding Pass")
    st.write("Confirm your travel itinerary, enter passenger details, apply discount coupons, and receive your verified Booking Pass instantly.")

    with st.form("travel_booking_form"):
        st.subheader("1. Destination & Package Details")
        book_col1, book_col2 = st.columns(2)
        
        with book_col1:
            booking_destination = st.selectbox(
                "Choose Destination 📍",
                dest_names,
                index=dest_names.index(st.session_state.prefill_dest) if st.session_state.prefill_dest in dest_names else 0
            )
            b_dest_obj = dest_dict[booking_destination]
            
            booking_tier = st.selectbox(
                "Package Tier ⭐",
                ["Standard Comfort (3-Star Hotel)", "Luxury Executive (4/5-Star Resort)", "Backpacker Economy (Homestay)"]
            )
            
            booking_transport = st.selectbox(
                "Travel Transit Preference 🚆/✈️",
                ["AC Sleeper Train / Volvo Bus", "Flight Transfers Included", "Private AC Cab / Self Drive"]
            )

        with book_col2:
            today = datetime.date.today()
            travel_date = st.date_input(
                "Travel Start Date 📅",
                value=today + datetime.timedelta(days=14),
                min_value=today
            )
            
            booking_days = st.number_input(
                "Duration (Days) ⏳",
                min_value=1,
                max_value=15,
                value=b_dest_obj["days"]
            )

            booking_travelers = st.number_input(
                "Number of Passengers 👥",
                min_value=1,
                max_value=12,
                value=2
            )

        st.subheader("2. Primary Passenger Information")
        pass_col1, pass_col2, pass_col3 = st.columns(3)
        with pass_col1:
            p_name = st.text_input("Lead Passenger Full Name *", placeholder="e.g. Rahul Sharma")
        with pass_col2:
            p_email = st.text_input("Email Address *", placeholder="e.g. rahul@gmail.com")
        with pass_col3:
            p_phone = st.text_input("Mobile Phone Number *", placeholder="+91 98765 43210")

        st.subheader("3. Add-on Services & Promo Code")
        add_col1, add_col2 = st.columns(2)
        with add_col1:
            add_insurance = st.checkbox("Travel Insurance & Medical Protection (₹250 / person)", value=True)
            add_pickup = st.checkbox("Airport / Railway Station Dedicated Pickup & Drop (₹800)", value=False)
            add_breakfast = st.checkbox("Daily Complimentary Buffet Breakfast (₹400 / person)", value=True)
        
        with add_col2:
            coupon_code = st.text_input("Have a Promo Code? 🏷️", placeholder="Try: WANDER10 or STUDENT500").strip().upper()
            st.caption("Available Promo Codes: **`WANDER10`** (10% Discount) or **`STUDENT500`** (₹500 OFF)")

        submit_booking = st.form_submit_button("💳 Confirm Booking & Generate Boarding Pass", type="primary", use_container_width=True)

    if submit_booking:
        if not p_name.strip() or not p_email.strip() or not p_phone.strip():
            st.error("⚠️ Please fill in all required passenger information (Name, Email, and Phone Number).")
        else:
            base_rate = b_dest_obj["cost"]
            tier_mult = 1.45 if "Luxury" in booking_tier else (0.75 if "Backpacker" in booking_tier else 1.0)
            trans_addon = (3500 * booking_travelers) if "Flight" in booking_transport else ((1800 * booking_travelers) if "Private" in booking_transport else 0)

            addons_list = []
            addon_cost = 0
            if add_insurance:
                addon_cost += 250 * booking_travelers
                addons_list.append("Travel Insurance")
            if add_pickup:
                addon_cost += 800
                addons_list.append("Airport/Station Pickup")
            if add_breakfast:
                addon_cost += 400 * booking_travelers * booking_days
                addons_list.append("Daily Buffet Breakfast")

            base_calc = int((base_rate * tier_mult * booking_travelers) + trans_addon + addon_cost)
            
            discount = 0
            if coupon_code == "WANDER10":
                discount = int(base_calc * 0.10)
                st.toast("🎉 Promo Code WANDER10 Applied! 10% Discount saved!")
            elif coupon_code == "STUDENT500":
                discount = 500
                st.toast("🎉 Promo Code STUDENT500 Applied! ₹500 Discount saved!")
            elif coupon_code != "":
                st.warning("Invalid promo code entered. Proceeding without discount.")

            final_total = max(1000, base_calc - discount)
            booking_ref = f"WL-{random.randint(1000, 9999)}-{b_dest_obj['id'].upper()}"

            new_booking = {
                "booking_id": booking_ref,
                "destination": booking_destination,
                "state": b_dest_obj["state"],
                "passenger_name": p_name,
                "contact": p_email,
                "phone": p_phone,
                "travel_date": str(travel_date),
                "days": booking_days,
                "travelers": booking_travelers,
                "tier": booking_tier,
                "transport": booking_transport,
                "addons": addons_list if addons_list else ["Standard Package"],
                "total_amount": final_total,
                "status": "Confirmed 🟢",
                "booked_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            }

            st.session_state.bookings.insert(0, new_booking)
            st.session_state.booking_success_data = new_booking
            st.session_state.last_booked_id = booking_ref
            st.balloons()
            st.success(f"🎉 Booking Confirmed Successfully! Reference ID: **{booking_ref}**")

    # Render Booking Confirmation Pass if exists
    if st.session_state.booking_success_data:
        bk = st.session_state.booking_success_data
        st.markdown(f"""
        <div class="ticket-card">
            <div class="ticket-header">
                <div>
                    <span style="font-size: 0.82rem; font-weight: 700; text-transform: uppercase; color: #0d9488;">Official E-Ticket & Confirmation</span>
                    <h2 style="margin: 3px 0 0 0;">✈️ {bk['destination']}</h2>
                    <span style="font-size: 0.9rem; color: #64748b;">State: {bk['state']}</span>
                </div>
                <div style="text-align: right;">
                    <div class="ticket-code">{bk['booking_id']}</div>
                    <div style="font-size: 0.85rem; color: #16a34a; font-weight: 700; margin-top: 5px;">STATUS: {bk['status']}</div>
                </div>
            </div>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; margin-top: 15px;">
                <div>
                    <span style="font-size: 0.78rem; text-transform: uppercase; color: #94a3b8; font-weight: 600;">Lead Passenger</span>
                    <div style="font-weight: 700; font-size: 1.05rem;">{bk['passenger_name']}</div>
                    <div style="font-size: 0.85rem; color: #64748b;">{bk['phone']}</div>
                </div>
                <div>
                    <span style="font-size: 0.78rem; text-transform: uppercase; color: #94a3b8; font-weight: 600;">Departure Date</span>
                    <div style="font-weight: 700; font-size: 1.05rem;">{bk['travel_date']}</div>
                    <div style="font-size: 0.85rem; color: #64748b;">Duration: {bk['days']} Days</div>
                </div>
                <div>
                    <span style="font-size: 0.78rem; text-transform: uppercase; color: #94a3b8; font-weight: 600;">Party Size</span>
                    <div style="font-weight: 700; font-size: 1.05rem;">{bk['travelers']} Traveller(s)</div>
                    <div style="font-size: 0.85rem; color: #64748b;">Package: {bk['tier'].split('(')[0]}</div>
                </div>
                <div>
                    <span style="font-size: 0.78rem; text-transform: uppercase; color: #94a3b8; font-weight: 600;">Total Amount Paid</span>
                    <div style="font-weight: 800; font-size: 1.3rem; color: #0d9488;">₹{bk['total_amount']:,}</div>
                    <div style="font-size: 0.85rem; color: #64748b;">Incl. all taxes & fees</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        ticket_receipt = f"""==================================================
WANDERLUST AI - OFFICIAL TRAVEL BOOKING RECEIPT
==================================================
Booking Reference: {bk['booking_id']}
Booking Timestamp: {bk['booked_at']}
Booking Status   : {bk['status']}

PASSENGER DETAILS:
- Lead Passenger : {bk['passenger_name']}
- Contact Email  : {bk['contact']}
- Mobile Phone   : {bk['phone']}

TRIP DETAILS:
- Destination    : {bk['destination']} ({bk['state']})
- Departure Date : {bk['travel_date']}
- Duration       : {bk['days']} Days
- Travellers     : {bk['travelers']} Person(s)
- Package Tier   : {bk['tier']}
- Transit Choice : {bk['transport']}
- Add-on Benefits: {', '.join(bk['addons'])}

PAYMENT SUMMARY:
- Total Paid     : ₹{bk['total_amount']:,} (All Inclusive)

IMPORTANT NOTICE:
Please carry this digital or printed pass along with a valid Government
Photo ID at check-in. Free cancellations available up to 48 hours before travel.
=================================================="""

        st.download_button(
            label="📥 Download Official Boarding Pass & Receipt (.txt)",
            data=ticket_receipt,
            file_name=f"{bk['booking_id']}_receipt.txt",
            mime="text/plain",
            key="dl_official_ticket"
        )

# =========================================================================
# TAB 4: MY BOOKINGS HISTORY
# =========================================================================
with tab_my_bookings:
    st.header("📋 Your Travel Bookings")
    st.write(f"Showing all active and recorded trip bookings ({len(st.session_state.bookings)} found).")

    if not st.session_state.bookings:
        st.info("You do not have any active travel bookings yet. Use the **'Find My Travel'** or **'Book Travel Package'** tab to book your first adventure!")
    else:
        for idx, item in enumerate(st.session_state.bookings):
            with st.container(border=True):
                c_a, c_b, c_c = st.columns([3, 2, 2])
                with c_a:
                    st.markdown(f"### {item['destination']}")
                    st.caption(f"Ref: **`{item['booking_id']}`** • Passenger: **{item['passenger_name']}**")
                    st.write(f"📅 **Date:** {item['travel_date']} • **Duration:** {item['days']} Days • **Guests:** {item['travelers']}")
                
                with c_b:
                    st.write(f"🏨 **Package:** {item['tier']}")
                    st.write(f"🚗 **Transit:** {item['transport']}")
                    st.write(f"🛡️ **Addons:** {', '.join(item['addons'])}")
                
                with c_c:
                    st.metric("Total Paid", f"₹{item['total_amount']:,}", delta=item["status"])
                    if st.button("Cancel Booking ❌", key=f"cancel_bk_{idx}"):
                        st.session_state.bookings.pop(idx)
                        st.rerun()

# Extra Interactive Feature: Smart Packing Checklist
st.divider()
with st.expander("🧳 Smart Travel Packing Checklist (Click to view)"):
    st.markdown("Here is your essential packing checklist based on trip type:")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("**Essential Documents & Gear**")
        st.checkbox("Government Photo ID (Aadhaar / Voter ID / Passport)", value=True, key="chk_id")
        st.checkbox("Power Bank & Phone Charger", value=True, key="chk_pwr")
        st.checkbox("Emergency cash & UPI apps", value=True, key="chk_cash")
        st.checkbox("Personal medication kit", value=True, key="chk_med")
    with c2:
        st.markdown("**Clothing & Comfort**")
        st.checkbox("Comfortable walking sneakers / sandals", value=True, key="chk_shoes")
        st.checkbox("Quick-dry lightweight clothing", value=True, key="chk_clothes")
        st.checkbox("Sunglasses & Sunscreen SPF 50+", value=True, key="chk_sun")
        st.checkbox("Light jacket / shawl for AC buses & evening breeze", key="chk_jkt")
    with c3:
        st.markdown("**Trip Extras**")
        st.checkbox("Water bottle (stay hydrated)", value=True, key="chk_bottle")
        st.checkbox("Rain cover / compact umbrella", key="chk_umb")
        st.checkbox("Offline Google Maps downloaded", key="chk_map")
        st.checkbox("Mini backpack for day outings", value=True, key="chk_pack")

# Footer
st.markdown("---")
f_col1, f_col2 = st.columns([3, 1])
with f_col1:
    st.caption("✨ **WanderLust AI Travel Agent & Booking Platform** • Built with Python & Streamlit • Fast, responsive, and completely free.")
with f_col2:
    st.caption("Developed for Academic & Student Project Demo")
