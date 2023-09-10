FROM jupyter/base-notebook:notebook-7.0.2
RUN pip install nbdev
RUN pip install pre-commit
RUN pre-commit install
RUN nbdev_install_quarto