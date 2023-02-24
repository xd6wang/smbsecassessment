
## 创建CloudFormation 堆栈（Stack）
1. 打开链接一键启动扫描堆栈： https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/template?stackName=ots-scan&templateURL=https://ots-template.s3.amazonaws.com/SelfServiceSec.yml
2. 权限部分可选择一个具备创建之前所述资源的IAM角色或者留空。若留空，则会使用您当前操作所使用的IAM权限进行资源创建
3. 堆栈故障选项选择“回滚所有堆栈资源”
4. 高级选项全部使用默认值
5. 确认所有选项填写无误后，勾选以下两个选项后，点击“创建堆栈”：
   - 我确认，AWS CloudFormation 可能创建具有自定义名称的 IAM 资源。
   - 我确认，AWS CloudFormation 可能需要以下功能: CAPABILITY_AUTO_EXPAND

## 开启扫描与结束扫描
1. CloudFormation堆栈创建完成后，将自动立即使用堆栈中创建的EC2主机进行扫描，无需进行任何手动操作
2. 扫描结束后，EC2主机将自动关机，因此只要观察到该EC2关机即可认为扫描结束

## 下载报告
1. 打开S3存储桶控制台，找到以创建CloudFormation堆栈时填入的堆栈名开头的存储桶，例如:yourstackname-rs3stack-xxxxx-rcentralizedbucket-xxxxxxxxxx
2. 将其中的.docx文件下载至本地用Word打开即可。注意：若执行扫描的EC2主机已关机但是在该S3存储桶中没有看到扫描报告，说明扫描出错，请在Issues中留言告知。

## 清理环境
1. 当完成所有扫描并下载完扫描报告后，删除存放报告的S3存储桶中的所有文件
2. S3存储桶清空后，打开CloudFormation控制台，选择之前创建的堆栈，点击删除按钮
3. 手动删除之前用于上传Cloudformation代码的S3存储桶中的所有文件，然后再删除该存储桶



# 本工具所创建的资源

+ 一个VPC
    + 一个 /26 网段大小的VPC
    + 两个在同一可用区的子网, 一个公有子网，一个私有子网
    + 必要的路由表和ACL

 + 一个EIP
    + 将用于NAT Gateway

 + 一个NAT Gateway
    + 用于EC2实例通过Internet下载Prowler、报告生成代码及相关依赖库，以及调用AWS API用于配置检查

 + 一个安全组（Security Group）
    + 将挂载至所创建的EC2实例

 + 一个m5a.large EC2实例
    + 用于运行扫描工具 
    + 10 GB gp2 EBS卷
    + 部署在私有子网
    + 没有EC2 Key Pair，因此无法通过外部SSH客户端登陆
    + 安全组不允许任何从外部向该EC2的连入
    + 扫描完成后该EC2实例将自动关机

 + 一个自定义IAM策略
    + 在SelfServiceSecIAM.yml中描述了策略内容
    + 该IAM策略内容遵照Prowler官方文档，用于执行Extra检测项
      + Prowler文档说明 [链接](https://github.com/prowler-cloud/prowler#custom-iam-policy)

 + 一个IAM角色
    + 挂载给EC2实例用于调用AWS API进行配置检查
    + 挂载了3个IAM策略：
      + arn:aws:iam::aws:policy/job-function/ViewOnlyAccess
      + arn:aws:iam::aws:policy/SecurityAudit
      + 上面的自定义IAM策略

 + 一个S3存储桶
    + 用于存放扫描报告
