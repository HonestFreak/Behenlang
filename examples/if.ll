; ModuleID = "main"
target triple = "x86_64-pc-windows-msvc"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...) 

define i32 @"oddeven"() 
{
oddeven_entry:
  %".2" = alloca i32
  store i32 18, i32* %".2"
  %".4" = load i32, i32* %".2"
  %".5" = srem i32 %".4", 2
  %".6" = alloca i32
  store i32 %".5", i32* %".6"
  ret i32 0
}

define i32 @"main"() 
{
main_entry:
  %".2" = alloca [23 x i8]
  store [23 x i8] c"Testing odd and even\0a\00\00", [23 x i8]* %".2"
  %".4" = getelementptr [23 x i8], [23 x i8]* %".2", i32 0, i32 0
  %".5" = call i32 (i8*, ...) @"printf"(i8* %".4")
  %".6" = call i32 @"oddeven"()
  ret i32 0
}
