# AWS安全自动检查（SMB Sec Assessment 部署） 

## 一、创建IAM用户

新创建一个AWS IAM用户来执行 安全自动检查 的脚步，并完成对其权限的分配。如下：

1. 打开IAM
2. 新建用户 《**prowler-additions-policy-user》**
3. Attach policies directly 如下
    - AmazonEC2FullAccess	AWS managed	Directly
    - AmazonS3FullAccess	AWS managed	Directly
    - AmazonSSMFullAccess	AWS managed	Directly
    - AmazonVPCFullAccess	AWS managed	Directly
    - AWSCloudFormationFullAccess	AWS managed	Directly
    - IAMFullAccess	AWS managed	Directly
4. 创建用户完成

![Untitled](https://raw.githubusercontent.com/liangyimingcom/storage/master/PicGo/Untitled.png)

IAM所需权限的介绍： 部署过程将在您的账号中创建一系列的资源，使用Admin账号或者其他具备以下资源创建权限的IAM用户或角色：

- IAM Role
- IAM Managed Policy
- VPC
- IGW
- Route tables
- Security Group
- NAT Gateway
- Elastic IP (EIP)
- EC2 Instance
- S3 Bucket





## 二、登陆新的用户，完成 **S3存储桶及cfn脚本** 准备工作

您需要把Cloudformation脚本复制到一个S3存储桶，用以创建Cloudformation 堆栈（Stack），因此请：

1. 登陆AWS Console控制太，登陆用户为上一步创建的 《**prowler-additions-policy-user》**
2. 打开 S3，并创建S3 存储桶《smbsecassessment-yiming-20230309》，请注意不能重名；
3. 务必选择 cloud formation执行的同一个区域 
4. ACLs enabled 和 **取消**Block all public access 为了共享json脚步方便cloud formation执行；

![Untitled](https://raw.githubusercontent.com/liangyimingcom/storage/master/PicGo/Untitled%201.png)

1. 创建成功后，将CloudFormation-Templates目录中的所有.yml文件上传到该存储桶中（[Github代码库](https://github.com/xd6wang/smbsecassessment/tree/main/CloudFormation-Templates)）。请注意务必把文件直接上传到S3桶的根目录（不允许有二级目录）！
2. 选择全部的yml文件，然后 **Make public using ACL**

![Untitled](https://raw.githubusercontent.com/liangyimingcom/storage/master/PicGo/Untitled%202.png)

1. 记录下 SelfServiceSec.yml 文件的S3对象URL，例如： [https://s3-us-east-1.amazonaws.com/Bucket-Name/SelfServiceSec.yml](https://s3-us-west-2.amazonaws.com/Your-Bucket-Name-Here/SelfServiceSec.yml)

![Untitled](https://raw.githubusercontent.com/liangyimingcom/storage/master/PicGo/Untitled%203.png)





## 三、部署堆栈（Stack）

您需要在AWS 同一个账号下，同一个S3 Region内，创建一些资源及组件用以进行配置安全扫描，具体步骤如下：

1. 打开CloudFormation控制台界面，选择“**创建堆栈**”；
2. 选择“**模版已就绪**”，模版源选择“Amazon S3 URL”并填入上一步记录的 SelfServiceSec.yml 文件的S3对象URL
   
    ![Untitled](https://raw.githubusercontent.com/liangyimingcom/storage/master/PicGo/Untitled%204.png)
    
3. 填入一个唯一的堆栈名字, 如 **smbsecassessment**
4. 在参数“TemplateS3Bucket”中填写之前创建的S3存储桶的名字。**注意这里只填存储桶名**
   
    ![Untitled](https://raw.githubusercontent.com/liangyimingcom/storage/master/PicGo/Untitled%205.png)
    
5. 按需填写标签（Tag）
6. 权限部分可选择一个具备创建之前所述资源的IAM角色或者留空。**建议留空**，会使用您当前操作所使用的IAM权限进行资源创建
7. 堆栈故障选项选择“回滚所有堆栈资源”
   
    ![Untitled](https://raw.githubusercontent.com/liangyimingcom/storage/master/PicGo/Untitled%206.png)
    
8. 高级选项全部使用默认值
9. 确认所有选项填写无误后，勾选以下两个选项后，点击“创建堆栈”：
    - 我确认，AWS CloudFormation 可能创建具有自定义名称的 IAM 资源。
    - 我确认，AWS CloudFormation 可能需要以下功能: CAPABILITY_AUTO_EXPAND
    
    ![Untitled](https://raw.githubusercontent.com/liangyimingcom/storage/master/PicGo/Untitled%207.png)
    
10. 等待5分钟左右堆栈状态显示 “CREATE_COMPLETE” ，部署完成
    
    ![Untitled](https://raw.githubusercontent.com/liangyimingcom/storage/master/PicGo/Untitled%208.png)
    

## 四、下载报告

1. 堆栈部署完成后，工具会自动对账号下所有region的资源进行扫描，需要几十分钟（若账号内资源过多花费的时间可能更长），通常一个小时的扫描所需要的花费不足$1美金；
2. 待工具扫描完成后，会在以堆栈名开头的S3存储桶中（例如: smbsecassessment-rs3stack-xxxxx-rcentralizedbucket-xxxxxxxxxx）生成报告文件；
3. 将其中的.docx文件下载至本地用Word打开：
   
    ![Untitled](https://raw.githubusercontent.com/liangyimingcom/storage/master/PicGo/Untitled%209.png)
    



## 五、清理环境

1. 当完成所有扫描并下载完扫描报告后，删除存放报告的S3存储桶中的所有文件；
2. 打开CloudFormation控制台，选择之前创建的堆栈，点击删除按钮；
3. 如遇到rS3Stack 删除失败，再次确保手动删除S3存储桶中的所有文件，然后再删除该堆栈
   
    ![Untitled](https://raw.githubusercontent.com/liangyimingcom/storage/master/PicGo/Untitled%2010.png)
    






## 六、结束




## 附件、常见问题与troubleshooting

再同一个账号下如果重复运行，或者之前的运行资源清除不够干净，会出现的常见问题如下：

Embedded stack arn:aws:cloudformation:us-west-2:153705321444:stack/smbsecassessment-rIAMStack-D5S116AA19UC/c5915290-beef-11ed-bd43-06f95d496a8b was not successfully created: The following resource(s) failed to create: [rSelfServiceSecSecurityRole].

![image-20230310110539971](https://raw.githubusercontent.com/liangyimingcom/storage/master/PicGo/image-20230310110539971.png)

解决方法：去IAM里面删除role，名字为：SelfServiceSecSecurityRole

问题解决；

![image-20230310110705084](https://raw.githubusercontent.com/liangyimingcom/storage/master/PicGo/image-20230310110705084.png)
