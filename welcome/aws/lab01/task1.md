
## **Task 1: Explore the users and groups**

In this task, you will explore the users and groups that have already been created for you in IAM.

1. First, note the Region that you are in; for example, **N. Virginia**. The Region is displayed in the upper-right corner of the console page.
2. Choose the **Services** menu, locate the **Security, Identity, & Compliance** services, and choose **IAM**.
3. In the navigation pane on the left, choose **Users**.

The following IAM users have been created for you:

- user-1
- user-2
- user-3

| **User** | **In Group** | **Permissions** |
| --- | --- | --- |
| user-1 | S3-Support | Read-only access to Amazon S3 |
| user-2 | EC2-Support | Read-only access to Amazon EC2 |
| user-3 | EC2-Admin | View, Start, and Stop Amazon EC2 instances |

1. Choose the name of **user-1**.
   - This brings you to a summary page for user-1. The **Permissions** tab will be displayed.
   - Notice that user-1 does not have any permissions.
2. Choose the **Groups** tab.

Notice that user-1 also is not a member of any groups.

1. Choose the **Security credentials** tab.

Notice that user-1 is assigned a **Console password**. This allows the user to access the AWS Management Console.

2. In the navigation pane on the left, choose **User groups**.

The following groups have already been created for you:

- EC2-Admin
- EC2-Support
- S3-Support

Choose the name of the **EC2-Support** group. This brings you to the summary page for the **EC2-Support** group.

1. Choose the **Permissions** tab.
   This group has a managed policy called **AmazonEC2ReadOnlyAccess** associated with it. Managed policies are prebuilt policies (built either by AWS or by your administrators) that can be attached to IAM users and groups. When the policy is updated, the changes to the policy are immediately applied against all users and groups that are attached to the policy.

2. Under **Policy Name**, choose the link for the **AmazonEC2ReadOnlyAccess** policy.
3. Choose the **{} JSON** tab.
   - A policy defines what actions are allowed or denied for specific AWS resources. This policy is granting permission to _List_ and _Describe_ (view) information about Amazon Elastic Compute Cloud (Amazon EC2), Elastic Load Balancing, Amazon CloudWatch, and Amazon EC2 Auto Scaling. This ability to view resources, but not modify them, is ideal for assigning to a support role.
   - Statements in an IAM policy have the following basic structure:
     - **Effect** says whether to _Allow_ or _Deny_ the permissions.
     - **Action** specifies the API calls that can be made against an AWS service (for example, _cloudwatch:ListMetrics_).
     - **Resource** defines the scope of entities covered by the policy rule (for example, a specific Amazon Simple Storage Service [Amazon S3] bucket or Amazon EC2 instance; an asterisk [\*] means _any resource_).

4. In the navigation pane on the left, choose **User groups**.
5. Choose the name of the **S3-Support** group.
6. Choose the **Permissions** tab.

The S3-Support group has the **AmazonS3ReadOnlyAccess** policy attached.

1. Under **Policy Name**, choose the link for the **AmazonS3ReadOnlyAccess** policy.
2. Choose the **{} JSON** tab.

This policy has permissions to _Get_ and _List_ for _all_ resources in Amazon S3.

1. In the navigation pane on the left, choose **User groups**.
2. Choose the name of the **EC2-Admin** group.
3. Choose the **Permissions** tab.

This group is different from the other two. Instead of a managed policy, the group has an _inline policy_, which is a policy assigned to just one user or group. Inline policies are typically used to apply permissions for specific situations.

1. Under **Policy Name**, choose the name of the **EC2-Admin-Policy** policy.
2. Choose the **JSON** tab.

This policy grants permission to _Describe_ information about Amazon EC2 instances, and also the ability to _Start_ and _Stop_ instances.

3. At the bottom of the screen, choose **Cancel** to close the policy.
