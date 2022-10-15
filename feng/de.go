package feng

import "fmt"
// 若import github.com/xxx/xx 等非标准库，cargo run 后编译 静态文件问题
// 可考虑通过build.rs调用外部python脚本进行打包

func MainLog(){
	fmt.Println("------4--feng---------main.log--引用本项目依赖中的输出")
}