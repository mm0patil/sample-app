### Project Submission: AV Equipment & RBAC Control Prototype

Hi ,

I have completed the prototype application demonstrating data integration, Role-Based Access Control (RBAC), and serialized JSON device control. 

I chose a Python + Streamlit stack for this implementation to ensure an interactive, responsive UI paired with clean session-state security logic.

#### 🔗 Project Access
* **Live Application URL:** https://sample-app-55cpxo84ogc23epiw87ppr.streamlit.app/
* **Code Repository:** https://github.com/mm0patil/sample-app

---

#### 🧪 Step-by-Step Testing Guide

1. **Review the Unified Data View:**
   Upon loading the dashboard, you will observe a unified view displaying data aggregated from two separate sources: Spreadsheet A (AV Equipment Inventory) and Spreadsheet B (Staff Shift Schedules). Both tables are dynamically mapped to show relational spatial contexts (Rooms/Zones).

2. **Test Role A (Technician) Permissions:**
   * In the left sidebar, ensure the login role is set to **"Technician (Role A)"**.
   * Observe the "Device Control Panel" at the bottom. The application actively enforces a read-only state, presenting an access-denied warning and completely restricting any command triggers.

3. **Test Role B (Manager) Permissions & JSON Control:**
   * Switch the sidebar login role to **"Manager (Role B)"**.
   * The security layer dynamically unlocks the execution module. 
   * Select a target hardware component from the dynamic dropdown (which actively parses its structural metadata from the inventory dataset).
   * Choose an execution method (e.g., `power_on`, `mute_audio`) and click **"Trigger Device Command"**.

4. **Verify the Generated JSON Payload:**
   * Upon clicking the button, view the dark **Simulated Live JSON Output Terminal** box on the right. 
   * It instantly compiles and prints a strictly validated, standard-compliant serialized JSON payload containing real-time timestamps, operator credentials, and localized payload routing arrays—simulating a live edge-device API transmission.
