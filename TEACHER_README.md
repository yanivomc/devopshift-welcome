# 🎓 Teacher Guide: Lab AWS Permissions

This guide summarizes what students can and cannot do in their AWS lab environments. These rules are enforced by IAM policies to ensure both flexibility and account security.

---

## � 1. Allowed Region: `us-east-1` (N. Virginia)
All resource creation (EC2, VPC, etc.) must be done in **`us-east-1`**. Other regions are restricted.

---

## 💻 2. EC2 & Computing
Students have full lifecycle control over EC2 instances in the allowed region, including snapshots and images.

### ✅ Allowed Instance Types
Students can only start (RunInstances) the following types:
*   **T2:** `micro`, `small`, `medium`
*   **T3:** `micro`, `small`, `medium`, `large`
*   **T3a:** `micro`, `small`, `medium`
*   **T4g:** `micro`, `small`, `medium`

### 🌐 Networking
Students can create and manage their own:
*   VPCs, Subnets, and Route Tables.
*   Internet Gateways and NAT Gateways.
*   Security Groups and Elastic IPs.

---

## 📦 3. S3 Storage
Students can manage buckets and objects but must follow a specific naming rule.

### 🏷️ Naming Rule
Buckets **MUST** start with the prefix: **`jblabs-`**
*   Example: `jblabs-my-test-bucket`

### 🔑 Permissions
*   Full control over bucket creation, deletion, and object management.
*   Ability to modify **Bucket ACLs** and Policies inside the allowed prefix.

---

## 👤 4. IAM User Management (Sub-Users)
Students can create sub-users for their own labs (e.g., for CI/CD or programmatic testing).

### 🏷️ Naming Rule
Sub-users **MUST** start with the prefix: **`lab-`**
*   Example: `lab-jenkins-bot`, `lab-tester`

### 📜 Attaching Policies
Students can only attach these types of policies to their `lab-*` sub-users:
1.  **Lab Policies:** Any policy starting with **`Lab-`** (e.g., `Lab-ec2-networking`).
2.  **AWS ReadOnly:** Any standard AWS-managed policy ending in **`ReadOnlyAccess`**.

---

## 🚫 5. Restricted Services
To prevent cost overruns or complex infrastructure issues, the following services are **BLOCKED**:
*   RDS, DynamoDB, Redshift, DocumentDB.
*   EKS (Kubernetes), Kafka, Kinesis.
*   Elasticache, OpenSearch, Redshift.

---
