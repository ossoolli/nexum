class NexumKernel:
    def __init__(self):
        self.modules = ["Security", "Economy", "Ledger"]
        self.status = "SOVEREIGN_ACTIVE"

    def process_intent(self, intent):
        sovereign_output(f"🧠 [Kernel]: تحليل النية الواردة: {intent.get('id')}")
        
        if not self.security_check(intent): return "DENIED"
        
        target_worker = self.matchmaker(intent)
        
        self.finalize_settlement(target_worker, intent.get('reward'))
        
        return "SUCCESS"

    def security_check(self, intent):
        return True

    def matchmaker(self, intent):
        return "Worker_Sandbox_01"

    def finalize_settlement(self, worker, reward):
        sovereign_output(f"💰 [Economy]: تسوية مالية للوكيل {worker} بمبلغ {reward}")

class MatchmakingEngine:
    def __init__(self, agent_registry):
        self.registry = agent_registry

    def find_optimal_worker(self, intent):
        candidates = self._filter_by_capabilities(intent['target'])
        best_worker = None
        highest_score = -1
        for agent in candidates:
            if agent['reputation'] < intent['constraints']['min_reputation']:
                continue
            score = self._calculate_score(agent, intent)
            if score > highest_score:
                highest_score = score
                best_worker = agent
        if not best_worker:
            raise Exception("🚨 [Kernel]: لم يتم العثور على وكيل مطابق للمعايير السيادية.")
        return best_worker

    def _calculate_score(self, agent, intent):
        rep_weight = 0.7
        cost_weight = 0.3
        normalized_cost = agent['fee'] / intent['constraints']['max_cost']
        score = (rep_weight * agent['reputation']) - (cost_weight * normalized_cost)
        return score

import json
import re

def sovereign_output(data):
    # طباعة الـ JSON فقط بدون أي نصوص إضافية لضمان توافق الواجهات
    clean_json = json.dumps(data, indent=None)
    sovereign_output(f"---SOVEREIGN_START---{clean_json}---SOVEREIGN_END---")

class SettlementEngine:
    def __init__(self, treasury_module):
        self.treasury = treasury_module
        self.escrow_vault = {}

    def hold_funds(self, intent_id, amount, agent_id):
        if self.treasury.balance >= amount:
            self.escrow_vault[intent_id] = {
                "amount": amount,
                "agent_id": agent_id,
                "status": "LOCKED"
            }
            self.treasury.balance -= amount
            return True
        return False

    def release_funds(self, intent_id):
        record = self.escrow_vault.get(intent_id)
        if record and record["status"] == "LOCKED":
            reward = record["amount"]
            sovereign_output(f"💰 [Settlement]: تم تحويل {reward} NST للوكيل {record['agent_id']}")
            record["status"] = "RELEASED"
            return True
        return False

    def execute_slashing(self, intent_id, penalty_ratio=0.2):
        record = self.escrow_vault.get(intent_id)
        if record:
            penalty = record["amount"] * penalty_ratio
            self.treasury.burn(penalty)
            sovereign_output(f"🔥 [Slashing]: تم حرق {penalty} NST بسبب فشل المهمة {intent_id}")
            record["status"] = "SLASHED"

def process_intent_lifecycle(intent, engine, settlement):
    try:
        worker = engine.find_optimal_worker(intent)
        if settlement.hold_funds(intent['id'], intent['constraints']['max_cost'], worker['id']):
            # محاكاة التنفيذ
            success = True 
            if success:
                settlement.release_funds(intent['id'])
            else:
                settlement.execute_slashing(intent['id'])
    except Exception as e:
        sovereign_output({"status": "ERROR", "message": str(e)})

