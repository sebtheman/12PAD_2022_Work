import sys
import time
import curses

# for i in range(10):
#     sys.stdout.flush()
#     print("\rTest: "+str(i+1)+"/"+str(10),end='')
#     time.sleep(0.2)
# print('\n')

def report_progress(filename, progress):
    """progress: 0-10"""
    stdscr.addstr(0, 0, "Moving file: {0}".format(filename))
    stdscr.addstr(1, 0, "Total progress: [{1:10}] {0}%".format(progress * 10, "#" * progress))
    stdscr.refresh()

if __name__ == "__main__":
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()

    try:
        for i in range(10):
            report_progress("file_{0}.txt".format(i), i+1)
            time.sleep(0.5)
        curses.echo()
        curses.nocbreak()
        inputFromUser = input('\nDo some more printing? Y/N: ')
        curses.noecho()
        curses.cbreak()
        if inputFromUser == 'Y':
            for i in range(10):
                report_progress("file_{0}.txt".format(i), i+1)
                time.sleep(0.5)
    finally:
        curses.echo()
        curses.nocbreak()
        curses.endwin()