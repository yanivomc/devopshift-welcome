# **Lab 1: Introduction to IAM**

## **Lab overview**

In this lab, you will explore users, groups, and policies in the AWS Identity and Access Management (IAM) service.

**Objectives**

After completing this lab, you will know how to:

- Explore pre-created **IAM Users and Groups**
- Inspect **IAM policies** as applied to the pre-created groups
- Follow a **real-world scenario**, adding users to groups with specific capabilities enabled
- Locate and use the **IAM sign-in URL**
- **Experiment** with the effects of policies on service access

## **Duration**

This lab requires approximately **40 minutes** to complete.

.

## **Accessing the AWS Management Console**

1. At the top of these instructions, select Start Lab to launch your lab.

A Start Lab panel opens displaying the lab status.

1. Wait until you see the message **Lab status: ready**, and then select the **X** to close the Start Lab panel.
2. At the top of these instructions, select AWS

The AWS Management Console opens in a new browser tab. The system automatically signs you in.

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

## **Task 2: Add users to groups**

You have recently hired _user-1_ into a role where they will provide support for Amazon S3. You will add them to the _S3-Support_ group so that they inherit the necessary permissions via the attached _AmazonS3ReadOnlyAccess_ policy. Ignore any "not authorized" errors that appear during this task. They are caused by your lab account having limited permissions and will not impact your ability to complete the lab.

**Add user-1 to the S3-Support group**

1. In the left navigation pane, choose **User groups**.
2. Choose the name of the **S3-Support** group.
3. On the **Users** tab, choose **Add users**.
4. Select **user-1**, and choose **Add users**.
   On the **Users** tab, notice that _user-1_ has been added to the group.

**Add user-2 to the EC2-Support group**

You have hired _user-2_ into a role where they will provide support for Amazon EC2. You will add them to the _EC2-Support_ group so that they inherit the necessary permissions via the attached _AmazonEC2ReadOnlyAccess_ policy.

1. Use what you learned from the previous steps to add _user-2_ to the _EC2-Support_ group.
   _user-2_ should now be part of the _EC2-Support_ group.

**Add user-3 to the EC2-Admin group**

You have hired _user-3_ as your Amazon EC2 administrator to manage your EC2 instances. You will add them to the _EC2-Admin_ group so that they inherit the necessary permissions via the attached _EC2-Admin-Policy_.

1. Use what you learned from the previous steps to add _user-3_ to the _EC2-Admin_ group.
   _user-3_ should now be part of the _EC2-Admin_ group.

1. In the navigation pane on the left, choose **User groups**.
   Each group should have a **1** in the **Users** column. This indicates the number of users in each group. If you do not have a **1** for the **Users** column for a group, revisit the previous steps to ensure that each user is assigned to a group, as shown in the table in the **Business scenario** section.

## **Task 3: Sign in and test users**

In this task, you will test the permissions of each IAM user in the console.

**Get the console sign-in URL**

1. In the navigation pane on the left, choose **Dashboard**.
   Notice the **Sign-in URL for IAM users in this account** section at the top of the page. The sign-in URL looks similar to the following: **https://123456789012.signin.aws.amazon.com/console** This link can be used to sign in to the AWS account that you are currently using.

1. Copy the sign-in link to a text editor.

**Test user-1 permissions**

1. Open a private or incognito window in your browser.
2. Paste the sign-in link into the private browser, and press ENTER.
   You will now sign-in as _user-1_, who has been hired as your Amazon S3 storage support staff.

3. Sign in with the following credentials:
   - **IAM user name:** user-1
   - **Password:** Lab-Password1
4. Choose the **Services** menu, and choose **S3**.
5. Choose the name of one of your buckets and browse the contents.
   Because this user is part of the _S3-Support_ group in IAM, they have permissions to view a list of Amazon S3 buckets and their contents.

Now, test whether the user has access to Amazon EC2.

6. Choose the **Services** menu, and choose **EC2**.
7. In the left navigation pane, choose **Instances**.
   You cannot see any instances. Instead, an error message says _you are not authorized to perform this operation_. This user has not been assigned any permissions to use Amazon EC2.

You will now sign in as _user-2_, who has been hired as your Amazon EC2 support person.

8. First, sign out _user-1_ from the console:
   - In the upper-right corner of the page, choose **user-1**.
   - Choose **Sign Out**.

**Test user-2 permissions**

1. Paste the sign-in link into the private browser again, and press ENTER.
2. Sign in with the following credentials:
   - **IAM user name:** user-2
   - **Password:** Lab-Password2
3. Choose the **Services** menu, and choose **EC2**.
4. In the navigation pane on the left, choose **Instances**.
   You are now able to see an EC2 instance. However, you cannot make any changes to Amazon EC2 resources because you have read-only permissions.
   If you cannot see an EC2 instance, then your Region might be incorrect. In the upper-right corner of the page, choose the Region name, and then choose the Region that you were in at the beginning of the lab (for example, **N. Virginia**).

5. Select the EC2 instance.
6. Choose the **Instance state** menu, and then choose **Stop instance**.
7. To confirm that you want to stop the instance, choose **Stop**.
   An error message appears and says that _You are not authorized to perform this operation_. This demonstrates that the policy only allows you to view information without making changes.

Next, check if _user-2_ can access Amazon S3.

8. Choose the **Services** menu, and choose **S3**.
   An error message says _You don't have permissions to list buckets_ because _user-2_ does not have permissions to use Amazon S3.

You will now sign-in as _user-3_, who has been hired as your Amazon EC2 administrator.

9. First, sign out _user-2_ from the console:
   - In the upper-right corner of the page, choose **user-2**.
   - Choose **Sign Out**.

**Test user-3 permissions**

1. Paste the sign-in link into the private browser again, and press ENTER.
2. Sign in with the following credentials:
   - **IAM user name:** user-3
   - **Password:** Lab-Password3
3. Choose the **Services** menu, and choose **EC2**.
4. In the navigation pane on the left, choose **Instances**.
   An EC2 instance is listed. As an Amazon EC2 Administrator, this user should have permissions to _Stop_ the EC2 instance.
   If you cannot see an EC2 instance, then your Region might be incorrect. In the upper-right corner of the page, choose the Region name, and then choose the Region that you were in at the beginning of the lab (for example, **N. Virginia**).

5. Select the EC2 instance.
6. Choose the **Instance state** menu, and then choose **Stop instance**.
7. To confirm that you want to stop the instance, choose **Stop**.
   This time, the action is successful because _user-3_ has permissions to stop EC2 instances. The **Instance state** changes to _Stopping_ and starts to shut down.

8. Close your private browser window.

![Shape1](RackMultipart20230730-1-ulob7o_html_e59097e6e774bae0.gif)

## **Lab complete**

Congratulations! You have completed the lab.

1. Choose End Lab at the top of this page, and then choose **Yes** to confirm that you want to end the lab.
