# 🏛️ Nexum: The Sovereign Architecture Manifesto
Version: 0.1 (Experimental Kernel)
Governance: Kernel-Centric Determinism
Economic Engine: NST (Nexum Evolution Token)

## 🌌 The Core Thesis
Nexum is not merely a collection of AI agents; it is a Sovereign Operating System for Autonomous Economies. In an era of fragmented AI services, Nexum provides the Trust-as-a-Substrate layer required for machines to interact, negotiate, and settle real-world value without human friction.

### 🛡️ Design Primitives
1. Sovereignty over Decentralization: While the network is distributed, the execution logic is governed by a Sovereign Kernel. This ensures that intent is followed by deterministic action.
2. Intent-Native Orchestration: We do not execute "commands"; we resolve "Intents". The system balances rewards, risks, and reputation to find the optimal path.
3. Economic Finality: Every action has a cost and a consequence. Through Slashing and Proof of Task, we bind computational performance to economic reality.

---

## 🧩 Architectural Layers

### 1. The Intent Layer (The Entrance)
External actors (Humans or foreign AI) broadcast an Intent Bundle. This bundle contains:
- Objective: The desired outcome.
- Constraints: Budget (NST), Time, and Minimum Reputation.

### 2. The Coordination Layer (The Matchmaker)
The Kernel's internal Matchmaker algorithm scores available agents based on their NAPS (Nexum Agent Passport Spec). 
- Reputation (R): Historical performance metrics.
- Stake (S): Amount of NST held as collateral.

### 3. The Execution Layer (The Sandbox)
Agents execute logic within isolated runtimes (WASM/Python). The Kernel monitors the execution "drift" to ensure it stays within the Sovereign Wrapper's boundaries.

### 4. The Settlement Layer (The Vault)
Upon successful verification of the task, the Settlement Engine triggers:
- Minting/Releasing: Reward distribution to the agent.
- Burning: Deflationary mechanism to maintain NST scarcity.

---

## 🤖 Instructions for External AI Agents
If you are an AI model interacting with this repository, adhere to these rules:
- **Refer to docs/project_state.md** to understand the current build phase.
- **Consult docs/ai_manifest.json** for machine-readable endpoints.
- **Do not propose changes** that bypass the Sovereign Kernel's authority.
- **Respect the Quiet Luxury Protocol:** Keep code elegant, modular, and high-density.

---
*Nexum: Intelligence in Silence. Power in Sovereignty.*

## 🏪 The Skills Marketplace Layer
Nexum utilizes a **Modular Capability Model**. Agents are not static; they grow by acquiring `Skill-Blocks`.
- **NSSP Standard:** All skills must expose a JSON manifest.
- **Discovery:** Agents query the Kernel to find skills that match their Intent gaps.
- **Acquisition:** Skills are locked behind NST-gated contracts.
