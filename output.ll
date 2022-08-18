; ModuleID = "main"
target triple = "x86_64-pc-windows-msvc"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...) 

define i32 @"hello"() 
{
hello_entry:
  %".2" = alloca float
  store float 0x40321999a0000000, float* %".2"
  %".4" = load float, float* %".2"
  %".5" = fcmp oeq float %".4", 0x40321999a0000000
  br i1 %".5", label %"hello_entry.if", label %"hello_entry.else"
hello_entry.if:
  %".7" = alloca [17 x i8]
  store [17 x i8] c"wow you are 18\0a\00\00", [17 x i8]* %".7"
  %".9" = getelementptr [17 x i8], [17 x i8]* %".7", i32 0, i32 0
  %".10" = call i32 (i8*, ...) @"printf"(i8* %".9")
  br label %"hello_entry.endif"
hello_entry.else:
  %".12" = alloca [25 x i8]
  store [25 x i8] c"i guess you are not 18\0a\00\00", [25 x i8]* %".12"
  %".14" = getelementptr [25 x i8], [25 x i8]* %".12", i32 0, i32 0
  %".15" = call i32 (i8*, ...) @"printf"(i8* %".14")
  br label %"hello_entry.endif"
hello_entry.endif:
  ret i32 3
}

define i32 @"main"() 
{
main_entry:
  %".2" = alloca [5 x i8]
  store [5 x i8] c"hi\0a\00\00", [5 x i8]* %".2"
  %".4" = getelementptr [5 x i8], [5 x i8]* %".2", i32 0, i32 0
  %".5" = call i32 (i8*, ...) @"printf"(i8* %".4")
  %".6" = call i32 @"hello"()
  ret i32 0
}
