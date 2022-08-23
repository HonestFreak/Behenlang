; ModuleID = "module"
target triple = "x86_64-pc-windows-msvc"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...) 

define i32 @"main"() 
{
main_entry:
  %".2" = alloca i32
  store i32 0, i32* %".2"
  %".4" = load i32, i32* %".2"
  %".5" = icmp slt i32 %".4", 10
  br i1 %".5", label %"while_loop_entry1", label %"while_loop_otherwise1"
while_loop_entry1:
  %".7" = alloca [7 x i8]
  store [7 x i8] c"Hello \00", [7 x i8]* %".7"
  %".9" = getelementptr [7 x i8], [7 x i8]* %".7", i32 0, i32 0
  %".10" = call i32 (i8*, ...) @"printf"(i8* %".9")
  %".11" = load i32, i32* %".2"
  %".12" = add i32 %".11", 2
  store i32 %".12", i32* %".2"
  %".14" = load i32, i32* %".2"
  %".15" = icmp slt i32 %".14", 10
  br i1 %".15", label %"while_loop_entry1", label %"while_loop_otherwise1"
while_loop_otherwise1:
  %".17" = load i32, i32* %".2"
  ret i32 %".17"
}
