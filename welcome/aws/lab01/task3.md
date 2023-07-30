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