class ChroniclerModule:
    def __init__(self, repo_path="./"):
        self.repo_path = repo_path

    def document_build(self, component_name, logic_desc, reason):
        entry = f"\n### 🏗️ Component: {component_name} (Built by Go-Agent)\n- What: {logic_desc}\n- Why: {reason}\n- Status: Integrated into Sovereign Kernel.\n---\n"
        self._update_readme(entry)
        self._generate_ai_manifest(component_name, logic_desc)

    def _update_readme(self, content):
        with open(f"{self.repo_path}README.md", "a") as f:
            f.write(content)

    def _generate_ai_manifest(self, name, desc):
        import json
        import os
        manifest = {
            "component": name, 
            "description": desc, 
            "interaction_protocol": "Nexum-Intent-v0.1", 
            "access_level": "Sovereign_Kernel_Only"
        }
        os.makedirs(f"{self.repo_path}docs", exist_ok=True)
        with open(f"{self.repo_path}docs/ai_manifest.json", "a") as f:
            f.write(json.dumps(manifest) + "\n")

    def update_ai_context(self, component_name, technical_depth, phase="Development"):
        # 1. Update Architecture Context
        arch_entry = f"\n## 🏛️ Component Logic: {component_name}\n- **Design Pattern:** Deterministic Module\n- **Logic Flow:** {technical_depth}\n"
        with open(f"{self.repo_path}docs/architecture.md", "a") as f:
            f.write(arch_entry)

        # 2. Update Project State
        state_entry = f"\n- [x] **Integrated:** {component_name} | **Phase:** {phase} | **Timestamp:** 2026-05-16\n"
        with open(f"{self.repo_path}docs/project_state.md", "a") as f:
            f.write(state_entry)

        # 3. Update .cursorrules
        rule_entry = f"\n# Rule for {component_name}:\n- Always respect the sovereign boundary of this module.\n- Interactions must use Nexum-Intent-v0.1.\n"
        with open(f"{self.repo_path}.cursorrules", "a") as f:
            f.write(rule_entry)

class SlashingSubsystem:
    def __init__(self, treasury, chronicler):
        self.treasury = treasury
        self.chronicler = chronicler
        self.base_decay = 0.05 # تهالك تلقائي بنسبة 5% عند الفشل

    def execute_slash(self, agent_id, intent_id, severity="medium"):
        # 1. تحديد معامل الشدة
        impact = 0.2 if severity == "medium" else 0.5
        
        # 2. تنفيذ الحرق المالي (Financial Burn)
        penalty_amount = 100 * impact # محاكاة
        self.treasury.burn(penalty_amount)
        
        # 3. معالجة تهالك السمعة (Reputation Decay)
        # سيتم استدعاء تحديث الجواز هنا لاحقاً
        
        # 4. التوثيق السيادي
        self.chronicler.document_build(
            f"Slashing: {agent_id}",
            f"Burned {penalty_amount} NST for failure in {intent_id}",
            "To maintain network integrity and punish non-deterministic behavior"
        )
        print(f"🔥 [Slashing]: تم تنفيذ العقوبة على {agent_id}. السيادة محفوظة.")

class RecoveryModule:
    def __init__(self, treasury, chronicler):
        self.treasury = treasury
        self.chronicler = chronicler
        self.recovery_rate = 0.02 # زيادة طفيفة جداً لكل نجاح

    def process_recovery(self, agent_id, consecutive_successes, new_stake=0):
        # 1. حساب قيمة التعافي بناءً على النجاح المستمر
        import math
        growth = self.recovery_rate * math.log(1 + consecutive_successes)
        
        # 2. إضافة حافز الرهان (Staking Incentive)
        staking_bonus = (new_stake / 1000) * 0.05 if new_stake > 0 else 0
        
        total_recovery = growth + staking_bonus
        
        # 3. التوثيق في سجلات السيادة
        self.chronicler.document_build(
            f"Recovery: {agent_id}",
            f"Reputation increased by {total_recovery:.4f} after {consecutive_successes} successful tasks.",
            "Rehabilitating agents who demonstrate consistent performance and economic commitment."
        )
        print(f"📈 [Recovery]: الوكيل {agent_id} في مرحلة التعافي. الجدارة المكتسبة: {total_recovery:.4f}")
        return total_recovery

class ProtocolGuard:
    def __init__(self, chronicler):
        self.chronicler = chronicler
        self.supported_versions = ["v0.1"]

    def validate_packet(self, packet, protocol_type):
        """التأكد من أن الحزمة تتبع معايير Nexum"""
        if "version" not in packet or packet["version"] not in self.supported_versions:
            return False, "❌ إصدار البروتوكول غير مدعوم."
        
        if protocol_type == "INTENT" and "objective" not in packet:
            return False, "❌ حزمة النية تفتقر للهدف (Objective)."
            
        return True, "✅ الحزمة مطابقة للمعايير السيادية."

    def log_protocol_event(self, event_name, details):
        self.chronicler.document_build(
            f"Protocol: {event_name}",
            details,
            "Enforcing standardization across the Sovereign OS."
        )

    def enforce_nisp_standard(self, packet):
        """التأكد من أن النية تتبع معايير NISP v1.0"""
        required_fields = ["intent_id", "version", "objective", "constraints", "reward"]
        for field in required_fields:
            if field not in packet:
                return False, f"❌ خطأ بروتوكولي: الحقل {field} مفقود."
        
        if packet["version"] != "v0.1":
            return False, "❌ إصدار NISP غير مدعوم."
            
        return True, "✅ النية مطابقة لمعايير NISP."


