"""
Network Analyzer for BioShield-B
Adapted from HydroNet network analysis

Author: Samir Baladi
Organization: Emerlad Compass 🧭
📧 Email: emerladcompass@gmail.com
🔬 ORCID: 0009-0003-8903-0029
🌐 Website: emerladcompass.github.io/bioshield
💼 GitHub: https://github.com/emerladcompass/BioShield
🔗 Live Dashboard: bioshield-b1.netlify.app
Affiliation: Interdisciplinary AI Researcher
"""

import numpy as np
import pandas as pd
from datetime import datetime, timedelta

class NetworkAnalyzer:
    """Network topology analysis for agro-immunity"""
    
    def __init__(self, window_size=12):
        self.window_size = window_size  # months
        self.network_history = []
        
        # Author information - CORRECTED
        self.author_info = {
            "name": "Samir Baladi",
            "organization": "Emerlad Compass 🧭",
            "email": "emerladcompass@gmail.com"
        }
    
    def calculate_transfer_entropy(self, source_series, target_series, k=3, l=3):
        """
        Calculate transfer entropy from source to target
        Simplified implementation
        """
        if len(source_series) != len(target_series):
            raise ValueError("Series must have same length")
        
        n = len(source_series)
        if n < 10:
            return 0.0
        
        # Simple correlation-based approximation
        correlation = np.corrcoef(source_series, target_series)[0, 1]
        
        # Transfer entropy approximation
        te = abs(correlation) * 0.5  # Simplified
        
        return max(0.0, min(1.0, te))
    
    def construct_network(self, indicators_data):
        """
        Construct multiplex network from indicators data
        indicators_data: dict with time series for each indicator
        """
        indicators = list(indicators_data.keys())
        n_indicators = len(indicators)
        
        # Initialize adjacency matrix
        adjacency = np.zeros((n_indicators, n_indicators))
        
        # Calculate transfer entropy between all pairs
        for i in range(n_indicators):
            for j in range(n_indicators):
                if i != j:
                    source = indicators_data[indicators[i]]
                    target = indicators_data[indicators[j]]
                    
                    if len(source) == len(target):
                        te = self.calculate_transfer_entropy(source, target)
                        adjacency[i, j] = te
        
        # Create network metadata
        network = {
            "author": self.author_info['name'],
            "organization": self.author_info['organization'],
            "timestamp": datetime.now().isoformat(),
            "indicators": indicators,
            "adjacency_matrix": adjacency.tolist(),
            "n_nodes": n_indicators,
            "n_edges": np.sum(adjacency > 0)
        }
        
        # Calculate network metrics
        network.update(self._calculate_network_metrics(adjacency, indicators))
        
        self.network_history.append(network)
        
        return network
    
    def _calculate_network_metrics(self, adjacency, indicators):
        """Calculate various network metrics"""
        n = len(indicators)
        
        # Node centrality (simplified)
        out_degree = np.sum(adjacency > 0, axis=1)
        in_degree = np.sum(adjacency > 0, axis=0)
        
        centrality = {
            indicators[i]: {
                "out_degree": float(out_degree[i]),
                "in_degree": float(in_degree[i]),
                "total_degree": float(out_degree[i] + in_degree[i])
            }
            for i in range(n)
        }
        
        # Most central node
        max_centrality_idx = np.argmax(out_degree + in_degree)
        most_central = indicators[max_centrality_idx]
        
        # Network density
        max_possible_edges = n * (n - 1)
        actual_edges = np.sum(adjacency > 0)
        density = actual_edges / max_possible_edges if max_possible_edges > 0 else 0
        
        # Clustering coefficient (simplified)
        clustering = np.mean([
            self._calculate_clustering(adjacency, i)
            for i in range(n)
        ])
        
        return {
            "centrality": centrality,
            "most_central_node": most_central,
            "max_centrality": float(np.max(out_degree + in_degree)),
            "network_density": float(density),
            "clustering_coefficient": float(clustering),
            "actual_edges": int(actual_edges)
        }
    
    def _calculate_clustering(self, adjacency, node_idx):
        """Calculate clustering coefficient for a node"""
        neighbors = np.where(adjacency[node_idx, :] > 0)[0]
        k = len(neighbors)
        
        if k < 2:
            return 0.0
        
        # Count triangles
        triangles = 0
        for i in range(k):
            for j in range(i + 1, k):
                if adjacency[neighbors[i], neighbors[j]] > 0:
                    triangles += 1
        
        max_triangles = k * (k - 1) / 2
        return triangles / max_triangles if max_triangles > 0 else 0.0
    
    def detect_network_instability(self, current_network, history_window=3):
        """
        Detect network instability by comparing with historical patterns
        """
        if len(self.network_history) < history_window:
            return {
                "author": self.author_info['name'],
                "organization": self.author_info['organization'],
                "instability_detected": False,
                "reason": "Insufficient history",
                "confidence": 0.0
            }
        
        # Get recent networks
        recent_networks = self.network_history[-history_window:]
        
        # Calculate stability metrics
        density_changes = []
        centrality_changes = []
        
        for network in recent_networks:
            density_changes.append(abs(network["network_density"] - current_network["network_density"]))
            
            # Compare centrality patterns
            current_central = current_network["most_central_node"]
            if "most_central_node" in network:
                centrality_changes.append(1.0 if network["most_central_node"] != current_central else 0.0)
        
        avg_density_change = np.mean(density_changes) if density_changes else 0
        avg_centrality_change = np.mean(centrality_changes) if centrality_changes else 0
        
        instability_score = (avg_density_change * 0.6) + (avg_centrality_change * 0.4)
        
        result = {
            "author": self.author_info['name'],
            "organization": self.author_info['organization'],
            "instability_detected": instability_score > 0.3,
            "instability_score": float(instability_score),
            "density_change": float(avg_density_change),
            "centrality_change": float(avg_centrality_change),
            "current_central_node": current_network["most_central_node"],
            "confidence": min(1.0, instability_score * 2),
            "timestamp": datetime.now().isoformat()
        }
        
        return result
    
    def predict_collapse_risk(self, network_metrics, svi_score):
        """
        Predict collapse risk based on network metrics and SVI
        """
        # Extract features
        density = network_metrics.get("network_density", 0.5)
        clustering = network_metrics.get("clustering_coefficient", 0.5)
        max_centrality = network_metrics.get("max_centrality", 0)
        
        # Simplified risk calculation
        risk_factors = [
            (1.0 - density) * 0.3,          # Low density increases risk
            (1.0 - clustering) * 0.2,       # Low clustering increases risk
            (max_centrality / 10) * 0.3,    # High centrality increases risk
            (1.0 - svi_score) * 0.2         # Low SVI increases risk
        ]
        
        collapse_risk = sum(risk_factors)
        
        # Time to collapse estimate (simplified)
        if collapse_risk > 0.7:
            time_to_collapse = "1-3 months"
        elif collapse_risk > 0.5:
            time_to_collapse = "4-6 months"
        elif collapse_risk > 0.3:
            time_to_collapse = "7-8 months"
        else:
            time_to_collapse = ">8 months"
        
        return {
            "author": self.author_info['name'],
            "organization": self.author_info['organization'],
            "collapse_risk": float(collapse_risk),
            "time_to_collapse": time_to_collapse,
            "risk_level": "HIGH" if collapse_risk > 0.6 else "MEDIUM" if collapse_risk > 0.3 else "LOW",
            "factors": {
                "density_factor": float(risk_factors[0]),
                "clustering_factor": float(risk_factors[1]),
                "centrality_factor": float(risk_factors[2]),
                "svi_factor": float(risk_factors[3])
            },
            "timestamp": datetime.now().isoformat()
        }


