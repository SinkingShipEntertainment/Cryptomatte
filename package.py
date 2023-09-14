name = "Cryptomatte"

# NOTE: <external_version>.sse.<internal_version>
version = "1.5.0.beta.sse.1.0.0"

authors = [
    "Jonah Friedman",
    "Andy Jones",
]

description = """Nuke and Fusion plugin"""

with scope("config") as c:
    import os
    c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_EXT"]

requires = [
    "nuke-11",
]

private_build_requires = [
]

variants = [
]

build_command = "rez python {root}/rez_build.py"
uuid = "repository.Cryptomatte"


def pre_commands():
    pass

def commands():

    # NOTE: REZ package versions can have ".sse." to separate the external
    # version from the internal modification version.
    split_versions = str(version).split(".sse.")
    external_version = split_versions[0]
    internal_version = None
    if len(split_versions) == 2:
        internal_version = split_versions[1]

    env.CRYPTOMATTE_VERSION = external_version
    env.CRYPTOMATTE_PACKAGE_VERSION = external_version
    if internal_version:
        env.CRYPTOMATTE_PACKAGE_VERSION = internal_version

    env.CRYPTOMATTE_ROOT.append("{root}")
    env.CRYPTOMATTE_LOCATION.append("{root}")
    env.REZ_CRYPTOMATTE_ROOT = '{root}'

    env.NUKE_PATH.append('{root}/nuke')  # so Nuke can find it

def post_commands():
    pass