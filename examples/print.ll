; ModuleID = "module"
target triple = "x86_64-pc-windows-msvc"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...) 

define i32 @"main"() 
{
main_entry:
  %".2" = alloca [17 x i8]
  store [17 x i8] c"Namste Duniya \0a\00\00", [17 x i8]* %".2"
  %".4" = getelementptr [17 x i8], [17 x i8]* %".2", i32 0, i32 0
  %".5" = call i32 (i8*, ...) @"printf"(i8* %".4")
  %".6" = alloca [12 x i8]
  store [12 x i8] c"Hello World\00", [12 x i8]* %".6"
  %".8" = getelementptr [12 x i8], [12 x i8]* %".6", i32 0, i32 0
  %".9" = call i32 (i8*, ...) @"printf"(i8* %".8")
  %".10" = alloca i32
  store i32 10, i32* %".10"
  %".12" = alloca float
  store float 0x4025000000000000, float* %".12"
  ret i32 0
}
