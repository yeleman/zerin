Name "Gestion pour les vendeurs de zerin"

!define MUI_PRODUCT "ZERIN"
!define MUI_FILE "zmain"
OutFile "Install-${MUI_FILE}.exe"

; default destination dir
InstallDir "C:\${MUI_PRODUCT}"

; request application privilege
; user should be ok. one can still right-click to install as admin
RequestExecutionLevel user

Page directory
Page instfiles

Section ""
  ; destination folder
  SetOutPath $INSTDIR
  
  ; List of files/folders to copy
  File /r dist\*.*
  File /r *.dll
  File /r *.manifest
  File /r templates
  File /r static

  ; start menu entry
  CreateDirectory "$SMPROGRAMS\${MUI_PRODUCT}"
  CreateShortCut "$SMPROGRAMS\${MUI_PRODUCT}\${MUI_FILE}.lnk" "$INSTDIR\${MUI_FILE}.exe" "" "$INSTDIR\${MUI_FILE}.exe" 0
  createShortCut "$SMPROGRAMS\${MUI_PRODUCT}\Uninstall ${MUI_FILE}.lnk" "$INSTDIR\uninstaller.exe"

  ; uninstaller
  writeUninstaller $INSTDIR\uninstaller.exe

SectionEnd

Section "Uninstall"
 
# Always delete uninstaller first
delete $INSTDIR\uninstaller.exe

RMDir /r $SMPROGRAMS\${MUI_PRODUCT}
 
# now delete installed file
delete $INSTDIR\*.exe
delete $INSTDIR\*.dll
delete $INSTDIR\*.manifest
delete $INSTDIR\*.exe
delete $INSTDIR\*.lib
delete $INSTDIR\*.zip
delete $INSTDIR\*.js
delete $INSTDIR\bootstrap
delete $INSTDIR\css
delete $INSTDIR\images
delete $INSTDIR\js
delete $INSTDIR\tcl
delete $INSTDIR\build
RMDir /r $INSTDIR\templates
RMDir /r $INSTDIR\static
 
SectionEnd
