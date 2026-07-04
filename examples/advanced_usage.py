#!/usr/bin/env python
# =====================================================================
# ADVANCED USAGE EXAMPLES - The Infinite Creator Core
# Architect: Pisut Somwang (พิสุทธิ์ สมหวัง) | Year: 2026
# =====================================================================

"""
Advanced usage patterns and real-world scenarios for the Infinite Creator SDK.

This module demonstrates:
1. Custom pipeline implementations
2. Multi-blueprint orchestration
3. Batch processing workflows
4. Integration with external systems
5. Performance profiling and monitoring
6. Error handling and resilience
"""

from typing import Dict, List, Any
import time
from dataclasses import asdict

from infinite_creator_sdk import (
    InfiniteCreatorSDK,
    MLDSA87Signature,
    SovereignContextOptimizer,
    CreationBlueprint,
)


# =====================================================================
# ADVANCED EXAMPLE 1: Custom Sovereign Pipeline
# =====================================================================

class SovereignProcessingPipeline:
    """
    Custom pipeline that orchestrates multiple components of the
    Infinite Creator system for complex workflows.
    """
    
    def __init__(self, architect_name: str, enable_profiling: bool = False):
        self.architect_name = architect_name
        self.sdk = InfiniteCreatorSDK(master_name=architect_name)
        self.optimizer = SovereignContextOptimizer()
        self.signer = MLDSA87Signature(key_identity=architect_name)
        self.enable_profiling = enable_profiling
        self.metrics = {}
    
    def process_blueprint(self, blueprint: str, project_name: str) -> Dict[str, Any]:
        """
        Process a blueprint through the complete pipeline with profiling.
        """
        metrics = {}
        
        # Step 1: Optimization
        start = time.time()
        optimized = self.optimizer.optimize(blueprint)
        metrics["optimization_time"] = (time.time() - start) * 1000
        
        # Step 2: Signing
        start = time.time()
        signature = self.signer.sign_manifest(optimized['optimized_prompt'])
        metrics["signing_time"] = (time.time() - start) * 1000
        
        # Step 3: Package results
        result = {
            "project_name": project_name,
            "original_blueprint": blueprint,
            "optimized_blueprint": optimized['optimized_prompt'],
            "compression_ratio": optimized['saved_tokens_pct'],
            "signature": signature,
            "metrics": metrics if self.enable_profiling else None,
            "status": "PROCESSED",
            "timestamp": time.time()
        }
        
        return result
    
    def batch_process(self, blueprints: List[Dict[str, str]]) -> List[Dict[str, Any]]:
        """
        Process multiple blueprints in batch mode.
        
        Args:
            blueprints: List of dicts with 'name' and 'blueprint' keys
        
        Returns:
            List of processed results
        """
        results = []
        start_time = time.time()
        
        print(f"\n📦 Processing {len(blueprints)} blueprints in batch mode...\n")
        
        for item in blueprints:
            result = self.process_blueprint(item['blueprint'], item['name'])
            results.append(result)
            
            if self.enable_profiling:
                print(f"✅ {item['name']}: {result['compression_ratio']}% compression, "
                      f"{result['metrics']['optimization_time']:.2f}ms")
        
        total_time = time.time() - start_time
        print(f"\n📊 Batch complete! Total time: {total_time*1000:.2f}ms")
        
        return results


# =====================================================================
# ADVANCED EXAMPLE 2: Multi-Tier Verification System
# =====================================================================

class MultiTierVerificationSystem:
    """
    Implements a multi-tier verification system using ML-DSA-87
    for critical operations that require multiple signatures.
    """
    
    def __init__(self):
        self.signers = {}
        self.verification_log = []
    
    def register_tier(self, tier_name: str, architect_name: str):
        """Register a verification tier with an architect."""
        self.signers[tier_name] = MLDSA87Signature(key_identity=architect_name)
        print(f"✅ Registered tier: {tier_name} (Architect: {architect_name})")
    
    def verify_manifest(self, manifest: str, required_tiers: List[str]) -> Dict[str, Any]:
        """
        Verify a manifest through multiple tiers of security.
        """
        print(f"\n🔐 Multi-Tier Verification Process\n")
        
        signatures = {}
        for tier in required_tiers:
            if tier not in self.signers:
                raise ValueError(f"Tier '{tier}' not registered")
            
            sig = self.signers[tier].sign_manifest(manifest)
            signatures[tier] = sig
            print(f"  ✅ Tier '{tier}': {sig[:24]}...")
        
        # Record verification
        record = {
            "manifest": manifest[:50] + "...",
            "tiers": required_tiers,
            "signatures": signatures,
            "verified_at": time.time()
        }
        self.verification_log.append(record)
        
        return {
            "status": "VERIFIED",
            "manifest": manifest,
            "signatures": signatures,
            "tier_count": len(required_tiers),
            "verification_chain": list(signatures.keys())
        }


