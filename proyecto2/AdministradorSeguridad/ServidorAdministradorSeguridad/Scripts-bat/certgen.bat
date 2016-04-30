@ECHO off
set arg1=%1
cd C:\Certitemp
certreq -submit -config MascotSens-CA.mascotsens.co\MASCOTSENS-CA %arg1%.csr %arg1%.crt %arg1%.p7b