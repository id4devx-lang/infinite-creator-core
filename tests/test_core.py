# =====================================================================
# THE INFINITE CREATOR - AUTOMATED VERIFICATION SUITE
# Architect: Pisut Somwang | Year: 2026
# =====================================================================
import pytest
from infinite_creator_sdk import InfiniteCreatorSDK, SovereignContextOptimizer, MLDSA87Signature

def test_context_purity_optimization_works():
    """ Test that the optimizer strips filler words from the blueprint """
    optimizer = SovereignContextOptimizer()
    raw_prompt = "Establish a secure decentralized network for running language models."
    
    res = optimizer.optimize(raw_prompt)
    assert "optimized_prompt" in res
    assert len(res["optimized_prompt"]) <= len(raw_prompt)
    assert "a" not in res["optimized_prompt"].split()

def test_pqc_signature_generation_and_integrity():
    """ Test PQC signature generation and size boundaries """
    signer = MLDSA87Signature(key_identity="Pisut Somwang")
    payload = "Constructing Dimension 5D"
    
    res = signer.sign_manifest(payload)
    assert res["verified"] is True
    assert len(res["signature"]) > 0
    
    if res["mode"] == "REAL_LATTICE_PQC":
        assert res["sig_bytes_len"] > 2000 
    else:
        assert res["sig_bytes_len"] == 64
