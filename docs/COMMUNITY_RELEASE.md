# Community release engineering — 2026-11-28

**STATUS: PARTIAL. Owner use: GO on the exact tested configuration. Public installation: NO-GO.** Manual and Permanent have separate gates; missing full recovery media must not block offline Manual engineering.

## Baseline

- Exact firmware: `Thor_V1.0.0.377_20260206_165408_user`, kalama/API 33/slot a; one physical console.
- Manual RC1: reusable private pilot; hardened RC2 bootstrap and complete uninstall unqualified.
- Permanent V4.3 RC1: private exact tuple, three corrected boots, six health checks, normal recurrence, guard-state simulation, disable/uninstall/reinstall PASS. Real boot failure recovery and physical init_boot restore untested.
- Preserve exact qualified artifacts and immutable generator. Never repackage proprietary binaries in the repository, release assets or CI.
- Public guides in English, French, Spanish, German, Simplified Chinese, Japanese, Korean and Russian. English is the canonical translation source. All translations are machine-generated drafts pending native/technical review; identical commands and technical literals. Update translations in the same change when possible.

## Work packages and acceptance criteria

| ID | Deliverable | Current status | Exit criteria |
|---|---|---|---|
| D01 | Current status and 8-language preview | PASS (drafts) | Links valid, scope/limits consistent; human review before stable release |
| B01 | Standalone local build | PARTIAL | Exact JAR/DEX from user-owned stock on independent clean host, dependency provenance and immutable toolchain |
| B02 | Native ART portability | BLOCKED | Exact JAR/ODEX/VDEX tuple from independent workflow, or separately reviewed and physically qualified metadata-only variant; no relaxed hash gate |
| B03 | Shared offline pipeline | TODO | Explicit inputs, isolated outputs, no bundled proprietary files, no device activation by default, deterministic report, negative tests |
| M01 | Manual community installer | BLOCKED | Resolve native privileged bootstrap and uninstall; prove stage integrity, watchdog, exact rollback, install/reuse on independent device |
| P01 | Permanent community packaging | PARTIAL | Preserve tested boot scripts and strict tuple; review state-file safety, rollback failure, concurrent modules, early boot timeout, root prerequisites |
| P02 | Recovery and compatibility | BLOCKED | Independently usable recovery route for each target, authenticated local backups, documented limitations; no automatic partition writes |
| S01 | Security and licensing | TODO | Source/third-party license inventory; independent review; vendor coordination before detailed transformation disclosure |
| Q01 | External qualification | TODO | At least one other compatible Thor, controlled consent, private redacted evidence; no new flash merely for testing |
| R01 | Distribution | NO-GO | Each edition's relevant gates closed, published checksums, FR/EN + six translation reviews, explicit release decision |

## Host inventory and current offline evidence

Reference versions from the private qualified build: Python 3.14.4, zlib runtime 1.3.1, Java 21.0.13.1, smali/baksmali 2.5.2.git2771eae-debian, API 33, single job. These are observed version pins, not a complete dependency lock or independent reproducibility proof. Obtain verified tool package provenance before claiming portability.

On 2026-11-28 the available private generator and standalone builder SHA256 values matched the recorded baseline. Python syntax (three tools), POSIX sh and Bash syntax (two V4.3 scripts), archive CRC and all six manifest file hashes, Bash syntax (two RC2 scripts) passed. No build from stock, physical compile, device modification or independent host test executed in this review. The available local JAR is a candidate, not the stock input; never substitute it for stock. The ODEX/VDEX pair and exact stock input are required from the owner's private workspace.

## Release order

1. Resolve B01/B02 offline, test isolated local construction, preserve strict exact verification.
2. Review and package separate Manual and Permanent workflows using the same verified tuple. Manual needs no boot modification; Permanent requires independently established Magisk/recovery prerequisites.
3. Test rejection paths and independent clean host; document missing prerequisites and abort behavior.
4. Coordinate vendor disclosure privately, review licensing and source security, qualify a compatible independent device with consent.
5. Publish a candidate release only after applicable gates pass. Keep preview docs accessible meanwhile.

## Operations boundaries

No change to the owner's working V4.3 installation. No repeated routine physical scans, boot trials, flashes, forced power cuts, shared boot images, firmware uploads or detailed defect trigger publication. No new hardware qualification claimed by this document. A future independent trial may be needed only for a changed input or genuinely untested path. Keep historical logs as evidence, but current status here and the current matrix take precedence.


