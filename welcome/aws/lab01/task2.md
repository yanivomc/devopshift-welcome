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
