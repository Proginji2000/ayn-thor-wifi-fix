# AYN Thor Wi-Fi 수정 — 커뮤니티 가이드

[English](en.md) · [Français](fr.md) · [Español](es.md) · [Deutsch](de.md) · [简体中文](zh-CN.md) · [日本語](ja.md) · [한국어](ko.md) · [Русский](ru.md)

**미리보기: 공개 설치 프로그램은 아직 없습니다.** Manual Edition RC1 및 Permanent Edition V4.3 RC1은 한 대의 기기에서만 비공개로 테스트했습니다. 공개 배포는 승인되지 않았습니다.

## 호환성
`Thor_V1.0.0.377_20260206_165408_user`, kalama, Android 13(API 33), 슬롯 a만 테스트했습니다. 다른 펌웨어, 슬롯, 하드웨어 변형 및 OTA 업데이트는 검증되지 않았습니다. 버전이나 무결성 검사 결과가 다르면 중단하십시오.

## 에디션 선택
- Manual Edition: 비공개 재사용 런처. 완전히 부팅한 후마다 수동 활성화합니다. 활성화하면 Android 프레임워크가 다시 시작되고 앱이 종료됩니다. 완전 재부팅하면 순정 Wi-Fi 구성 요소가 복원됩니다. 완전 제거 및 강화된 RC2 설치는 검증되지 않았습니다.
- Permanent Edition: 테스트 기기의 Magisk 31.1용 비공개 V4.3 RC1 모듈. Zygote 시작 전에 활성화하고 상태를 두 번 확인합니다. 수정 상태 부팅 3회, 상태 검사 6회, 반복 활성화, 미확인 부팅 상태 모의 보호, 비활성화, 제거 및 재설치가 통과했습니다. 두 에디션을 동시에 사용하지 마십시오.

## 현재 제공되는 기능
순정 Wi-Fi 구성 요소로 완전히 부팅된 기기에서 Python 3 및 공식 [Android Platform-Tools](https://developer.android.com/tools/releases/platform-tools)를 설치하십시오. USB 디버깅을 활성화하고 USB 기기 한 대만 연결하여 승인하십시오. 저장소 루트에서 실행합니다.
```bash
python3 tools/manual_preflight.py
python3 tools/manual_preflight.py --extract-stock thor-stock-private
```

Windows에서는 필요에 따라 `python3` 대신 `py -3`을 사용하십시오. ADB 경로가 다르면 `--adb /path/to/adb`를 지정합니다(WSL에서 Windows ADB 사용 시 adb.exe). 두 번째 명령은 새로운 비공개 로컬 디렉터리를 생성합니다. 도구는 읽기 전용이며 루팅, 플래싱, 설치 또는 재부팅을 하지 않습니다. 수정이 활성화된 상태에서 순정 검사를 하지 마십시오. 추출 파일은 비공개로 보관하십시오.

로컬에서 이미 생성한 후보 파일은 오프라인으로 검증할 수 있습니다.
```bash
python3 tools/manual_verify_bundle.py path-to-candidate
```

PASS는 정확한 해시 일치만 의미하며 설치 승인이 아닙니다. 공개 빌더와 전체 설치 절차는 아직 제공되지 않습니다.

## 안전 및 복구
향후 설치 전에 데이터를 백업하십시오. 영구 에디션에는 독립적으로 검증된 root 및 복구 환경이 필요합니다. 공유된 패치 부팅 이미지를 사용하거나 이 미리보기를 근거로 잠금 해제 또는 플래싱하지 마십시오. 슬롯이나 AVB를 변경하지 마십시오. 알 수 없는 펌웨어, 해시 불일치, 미확인 부팅 또는 오류가 발생하면 중단하십시오. `pending`을 수동으로 삭제하지 마십시오. 테스트한 비공개 설치에서는 Magisk에서 모듈을 비활성화하거나 제거한 뒤 정상 재부팅하면 순정 Wi-Fi 구성 요소로 돌아갑니다. 부팅 파티션 또는 root 상태는 복원되지 않습니다. Manual은 Enable을 실행하지 않고 재부팅하십시오. 실제 부팅 장애 복구, 전원 차단 내구성, init_boot 실제 복원 및 장기 안정성은 검증되지 않았습니다. 다른 기기도 검증되지 않았습니다.

## 지원
에디션, 펌웨어, 실패 단계 및 익명화된 진단 표시만 보고하십시오. 일련번호, 부팅 ID, SSID, BSSID, 주소 및 개인정보를 제거하십시오. 펌웨어, JAR/ODEX/VDEX 파일 또는 부팅 이미지를 업로드하지 마십시오. 지원이 시작되면 저장소 이슈를 사용하십시오. AYN 공식 배포가 아닌 독립 프로젝트입니다.

[Compatibility matrix](../../compatibility/firmware-matrix.json) · [Release gates](../COMMUNITY_RELEASE.md)
