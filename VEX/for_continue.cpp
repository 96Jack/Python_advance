// continue跳出本次循环；
// result : 01234678910

#include "vex.h"


using namespace vex;

int main() {
  // Initializing Robot Configuration. DO NOT REMOVE!
  vexcodeInit();
  // while (BumperA.pressing()==0){}
  // Brain.Screen.print("Good job");
  int a;
  for (a=0; a<=10;)
  {
    if (a==5){
      a += 1;
      continue;
    }
    Brain.Screen.print(a);
    a += 1;
  }

}
