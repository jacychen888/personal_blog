### --help  
>列出简单的用法。

### -v
>命令行的每一个-v将增加反馈信息的级别。Level 0(缺省值)除启动提示、测试完成和最终结果之外，提供较少信息。Level 1提供较为详细的测试信息，如逐个发送到Activity的事件。Level 2提供更加详细的设置信息，如测试中被选中的或未被选中的Activity。

###-s <seed>
>伪随机数生成器的seed值。如果用相同的seed值再次运行Monkey，它将生成相同的事件序列。

###--throttle <milliseconds>
>在事件之间插入固定延迟。通过这个选项可以减缓Monkey的执行速度。如果不指定该选项，Monkey将不会被延迟，事件将尽可能快地被产成。

###--pct-touch <percent>
>调整触摸事件的百分比(触摸事件是一个down-up事件，它发生在屏幕上的某单一位置)。

###--pct-motion <percent>
>调整动作事件的百分比(动作事件由屏幕上某处的一个down事件、一系列的伪随机事件和一个up事件组成)。

###--pct-trackball <percent>
>调整轨迹事件的百分比(轨迹事件由一个或几个随机的移动组成，有时还伴随有点击)。

###--pct-nav <percent>
>调整“基本”导航事件的百分比(导航事件由来自方向输入设备的up/down/left/right组成)。

###--pct-majornav <percent>
>调整“主要”导航事件的百分比(这些导航事件通常引发图形界面中的动作，如：5-way键盘的中间按键、回退按键、菜单按键)

###--pct-syskeys <percent>
>调整“系统”按键事件的百分比(这些按键通常被保留，由系统使用，如Home、Back、Start Call、End Call及音量控制键)。

###--pct-appswitch <percent>
>调整启动Activity的百分比。在随机间隔里，Monkey将执行一个startActivity()调用，作为最大程度覆盖包中全部Activity的一种方法。

###--pct-anyevent <percent>
>调整其它类型事件的百分比。它包罗了所有其它类型的事件，如：按键、其它不常用的设备按钮、等等。


###-p <allowed-package-name>
>如果用此参数指定了一个或几个包，Monkey将只允许系统启动这些包里的Activity。如果你的应用程序还需要访问其它包里的Activity(如选择取一个联系人)，那些包也需要在此同时指定。如果不指定任何包，Monkey将允许系统启动全部包里的Activity。要指定多个包，需要使用多个 -p选项，每个-p选项只能用于一个包。

###-c <main-category>
>如果用此参数指定了一个或几个类别，Monkey将只允许系统启动被这些类别中的某个类别列出的Activity。如果不指定任何类别，Monkey将选 择下列类别中列出的Activity： Intent.CATEGORY_LAUNCHER或Intent.CATEGORY_MONKEY。要指定多个类别，需要使用多个-c选项，每个-c选 项只能用于一个类别。

###--dbg-no-events
>设置此选项，Monkey将执行初始启动，进入到一个测试Activity，然后不会再进一步生成事件。为了得到最佳结果，把它与-v、一个或几个包约 束、以及一个保持Monkey运行30秒或更长时间的非零值联合起来，从而提供一个环境，可以监视应用程序所调用的包之间的转换。

###--hprof
>设置此选项，将在Monkey事件序列之前和之后立即生成profiling报告。这将会在data/misc中生成大文件(~5Mb)，所以要小心使用它。

###--ignore-crashes
>通常，当应用程序崩溃或发生任何失控异常时，Monkey将停止运行。如果设置此选项，Monkey将继续向系统发送事件，直到计数完成。

###--ignore-timeouts
>通常，当应用程序发生任何超时错误(如“Application Not Responding”对话框)时，Monkey将停止运行。如果设置此选项，Monkey将继续向系统发送事件，直到计数完成。

###--ignore-security-exceptions
>通常，当应用程序发生许可错误(如启动一个需要某些许可的Activity)时，Monkey将停止运行。如果设置了此选项，Monkey将继续向系统发送事件，直到计数完成。

###--kill-process-after-error
>通常，当Monkey由于一个错误而停止时，出错的应用程序将继续处于运行状态。当设置了此选项时，将会通知系统停止发生错误的进程。注意，正常的(成功的)结束，并没有停止启动的进程，设备只是在结束事件之后，简单地保持在最后的状态。

###--monitor-native-crashes
>监视并报告Android系统中本地代码的崩溃事件。如果设置了--kill-process-after-error，系统将停止运行。

###--wait-dbg
>停止执行中的Monkey，直到有调试器和它相连接。