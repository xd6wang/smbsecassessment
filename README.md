# 亚马逊云配置安全扫描 - 中小企业版

云上安全建设是用户上云之后需要非常重视的一部分工作，近些年来随着越来越多的企业的业务系统开始上云，云上的安全事故也随之越来越频繁的发生。这些事故中有相当一部分是由于不安全的云上配置所导致的，例如，错误的将存有敏感数据的存储桶设置为公开访问、缺少对特权账号密钥泄漏的防护等。许多安全厂商及云服务提供商自身都提供了许多的工具和服务来帮助用户发现云上的不安全配置并监控云上的安全威胁事件，但受限于资金，资源的不足，许多中小企业没有足够的意愿或精力来部署这些工具和服务，他们的云上资源和系统长期处于“裸奔”状态，使得许多的攻击者将攻击的目标由知名、高价值企业转向了数量众多且易于攻破的中小企业。

因此，本工具致力于帮助中小企业用户快速发现亚马逊云账号中的高危配置错误，使用户可以对这些极易被攻击者利用的潜在漏洞进行及时修复。本工具基于开源工具“[Prowler](https://github.com/prowler-cloud/prowler)”，并将其中的240多项检查精简为70余项，这70余项检查对云上安全至关重要并且易于修复，因此非常适合中小企业用户快速进行云上安全的基础加固。

需要说明的是，安全建设不是一次性的工作，安全需要我们持续的投入，我们应该不断的对云上新的资源、配置、服务、威胁等进行持续的检查和监控。本工具的目的只是为了帮助用户快速评估当前时间节点的高危配置问题，即使扫描没有发现任何问题或者所有发现的问题都已被修复，也不能代表在之后的时间里不会出现新的问题。并且，安全的风险可能来自各个方面，本工具只对部分高危配置问题进行检查，但是除此之外还有非常多可能被攻击者所利用的配置问题也需要我们需进行关注和加固。因此，为保障云上系统和业务的长期安全，建议用户采用Amazon GuardDuty, AWS Security Hub, AWS Config或其他安全工具对云上资源和配置进行持续的扫描和监控。
<br />
<br />

# 开始部署

- 在 AWS 海外区域部署
https://github.com/xd6wang/smbsecassessment/blob/main/readme-global.md

- 在 AWS 中国区域部署
https://github.com/xd6wang/smbsecassessment/blob/main/readme-zhy-region.md


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



# License

Apache-2.0 License.
