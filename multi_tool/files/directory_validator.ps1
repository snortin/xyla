Add-Type -AssemblyName PresentationFramework

[System.Windows.MessageBox]::Show("directory finder", "ratio", "OK", "Question")

$directory = Read-Host -Prompt "Directory you would like to check"

$valid = Test-Path -Path $directory 

if ($directory)
{
	Write-Output "$directory is $valid "
}