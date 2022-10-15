# !/usr/bin/env python3
import os

command = 'go build -o /Volumes/HD/src/rust-learn/rust-call-go-example/target/debug/build/rust-go-example-8b62a236fbe1d0bb/out/libawesome.a -buildmode=c-archive awesome.go'  # 此行为混合编译后可正确执行行
# command = 'GOARCH=AMD64 GOOS=darwin go build -o /Volumes/HD/src/rust-learn/rust-call-go-example/target/debug/build/rust-go-example-8b62a236fbe1d0bb/out/libawesome.a -buildmode=c-archive awesome.go'
# command = 'GOARCH=AMD64 GOOS=linux go build -o /Volumes/HD/src/rust-learn/rust-call-go-example/target/debug/build/rust-go-example-8b62a236fbe1d0bb/out/libawesome.a -buildmode=c-archive awesome.go'
# command = 'GOARCH=AMD64 GOOS=linux go build -t -o /Volumes/HD/src/rust-learn/rust-call-go-example/target/debug/build/rust-go-example-8b62a236fbe1d0bb/out/libawesome.a -buildmode=c-archive awesome.go'
# command = 'CGO_ENABLED=0 CC="GCC-12" go build -gcflags=-m  -ldflags "-w -s" -o /Volumes/HD/src/rust-learn/rust-call-go-example/target/debug/build/rust-go-example-8b62a236fbe1d0bb/out/libawesome.a -buildmode=c-archive awesome.go'

tt = os.popen(command)
print(tt)
print(type(tt))