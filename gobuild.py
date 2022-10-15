# !/usr/bin/env python3
import os

command = 'go build -o /Volumes/HD/src/rust-learn/rust-call-go-example/target/debug/build/rust-go-example-8b62a236fbe1d0bb/out/libawesome.a -buildmode=c-archive awesome.go'
tt = os.popen(command)
print(tt)
print(type(tt))