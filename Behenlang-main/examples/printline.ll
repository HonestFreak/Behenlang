; ModuleID = "module"
target triple = "x86_64-pc-windows-msvc"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...) 

define i32 @"main"() 
{
main_entry:
  %".2" = alloca [9 x i8]
  store [9 x i8] c"hello\0a%6\00", [9 x i8]* %".2"
  %".4" = getelementptr [9 x i8], [9 x i8]* %".2", i32 0, i32 0
  %".5" = call i32 (i8*, ...) @"printf"(i8* %".4")
  %".6" = alloca [20 x i8]
  store [20 x i8] c"this is new line\0a%6\00", [20 x i8]* %".6"
  %".8" = getelementptr [20 x i8], [20 x i8]* %".6", i32 0, i32 0
  %".9" = call i32 (i8*, ...) @"printf"(i8* %".8")
  %".10" = alloca [20 x i8]
  store [20 x i8] c"this is 3rd line\0a%6\00", [20 x i8]* %".10"
  %".12" = getelementptr [20 x i8], [20 x i8]* %".10", i32 0, i32 0
  %".13" = call i32 (i8*, ...) @"printf"(i8* %".12")
  ret i32 0
}
