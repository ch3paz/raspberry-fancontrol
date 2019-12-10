#!/usr/bin/env python

import json


def check_condition(data_json):
    # print(data_json)
    data_dict = json.loads(data_json)

    print(data_dict)

    # return data_json


    """
/* Check conditions for running fans. */
void check_fan(double haIn, double haOut, double rhIn,
               double tempIn, double tempOut){
  if (
      ((haIn-haOut) >= values.min_ha_diff) &&
      (rhIn > values.min_rh) &&
      (tempIn > values.min_temp) &&
      (tempIn >= (tempOut - values.deltaTD))
     ){
      /* Don't ignore the delta$-values :-P */
      switch (firstCycleFlag){
        case 1  :  PORTB &= ~(1<<PB3);
                   fan.running = 1;
                   firstCycleFlag = FALSE;
                   break;
        case 0  :  if (
                        (tempIn > (values.min_temp+values.deltaT)) &&
                        (rhIn > (values.min_rh+values.deltaRH))
                      ){
                        PORTB &= ~(1<<PB3);
                        fan.running = 1;
                       }
                   break;
      }
  }
  else{
    PORTB |= (1<<PB3);
    fan.running = 0;
  }
}
    """
