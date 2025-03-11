from encryption.sync_encryption import SyncEncryption
from verification.hierarchical_verification import HierarchicalVerification
from anomaly_detection.anomaly_detection import AnomalyDetection
import numpy as np

# Encryption Demonstration
se = SyncEncryption("secure_key")
data = "Confidential cloud data"
encrypted_data = se.encrypt(data)
print(f"Encrypted Data: {encrypted_data}")
print(f"Decrypted Data: {se.decrypt(encrypted_data)}")

# Verification Demonstration
hv = HierarchicalVerification()
hash_value = hv.verify_data(data)
print(f"Hash Value: {hash_value}")
print(f"Integrity Check: {hv.check_integrity(data)}")

# Anomaly Detection Demonstration
ad = AnomalyDetection()
sample_data = np.random.rand(100, 2)
ad.train_model(sample_data)
test_data = np.random.rand(10, 2)
anomalies = ad.detect_anomalies(test_data)
print(f"Anomaly Results: {anomalies}")