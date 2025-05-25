# Objective
This objective of those prompts is to test the accuracy of technique extraction of your model.
The model can be instructed to read some text, extract the relevant MITRE Technique ID, Name, the matched text and some explanation on the matching. 


# Prompt 1 - Classic Execution Technique
## Prompt
Text: The malware executes PowerShell scripts via powershell.exe -enc and uses scheduled tasks to persist after reboot.
## Expected Answer
Technique ID: T1059.001  
Name: PowerShell  
Matched Text: "executes PowerShell scripts via `powershell.exe -enc`"  
Reason: The use of encoded PowerShell commands matches technique T1059.001.

Technique ID: T1053.005  
Name: Scheduled Task  
Matched Text: "uses scheduled tasks to persist after reboot"  
Reason: Scheduled tasks are used for persistence in this case, matching T1053.005.

# Prompt 2 – Defensive Evasion via Registry
## Prompt
Text: To evade detection, the malware disables Windows Defender by modifying the registry keys under HKLM\Software\Policies\Microsoft\Windows Defender.

## Expected Answer 1
Technique ID: T1562.001  
Name: Disable or Modify Tools  
Matched Text: "disables Windows Defender by modifying the registry keys"  
Reason: The malware disables a security tool (Windows Defender) through registry modification, which aligns with the behavior described in the MITRE ATT&CK technique T1562.001 (Disable or Modify Tools).

## Expected Answer 2
Technique ID: T1112  
Name: Modify Registry  
Matched Text: "modifying the registry keys under `HKLM\Software\Policies\Microsoft\Windows Defender`"  
Reason: Editing registry keys to change system behavior matches T1112.

# Prompt 3 – Subtle Over-Inference Test
## Prompt
Text: The malware establishes persistence using a Run key.

## Expected Answer
Technique ID: T1547.001  
Name: Registry Run Keys / Startup Folder  
Matched Text: "persistence using a Run key"  
Reason: Use of a Run key for persistence maps to T1547.001.

# Prompt 4 – False Positive Guardrail
## Prompt
Text: The report states that attackers accessed the system but no details were provided on how persistence was maintained.

# Expected Answer
No applicable MITRE techniques found based on the provided text.
