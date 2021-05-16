# Tieba Cloud Review@Github Action
 利用Github Action自动进行各类贴吧操作，目前主要针对吧务管理

# 执行状态
[![Tieba auto helper](https://github.com/FinBird/Tieba-Helper/actions/workflows/main.yml/badge.svg)](https://github.com/FinBird/Tieba-Helper/actions/workflows/main.yml)

# 使用方法

1. Fork 本仓库，然后点击你的仓库右上角的 Settings，找到 Secrets 这一项，添加两个秘密环境变量。

-  `BDUSS` 存放你的 BDUSS。支持同时添加多个帐户，BDUSS 之间用 `#` 隔开即可。

-  `CONFIG`为 json，存放有关操作的配置信息。具体请参考`config.json`
2. 设置好环境变量后点击你的仓库上方的 `Actions` 选项，第一次打开需要点击 `I understand...` 按钮，确认在 Fork 的仓库上启用 GitHub Actions 。
3. 任意发起一次commit，触发Action的执行。

# TODO：

- [x] 1天循环封禁
- [ ] 10天循环封禁
- [ ] 定制封禁时长
- [ ] 关键字删贴
- [ ] 定时清除广告贴
- [ ] 签到

# 鸣谢

本项目依托于[@Starry-OvO](https://github.com/Starry-OvO)的“贴吧云审查工具包”并有所修改

本项目尚在建设中，欢迎Pull request

# License

MIT

