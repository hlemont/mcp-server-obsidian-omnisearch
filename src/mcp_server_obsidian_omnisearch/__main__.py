import os
from .server import serve


def main():
    import sys
    import asyncio

    if len(sys.argv) < 2:
        print("Usage: python server.py <obsidian_vault_path>")
        sys.exit(1)

    obsidian_vault_path = sys.argv[1]
    host = os.environ.get("OBSIDIAN_HOST", "localhost")
    port = os.environ.get("OBSIDIAN_PORT", "51361")

    base_path = os.environ.get("BASE_PATH", None)
    
    asyncio.run(serve(host, port, base_path=base_path))


if __name__ == "__main__":
    main()
