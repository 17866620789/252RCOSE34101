@echo off
for /L %%i in (1,1,10) do (
    mkdir %%i
    for /L %%j in (1,1,9) do (
        mkdir %%i\%%i%%j
    )
)
echo done

pause
