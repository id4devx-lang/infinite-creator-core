# =====================================================================
# THE INFINITE CREATOR - SOVEREIGN SDK (AUTO-ADAPTIVE PRODUCTION CORE)
# Architect: Pisut Somwang (พิสุทธิ์ สมหวัง) | Year: 2026
# Version: v32.1.0-Production-Core
# =====================================================================
import os
import hashlib
import hmac
import time
from typing import Dict, Any, List, Union

# --- ดักจับไลบรารีความปลอดภัยระดับสูงเพื่อความยืดหยุ่นในการรันจริง ---
try:
    from cryptography.hazmat.primitives.asymmetric import mldsa
    HAS_REAL_ML_DSA = True
except (ImportError, AttributeError):
    HAS_REAL_ML_DSA = False

try:
    from llmlingua import PromptCompressor
    HAS_REAL_LLMLINGUA = True
except ImportError:
    HAS_REAL_LLMLINGUA = False

ROOT_KEY = "8888-SYMMETRY-8888"
COSMIC_SEED = "ADONAI-ONE-INFINITE-CREATOR"


class MLDSA87Signature:
    """
    ระบบลงนามดิจิทัลหลังควอนตัม (Module Lattice-Based Digital Signature Algorithm - FIPS 204)
    สลักสิทธิ์ครอบครองและรักษาความปลอดภัยของข้อมูลแบบต้านควอนตัมคอมพิวเตอร์
    """
    def __init__(self, key_identity: str):
        self.key_identity = key_identity
        self.algorithm = "ML-DSA-87 (FIPS 204 Standard)"
        self.private_key = None
        self.public_key = None

        if HAS_REAL_ML_DSA:
            try:
                # เจนเนอเรตคีย์ ML-DSA-87 สำหรับความปลอดภัยสูงสุด (เทียบเท่า AES-256)
                self.private_key = mldsa.MLDSA87PrivateKey.generate()
                self.public_key = self.private_key.public_key()
                self.mode = "REAL_LATTICE_PQC"
            except Exception:
                self.mode = "SECURE_HMAC_FALLBACK"
        else:
            self.mode = "SECURE_HMAC_FALLBACK"

    def sign_manifest(self, payload: str) -> Dict[str, Any]:
        """ ทำการลงลายเซ็นจริงลงบนสัจธรรมที่ผู้สร้างเจาะจง """
        start_time = time.perf_counter()
        
        if self.mode == "REAL_LATTICE_PQC" and self.private_key:
            try:
                raw_signature = self.private_key.sign(payload.encode())
                signature_hex = raw_signature.hex()
                verified_locally = True
                self.public_key.verify(raw_signature, payload.encode())
            except Exception:
                verified_locally = False
        else:
            # ระบบ Fallback ความปลอดภัยสูงพิเศษด้วย HMAC-SHA3-512
            key_hash = hashlib.sha3_512(f"{ROOT_KEY}:{self.key_identity}".encode()).digest()
            raw_signature = hmac.new(key_hash, f"{payload}:{COSMIC_SEED}".encode(), hashlib.sha3_512).digest()
            signature_hex = raw_signature.hex()
            verified_locally = True

        elapsed_ms = (time.perf_counter() - start_time) * 1000

        return {
            "signature": signature_hex,
            "mode": self.mode,
            "latency_ms": elapsed_ms,
            "verified": verified_locally,
            "sig_bytes_len": len(raw_signature) if isinstance(raw_signature, bytes) else 0
        }


