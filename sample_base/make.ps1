If($Args[0] -eq "init"){
     Write-Host "git clone" 
     #git clone http://fw.git
}ElseIf($Args[0] -eq "update"){
     Write-Host "git update"
     rm -r -fo test
     #git clone http://fw.git
}Else{
     Write-Host "disable args"
}
