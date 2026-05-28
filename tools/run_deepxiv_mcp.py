from pathlib import Path
import os


def load_project_env() -> None:
    project_root = Path(__file__).resolve().parents[1]
    env_path = project_root / ".env"
    if not env_path.exists():
        return

    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue

        name, value = line.split("=", 1)
        name = name.strip()
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
            value = value[1:-1]
        if name:
            os.environ[name] = value

    if not os.environ.get("DEEPXIV_TOKEN") and os.environ.get("DEEPXIV_API_TOKEN"):
        os.environ["DEEPXIV_TOKEN"] = os.environ["DEEPXIV_API_TOKEN"]


def main() -> None:
    load_project_env()
    from deepxiv_sdk.mcp_server import create_server

    create_server().run(transport="stdio")


if __name__ == "__main__":
    main()