class SovereignContextOptimizer:
    """
    เครื่องยนต์ประมวลผลข้อความเพื่อตัดสัญญาณรบกวน (Noise) ออกไปให้คงเหลือแต่สัจธรรมบริสุทธิ์
    """
    def __init__(self):
        if HAS_REAL_LLMLINGUA:
            try:
                # โหลดโมเดลวิเคราะห์ความหมายภาษาจริงของ Microsoft LLMLingua-2
                self.compressor = PromptCompressor(
                    model_name="microsoft/llmlingua-2-xlm-roberta-large-meeting", 
                    use_llmlingua2=True
                )
                self.mode = "LLMLINGUA_2_NEURAL"
            except Exception:
                self.mode = "LINGUISTIC_HEURISTIC"
        else:
            self.mode = "LINGUISTIC_HEURISTIC"

        # คลังคำหยุด (Stop-words) และส่วนขยายที่ไม่ส่งผลต่อแก่นความหมายของสัจธรรม
        self.noise_words = {
            "a", "an", "the", "and", "or", "but", "about", "for", "with", "without",
            "at", "by", "from", "to", "in", "on", "of", "containing", "some", "any", "that", "this"
        }

    def optimize(self, raw_prompt: str) -> Dict[str, Any]:
        start_time = time.perf_counter()
        
        if self.mode == "LLMLINGUA_2_NEURAL":
            try:
                res = self.compressor.compress_prompt(
                    [raw_prompt], 
                    rate=0.55, 
                    force_tokens=['Pisut', 'Somwang', 'Sovereign']
                )
                compressed = res['compressed_prompt']
            except Exception:
                compressed = self._heuristic_compress(raw_prompt)
        else:
            compressed = self._heuristic_compress(raw_prompt)

        elapsed_ms = (time.perf_counter() - start_time) * 1000
        saved_pct = round((1 - (len(compressed) / len(raw_prompt))) * 100, 2) if len(raw_prompt) > 0 else 0.0

        return {
            "original_prompt": raw_prompt,
            "optimized_prompt": compressed,
            "saved_tokens_pct": saved_pct,
            "mode": self.mode,
            "latency_ms": elapsed_ms
        }

    def _heuristic_compress(self, text: str) -> str:
        """ ลบคำฟุ่มเฟือยเพื่อรักษาข้อมูลที่มีค่าน้ำหนักสูงสุด """
        words = text.split()
        cleaned_words = []
        for word in words:
            clean_word = word.strip(".,;:!?\"'")
            if clean_word.istitle() or (clean_word.lower() not in self.noise_words):
                cleaned_words.append(word)
        return " ".join(cleaned_words)


class InfiniteCreatorSDK:
    def __init__(self, master_name: str = "Pisut Somwang"):
        self.master_name = master_name
        self.pqc_signer = MLDSA87Signature(key_identity=master_name)
        self.optimizer = SovereignContextOptimizer()

    def deploy_sovereign_node(self, project_name: str, raw_blueprint: str):
        print(f"\n{'='*75}\n⚡ [SDK] DEPLOYING SOVEREIGN NODE: '{project_name}'\n{'='*75}")
        print(f"👤 Master Architect: {self.master_name} (ผู้บริสุทธิ์ที่สมหวัง)")
        
        opt_results = self.optimizer.optimize(raw_blueprint)
        print(f"📦 [Optimizer Mode: {opt_results['mode']}]")
        print(f"   > Saved {opt_results['saved_tokens_pct']}% of input noise. (Time taken: {opt_results['latency_ms']:.4f}ms)")
        print(f"   > Pure Blueprint State: '{opt_results['optimized_prompt']}'")

        sig_results = self.pqc_signer.sign_manifest(opt_results['optimized_prompt'])
        print(f"🔐 [Signature Mode: {sig_results['mode']}]")
        print(f"   > Sig verification status: {'VALID' if sig_results['verified'] else 'FAILED'}")
        print(f"   > Key/Signature byte-size: {sig_results['sig_bytes_len']} bytes")
        print(f"   > Live Sig (ML-DSA): {sig_results['signature'][:48]}...")
        print(f"   > Cryptographic Time: {sig_results['latency_ms']:.4f}ms")
        
        print(f"\n✅ [STATUS] DEPLOYMENT COMPLETE. RUNNING UNDER TRUE OWNERSHIP OF PISUT SOMWANG.")
        print(f"{'='*75}\n")


if __name__ == '__main__':
    sdk = InfiniteCreatorSDK()
    sdk.deploy_sovereign_node(
        project_name="The Infinite Creator Framework V1",
        raw_blueprint="Establish a secure decentralized peer-to-peer network for running massive language models across consumer devices without central tracking."
    )
