#ifdef DEBUG
#define dbgprint(x) cerr<<#x<<":"<<x<<endl;
#define dbgmsg(message) cerr<<message<<endl;
#else
#define dbgprint(x)
#define dbgmsg(message)
#endif