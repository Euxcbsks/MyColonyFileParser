# mcp - My Colony Python
主要功能是整理My Colony的遊戲資料，並提供使用
目前尚不支援My Colony 2

* [初次使用與config()](#%E5%88%9D%E6%AC%A1%E4%BD%BF%E7%94%A8%E8%88%87config)
  * [1.使用package](#1%E4%BD%BF%E7%94%A8package)
  * [2.不帶參數的config()](#2%E4%B8%8D%E5%B8%B6%E5%8F%83%E6%95%B8%E7%9A%84config)
  * [3.一次調整多項設定](#3%E4%B8%80%E6%AC%A1%E8%AA%BF%E6%95%B4%E5%A4%9A%E9%A0%85%E8%A8%AD%E5%AE%9A)

## 初次使用與config()
### 1.使用package

package預設會執行check_update並有提示訊息
```py
import mcp
#mcp check_update process
#        Checking update...
#        Local game files have been updated to latest version(v1.10.0)
```

可使用config功能關閉check_update機制
(若原設定值與新設定值相同，則不會有任何變動)
```py
import mcp

mcp.config(check_update = False) #將check_update功能關閉
#Success update config file
#        "check_update": True >>> False
```


### 2.不帶參數的config()
不帶參數的config()會返回設定列表與其目前的設定值

***不會自動print!***
```py
import mcp

print(mcp.config())
#{
#        "check_update": true,
#        "show_update_message": true,
#        "timeout": 1
#}
```
*config檔使用json格式


### 3.一次調整多項設定
config()支援一次調整多項設定
```py
import mcp

mcp.config(check_update = False, show_update_message = False, timeout = 1)
#Success update config file
#        "check_update": True >>> False
```
