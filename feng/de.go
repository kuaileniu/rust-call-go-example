package feng

import "fmt"
// 若import github.com/xxx/xx 等非标准库，cargo run 后编译 静态文件问题


func MainLog(){
	fmt.Println("------3--feng---------main.log--引用本项目依赖中的输出")
}