# AYN Thor Wi-Fi 修正 — コミュニティガイド

[English](en.md) · [Français](fr.md) · [Español](es.md) · [Deutsch](de.md) · [简体中文](zh-CN.md) · [日本語](ja.md) · [한국어](ko.md) · [Русский](ru.md)

**プレビュー版：公開インストーラーは未提供です。** Manual Edition RC1 と Permanent Edition V4.3 RC1 は、1 台の実機でのみ非公開テストを実施しました。一般配布は未承認です。

## 互換性
テスト対象は `Thor_V1.0.0.377_20260206_165408_user`、kalama、Android 13（API 33）、スロット a のみです。他のファームウェア、スロット、ハードウェア構成、OTA 更新は未検証です。バージョンや整合性が一致しない場合は中止してください。

## エディションの選択
- Manual Edition：非公開の再利用可能なランチャー。完全起動のたびに手動で有効化します。有効化時に Android フレームワークが再起動し、アプリが終了します。完全再起動で純正 Wi-Fi コンポーネントに戻ります。完全アンインストールと強化版 RC2 のインストールは未検証です。
- Permanent Edition：検証端末上の Magisk 31.1 用非公開 V4.3 RC1 モジュール。Zygote 起動前に有効化し、2 回の状態確認を行います。修正状態での起動 3 回、状態確認 6 回、繰り返し有効化、未確認起動を模擬した保護、無効化、削除、再インストールに成功しました。両エディションを同時に使用しないでください。

## 現在利用できる機能
純正 Wi-Fi コンポーネントで完全起動した端末を使用し、Python 3 と公式 [Android Platform-Tools](https://developer.android.com/tools/releases/platform-tools) をインストールします。USB デバッグを有効にし、USB 端末を 1 台だけ接続して認証します。リポジトリのルートで実行します。
```bash
python3 tools/manual_preflight.py
python3 tools/manual_preflight.py --extract-stock thor-stock-private
```

Windows では必要に応じて `python3` の代わりに `py -3` を使用します。ADB の場所が異なる場合は `--adb /path/to/adb` を指定します（WSL から Windows ADB を使う場合は adb.exe）。2 番目のコマンドは新しい非公開ローカルディレクトリを作成します。端末の読み取りのみを行い、root 化、書き込み、インストール、再起動は行いません。修正が有効な状態で純正チェックを行わないでください。抽出ファイルは非公開で保管してください。

ローカルで作成済みの候補ファイルはオフラインで検証できます。
```bash
python3 tools/manual_verify_bundle.py path-to-candidate
```

PASS はハッシュの完全一致のみを示し、インストールの許可ではありません。公開ビルダーと完全なインストール手順は未提供です。

## 安全性と復旧
今後のインストール前にデータをバックアップしてください。永久版には独立して検証済みの root・復旧環境が必要です。共有された修正済みブートイメージを使わず、このプレビューを根拠にロック解除や書き込みを行わないでください。スロットや AVB を変更しないでください。不明なファームウェア、ハッシュ不一致、未確認起動、エラーがあれば中止してください。`pending` を手動で削除しないでください。検証済みの非公開環境では Magisk でモジュールを無効化または削除し、通常再起動すると純正 Wi-Fi コンポーネントに戻ります。ブートパーティションや root 状態は戻りません。Manual は Enable を実行せず再起動します。実際の起動障害からの復旧、電源断への耐性、init_boot の実復元、長期安定性は未検証です。他の端末は未検証です。

## サポート
エディション、ファームウェア、失敗段階、匿名化した診断マーカーのみを報告してください。シリアル番号、起動 ID、SSID、BSSID、アドレス、個人情報は除去してください。ファームウェア、JAR/ODEX/VDEX、ブートイメージをアップロードしないでください。サポート開始後はリポジトリの Issue を使用してください。AYN 公式ではない独立プロジェクトです。

[Compatibility matrix](../../compatibility/firmware-matrix.json) · [Release gates](../COMMUNITY_RELEASE.md)
