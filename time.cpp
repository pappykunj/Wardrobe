/* localtime example */
#include <iostream>     /* puts, printf */
#include <time.h>       /* time_t, struct tm, time, localtime */

using namespace std;
int main ()
{
  time_t rawtime;
  struct tm * timeinfo;

  time (&rawtime);
  timeinfo = localtime (&rawtime);
  cout << asctime(timeinfo);

  return 0;
}