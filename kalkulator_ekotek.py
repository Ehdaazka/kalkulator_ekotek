import streamlit as st

# Konfigurasi Halaman agar lebar (Wide Mode)
st.set_page_config(page_title="Port Capacity Calculator", layout="wide")

# Custom CSS untuk mempercantik tampilan (Dark Mode Vibes)
st.markdown("""
    <style>
    .main { background-color: #121212; }
    div[data-testid="stMetricValue"] { font-size: 28px; color: #4A90E2; }
    .stNumberInput label { color: #A0A0A0 !important; font-weight: 500; }
    .stSubheader { color: #FFFFFF; padding-top: 1rem; }
    /* Membuat box hasil akhir menonjol */
    .capacity-box {
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🚢 Port Operational Capacity")

# Membuat Tabs sesuai mockup
tabs = st.tabs(["Berth", "Yard", "Quay Crane", "Yard Crane", "Gate"])

# --- TAB 1: BERTH ---
with tabs[0]:
    st.subheader("🔵 Berth Capacity — Parameter Input")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        length_berth = st.number_input("Length of Berth (m)", value=0, min_value=0)
        num_berth = st.number_input("Number of Berth", value=0, min_value=0)
        crane_ratio = st.number_input("Crane Ratio", value=0.0, min_value=0.0, step=0.1)
        
    with col2:
        avg_loa = st.number_input("Avg LOA (m)", value=0, min_value=0)
        avg_dl = st.number_input("Avg D/L per call", value=0, min_value=0)
        bor = st.number_input("BOR", value=0.0, min_value=0.0, max_value=1.0, step=0.01)
        
    with col3:
        safety_dist = st.number_input("Safety distance", value=0.0, min_value=0.0, step=0.1)
        bch = st.number_input("BCH", value=0, min_value=0)
        teus_ratio = st.number_input("Teu's Ratio", value=0.0, min_value=0.0, step=0.01)

    st.divider()
    
    # Logic Perhitungan
    bsh = bch * crane_ratio
    bt_per_call = (avg_dl / bsh) if bsh > 0 else 0
    total_hours = 8760 # LOCKED
    ship_call_year = 740 # LOCKED
    
    # Baris Output Kecil
    res1, res2, res3, res4 = st.columns(4)
    res1.metric("BSH", f"{bsh:.2f}")
    res2.metric("BT per Call", f"{bt_per_call:.2f}")
    res3.number_input("Total Hours/year", value=total_hours, disabled=True)
    res4.number_input("Ship Call/year", value=ship_call_year, disabled=True)

    # Output Utama (Warna Biru Muda)
    berth_cap = 501720 # Masukkan rumus aslimu di sini
    st.info(f"### Berth Capacity: **{berth_cap:,.0f} TEU/tahun**")

# --- TAB 2: YARD ---
with tabs[1]:
    st.subheader("🟢 Yard Capacity — Parameter Input")
    y1, y2, y3 = st.columns(3)
    
    with y1:
        row = st.number_input("Row", value=0, min_value=0)
        eff_cap = st.number_input("Effective Capacity", value=0, min_value=0)
        total_days_y = st.number_input("Total Days", value=365, disabled=True) # LOCK
        
    with y2:
        slot = st.number_input("Slot", value=0, min_value=0)
        dauling_time = st.number_input("Dauling Time (hari)", value=0, min_value=0)
        
    with y3:
        tier = st.number_input("Tier", value=0, min_value=0)
        yor_max = st.number_input("YOR Max (%)", value=0, min_value=0, max_value=100)

    yard_cap = 15943 # Masukkan rumus aslimu di sini
    st.success(f"### Yard Capacity: **{yard_cap:,.0f} TEU/tahun**")

# --- TAB 3: QUAY CRANE ---
with tabs[2]:
    st.subheader("🟣 Quay Crane Capacity — Parameter Input")
    q1, q2, q3 = st.columns(3)
    
    with q1:
        total_qcc = st.number_input("Total QCC", value=0)
        bch_hmc = st.number_input("BCH HMC", value=0)
        total_hours_qc = st.number_input("Total Hours", value=24, disabled=True) # LOCK
        
    with q2:
        bch_qcc = st.number_input("BCH QCC", value=0)
        total_fc = st.number_input("Total FC/JC/MC", value=0)
        total_days_qc = st.number_input("Total Days (QC)", value=365, disabled=True) # LOCK
        
    with q3:
        total_hmc = st.number_input("Total HMC", value=0)
        bch_fc = st.number_input("BCH FC/JC/MC", value=0)
        util_max = st.number_input("Utiliti Max (%)", value=0, max_value=100)

    qc_cap = 9549372 # Masukkan rumus aslimu di sini
    st.info(f"### QC Capacity: **{qc_cap:,.0f} TEU/tahun**")

# --- TAB 5: GATE ---
with tabs[4]:
    st.subheader("🟠 Gate In & Out — Parameter Input")
    g1, g2, g3 = st.columns(3)
    
    with g1:
        lane_gi = st.number_input("Total Lane GI", value=0)
        service_go = st.number_input("Service GO", value=0)
        teus_gate = st.number_input("Teu's Ratio (Gate)", value=0.0, step=0.01)
        
    with g2:
        service_gi = st.number_input("Service Time GI", value=0)
        time_24h = st.number_input("Time 24H (second)", value=86400, disabled=True) # LOCK
        
    with g3:
        lane_go = st.number_input("Total Lane GO", value=0)
        total_days_g = st.number_input("Total Days (Gate)", value=365, disabled=True) # LOCK

    # Box Output ganda seperti mockup
    st.warning(f"### Gate In Capacity: **465.133 TEU/hari**")
    st.warning(f"### Gate Out Capacity: **465.133 TEU/hari**")