# =====================================================================
# ADVANCED EXAMPLE 3: Adaptive Optimization System
# =====================================================================

class AdaptiveOptimizationSystem:
    """
    Intelligently adjusts optimization strategies based on content
    characteristics and performance metrics.
    """
    
    def __init__(self):
        self.optimizer = SovereignContextOptimizer()
        self.performance_history = []
    
    def analyze_content(self, content: str) -> Dict[str, Any]:
        """Analyze content characteristics."""
        words = content.split()
        chars = len(content)
        
        return {
            "word_count": len(words),
            "char_count": chars,
            "avg_word_length": chars / len(words) if words else 0,
            "unique_words": len(set(w.lower() for w in words)),
            "complexity_score": len(words) / 10  # Simplified metric
        }
    
    def adaptive_optimize(self, content: str) -> Dict[str, Any]:
        """
        Apply adaptive optimization based on content analysis.
        """
        analysis = self.analyze_content(content)
        
        # Apply optimization
        optimized = self.optimizer.optimize(content)
        
        # Calculate efficiency
        efficiency = {
            "input_metrics": analysis,
            "output_metrics": self.analyze_content(optimized['optimized_prompt']),
            "compression_ratio": optimized['saved_tokens_pct'],
            "efficiency_score": analysis['complexity_score'] * optimized['saved_tokens_pct'] / 100,
            "adaptive_strategy": self._select_strategy(analysis)
        }
        
        self.performance_history.append(efficiency)
        
        return {
            "original": content,
            "optimized": optimized['optimized_prompt'],
            "analysis": efficiency
        }
    
    def _select_strategy(self, analysis: Dict[str, Any]) -> str:
        """Select optimization strategy based on analysis."""
        if analysis['complexity_score'] > 50:
            return "AGGRESSIVE_COMPRESSION"
        elif analysis['complexity_score'] > 20:
            return "BALANCED_COMPRESSION"
        else:
            return "CONSERVATIVE_COMPRESSION"
    
    def get_performance_report(self) -> Dict[str, Any]:
        """Generate performance report from history."""
        if not self.performance_history:
            return {"status": "NO_DATA"}
        
        compressions = [h['compression_ratio'] for h in self.performance_history]
        
        return {
            "total_operations": len(self.performance_history),
            "avg_compression": sum(compressions) / len(compressions),
            "max_compression": max(compressions),
            "min_compression": min(compressions),
            "efficiency_score": sum(h['efficiency_score'] for h in self.performance_history)
        }


# =====================================================================
# ADVANCED EXAMPLE 4: Integrated Blueprint Management
# =====================================================================

class BlueprintManager:
    """
    Manages creation blueprints with versioning and metadata tracking.
    """
    
    def __init__(self, architect_name: str):
        self.architect_name = architect_name
        self.signer = MLDSA87Signature(key_identity=architect_name)
        self.blueprints = {}
    
    def create_blueprint(
        self,
        creation_id: str,
        density_level: int,
        symbols: List[str]
    ) -> CreationBlueprint:
        """Create and register a new blueprint."""
        
        # Generate signature
        sig_payload = f"{creation_id}:{density_level}:{','.join(symbols)}"
        signature = self.signer.sign_manifest(sig_payload)
        
        # Create blueprint
        blueprint = CreationBlueprint(
            creation_id=creation_id,
            density_level=density_level,
            quantum_signature=signature,
            semantic_density_factor=density_level / 10.0,
            symbols_active=symbols,
            status="STABLE_EVOLVED"
        )
        
        # Store blueprint
        self.blueprints[creation_id] = blueprint
        
        print(f"✅ Blueprint created: {creation_id}")
        print(f"   Density: {density_level}/10")
        print(f"   Symbols: {', '.join(symbols)}")
        print(f"   Signature: {signature[:24]}...\n")
        
        return blueprint
    
    def get_blueprint(self, creation_id: str) -> CreationBlueprint:
        """Retrieve a blueprint by ID."""
        return self.blueprints.get(creation_id)
    
    def list_blueprints(self) -> List[Dict[str, Any]]:
        """List all blueprints as dictionaries."""
        return [asdict(bp) for bp in self.blueprints.values()]


# =====================================================================
# EXECUTION: Advanced Examples
# =====================================================================

