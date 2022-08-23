; ModuleID = "module"
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
  %".8" = load i32, i32* %".6"
  %".9" = icmp eq i32 %".8", 0
  br i1 %".9", label %"oddeven_entry.if", label %"oddeven_entry.else"
oddeven_entry.if:
  %".11" = alloca [5 x i8]
  store [5 x i8] c"Even\00", [5 x i8]* %".11"
  %".13" = getelementptr [5 x i8], [5 x i8]* %".11", i32 0, i32 0
  %".14" = call i32 (i8*, ...) @"printf"(i8* %".13")
  br label %"oddeven_entry.endif"
oddeven_entry.else:
  %".16" = alloca [6 x i8]
  store [6 x i8] c"Odd\0a\00\00", [6 x i8]* %".16"
  %".18" = getelementptr [6 x i8], [6 x i8]* %".16", i32 0, i32 0
  %".19" = call i32 (i8*, ...) @"printf"(i8* %".18")
  br label %"oddeven_entry.endif"
oddeven_entry.endif:
  ret i32 0
}

define i32 @"main"() 
{
main_entry:
  %".2" = alloca [24 x i8]
  store [24 x i8] c"Testing odd and even\0a%6\00", [24 x i8]* %".2"
  %".4" = getelementptr [24 x i8], [24 x i8]* %".2", i32 0, i32 0
  %".5" = call i32 (i8*, ...) @"printf"(i8* %".4")
  %".6" = call i32 @"oddeven"()
  ret i32 0
}