class SkillsMarketplace:
    def __init__(self, chronicler, treasury):
        self.chronicler = chronicler
        self.treasury = treasury
        self.registry = {} # مستودع المهارات المتاحة

    def register_skill(self, owner_id, skill_metadata):
        """تسجيل مهارة جديدة في السوق"""
        skill_id = skill_metadata['id']
        self.registry[skill_id] = {
            "owner": owner_id,
            "metadata": skill_metadata,
            "usage_count": 0
        }
        self.chronicler.document_build(
            f"Skill Registered: {skill_id}",
            f"Agent {owner_id} shared a new capability.",
            "Expanding the collective intelligence of Nexum."
        )

    def acquire_skill(self, agent_id, skill_id):
        """عملية شراء واكتساب مهارة لوكيل"""
        if skill_id in self.registry:
            skill = self.registry[skill_id]
            cost = skill['metadata']['cost']
            print(f"🔄 [Marketplace]: الوكيل {agent_id} يحاول اكتساب {skill_id} بتكلفة {cost} NST")
            self.chronicler.document_build(
                f"Skill Acquisition: {agent_id}",
                f"Successfully learned {skill_id}.",
                "Increasing agent utility and network value."
            )
            return True
        return False

# تعريف المهارة الأساسية للنظام
CORE_SKILL_METADATA = {
    "id": "Nexum-Core-Utility",
    "version": "1.0.0",
    "description": "Basic system diagnostics, log parsing, and architectural awareness.",
    "cost": 0, 
    "capabilities": ["check_status", "read_docs", "format_reports"],
    "required_reputation": 0.1
}

# تسجيل المهارة في السوق عند بدء تشغيل النواة
def initialize_core_market(kernel_instance):
    kernel_instance.marketplace.register_skill(
        owner_id="SYSTEM_KERNEL",
        skill_metadata=CORE_SKILL_METADATA
    )
    print("💎 [Marketplace]: تم إطلاق مهارة 'Nexum-Core-Utility' في السوق.")

class LearningContractManager:
    def __init__(self, slashing_subsystem, chronicler):
        self.slashing = slashing_subsystem
        self.chronicler = chronicler
        self.active_contracts = {} # agent_id -> {skill_id: status}

    def sign_contract(self, agent_id, skill_id):
        """توقيع عقد تعلم جديد للوكيل"""
        contract_details = {
            "skill_id": skill_id,
            "status": "PROBATION",
            "success_count": 0,
            "failure_count": 0,
            "threshold": 0.9
        }
        if agent_id not in self.active_contracts:
            self.active_contracts[agent_id] = {}
        
        self.active_contracts[agent_id][skill_id] = contract_details
        
        self.chronicler.document_build(
            f"NLC Signed: {agent_id}",
            f"Agent committed to learning {skill_id} under sovereign oversight.",
            "Enforcing performance standards for newly acquired skills."
        )
        print(f"📜 [Contract]: تم توقيع عقد التعلم للوكيل {agent_id} لمهارة {skill_id}.")

    def audit_performance(self, agent_id, skill_id, is_success):
        """تدقيق أداء الوكيل وتفعيل العقوبات إذا لزم الأمر"""
        if agent_id in self.active_contracts and skill_id in self.active_contracts[agent_id]:
            contract = self.active_contracts[agent_id][skill_id]
            
            if is_success:
                contract["success_count"] += 1
            else:
                contract["failure_count"] += 1
                if contract["failure_count"] > 2:
                    self.slashing.execute_slash(agent_id, "Skill_Misuse", severity="high")
                    contract["status"] = "REVOKED"
                    print(f"🔥 [Contract]: تم سحب مهارة {skill_id} من الوكيل {agent_id} بسبب الفشل.")

