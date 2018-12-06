from setuptools import setup

setup(
    name="verbify_service_websockets",
    version="0.1",
    packages=[
        "verbify_service_websockets"
    ],
    install_requires=[
        "gevent",
        "gevent-websocket",
        "haigha",
        "baseplate",
        "manhole",
    ],
)
