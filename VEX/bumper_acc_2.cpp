// 疑问： 为什么在while中的speed会比before的speed的速度慢半拍

#include "vex.h"


using namespace vex;

int main() {
  // Initializing Robot Configuration. DO NOT REMOVE!
  vexcodeInit();
  // while (BumperA.pressing()==0){}
  // Brain.Screen.print("Good job");
  int speed=0;
  while(1){
  Brain.Screen.newLine();
  Brain.Screen.print("before speed is %d",speed);
  // wait(3,sec);
  Motor20.spin(fwd, speed, pct);
  if (BumperA.pressing()==1){
    while (BumperA.pressing()==1)
    {
      Brain.Screen.newLine();
      Brain.Screen.print("in while speed is %d",speed,"\n");
    }
      speed += 20;
  if (speed > 100){
    speed = 100;
  }
  }
  Brain.Screen.setCursor(1, 1);
  Brain.Screen.print("after speed is %d",speed,"\n");
  }
}
