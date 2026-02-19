# astrbot-plugin-fuduji

AstrBot 复读插件 / Repeater plugin for AstrBot

## 功能介绍

当有超过2个不同的玩家说相同的话时，机器人会自动复读这句话。

## 使用场景

- 群聊中多人说同一句话时，机器人参与复读
- 增加群聊互动趣味性
- 自动检测群组消息，无需手动触发

## 使用说明

1. 安装插件到 AstrBot
2. 重载插件
3. 在群聊中让2个以上的不同用户发送相同的消息
4. 机器人会自动复读

## 配置

- 最多记录最近10条消息
- 只统计不同用户发送的相同内容
- 自动忽略空消息和命令（以 `/` 开头）

## 支持

- [AstrBot Repo](https://github.com/AstrBotDevs/AstrBot)
- [AstrBot Plugin Development Docs (Chinese)](https://docs.astrbot.app/dev/star/plugin-new.html)
- [AstrBot Plugin Development Docs (English)](https://docs.astrbot.app/en/dev/star/plugin-new.html)

## 作者

andjie98

## 许可证

AGPL-3.0 license
