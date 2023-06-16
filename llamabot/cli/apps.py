"""Run llamabot codebot panel apps."""
import os

import typer

from llamabot.bot_library import coding

app = typer.Typer()


@app.command()
def codebot(port: int = 5050, address: str = "0.0.0.0"):
    """Run the codebot app.

    :param port: Port to run the app on.
    :param address: Address to run the app on.
    """

    codebot_app = coding.create_panel_app()
    os.environ["BOKEH_ALLOW_WS_ORIGIN"] = f"{address}:{port}"
    codebot_app.show(title="Codebot", port=port, address=address)


if __name__ == "__main__":
    app()
