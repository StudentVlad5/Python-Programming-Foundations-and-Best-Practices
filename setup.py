from setuptools import setup, find_packages

setup(
    name="main_project",
    version="0.1",
    packages=find_packages(),  # Автоматично знаходить усі пакети
    install_requires=[
        # Твої залежності, або просто залиш requirements.txt
    ],
    entry_points={
        "console_scripts": [
            "main-project=main_project.main:main",  # команда => функція
        ]
    },
    include_package_data=True,
)