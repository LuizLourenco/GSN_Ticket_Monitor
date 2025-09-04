
Neste exemplo:

/tn "IM-DAR-INC-EUSLATAM_PreClosure" define o nome da tarefa.
/tr "%windir%\system32\cmd.exe /c C:\Users\rpa01EUSLD\OneDrive - DPDHL\RobotEUS\IM_Data_Analytic_Report\PROD\EUSLATAM_PreClosure\run.cmd" especifica o comando a ser executado.
/sc daily define a frequência da tarefa como diária.
/st 10:05 define a hora de início da tarefa.
Você pode ajustar a frequência e o horário conforme necessário. Se precisar de mais alguma coisa, é só avisar!


``` bash

    schtasks /create /tn "IM-DAR-INC-EUSLATAM_PreClosure" /tr "%windir%\system32\cmd.exe /c C:\Users\'rpa01EUSLD\OneDrive - DPDHL'\RobotEUS\IM_Data_Analytic_Report\PROD\EUSLATAM_PreClosure\run.cmd" /sc daily /st 10:05
```