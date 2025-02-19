"""Utilities for working with Mermaid graphs in Jupyter notebooks.

Credit: https://gist.github.com/MLKrisJohnson/2d2df47879ee6afd3be9d6788241fe99

This module provides functions for working with Mermaid graphs in Jupyter notebooks. The functions allow you to:

- Display a Mermaid graph in a Jupyter notebook cell.
- Generate a URL that will display the graph in a web browser.
- Save the graph as a PNG file.
- Load a graph from a file and display it in a Jupyter notebook cell.

"""

import base64
from typing import Annotated
import requests, os
from IPython.core.display_functions import DisplayHandle
from IPython.display import Image, display

from src.utils.logger import getLogger

log = getLogger(__name__)

MermaidGraph = Annotated[str, bytes, "A string containing a Mermaid-format graph"]
Bytes = Annotated[bytes, "A bytes object"]
Path = Annotated[str, bytes, "A path to a file"]


def mm_ink(graphbytes: Bytes) -> str:
    """Given a bytes object holding a Mermaid-format graph, return a
    URL that will generate the image.

    :param graphbytes: (bytes): The Mermaid-format graph
    :return: (str): The URL for displaying the graph
    """
    base64_bytes = base64.b64encode(graphbytes)
    base64_string = base64_bytes.decode("ascii")
    url_link = "https://mermaid.ink/img/" + base64_string
    return url_link


def mm_display(graphbytes: Bytes) -> DisplayHandle:
    """Given a bytes object holding a Mermaid-format graph, display it.

    :param graphbytes: (bytes): The Mermaid-format graph
    :return: (DisplayHandle): The display handle for the graph
    """
    return display(Image(url=mm_ink(graphbytes)))


def mm(graph: MermaidGraph) -> DisplayHandle:
    """Given a string containing a Mermaid-format graph, display it.

    :param graph: (str): The Mermaid-format graph
    :return: (DisplayHandle): The display handle for the graph
    """
    graphbytes: bytes = graph.encode("ascii")
    return mm_display(graphbytes)


def mm_link(graph: Bytes) -> MermaidGraph:
    """Given a string containing a Mermaid-format graph, return URL for display.

    :param graph: (str): The Mermaid-format graph
    :return: (str): The URL for displaying the graph
    """
    if isinstance(graph, str):
        graphbytes = graph.encode("ascii")
    else:
        graphbytes = graph
    return mm_ink(graphbytes)


def display_image_from_file(path: str) -> DisplayHandle:
    """Given a path to a file containing a Mermaid-format graph, display
    the graph in a Jupyter notebook cell or IPython display.

    :param path: (str): The path to the file containing the Mermaid graph
    :return: (DisplayHandle): The display handle for the graph
    """
    with open(path, "rb") as f:
        graphbytes = f.read()
    return display(Image(graphbytes))


def mm_save_as_png(
        graph: MermaidGraph,
        output_file_path: str,
        mode: str = "w",
) -> Path:
    """
    Save a Mermaid graph as a PNG file
    :param graph: (MermaidGraph): The Mermaid graph
    :param output_file_path: (str): The path to save the PNG file
    :param mode: (str): The mode to open the file; default is "w" for write/overwrite and "a" for append/create new
    :return: (Path): The path to the saved PNG file
    """
    # Generate the Mermaid graph and get the DisplayHandle
    graph_bytes = graph.encode("ascii")
    url = mm_ink(graph_bytes)

    # Fetch the image from the URL
    response = requests.get(
        url=url,
        stream=True,
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Accept": "image/webp,image/apng,image/*,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Connection": "keep-alive",
            "Host": "mermaid.ink",
        },
    )
    assert (
            response.status_code == 200
    ), f"Failed to fetch image: {response.status_code}"  # Ensure we get a good response
    # response.raise_for_status()  # Ensure we notice bad responses
    log.debug(f"Response status code: {response.status_code}")

    # Ensure the output path is a PNG file
    image_filename = output_file_path.split("/")[-1].split(".")[0]
    output_dir = "/".join(output_file_path.split("/")[0:-1])
    output_file_path = os.path.abspath(output_dir + "/" + image_filename + ".png")
    log.debug(f"Output file path: \n{output_file_path}")

    # check if path exists and throw error if it does
    if not os.path.exists(output_dir):
        raise FileExistsError(f"Path does not exist: {output_dir}")

    # check for mode and create a new file if it does not exist
    if mode == "a":
        # check if file exists and create a new file if it does
        output_file_path = create_file_if_exists(output_file_path)
    elif mode == "w":
        pass
    else:
        raise ValueError(f"Invalid mode: {mode}")

    # Save the image as a PNG file
    with open(output_file_path, "wb") as f:
        f.write(response.content)
        f.close()
    return output_file_path


def create_file_if_exists(path: str, **kwargs) -> str:
    """
    Create a new file if the file already exists
    :param path: (str): The path to the file
    :param kwargs: (dict): Additional keyword arguments
    :return: (str): The path to the new file
    """
    import os

    index = kwargs.get("index", 1)

    try:
        path = os.path.abspath(path)
        if os.path.exists(path):
            raise FileExistsError(f"File already exists: {path}")
    except FileExistsError as e:
        if path.__contains__("_"):
            __prefix = "".join(path.split("_")[:-1])
            __suffix = path.split(".")[0].split("_")[-1]
            if __suffix.isdigit():
                path = __prefix + f"_{int(__suffix) + 1}.png"
            else:
                path = __prefix + f"_1.png"
            return create_file_if_exists(path, index=index + 1)
        else:
            __prefix = ".".join(path.split(".")[:-1])
            __suffix = path.split(".")[-1]
            path = __prefix + f"_{index}.png"
            return create_file_if_exists(path, index=index + 1)
    return path


def mm_encode(graph: MermaidGraph) -> Bytes:
    """Given a string containing a Mermaid-format graph, return bytes.

    :return: (Bytes): A bytes object holding the Mermaid-format graph.
    """
    return graph.encode("ascii")


def mm_decode(graphbytes: Bytes) -> MermaidGraph:
    """Given a bytes object holding a Mermaid-format graph, return the string.

    :return: (MermaidGraph): A string containing the Mermaid-format graph.
    """
    base64_bytes = base64.b64decode(graphbytes)
    return base64_bytes.decode("ascii")

