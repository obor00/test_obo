from packaging.version import Version

versions = [
    "ttt-4.10.0-rc2",
    "ttt-4.11.0",
    "ttt-4.11.0-rc1",
    "ttt-4.11.0-rc2",
    "ttt-4.11.8",
    "ttt-4.11.9",
    "ttt-4.11-bxcinteg1",
    "ttt-4.12.0",
    "ttt-4.12.0-cd1",
    "ttt-4.12.0-rc1",
    "ttt-4.12.0-rc2",
    "ttt-4.12.0-rc5",
    "ttt-4.12.8",
    "ttt-4.12.9",
    "ttt-4.13.0-cd1",
    "ttt-4.13.0-rc1",
    "ttt_4.7.2-8",
    "ttt_4.7.2-9",
    "ttt-4.8.0-rc1",
    "ttt-4.9.0-cd1",
    "ttt-4.9.0-rc1",
    "ttt-4.9.0-rc2",
    "ttt-4.9.0-rc3",
    "ttt-4.9.0-rc4",
    "ttt-4.9.1",
    "ttt-4.9.1-rc0",
    "ttt-4.9.1-rc1",
    "ttt-4.9.1-rc10",
    "ttt-4.9.1-rc11"
]

release_versions = {}

for version in versions:
    version = version.split("-")[-1]  # Extract the version part
    try:
        v = Version(version)
        release = version.split(".")[0]
        major_version = v.release[0]  # Extract the major version
        if release not in release_versions or major_version > release_versions[release].release[0]:
            release_versions[release] = v
    except:
        pass

for release, version in release_versions.items():
    print(f"Last major version for release {release}: {version}")

