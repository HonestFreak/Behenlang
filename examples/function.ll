; ModuleID = "module"
target triple = "x86_64-pc-windows-msvc"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...) 

define i32 @"hello"() 
{
hello_entry:
  %".2" = alloca [24 x i8]
  store [24 x i8] c"Ye hai hello function\0a\00\00", [24 x i8]* %".2"
  %".4" = getelementptr [24 x i8], [24 x i8]* %".2", i32 0, i32 0
  %".5" = call i32 (i8*, ...) @"printf"(i8* %".4")
  ret i32 0
}

define i32 @"main"() 
{
main_entry:
  %".2" = call i32 @"hello"()
  %".3" = alloca [16 x i8]
  store [16 x i8] c"Ye hai main fun\00", [16 x i8]* %".3"
  %".5" = getelementptr [16 x i8], [16 x i8]* %".3", i32 0, i32 0
  %".6" = call i32 (i8*, ...) @"printf"(i8* %".5")
  ret i32 0
}