def test_network_analyzer():
    """Test network analyzer"""
    print("Testing Network Analyzer...")
    print("Author: Samir Baladi")
    print("Organization: Emerlad Compass 🧭")
    print("="*50)
    
    analyzer = NetworkAnalyzer(window_size=12)
    
    # Generate test data
    n_points = 24
    indicators = {
        "B1": np.random.normal(0.7, 0.1, n_points),
        "B2": np.random.normal(0.6, 0.1, n_points),
        "B3": np.random.normal(0.8, 0.05, n_points),
        "B4": np.random.normal(0.5, 0.15, n_points)
    }
    
    # Construct network
    network = analyzer.construct_network(indicators)
    
    print(f"Network created with {network['n_nodes']} nodes and {network['n_edges']} edges")
    print(f"Most central node: {network['most_central_node']}")
    print(f"Network density: {network['network_density']:.3f}")
    
    # Detect instability
    instability = analyzer.detect_network_instability(network)
    print(f"Instability detected: {instability['instability_detected']}")
    print(f"Instability score: {instability['instability_score']:.3f}")
    
    # Predict collapse risk
    collapse_risk = analyzer.predict_collapse_risk(network, svi_score=0.65)
    print(f"Collapse risk: {collapse_risk['collapse_risk']:.3f} ({collapse_risk['risk_level']})")
    print(f"Time to collapse: {collapse_risk['time_to_collapse']}")
    
    return network, instability, collapse_risk


if __name__ == "__main__":
    test_network_analyzer()
