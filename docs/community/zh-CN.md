# AYN Thor Wi-Fi 修复 — 社区指南

[English](en.md) · [Français](fr.md) · [Español](es.md) · [Deutsch](de.md) · [简体中文](zh-CN.md) · [日本語](ja.md) · [한국어](ko.md) · [Русский](ru.md)

**预览文档，尚无公开安装程序。** Manual Edition RC1 和 Permanent Edition V4.3 RC1 仅在一台设备上进行了私下测试，尚未批准公开分发。

## 兼容性
仅测试了 `Thor_V1.0.0.377_20260206_165408_user`、kalama、Android 13（API 33）、a 槽位。其他固件、槽位、硬件变体及 OTA 更新均未通过验证。版本或完整性检查不一致时请停止。

## 选择版本
- Manual Edition：私有可重复使用的启动器，每次完整启动后手动启用。启用时会重启 Android 框架并关闭应用。完整重启可恢复原厂 Wi-Fi 组件。完整卸载及加固版 RC2 安装尚未验证。
- Permanent Edition：在测试设备上使用 Magisk 31.1 的私有 V4.3 RC1 模块。在 Zygote 启动前自动启用并进行两次健康检查。已通过三次修复状态启动、六次健康检查、重复启用、模拟未确认启动保护、停用、卸载和重新安装测试。切勿同时使用两个版本。

## 当前可用功能
在完全启动且 Wi-Fi 组件为原厂状态的设备上安装 Python 3 和官方 [Android Platform-Tools](https://developer.android.com/tools/releases/platform-tools)。启用 USB 调试，仅连接一台 USB 设备并授权连接。在仓库根目录执行：
```bash
python3 tools/manual_preflight.py
python3 tools/manual_preflight.py --extract-stock thor-stock-private
```

Windows 如有需要可使用 `py -3` 代替 `python3`。ADB 不在默认路径时使用 `--adb /path/to/adb`（从 WSL 使用 Windows ADB 时为 adb.exe）。第二条命令创建新的本地私有目录。工具只读取设备，不获取 root 权限、不刷写、不安装、不重启。修复生效时不要进行原厂状态检查。请私下保存提取的文件。

如已拥有本地构建的候选文件，可离线验证：
```bash
python3 tools/manual_verify_bundle.py path-to-candidate
```

PASS 仅表示哈希值完全匹配，不代表安装许可。公开构建工具及完整安装流程尚不可用。

## 安全与恢复
任何后续安装前备份数据。永久版需要已独立验证的 root 和恢复环境；不要使用他人分享的已修补启动镜像，不要根据本预览解锁或刷写。不要更改槽位或 AVB。固件未知、哈希不符、启动未确认或出现错误时请停止。不要手动删除 `pending`。在已测试的私有安装中，可在 Magisk 中停用或删除模块，然后正常重启；此操作仅恢复原厂 Wi-Fi 组件，不恢复启动分区或 root 状态。手动版请重启且不运行 Enable。真实启动故障恢复、断电耐久性、init_boot 实际恢复和长期稳定性尚未验证。未验证其他设备。

## 支持
报告版本、固件、失败阶段和脱敏诊断标记。移除序列号、启动 ID、SSID、BSSID、地址及个人数据。不要上传固件、JAR/ODEX/VDEX 文件或启动镜像。支持开放后使用仓库问题追踪系统。本项目独立开发，并非 AYN 官方发布。

[Compatibility matrix](../../compatibility/firmware-matrix.json) · [Release gates](../COMMUNITY_RELEASE.md)
