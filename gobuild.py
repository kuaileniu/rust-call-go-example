# bin python3
# python3 gobuild.py

import os
import argparse

parser = argparse.ArgumentParser(description="of argparse")
parser.add_argument('-n','--name', default='lib.a')
parser.add_argument('-p','--path',default="./")
args = parser.parse_args()
# print(args)
name = args.name
path = args.path
print('build info {}  {}'.format(name,path))


# command = 'go build -o /Volumes/HD/src/rust-learn/rust-call-go-example/target/debug/build/rust-go-example-8b62a236fbe1d0bb/out/libawesome.a -buildmode=c-archive awesome.go'  # 此行为混合编译后可正确执行行
command = 'go build -o {}/{} -buildmode=c-archive awesome.go'.format(path,name)  # 此行为混合编译后可正确执行行
# command = 'GOARCH=AMD64 GOOS=darwin go build -o /Volumes/HD/src/rust-learn/rust-call-go-example/target/debug/build/rust-go-example-8b62a236fbe1d0bb/out/libawesome.a -buildmode=c-archive awesome.go'
# command = 'GOARCH=AMD64 GOOS=linux go build -o /Volumes/HD/src/rust-learn/rust-call-go-example/target/debug/build/rust-go-example-8b62a236fbe1d0bb/out/libawesome.a -buildmode=c-archive awesome.go'
# command = 'GOARCH=AMD64 GOOS=linux go build -t -o /Volumes/HD/src/rust-learn/rust-call-go-example/target/debug/build/rust-go-example-8b62a236fbe1d0bb/out/libawesome.a -buildmode=c-archive awesome.go'
# command = 'CGO_ENABLED=0 CC="GCC-12" go build -gcflags=-m  -ldflags "-w -s" -o /Volumes/HD/src/rust-learn/rust-call-go-example/target/debug/build/rust-go-example-8b62a236fbe1d0bb/out/libawesome.a -buildmode=c-archive awesome.go'

os.popen(command)
