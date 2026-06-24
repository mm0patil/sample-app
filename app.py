import streamlit as st
import pandas as pd
import json
from datetime import datetime


st.set_page_config(
    page_title="AV Operations Command Center",
    page_icon="🎛️",
    layout="wide"
)

st.title("🎛️ AV Operations Command Center")
st.markdown("---")


@st.cache_data
def load_data():
    # Reading our two "spreadsheets"
    inventory_df = pd.read_csv("inventory.csv")
    schedules_df = pd.read_csv("schedules.csv")
    return inventory_df, schedules_df

try:
    inventory_df, schedules_df = load_data()
except FileNotFoundError:
    st.error("Data files missing! Please ensure 'inventory.csv' and 'schedules.csv' are in the same folder.")
    st.stop()


st.sidebar.header("🔐 User Authentication")
user_role = st.sidebar.selectbox(
    "Select your login role:",
    options=["Technician (Role A)", "Manager (Role B)"],
    index=0
)


is_manager = (user_role == "Manager (Role B)")


if is_manager:
    st.sidebar.success("Logged in as: **MANAGER**\n\nPermissions: Read + Write (Device Control Enabled)")
else:
    st.sidebar.info("Logged in as: **TECHNICIAN**\n\nPermissions: Read-Only")


st.header("📊 Unified Data Dashboard")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Spreadsheet A: AV Equipment Inventory")
    st.dataframe(inventory_df, use_container_width=True, hide_index=True)

with col2:
    st.subheader("Spreadsheet B: Staff Shift Schedules")
    st.dataframe(schedules_df, use_container_width=True, hide_index=True)

st.markdown("---")


st.header("⚡ Device Control Panel")

if not is_manager:
    
    st.warning("🔒 Access Denied: Device commands are restricted to **Manager (Role B)** level users only.")
else:
    
    st.success("🔓 Access Granted: Device control module unlocked.")
    
    col_ctrl1, col_ctrl2 = st.columns([1, 2])
    
    with col_ctrl1:
        st.write("### Configure Payload")
        # Target a device dynamically pulled from Spreadsheet A
        target_device = st.selectbox(
            "Select Target Device:",
            options=inventory_df["device_id"] + " - " + inventory_df["device_name"]
        )
        
        
        device_id = target_device.split(" - ")[0]
        
        device_loc = inventory_df[inventory_df["device_id"] == device_id]["location"].values[0]
        
        # Select action parameters
        command_action = st.selectbox(
            "Select Command Execution:",
            options=["power_on", "power_off", "mute_audio", "unmute_audio", "reboot"]
        )
        
        trigger_btn = st.button("🚀 Trigger Device Command", type="primary")

    with col_ctrl2:
        st.write("### Simulated Live JSON Output Terminal")
        
        if trigger_btn:
            # Construct JSON Control Payload dynamically
            payload = {
                "status": "success",
                "timestamp": datetime.now().isoformat() + "Z",
                "triggered_by": "Manager_User",
                "device_control": {
                    "device_id": device_id,
                    "location": device_loc,
                    "command": command_action
                }
            }
            
            st.code(json.dumps(payload, indent=2), language="json")
        else:
            st.info("Awaiting execution... Select a device configuration and press 'Trigger Device Command'.")