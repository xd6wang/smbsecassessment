
## 中国北京宁夏区域请使用以下步骤部署
1. 打开链接一键部署扫描堆栈： https://cn-northwest-1.console.amazonaws.cn/cloudformation/home?region=cn-northwest-1#/stacks/create/template?templateURL=https://ots-template.s3.amazonaws.com/bjs/SelfServiceSec.yml&stackName=ots-scan
2. 选项全部保持默认值，点击下一步
3. 确认所有选项填写无误后，勾选以下选项后，点击“创建堆栈”：
   - 我确认，AWS CloudFormation 可能创建具有自定义名称的 IAM 资源
4. 堆栈部署过程大概需要5分钟
5. 打开codebuild控制台，并点击开始构建 ProwlerCodeBuild-XXXX 项目： https://cn-northwest-1.console.amazonaws.cn/codesuite/codebuild/projects
6. 等待codebuild 运行结束之后，扫描就可以完成了，可以在S3控制台https://console.amazonaws.cn/s3 找到 ots-reports-cn-northwest-1-prowler-XXXX 存储桶 
7. 将其中的.docx文件下载至本地用Word打开即可

## 清理环境
1. 当完成所有扫描并下载完扫描报告后，删除存放报告的S3存储桶中的所有文件
2. S3存储桶清空后，打开CloudFormation控制台，选择之前创建的堆栈，点击删除按钮