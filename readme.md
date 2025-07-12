# How to build

First, make sure that python and git is installed (https://www.python.org/ftp/python/3.13.3/python-3.13.3-amd64.exe, https://github.com/git-for-windows/git/releases/download/v2.49.0.windows.1/Git-2.49.0-64-bit.exe).

```
git clone https://github.com/ElizaLobanova/E_Diagram.git
cd E_Diagram
pip install pandas openpyxl matplotlib
```

# How to use

Just run `python E_diagram.py -h`and read. Example:
```
python E_diagram.py 2 example/energy_levels.xlsx e_diag.pdf
```