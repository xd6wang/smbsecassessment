# 亚马逊云配置安全扫描 - 中小企业版

云上安全建设是用户上云之后需要非常重视的一部分工作，近些年来随着越来越多的企业的业务系统开始上云，云上的安全事故也随之越来越频繁的发生。这些事故中有相当一部分是由于不安全的云上配置所导致的，例如，错误的将存有敏感数据的存储桶设置为公开访问、缺少对特权账号密钥泄漏的防护等。许多安全厂商及云服务提供商自身都提供了许多的工具和服务来帮助用户发现云上的不安全配置并监控云上的安全威胁事件，但受限于资金，资源的不足，许多中小企业没有足够的意愿或精力来部署这些工具和服务，他们的云上资源和系统长期处于“裸奔”状态，使得许多的攻击者将攻击的目标由知名、高价值企业转向了数量众多且易于攻破的中小企业。

因此，本工具致力于帮助中小企业用户快速发现亚马逊云账号中的高危配置错误，使用户可以对这些极易被攻击者利用的潜在漏洞进行及时修复。本工具基于开源工具“[Prowler](https://github.com/prowler-cloud/prowler)”，并将其中的240多项检查精简为70余项，这70余项检查对云上安全至关重要并且易于修复，因此非常适合中小企业用户快速进行云上安全的基础加固。

需要说明的是，安全建设不是一次性的工作，安全需要我们持续的投入，我们应该不断的对云上新的资源、配置、服务、威胁等进行持续的检查和监控。本工具的目的只是为了帮助用户快速评估当前时间节点的高危配置问题，即使扫描没有发现任何问题或者所有发现的问题都已被修复，也不能代表在之后的时间里不会出现新的问题。并且，安全的风险可能来自各个方面，本工具只对部分高危配置问题进行检查，但是除此之外还有非常多可能被攻击者所利用的配置问题也需要我们需进行关注和加固。因此，为保障云上系统和业务的长期安全，建议用户采用Amazon GuardDuty, AWS Security Hub, AWS Config或其他安全工具对云上资源和配置进行持续的扫描和监控。


# 如何部署
## 权限
部署过程将在您的账号中创建一系列的资源，因此，请确保您做部署的IAM用户或角色有权限创建下列资源：
+ IAM Role
+ IAM Managed Policy
+ VPC
+ IGW
+ Route tables
+ Security Group
+ NAT Gateway
+ Elastic IP (EIP)
+ EC2 Instance
+ S3 Bucket

## 创建一个S3存储桶并上传Cloudformation代码
您需要把本代码库中的Cloudformation代码复制到一个S3存储桶中，用以创建Cloudformation 堆栈（Stack），因此请：
1. 创建一个S3存储桶
2. 将CloudFormation-Templates目录中的所有.yml文件上传到该存储桶中
3. 记录下SelfServiceSec.yml文件的S3对象URL，例如： https://s3-us-west-2.amazonaws.com/Your-Bucket-Name-Here/SelfServiceSec.yml

## 创建CloudFormation 堆栈（Stack）
1. 打开CloudFormation控制台界面，选择“创建堆栈”
2. 选择“模版已就绪”，模版源选择“Amazon S3 URL”并填入上一步记录的SelfServiceSec.yml文件的S3对象URL
3. 填入一个唯一的堆栈名字
4. 在参数“TemplateS3Bucket”中填写之前创建的S3存储桶的名字。注意这里只填存储桶名，例如：your-bucket-name
5. 按需填写标签（Tag）
6. 权限部分可选择一个具备创建之前所述资源的IAM角色或者留空。若留空，则会使用您当前操作所使用的IAM权限进行资源创建
7. 堆栈故障选项选择“回滚所有堆栈资源”
8. 高级选项全部使用默认值
9. 确认所有选项填写无误后，勾选以下两个选项后，点击“创建堆栈”：
   - 我确认，AWS CloudFormation 可能创建具有自定义名称的 IAM 资源。
   - 我确认，AWS CloudFormation 可能需要以下功能: CAPABILITY_AUTO_EXPAND

## 开启扫描与结束扫描
1. CloudFormation堆栈创建完成后，将自动立即使用堆栈中创建的EC2主机进行扫描，无需进行任何手动操作
2. 扫描结束后，EC2主机将自动关机，因此只要观察到该EC2关机即可认为扫描结束

## 下载报告
1. 打开S3存储桶控制台，找到以创建CloudFormation堆栈时填入的堆栈名开头的存储桶，例如:yourstackname-rs3stack-xxxxx-rcentralizedbucket-xxxxxxxxxx
2. 将其中的.docx文件下载至本地用Word打开即可
注意：若执行扫描的EC2主机已关机但是在该S3存储桶中没有看到扫描报告，说明扫描出错，请在Issues中留言告知。

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


# 常见问题

1. 这个工具是否产生费用，扫描一次需要花费多少钱?
    + 是的，如前所述，这个工具创建一些资源及组件用以进行扫描，通常一个小时的扫描所需要的花费不足$1美金

2. 这是一个持续扫描及监控工具吗?
    + 不是，这个工具适合执行单次扫描，用于快速发现账号中的高危配置问题，为保障云上系统和业务的长期安全，建议用户采用Amazon GuardDuty, AWS Security Hub, AWS Config或其他安全工具对云上资源和配置进行持续的扫描和监控
  
3.	为何删除CloudFormation堆栈的时候报错?
    + 请确保保存报告的S3存储桶中没有任何文件
    + 请确保没有手动向该堆栈所创建的VPC中添加任何额外资源

1. 扫描需要多长时间
    + 通常需要几十分钟，若账号内资源过多花费的时间可能更长
  
2. 是否支持多账号扫描
    + 暂不支持

3. 是否支持北京和宁夏区域
    + 暂不支持


# License

Apache-2.0 License.