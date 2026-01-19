; Script Inno Setup pour Ajout_Bureau
; Préserve les fichiers JSON existants

#define MyAppName "Ajout Bureau - Agenda Terminator"
#define MyAppVersion "1.0.0"
#define MyAppPublisher "Agenda Terminator"
#define MyAppExeName "Ajout_Bureau.exe"
#define MyAppURL "https://example.com"

[Setup]
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={localappdata}\Agenda_Event
DefaultGroupName={#MyAppName}
OutputDir=.\Output_Setup
OutputBaseFilename=Setup_Ajout_Bureau
SetupIconFile="Agenda Bureau\Compilation\Annexes\Agenda.ico"
Compression=zip
SolidCompression=yes
LicenseFile=
InfoBeforeFile=
PrivilegesRequired=lowest
AllowUNCPath=no
CreateUninstallRegKey=yes

[Languages]
Name: "french"; MessagesFile: "compiler:Languages\French.isl"
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "Créer un raccourci sur le Bureau"; GroupDescription: "Raccourcis supplémentaires:"; Flags: checkedonce

[Files]
; Inclure le fichier EXE principal
Source: "dist\Ajout_Bureau.exe"; DestDir: "{localappdata}\Agenda_Event"; Flags: ignoreversion

; Inclure le fichier JSON s'il n'existe pas déjà
Source: "Agenda_Terminator_JSON.json"; DestDir: "{localappdata}\Agenda_Event"; Flags: onlyifdoesntexist

; Inclure les ressources (icône)
Source: "Agenda.png"; DestDir: "{localappdata}\Agenda_Event"; Flags: ignoreversion

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{localappdata}\Agenda_Event\{#MyAppExeName}"
Name: "{userdesktop}\{#MyAppName}"; Filename: "{localappdata}\Agenda_Event\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{localappdata}\Agenda_Event\{#MyAppExeName}"; Description: "Lancer {#MyAppName}"; Flags: nowait postinstall skipifsilent

[Code]
// Code pour afficher des messages d'information
procedure InitializeWizard;
begin
  MsgBox('Installation de ' + ExpandConstant('{#MyAppName}') + ' v' + ExpandConstant('{#MyAppVersion}') + #13#13 +
         'Attention: Les fichiers JSON existants seront préservés.', mbInformation, MB_OK);
end;

procedure CurUninstallStepChanged(CurUninstallStep: TUninstallStep);
begin
  if CurUninstallStep = usPostUninstall then
  begin
    MsgBox('Le fichier JSON "Agenda_Terminator_JSON.json" a été conservé dans:' + #13 + ExpandConstant('{localappdata}\Agenda_Event'), 
           mbInformation, MB_OK);
  end;
end;
