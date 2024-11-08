from cx_Freeze import Executable, setup

exe_options = {
    "includes": ["sample"],
    "include_path": "src/"
}

setup(name="cxtempl",
      version = "0.0.1",
      install_requires = [
          "wxPython>=4.2.2"
      ],
      options = {
          "build_exe": exe_options
      },
      executables = [
          Executable("src/main.py", base="gui")
      ]
)
