import setuptools

setuptools.setup(
    name="trello-capture",
    version="0.0.1",
    author="Patrick Winter",
    author_email="patrickwinter@posteo.ch",
    description="Capture trello cards through dmenu",
    install_requires=[
        "requests",
        "pydantic",
        "typer",
        "sh",
    ],
    python_requires=">=3.6",
    py_modules=["trello_capture"],
    entry_points={"console_scripts": ["tc=trello_capture:main"]},
)
