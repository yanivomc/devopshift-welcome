# 🎓 Teacher Guide: Lab AWS Permissions

This guide summarizes what students can and cannot do in their AWS lab environments. These rules are enforced by IAM policies to ensure both flexibility and account security.

**Active policy files:** `usersPolicy/ec2-complete.json`, `usersPolicy/iam-complete.json`, `usersPolicy/s3-jblabs-buckets.json`, `usersPolicy/deny-non-ec2-and-db.json`

---

## 🌍 1. Allowed Region: `us-east-1` (N. Virginia)
All resource creation (EC2, VPC, etc.) must be done in **`us-east-1`**. Other regions are restricted.

---

## 💻 2. EC2 & Computing

Students have full lifecycle control over EC2 instances in the allowed region, including snapshots, images, volumes, tags, and **Windows password retrieval** (`GetPasswordData`) for RDP connections.

### ✅ Allowed Instance Types
Students can only launch (RunInstances) the following types:
*   **T2:** `micro`, `small`, `medium`
*   **T3:** `micro`, `small`, `medium`, `large`
*   **T3a:** `micro`, `small`, `medium`
*   **T4g:** `micro`, `small`, `medium`

### 🔑 Launch Templates & Key Pairs
Students can create and manage:
*   Launch Templates (create, delete, versioning).
*   EC2 Key Pairs (create, delete, import).

### 🌐 Networking
Students can create and manage their own:
*   VPCs (including Default VPC), Subnets, and Route Tables.
*   Internet Gateways and NAT Gateways.
*   VPC Endpoints (create, delete, modify).
*   Security Groups and Elastic IPs.

### ⚖️ Auto Scaling & Load Balancing
*   Full access to **Auto Scaling Groups** (`autoscaling:*`).
*   Full access to **Elastic Load Balancers** (`elasticloadbalancing:*`).

### 📊 CloudWatch Monitoring
*   Read access to CloudWatch metrics (Describe, Get, List).
*   Ability to create and delete CloudWatch alarms.

---

## 📦 3. S3 Storage
Students can manage buckets and objects but must follow a specific naming rule.

### 🏷️ Naming Rule
Buckets **MUST** start with the prefix: **`jblabs-`**
*   Example: `jblabs-my-test-bucket`

### 🔑 Permissions
*   Full control over bucket creation, deletion, and object management.
*   Ability to modify **Bucket ACLs** inside the allowed prefix.

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

### 🔒 IAM Self-Access
*   Students can read their own identity info (GetUser, ListAccessKeys, etc.).
*   Read-only console access to IAM (Get*, List*).
*   PassRole to EC2 and Auto Scaling services only.

---

## 🚫 5. Restricted Services
To prevent cost overruns or complex infrastructure issues, the following services are **BLOCKED**:
*   **Databases:** RDS, DynamoDB, Redshift, DocumentDB, ElastiCache, MemoryDB, Neptune, QLDB, OpenSearch.
*   **Big Data / Analytics:** EMR, Kafka, Kinesis, Glue, Lake Formation.
*   **Containers:** EKS (Kubernetes).
*   **Serverless:** Lambda, CloudWatch Logs.

---

## 🛠️ For Administrators
If policies are updated, run the bootstrap script to sync the environment:
```bash
# Sync specific account
python3 scripts/bootstrap_account.py <ACCOUNT_ID>

# Sync an entire Organizational Unit (OU)
python3 scripts/bootstrap_account.py <OU_ID>
```
