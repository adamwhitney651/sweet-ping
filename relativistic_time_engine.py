# Post-Binary Relativistic Time Engine
# Demonstrating Distributed Computational Relativity & Balanced Ternary State Gating.

import math

class RelativisticTernaryNode:
    def __init__(self, node_id, max_bandwidth=300000.0):
        self.node_id = node_id
        self.c = max_bandwidth  # System speed limit
        self.history = []

    def process_state(self, amplitude, raw_workload_v):
        # Balanced ternary mapping: Post-binary (-1, 0, 1)
        ternary_state = 1 if amplitude > 0.3 else (-1 if amplitude < -0.3 else 0)
        
        # Lorentz Time Dilation Calculation
        v = min(raw_workload_v, self.c - 0.1)
        gamma = 1.0 / math.sqrt(1.0 - (v**2) / (self.c**2))
        
        metrics = {
            "node": self.node_id,
            "state": ternary_state,
            "velocity": v,
            "gamma": round(gamma, 4),
            "local_cycle_stretch": round(gamma, 4)
        }
        self.history.append(metrics)
        return metrics

if __name__ == '__main__':
    print("Initializing Relativistic Time Engine...")
    engine = RelativisticTernaryNode("Node-Alpha")
    test_loads = [0.0, 150000.0, 250000.0, 295000.0]
    amplitudes = [0.8, -0.5, 0.0, 0.9]
    
    for load, amp in zip(test_loads, amplitudes):
        res = engine.process_state(amp, load)
        print(f"Velocity: {res['velocity']:.1f} -> Gamma: {res['gamma']}x | State: {res['state']}")