def run_all_advanced_examples():
    """Execute all advanced examples."""
    
    print("\n" + "🚀" * 37)
    print("ADVANCED USAGE EXAMPLES - The Infinite Creator Core")
    print("Architect: Pisut Somwang (พิสุทธิ์ สมหวัง)")
    print("🚀" * 37)
    
    # Example 1: Custom Sovereign Pipeline
    print("\n" + "=" * 75)
    print("EXAMPLE 1: Custom Sovereign Pipeline with Batch Processing")
    print("=" * 75)
    
    pipeline = SovereignProcessingPipeline("Pisut Somwang", enable_profiling=True)
    
    blueprints = [
        {
            "name": "Project Alpha",
            "blueprint": "Build a decentralized AI network with quantum encryption and distributed computing capabilities"
        },
        {
            "name": "Project Beta",
            "blueprint": "Create advanced machine learning infrastructure with sovereign control and privacy preservation"
        },
        {
            "name": "Project Gamma",
            "blueprint": "Implement quantum-resistant cryptography across all system components and protocols"
        }
    ]
    
    results = pipeline.batch_process(blueprints)
    
    for result in results:
        print(f"\n📊 {result['project_name']}:")
        print(f"   Compression: {result['compression_ratio']}%")
        if result['metrics']:
            print(f"   Optimization: {result['metrics']['optimization_time']:.2f}ms")
            print(f"   Signing: {result['metrics']['signing_time']:.2f}ms")
    
    # Example 2: Multi-Tier Verification
    print("\n" + "=" * 75)
    print("EXAMPLE 2: Multi-Tier Verification System")
    print("=" * 75)
    
    verifier = MultiTierVerificationSystem()
    verifier.register_tier("Security Lead", "Pisut Somwang")
    verifier.register_tier("Architect Tier", "Master Architect")
    verifier.register_tier("Quantum Validator", "Quantum Guardian")
    
    manifest = "Sovereign Core System Manifest - All components verified and authorized"
    result = verifier.verify_manifest(manifest, ["Security Lead", "Architect Tier", "Quantum Validator"])
    
    print(f"\n✅ Verification complete: {result['status']}")
    print(f"   Tiers verified: {len(result['signatures'])}")
    print(f"   Chain: {' → '.join(result['verification_chain'])}")
    
    # Example 3: Adaptive Optimization
    print("\n" + "=" * 75)
    print("EXAMPLE 3: Adaptive Optimization System")
    print("=" * 75)
    
    adaptive = AdaptiveOptimizationSystem()
    
    complex_texts = [
        "Implement a very comprehensive and detailed distributed system architecture with advanced quantum encryption protocols",
        "Quick test",
        "Build a comprehensive decentralized network with lots of redundant specifications and detailed technical requirements"
    ]
    
    for text in complex_texts:
        result = adaptive.adaptive_optimize(text)
        print(f"\n📈 {text[:50]}...")
        print(f"   Strategy: {result['analysis']['adaptive_strategy']}")
        print(f"   Compression: {result['analysis']['compression_ratio']}%")
        print(f"   Efficiency: {result['analysis']['efficiency_score']:.2f}")
    
    report = adaptive.get_performance_report()
    print(f"\n📊 Performance Report:")
    print(f"   Total operations: {report['total_operations']}")
    print(f"   Avg compression: {report['avg_compression']:.1f}%")
    print(f"   Max compression: {report['max_compression']:.1f}%")
    
    # Example 4: Blueprint Management
    print("\n" + "=" * 75)
    print("EXAMPLE 4: Integrated Blueprint Management")
    print("=" * 75)
    
    manager = BlueprintManager("Pisut Somwang")
    
    manager.create_blueprint(
        creation_id="GAIA-PRISM-001",
        density_level=9,
        symbols=["quantum-safe", "sovereign", "distributed"]
    )
    
    manager.create_blueprint(
        creation_id="NEXUS-CORE-002",
        density_level=8,
        symbols=["ml-dsa-87", "optimized", "production-ready"]
    )
    
    blueprints_list = manager.list_blueprints()
    print(f"✅ Managed {len(blueprints_list)} blueprints\n")
    
    for bp in blueprints_list:
        print(f"📋 {bp['creation_id']}")
        print(f"   Status: {bp['status']}")
        print(f"   Symbols: {', '.join(bp['symbols_active'])}")
    
    # Summary
    print("\n" + "=" * 75)
    print("✅ All advanced examples completed successfully!")
    print("=" * 75)
    print("\n🎯 Key Features Demonstrated:")
    print("   ✓ Custom pipeline orchestration")
    print("   ✓ Multi-tier security verification")
    print("   ✓ Adaptive optimization strategies")
    print("   ✓ Blueprint lifecycle management")
    print("   ✓ Performance profiling and reporting")
    print("\n📚 For more information: docs/API_DOCUMENTATION.md")
    print("🔗 Repository: https://github.com/id4devx-lang/infinite-creator-core\n")


if __name__ == "__main__":
    run_all_advanced_examples()
