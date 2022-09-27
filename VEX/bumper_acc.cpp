/*----------------------------------------------------------------------------*/
/*                                                                            */
/*    Module:       main.cpp                                                  */
/*    Author:       C:\Users\EDZ                                              */
/*    Created:      Sat Feb 19 2022                                           */
/*    Description:  V5 project                                                */
/*                                                                            */
/*----------------------------------------------------------------------------*/

// ---- START VEXCODE CONFIGURED DEVICES ----
// Robot Configuration:
// [Name]               [Type]        [Port(s)]
// right_Motor          motor         1               
// left_Motor           motor         2               
// BumperA              bumper        A               
// Motor20              motor         20              
// ---- END VEXCODE CONFIGURED DEVICES ----

#include "vex.h"


using namespace vex;

int main() {
  // Initializing Robot Configuration. DO NOT REMOVE!
  vexcodeInit();
  int speed=0;
  // int speed=50;
  // 开关A匀加速
  while(true){
    while(BumperA.pressing()==0){}
    while(BumperA.pressing()==1){}
    // wait(0.2, sec);
    while(BumperA.pressing()==0){
      // gradually_speed_add(speed);  
      // Motor20.spin(fwd,speed,pct);
      // while(speed<50){
      if (speed<=50){
        Motor20.spin(fwd, speed, pct);
        wait(0.2,sec);
        speed += 1;
      }
      else{
        Motor20.spin(fwd, 50, pct);
      }
    }
    while(BumperA.pressing()==1){
      // speed = 0;
      if (speed > 0){
        speed -= 1;
        Motor20.spin(fwd, speed, pct);
        wait(0.2, sec);
      }
      else{
        Motor20.stop();
      }
      // gradually_speed();
    }
  }

// 开关B匀减速

}
