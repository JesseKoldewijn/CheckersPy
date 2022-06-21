import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
        name="CheckersPy",
        options={
            "build_exe": {"packages":["pygame"]},
            "build_dmg": {"packages":["pygame"]},
            "build_msi": {"packages":["pygame"]}},
        executables = executables
    )