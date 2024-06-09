
## 中国北京宁夏区域请使用以下步骤部署
1. 打开链接一键启动扫描堆栈： https://cn-north-1.console.amazonaws.cn/cloudformation/home?region=cn-north-1#/stacks/create?stackName=ots-scan&templateURL=https://ots-template.s3.amazonaws.com/bjs-load-zip/SelfServiceSec.yml
2. 权限部分可选择一个具备创建之前所述资源的IAM角色或者留空。若留空，则会使用您当前操作所使用的IAM权限进行资源创建
3. 堆栈故障选项选择“回滚所有堆栈资源”
4. 高级选项全部使用默认值
5. 确认所有选项填写无误后，勾选以下两个选项后，点击“创建堆栈”：
   - 我确认，AWS CloudFormation 可能创建具有自定义名称的 IAM 资源。
   - 我确认，AWS CloudFormation 可能需要以下功能: CAPABILITY_AUTO_EXPAND

## 清理环境
1. 当完成所有扫描并下载完扫描报告后，删除存放报告的S3存储桶中的所有文件
2. S3存储桶清空后，打开CloudFormation控制台，选择之前创建的堆栈，点击删除按钮