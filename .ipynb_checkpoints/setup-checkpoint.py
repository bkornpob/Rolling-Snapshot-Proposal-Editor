import setuptools

setuptools.setup(
    name="rolling_snapshot_proposal_editor",
    version="1.2.0",
    author="Kornpob Bhirombhakdi",
    author_email="kbhirombhakdi@stsci.edu",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/bkornpob/Rolling-Snapshot-Proposal-Editor.git",
    package_data={'': ['./template/*','./demo/*']},
    include_package_data=True,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3"
        ,"License :: OSI Approved :: MIT License"
        ,"Operating System :: OS Independent"
    ],
    python_requires='>=3.'
)