## B01/B02 — Offline replay preparation
B01/B02 offline audit/replay preparation (2026-11-28): private thor-community-offline.py SHA256 2c82395ec958ee108d993d455d9b59c470ae9cf3ded51a17792db628cb517018. Reads exact private RC2 kit and extracts only verified builder, checks stock JAR and exact reference tuple/DEX, inventories executable hashes, versions and installed Debian packages, optional read-only previously qualified ODEX diagnostic with exact JAR/VDEX, optional replay in fresh HOME/TMPDIR and bounded subprocesses. No ADB, network calls, package installs, deployment or partition operations. Local executed checks: Python syntax, real RC2 kit/embedded builder hash, synthetic hash accept/reject, symlink reject, synthetic tuple accept and mixed tuple reject, negative CLI rebuild gate, existing output collision rejection. Current environment correctly BLOCKED (Python 3.13.5 instead of 3.14.4, candidate not stock input, reference ODEX/VDEX absent); no actual build or variant execution. Next collect reference WSL audit without redundant rebuild; inventory is not a complete dependency lock. Then provision separate isolated host with verified dependencies and replay from exact stock. Native ART fixed-reference-path compilation remains untested; no device action while V4.3 is in normal use. Public release still NO-GO; private script and kit not added to public Git. No owner-device changes.


## B01/B02 — Reference WSL audit PASS / isolated replay prepared
B01/B02 reference WSL audit PASS (2026-11-28): owner transcript AUDIT_RC=0; private kit, exact stock JAR, exact reference tuple, toolchain versions, known observed metadata-only ODEX variant diagnostic and builder preflight passed. Rebuild NOT_RUN; deployment_allowed=false. Observed packages include python3.14 3.14.4-1ubuntu0.2, libsmali-java 2.5.2.git2771eae-4, OpenJDK 21 headless 21.0.13.1+2-1~26.04.1, zlib1g 1:1.3.dfsg+really1.3.1-1ubuntu3.2, Guava 32.0.1-1build1, ANTLR3 runtime 3.5.3-4, JCommander 1.71-4build1. Private thor-community-isolated.sh SHA256 e31cbadf0b0c8ead6298338c903a2f91de346ff77627c08daed7640d01f691d4 prepared. Bash syntax and missing-input rejection executed PASS. Requires working Podman or Docker; no host package installation. Resolves Ubuntu 26.04 amd64 base to digest, requests exact observed package versions (repository availability unverified), builds image from clean context with no proprietary inputs, runs existing audit/rebuild with network disabled, read-only inputs/rootfs, dropped capabilities and writable private results only. Captures image identity, installed packages and executable hash comparisons. Full isolated build not executed here; this is a separate container environment on the same physical host, not independent physical host or full transitive dependency lock. If versions unavailable stop, do not substitute silently. No ART compilation, device access, or deployment. Public release remains NO-GO; no private code or binaries added to Git.


## B01 isolated reconstruction PASS / B02 fixed path trial
B01 isolated reconstruction PASS (2026-11-28): owner transcript confirms Podman 5.7.0 installed, Ubuntu 26.04 amd64 base digest sha256:0d5255be560e2d2ddcfbfda88549e9e815ef29e7cd7fc62183d5709e6e2963c6, built image ID 37ef4963eb3b519cef82f30be36873ee74db218f3aa5c2b4be32f385520a9f13. Exact package pins installed, offline rebuild PASS, exact JAR/DEX, java/smali/baksmali/python executable hashes match reference. ISOLATED_RC=0; isolated software environment on same physical host, not separate physical host or fully locked transitive dependencies. B02 remains open: private thor-community-art-fixed.sh SHA256 32279820d32cc807ac514cb5abd778ee225891f6962d16e9881ac3c453c25ac4 derived from verified RC2 native ART compiler, retaining metadata, state stability and strict output hash gates, using exact historical compilation path. Bash and embedded POSIX sh syntax plus three synthetic directory allocation cases (fresh, existing, dangling symlink) PASS. No actual Android execution. Next isolated native compile from container-built candidate in temporary shell-owned directory, no root, framework restart, mount, PCI write or partition change; if original directory exists, stop without reuse/removal. Retain V4.3 current installation; do not infer shell namespace snapshot alone proves system_server mount identity. Exact output and independent-device compatibility remain unqualified. No public installer or private code published.
