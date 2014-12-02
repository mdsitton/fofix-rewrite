cd ..
del /S *.pyc
for /D /R %%X in (__pycache__*) do rd /S /Q "%%X"
