# 🗺️ NEXUM Technical Context & Flow Map

### 1. The Entry Point (`main.py`)
- Logic: Authenticates the Maestro using `ADMIN_ID` and `MASTER_KEY`.
- Context: Acts as the secure firewall for all incoming commands. It routes requests to the Governor Agent.

### 2. The Heartbeat (`system_core/engine/pulse.go`)
- Logic: Utilizes Go's concurrency (Goroutines) to open persistent WebSockets.
- Context: Why Go? To handle massive data streams without blocking the AI logic, ensuring the UI always reflects live prices.

### 3. The Brain (`system_core/nexum_kernel.py`)
- Logic: Dynamic HTML generation and ZKP (Zero-Knowledge Proof) coordination.
- Context: This is where the "Sovereignty" happens. It ensures that the UI is always branded correctly as NEXUM.

### 4. The Shield (`Dockerfile` / `docker-compose.yml`)
- Logic: Environment isolation.
- Context: Guarantees that the project can scale globally on any cloud provider (Google, AWS, Azure) without "dependency hell".

---
Founded By
Mutaz Ismail Tailakh — Master Architect of Sovereign Systems.
<p align="center">
SECURED BY NEXUM-SHIELD PROTOCOL v0.7.1
</p>
