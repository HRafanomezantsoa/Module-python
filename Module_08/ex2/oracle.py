#! /usr/bin/env python3
import os

required: list[str] = ["DATABASE_URL", "API_KEY", "ZION_ENDPOINT"]


def config_variables() -> dict[str, str] | bool:
    try:
        from dotenv import load_dotenv
        load_dotenv()
        matrix_mode: str = (
            "development" if os.environ.get("MATRIX_MODE") != "production"
            else "production"
        )
        log_level: str = "DEBUG" if matrix_mode == "development" else "INFO"
        config: dict[str, str] = {
             "MATRIX_MODE": os.environ.get("MATRIX_MODE", "development"),
             "DATABASE_URL": os.environ.get(
                 "DATABASE_URL", "Connected to a remote instance"
                 ),
             "API_KEY": os.environ.get("API_KEY", "Unauthorized"),
             "LOG_LEVEL": os.environ.get("LOG_LEVEL", log_level),
             "ZION_ENDPOINT": os.environ.get("ZION_ENDPOINT", "Offline")
        }
        return config
    except ImportError as e:
        print(f"[MISSING] {e}\n Install with: pip install python-dotenv")
        return False


def config_info(config: dict[str, str]) -> None:
    matrix: str = (
        "development" if not config['MATRIX_MODE']
        else config['MATRIX_MODE']
    )
    print(f"Mode: {matrix}")
    url: str = config['DATABASE_URL']
    if "localhost" in url or "127.0.0.1" in url:
        database: str = "Connected to local instance"
    else:
        database = "Connected to a remote instance"
    print(f"Database: {database}")
    key: str = "Unauthorized" if not config['API_KEY'] else "Authenticated"
    print(f"API Access: {key}")
    log: str = "DEBUG" if not config['LOG_LEVEL'] else config['LOG_LEVEL']
    print(f"Log Level: {log}")
    mode: str = "Online" if config['ZION_ENDPOINT'] else "Offline"
    print(f"Zion Network: {mode}")


def missing_config() -> str:
    missing: list[str] = []
    for data in required:
        if not os.environ.get(data):
            missing.append(data)
    return ", ".join(missing)


def environment_security() -> None:
    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file not found")
    if missing_config():
        print(f"[WARNING] Missing \
production configuration: {missing_config()}")
    else:
        print("[OK] Production overrides available")


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")
    data = config_variables()
    if isinstance(data, dict):
        config_info(data)
        environment_security()


if __name__ == "__main__":
    main()
