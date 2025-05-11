import random
import matplotlib.pyplot as plt

def simulate_packets(n=100):
    packets = []
    suspicious_count = 0
    for i in range(n):
        packet = {
            'id': i,
            'source_ip': f"192.168.1.{random.randint(1, 255)}",
            'dest_ip': f"10.0.0.{random.randint(1, 255)}",
            'size': random.randint(20, 1500),
            'flagged': False
        }
        # Flag packet as suspicious if size is unusually large or randomly for simulation
        if packet['size'] > 1400 or random.random() < 0.05:
            packet['flagged'] = True
            suspicious_count += 1
        packets.append(packet)
    return packets, suspicious_count

def visualize_traffic(packets):
    sizes = [pkt['size'] for pkt in packets]
    flags = [pkt['flagged'] for pkt in packets]

    colors = ['red' if flagged else 'green' for flagged in flags]

    plt.figure(figsize=(10, 5))
    plt.scatter(range(len(packets)), sizes, c=colors, alpha=0.7)
    plt.title("Simulated Network Packet Sizes and Suspicious Flags")
    plt.xlabel("Packet ID")
    plt.ylabel("Packet Size (Bytes)")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()

# Run the simulation
packets, flagged_count = simulate_packets(200)
print(f"Total suspicious packets detected: {flagged_count}")
visualize_traffic(packets)
