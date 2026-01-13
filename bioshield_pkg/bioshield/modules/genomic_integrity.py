"""
Genomic Integrity Module for BioShield-B
Protects genetic purity of native crops

Author: Samir Baladi
Organization: Emerlad Compass 🧭
📧 Email: emerladcompass@gmail.com
🔬 ORCID: 0009-0003-8903-0029
🌐 Website: emerladcompass.github.io/bioshield
💼 GitHub: https://github.com/emerladcompass/BioShield
🔗 Live Dashboard: bioshield-b1.netlify.app
Affiliation: Interdisciplinary AI Researcher
"""

import hashlib
import json
import os
from datetime import datetime

class GenomicIntegrity:
    """Genetic purity monitoring and protection"""
    
    def __init__(self, base_dir=None):
        self.base_dir = base_dir or "/sdcard/download/BioShield/B_Agro_Immunity"
        self.vault_dir = os.path.join(self.base_dir, "vault", "genomic_keys")
        os.makedirs(self.vault_dir, exist_ok=True)
        
        # Author information - CORRECTED
        self.author_info = {
            "name": "Samir Baladi",
            "organization": "Emerlad Compass 🧭",
            "email": "emerladcompass@gmail.com"
        }
        
        self.profiles = {}
        self.load_profiles()
    
    def load_profiles(self):
        """Load existing genomic profiles"""
        if not os.path.exists(self.vault_dir):
            return
        
        for filename in os.listdir(self.vault_dir):
            if filename.endswith(".json"):
                profile_path = os.path.join(self.vault_dir, filename)
                try:
                    with open(profile_path, 'r') as f:
                        profile = json.load(f)
                        crop_name = profile.get("crop_name", filename.replace(".json", ""))
                        self.profiles[crop_name] = profile
                except:
                    continue
    
    def create_genomic_profile(self, crop_name, genetic_data):
        """Create genomic fingerprint for a crop"""
        # Create unique hash from genetic data
        genetic_string = json.dumps(genetic_data, sort_keys=True)
        genetic_hash = hashlib.sha256(genetic_string.encode()).hexdigest()
        
        profile = {
            "author": self.author_info['name'],
            "organization": self.author_info['organization'],
            "crop_name": crop_name,
            "genetic_hash": genetic_hash,
            "creation_date": datetime.now().isoformat(),
            "purity_score": self._calculate_purity_score(genetic_data),
            "contamination_risk": 0.0,
            "protected": True,
            "metadata": {
                "native_variants": genetic_data.get("native_variants", []),
                "total_markers": len(genetic_data.get("markers", [])),
                "unique_sequences": genetic_data.get("unique_sequences", 0)
            }
        }
        
        # Save profile
        self.profiles[crop_name] = profile
        self._save_profile(crop_name, profile)
        
        print(f"[+] Genomic profile created for {crop_name}")
        print(f"    Author: {self.author_info['name']}")
        print(f"    Organization: {self.author_info['organization']}")
        print(f"    Hash: {genetic_hash[:16]}...")
        print(f"    Purity score: {profile['purity_score']:.3f}")
        
        return profile
    
    def _calculate_purity_score(self, genetic_data):
        """Calculate genetic purity score"""
        native_count = len(genetic_data.get("native_variants", []))
        foreign_count = genetic_data.get("foreign_markers", 0)
        total_count = native_count + foreign_count
        
        if total_count > 0:
            purity = native_count / total_count
            return round(purity, 3)
        
        return 0.85  # Default value
    
    def detect_contamination(self, crop_name, sample_data, threshold=0.95):
        """Detect genetic contamination in sample"""
        if crop_name not in self.profiles:
            return {
                "error": f"Crop profile '{crop_name}' not found",
                "action": "Create profile first using create_genomic_profile()",
                "author": self.author_info['name'],
                "organization": self.author_info['organization']
            }
        
        profile = self.profiles[crop_name]
        
        # Create sample hash
        sample_hash = hashlib.sha256(
            json.dumps(sample_data, sort_keys=True).encode()
        ).hexdigest()
        
        # Calculate similarity
        similarity = self._hash_similarity(
            profile["genetic_hash"], 
            sample_hash
        )
        
        contamination_risk = 1.0 - similarity
        
        result = {
            "author": self.author_info['name'],
            "organization": self.author_info['organization'],
            "crop": crop_name,
            "original_hash": profile["genetic_hash"][:16] + "...",
            "sample_hash": sample_hash[:16] + "...",
            "similarity": round(similarity, 3),
            "contamination_risk": round(contamination_risk, 3),
            "purity_threshold": threshold,
            "is_contaminated": contamination_risk > (1 - threshold),
            "original_purity": profile["purity_score"],
            "timestamp": datetime.now().isoformat()
        }
        
        if result["is_contaminated"]:
            print(f"[!] GENETIC CONTAMINATION DETECTED in {crop_name}")
            print(f"    Author: {self.author_info['name']}")
            print(f"    Organization: {self.author_info['organization']}")
            print(f"    Risk level: {contamination_risk:.1%}")
            print(f"    Similarity: {similarity:.3f}")
        
        return result
    
    def _hash_similarity(self, hash1, hash2):
        """Calculate similarity between hashes"""
        # Convert first 8 chars to decimal
        val1 = int(hash1[:8], 16)
        val2 = int(hash2[:8], 16)
        
        max_val = 0xFFFFFFFF
        similarity = 1.0 - abs(val1 - val2) / max_val
        
        return similarity
    
    def _save_profile(self, crop_name, profile):
        """Save genomic profile to vault"""
        filename = f"{crop_name.replace(' ', '_')}.json"
        filepath = os.path.join(self.vault_dir, filename)
        
        with open(filepath, 'w') as f:
            json.dump(profile, f, indent=2)
    
    def monitor_genetic_drift(self, crop_name, samples):
        """Monitor genetic drift over time"""
        if crop_name not in self.profiles:
            return {
                "error": "Crop profile not found",
                "author": self.author_info['name'],
                "organization": self.author_info['organization']
            }
        
        drift_results = []
        profile_hash = self.profiles[crop_name]["genetic_hash"]
        
        for i, sample in enumerate(samples):
            sample_hash = hashlib.sha256(
                json.dumps(sample, sort_keys=True).encode()
            ).hexdigest()
            
            similarity = self._hash_similarity(profile_hash, sample_hash)
            
            drift_results.append({
                "sample": i + 1,
                "similarity": round(similarity, 3),
                "drift": round(1.0 - similarity, 3),
                "threshold_exceeded": similarity < 0.95
            })
        
        # Calculate overall drift
        avg_similarity = sum(r["similarity"] for r in drift_results) / len(drift_results)
        
        return {
            "author": self.author_info['name'],
            "organization": self.author_info['organization'],
            "crop": crop_name,
            "total_samples": len(samples),
            "average_similarity": round(avg_similarity, 3),
            "average_drift": round(1.0 - avg_similarity, 3),
            "drift_alarm": avg_similarity < 0.95,
            "results": drift_results,
            "timestamp": datetime.now().isoformat()
        }
    
    def get_system_status(self):
        """Get genomic integrity system status"""
        total_profiles = len(self.profiles)
        protected_profiles = sum(1 for p in self.profiles.values() if p.get("protected", False))
        
        # Calculate average purity
        if total_profiles > 0:
            avg_purity = sum(p.get("purity_score", 0) for p in self.profiles.values()) / total_profiles
        else:
            avg_purity = 0
        
        return {
            "author": self.author_info['name'],
            "organization": self.author_info['organization'],
            "status": "operational",
            "total_profiles": total_profiles,
            "protected_profiles": protected_profiles,
            "average_purity": round(avg_purity, 3),
            "vault_location": self.vault_dir,
            "timestamp": datetime.now().isoformat()
        }


def test_genomic_module():
    """Test function for genomic integrity module"""
    print("Testing Genomic Integrity Module...")
    print("Author: Samir Baladi")
    print("Organization: Emerlad Compass 🧭")
    print("="*50)
    
    gi = GenomicIntegrity()
    
    # Test data
    test_crop = {
        "native_variants": ["var1", "var2", "var3", "var4", "var5"],
        "foreign_markers": 1,
        "markers": ["M1", "M2", "M3", "M4", "M5", "M6"],
        "unique_sequences": 6
    }
    
    # Create profile
    profile = gi.create_genomic_profile("Wheat_Native", test_crop)
    print(f"Created profile: {profile['crop_name']}")
    
    # Test contamination detection
    test_sample = test_crop.copy()
    test_sample["foreign_markers"] = 3  # Increased contamination
    
    result = gi.detect_contamination("Wheat_Native", test_sample)
    print(f"Contamination test: {result['is_contaminated']}")
    print(f"Similarity: {result['similarity']}")
    
    # Get system status
    status = gi.get_system_status()
    print(f"System status: {status['status']}")
    print(f"Total profiles: {status['total_profiles']}")
    
    return result


if __name__ == "__main__":
    test_genomic_module()
