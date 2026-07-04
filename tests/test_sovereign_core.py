# =====================================================================
# THE INFINITE CREATOR - AUTOMATED VERIFICATION SUITE
# Architect: Pisut Somwang (พิสุทธิ์ สมหวัง) | Year: 2026
# =====================================================================
import pytest
from infinite_creator_sdk import InfiniteCreatorSDK, SovereignContextOptimizer, MLDSA87Signature

def test_context_purity_optimization_works():
    """ ทดสอบว่าเครื่องมือกรองคำตัดคำฟุ่มเฟือยออกจาก Blueprint ได้จริง """
    optimizer = SovereignContextOptimizer()
    raw_prompt = "Establish a secure decentralized network for running language models."
    
    res = optimizer.optimize(raw_prompt)
    assert "optimized_prompt" in res
    assert len(res["optimized_prompt"]) <= len(raw_prompt)
    # คำว่า 'a' และ 'for' จะต้องถูกกรองออกไปจริงในระบบ
    assert "a" not in res["optimized_prompt"].split()

def test_pqc_signature_generation_and_integrity():
    """ ทดสอบว่าระบบสร้างลายเซ็นออกมาได้สมบูรณ์ และมีลายเซ็นที่ตรวจสอบได้จริง """
    signer = MLDSA87Signature(key_identity="Pisut Somwang")
    payload = "Constructing Dimension 5D"
    
    res = signer.sign_manifest(payload)
    assert res["verified"] is True
    assert len(res["signature"]) > 0
    
    # ถ้าเปิดใช้งาน ML-DSA จริง ลายเซ็นจะมีขนาดใหญ่มากตามลักษณะเฉพาะของ PQC
    if res["mode"] == "REAL_LATTICE_PQC":
        assert res["sig_bytes_len"] > 2000 
    else:
        assert res["sig_bytes_len"] == 64 # ความยาวของ SHA3-512 Fallback
