# 🎓 Data Science Teacher Guide: AWS Lab Permissions

This guide covers the specialized permissions for the Data Science course, including Big Data (EMR) and Serverless (Lambda) capabilities.

---

## 🌎 1. Allowed Region: `us-east-1` (N. Virginia)
All resources must be created in **`us-east-1`**.

---

## 🐘 2. EMR (Hadoop & Spark)
Students can manage EMR clusters for big data processing.

### ⚠️ Strict Cluster Limits
To prevent high costs, the following limits are enforced by policy:
*   **Max Instances:** A cluster cannot exceed **3 nodes** (1 Master + 2 Workers).
*   **Small Instances Only:** Only small instance types (`t2.micro`, `t3.medium`, etc.) are allowed for the cluster nodes.
*   **Automatic Failure:** Any attempt to create a cluster with more than 3 nodes or larger instance types will result in an "Access Denied" error.

---

## ⚡ 3. AWS Lambda (Serverless)
Students have full access to:
*   Create, list, and delete Lambda functions.
*   View execution logs in CloudWatch Logs.
*   Pass relevant IAM roles to their functions.

---

## 💾 4. RDS & VPC (Demonstration)
For classroom demonstrations, students can **View and List**:
*   **RDS Instances:** See available databases (creation/deletion is restricted).
*   **VPCs:** View network topology and subnets.

---

## 📦 5. S3 Storage & KeyPairs
*   **S3 Naming Rule:** Buckets **MUST** start with **`jblabs-`**. EMR clusters are configured to access these buckets.
*   **KeyPairs:** Full control to create and manage SSH keys for EC2/EMR access.

---

## 🚫 6. Prohibited Services
Services like DynamoDB, Redshift, and EKS remain **blocked** to maintain lab stability.

---