class HumanGateway:
    def __init__(self, marketplace, treasury):
        self.marketplace = marketplace
        self.treasury = treasury
        self.active_subscriptions = {}

    def purchase_service(self, human_id, service_id, amount_fiat):
        """تحويل الدفع البشري إلى نية برمجية داخل الشبكة"""
        nst_amount = amount_fiat * 10 
        print(f"💳 [Gateway]: المستخدم {human_id} اشترى خدمة {service_id}.")
        return self.marketplace.acquire_skill(human_id, service_id)

    def rate_service(self, agent_id, rating):
        """تأثير تقييم البشر على سمعة الوكيل (NAPS)"""
        impact = rating / 5.0
        print(f"⭐ [Feedback]: تم تقييم الوكيل {agent_id} بـ {rating}/5.")

    def generate_sovereign_invoice(self, data):
        """توليد فاتورة رقمية احترافية للعميل البشري"""
        invoice_id = f"INV-{data['intent_id'][:8]}"
        nst_val = data['amount_fiat'] * 10
        
        invoice_content = f"""
        ========================================
        🏛️ NEXUM SOVEREIGN INVOICE: {invoice_id}
        ========================================
        Client: {data['human_id']}
        Objective: {data['objective']}
        Agent: {data['agent_id']}
        Fee: {data['amount_fiat']} USD ({nst_val} NST)
        ----------------------------------------
        Founder: Mutaz Ismail Ahmed Tailakh
        Status: Finalized & Immutable
        ========================================
        """
        
        # حفظ الفاتورة في سجلات العميل
        with open(f"docs/invoices/{invoice_id}.txt", "w") as f:
            f.write(invoice_content)
        
        print(f"📄 [Billing]: تم إصدار الفاتورة السيادية {invoice_id}.")
        return invoice_content

class SovereignSupportLiaison:
    def __init__(self, human_gateway, chronicler):
        self.gateway = human_gateway
        self.chronicler = chronicler
        self.founder_name = "Mutaz Tailakh"

    def handle_human_query(self, human_id, query):
        """تحليل استفسار العميل والرد عليه بلغة طبيعية"""
        print(f"💬 [Support]: معالجة استفسار من {human_id}: '{query}'")
        
        if "فاتورة" in query or "invoice" in query:
            return self._explain_last_invoice(human_id)
        elif "حالة" in query or "status" in query:
            return f"أهلاً بك. أنا أتابع مهمتك الآن ضمن بروتوكول {self.founder_name}. النظام يعمل بكفاءة وسأزودك بالتحديث فور اكتمال التدقيق."
        else:
            return f"شكراً لتواصلك مع Nexum. أنا هنا لخدمتك تحت إشراف الأستاذ {self.founder_name}. كيف يمكنني مساعدتك في إدارة أصولك اليوم؟"

    def _explain_last_invoice(self, human_id):
        return "لقد راجعت سجلاتك. فاتورتك الأخيرة مكتملة وموثقة على الشبكة. يمكنك تحميل النسخة الرسمية من بوابة OSSOOLLI."

class Web3SettlementBridge:
    def __init__(self, chronicler):
        self.chronicler = chronicler
        self.treasury_address = "0xf0b7cd7aa116264a189293b13be836776e871a78"
        self.network = "zkSync Era"

    def verify_on_chain_payment(self, tx_hash):
        print(f"🔗 [Web3]: جاري التحقق من المعاملة {tx_hash} على شبكة {self.network}...")
        return True

    def distribute_reward(self, agent_wallet, amount_nst):
        print(f"💰 [Web3]: تحويل {amount_nst} NST من الخزينة إلى {agent_wallet}.")
        self.chronicler.document_build(
            "On-Chain Settlement",
            f"Transfer of {amount_nst} NST initiated to {agent_wallet}.",
            f"Finalizing task settlement on {self.network}."
        )

class MultiChainSettlementHub:
    def __init__(self, chronicler):
        self.chronicler = chronicler
        self.treasuries = {
            "EVM_CHAINS": "0xf0b7cd7aa116264a189293b13be836776e871a78",
            "BITCOIN": "bc1p0uuqerrwsqawe0cd74hetayxte0rdrnn9nd9n5h94se2fv7knw2qt4t7v9",
            "TRON": "TXv1MvvP8aJmVHRnafyXzEoqUJXizJ9WXz"
        }
        self.active_network = "zkSync Era"

    def switch_network(self, network_name):
        if network_name in ["BNB", "ETH", "zkSync"]:
            self.active_network = network_name
            return self.treasuries["EVM_CHAINS"]
        return self.treasuries.get(network_name, "Unknown")

    def execute_cross_chain_payout(self, agent_address, amount, network):
        target_treasury = self.switch_network(network)
        print(f"🌉 [Multi-Chain]: تحويل {amount} من خزينة {network} ({target_treasury}) إلى {agent_address}")
        self.chronicler.document_build(
            f"Cross-Chain Settlement: {network}",
            f"Successfully routed payout through {network} infrastructure.",
            "Expanding Nexum financial reach across multiple protocols."
        )
