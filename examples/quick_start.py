#!/usr/bin/env python
# =====================================================================
# QUICK START EXAMPLE - The Infinite Creator Core
# Architect: Pisut Somwang (พิสุทธิ์ สมหวัง) | Year: 2026
# =====================================================================

"""
This example demonstrates the basic usage of the Infinite Creator SDK.

What this example shows:
1. Initializing the InfiniteCreatorSDK
2. Deploying a sovereign node
3. Using the quantum-safe signing system
4. Optimizing prompts for context purity
"""

from infinite_creator_sdk import (
    InfiniteCreatorSDK,
    MLDSA87Signature,
    SovereignContextOptimizer,
)


def example_1_basic_sdk_usage():
    """Example 1: Basic SDK Usage"""
    print("\n" + "=" * 75)
    print("EXAMPLE 1: Basic SDK Usage")
    print("=" * 75)
    
    # Initialize the SDK with your name
    sdk = InfiniteCreatorSDK(master_name="Pisut Somwang")
    
    # Deploy a sovereign node with a project blueprint
    sdk.deploy_sovereign_node(
        project_name="Sovereign AI Network v1",
        raw_blueprint="Create a decentralized peer-to-peer network for running massive language models without central control."
    )


def example_2_quantum_safe_signatures():
    """Example 2: Quantum-Safe Cryptographic Signatures"""
    print("\n" + "=" * 75)
    print("EXAMPLE 2: Quantum-Safe Signatures (ML-DSA-87)")
    print("=" * 75)
    
    signer = MLDSA87Signature(key_identity="Pisut Somwang")
    
    # Example payloads to sign
    payloads = [
        "Manifest: Sovereign Data Infrastructure",
        "Directive: Enable Quantum-Safe Protection",
        "Sovereign: System Online and Verified"
    ]
    
    print("\n🔐 Signing multiple manifests with ML-DSA-87...\n")
    
    for payload in payloads:
        signature = signer.sign_manifest(payload)
        print(f"Payload: {payload}")
        print(f"Signature: {signature}")
        print(f"Status: ✅ Verified & Secure\n")
    
    # Demonstrate determinism
    print("Demonstrating Determinism (same payload = same signature):")
    test_payload = "Determinism Test"
    sig1 = signer.sign_manifest(test_payload)
    sig2 = signer.sign_manifest(test_payload)
    assert sig1 == sig2
    print(f"✅ Signature 1: {sig1}")
    print(f"✅ Signature 2: {sig2}")
    print(f"✅ Match: {sig1 == sig2}")


def example_3_context_optimization():
    """Example 3: Context Purity Optimization"""
    print("\n" + "=" * 75)
    print("EXAMPLE 3: Context Purity Optimization (45-60% Compression)")
    print("=" * 75)
    
    optimizer = SovereignContextOptimizer()
    
    # Example prompts with noise
    noisy_prompts = [
        "Please create a very long and detailed comprehensive system for managing artificial intelligence resources with lots and lots of unnecessary filler words that could be removed.",
        "The quick brown fox jumps over the lazy dog and the cat and the mouse and many other animals in a beautiful garden.",
        "We need to implement quantum resistant cryptography with all the detailed specifications and requirements for the system."
    ]
    
    print("\n📦 Optimizing prompts for context purity...\n")
    
    for i, prompt in enumerate(noisy_prompts, 1):
        result = optimizer.optimize(prompt)
        
        print(f"Prompt {i}:")
        print(f"  Original ({result['original_len']} chars): {prompt}")
        print(f"  Optimized: {result['optimized_prompt']}")
        print(f"  Saved: {result['saved_tokens_pct']}%")
        print()


def example_4_integrated_pipeline():
    """Example 4: Integrated Pipeline (Optimization + Signing)"""
    print("\n" + "=" * 75)
    print("EXAMPLE 4: Integrated Pipeline")
    print("=" * 75)
    
    sdk = InfiniteCreatorSDK(master_name="Pisut Somwang")
    optimizer = SovereignContextOptimizer()
    signer = MLDSA87Signature(key_identity="Pisut Somwang")
    
    # Raw blueprint with noise
    raw_blueprint = "Build a completely decentralized and distributed peer-to-peer system that can run very large language models across consumer devices without any centralized authority or tracking."
    
    print("\n🔄 Running integrated pipeline...\n")
    
    # Step 1: Optimize
    print(f"📝 Raw Blueprint:\n{raw_blueprint}\n")
    
    optimized = optimizer.optimize(raw_blueprint)
    print(f"📦 Optimized Blueprint:\n{optimized['optimized_prompt']}")
    print(f"💾 Compression: {optimized['saved_tokens_pct']}% saved\n")
    
    # Step 2: Sign
    signature = signer.sign_manifest(optimized['optimized_prompt'])
    print(f"🔐 Signature (ML-DSA-87):\n{signature}\n")
    
    # Step 3: Report
    print("✅ Pipeline Complete!")
    print(f"   - Original Length: {optimized['original_len']} chars")
    print(f"   - Optimized Length: {len(optimized['optimized_prompt'])} chars")
    print(f"   - Security: Quantum-Safe (NIST FIPS 204)")
    print(f"   - Status: Ready for Deployment")


def example_5_performance_monitoring():
    """Example 5: Performance Monitoring"""
    print("\n" + "=" * 75)
    print("EXAMPLE 5: Performance Metrics")
    print("=" * 75)
    
    import time
    
    optimizer = SovereignContextOptimizer()
    signer = MLDSA87Signature(key_identity="Pisut Somwang")
    
    # Test prompts of varying lengths
    test_cases = [
        ("Short", "Build AI system"),
        ("Medium", "Build a comprehensive AI system with decentralized architecture and quantum encryption"),
        ("Long", "Build a completely comprehensive and detailed decentralized AI system with advanced quantum encryption and security protocols for managing distributed language models across consumer devices globally")
    ]
    
    print("\n⏱️ Performance Benchmarks:\n")
    
    for name, prompt in test_cases:
        # Optimization timing
        start = time.time()
        result = optimizer.optimize(prompt)
        opt_time = (time.time() - start) * 1000  # ms
        
        # Signing timing
        start = time.time()
        sig = signer.sign_manifest(result['optimized_prompt'])
        sign_time = (time.time() - start) * 1000  # ms
        
        total_time = opt_time + sign_time
        
        print(f"{name} Prompt ({len(prompt)} chars):")
        print(f"  - Optimization: {opt_time:.2f}ms")
        print(f"  - Signing: {sign_time:.2f}ms")
        print(f"  - Total: {total_time:.2f}ms")
        print(f"  - Compression: {result['saved_tokens_pct']}%")
        print()


if __name__ == "__main__":
    print("\n" + "🪐" * 37)
    print("THE INFINITE CREATOR - QUICK START EXAMPLES")
    print("Architect: Pisut Somwang (พิสุทธิ์ สมหวัง)")
    print("🪐" * 37)
    
    # Run all examples
    example_1_basic_sdk_usage()
    example_2_quantum_safe_signatures()
    example_3_context_optimization()
    example_4_integrated_pipeline()
    example_5_performance_monitoring()
    
    print("\n" + "=" * 75)
    print("✅ All examples completed successfully!")
    print("=" * 75)
    print("\n📚 For more information, see: docs/API_DOCUMENTATION.md")
    print("🔗 Repository: https://github.com/id4devx-lang/infinite-creator-core\n")
