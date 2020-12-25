import setuptools

with open("README.md", "r") as readme:
    long_description = readme.read()

setuptools.setup(
    name="mcp",
    version="0.0.1",
    author="Euxcbsks",
    author_email="hawhaw02030746@gmail.com",
    description="mcp - My Colony Py",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Euxcbsks/mcp",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
