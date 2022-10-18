
## 中国北京宁夏区域请使用以下步骤部署
1. 下载 cloudformation 文件：https://ots-tool.s3.us-west-2.amazonaws.com/bjs-zhy-codebuild-prowler-audit-account-cfn.yaml
2. 打开宁夏区域控制台： https://cn-northwest-1.console.amazonaws.cn/cloudformation/home?region=cn-northwest-1#/stacks/create/template
3. 上传下载的cloudformation 文件
4. 输入堆栈名称，其他值默认，下一步
5. 确认所有选项填写无误后，勾选以下两个选项后，点击“创建堆栈”：
   - 我确认，AWS CloudFormation 可能创建具有自定义名称的 IAM 资源
6. 大约几分钟即可完成部署

## 开启扫描与结束扫描
1. 等待五分钟，打开codebuild 控制台，并点击开始构建 ProwlerCodeBuild-XXXX 项目： https://cn-northwest-1.console.amazonaws.cn/codesuite/codebuild/projects
2. 等待codebuild 运行结束之后，扫描就可以完成了，可以在S3https://console.amazonaws.cn/s3 找到 ots-reports-cn-northwest-1-prowler-XXXX 存储桶 
3. 将其中的.docx文件下载至本地用Word打开即可

## 清理环境
1. 当完成所有扫描并下载完扫描报告后，删除存放报告的S3存储桶中的所有文件
2. S3存储桶清空后，打开CloudFormation控制台，选择之前创建的堆栈，点击删除按钮
3. 手动删除之前用于上传Cloudformation代码的S3存储桶中的所有文件，然后再删除该存储桶

