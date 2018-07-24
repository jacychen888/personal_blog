##导入模块 
    from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage 

##连接当前设备,并返回一个MonkeyDevice对象 
	device = MonkeyRunner.waitForConnection() 
	if not device: 
		print "Please connect a device to start!" 
	else: 
		print "Start " 
    
##安装Android包，此方法返回的返回值为boolean，由此可以判断安装过程是否正常  
    device.installPackage('myproject/bin/MyApplication.apk') 
    device.removePackage ('com.example.android.notepad') 
    print ('卸载成功') 
    device.installPackage('ApiDemos.apk') 
    print ('安装成功') 

##启动一个Activity; 
    device.startActivity (component='com.android.htccontacts/com.android.htccontacts.ContactsTabActivity')

##截图; 
    result = device.takeSnapshot() 
    result.writeToFile('C:\\Users\\Martin\\Desktop\\test.png','png') 

##时延(秒); 
    MonkeyRunner.sleep(3) 

##滑动屏幕; 
    for i in range(1,70): 
**例如**：

    device.drag((180,180),(600,600),0.1,10) 
     //开始，结束，持续时间，步骤   

    for i in range(1,100): 
       device.drag((180,180),(600,600),0.1,10) 
    MonkeyRunner.sleep(1) 

##触击屏幕; 
    device.touch(408,66,"DOWN_AND_UP") 

##执行adb shell命令; 
    device.shell("input text goup01") 
	
    #按下HOME键  
	device.press('KEYCODE_HOME','DOWN_AND_UP') 

    #按下BACK键   
	device.press('KEYCODE_BACK','DOWN_AND_UP') 

    #按下下导航键 
	device.press('KEYCODE_DPAD_DOWN','DOWN_AND_UP') 

    #按下上导航键 
	device.press('KEYCODE_DPAD_UP','DOWN_AND_UP') 

    #按下OK键
	device.press('KEYCODE_DPAD_CENTER','DOWN_AND_UP') 
         

##备注查询

相应的按键对应的名称如下：

|按键名|对应code|
|:--:|:--:|
|home|KEYCODE_HOME|
|back|KEYCODE_BACK|
|send|KEYCODE_CALL|
|end|KEYCODE_ENDCALL|
|上导航|KEYCODE_DPAD_UP|
|下导航|KEYCODE_DPAD_DOWN|
|左导航|KEYCODE_DPAD_LEFT|
|右导航|KEYCODE_DPAD_RIGHT|
|ok|KEYCODE_DPAD_CENTER|
|上音量|KEYCODE_VOLUME_UP|
|下音量|KEYCODE_VOLUME_DOWN|
|power|KEYCODE_POWER|
|camera|KEYCODE_CAMERA|
|menu|KEYCODE_MENU|

*** reference ***:   [google-Monkey](https://developer.android.google.cn/studio/test/monkeyrunner/)