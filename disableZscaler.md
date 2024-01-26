[Ref](https://www.reddit.com/r/techsupport/comments/xm2jng/comment/ivflauk/)

#Command use for disable Zscaler 
```
Get-NetAdapterBinding -AllBindings | where ComponentID -Like 'ZS*' | Disable-NetAdapterBinding
```
