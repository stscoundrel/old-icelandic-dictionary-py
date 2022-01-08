import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="old-icelandic-dictionary",
    version="1.0.2",
    author="stscoundrel",
    description="Old Icelandic dictionary for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/stscoundrel/old-icelandic-dictionary-py",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9",
    package_data={"": ["**/*.json"]},
)
