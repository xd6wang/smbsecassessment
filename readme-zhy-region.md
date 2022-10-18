
## 中国北京宁夏区域请使用以下步骤部署
1. 下载 cloudformation 文件：https://ots-tool.s3.us-west-2.amazonaws.com/bjs-zhy-codebuild-prowler-audit-account-cfn.yaml
2. 打开宁夏区域控制台： https://cn-northwest-1.console.amazonaws.cn/cloudformation/home?region=cn-northwest-1#/stacks/create/template
3. 上传下载的cloudformation 文件
4. 输入堆栈名称，其他值默认
5. 等待五分钟，打开codebuild 控制台，并开始构建 ProwlerCodeBuild-XXXX 项目： https://cn-northwest-1.console.amazonaws.cn/codesuite/codebuild/projects
6. 等待codebuild 运行之后，可以在S3 ots-reports-cn-northwest-1-prowler-XXXX 存储桶找到扫描报告
