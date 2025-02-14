'''
Docstring
'''

from random import randint
from time import time
import pygame
from algs import algorithmsDict
import display

# Declared in display.py
# 1. global variables : numBars, delay, do_sorting, paused, timer_space_bar
# 2. widgets : sizeBox, delayBox, algorithmBox, playButton, stopButton


def main():
    '''
    main doc string
    '''
    numbers = []
    running = True
    display.algorithmBox.add_options(list(algorithmsDict.keys()))

    currentAlg = None
    algIterator = None

    timerDelay = time()

    while running:
        if not display.graphBox.isActive:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type ==pygame.KEYDOWN and event.key == pygame.K_SPACE and display.do_sorting:
                    display.paused = not display.paused
                    display.timer_space_bar = time()

                display.updateWidgets(event)

            display.delay = (display.delayBox.value-display.delayBox.rect.x-6)/1000 # delay is in ms

            if display.playButton.isActive: # play button clicked
                display.playButton.isActive = False
                display.do_sorting = True
                currentAlg = display.algorithmBox.get_active_option()
                display.numBars = int(display.sizeBox.text)
                numbers = [randint(10, 400) for i in range(display.numBars)] # random list to be sorted
                # initialize iterator
                algIterator = algorithmsDict[currentAlg](numbers, 0, display.numBars-1)

            if display.stopButton.isActive: # stop button clicked
                display.stopButton.isActive = False
                display.do_sorting = False
                display.paused = False
                try: # deplete generator to display sorted numbers
                    while True:
                        numbers, redBar1, redBar2, blueBar1, blueBar2 = next(algIterator)
                except StopIteration:
                    pass

            if display.do_sorting and not display.paused: # sorting animation
                try:
                    if time()-timerDelay >= display.delay:
                        numbers, redBar1, redBar2, blueBar1, blueBar2 = next(algIterator)
                        display.drawInterface(numbers, redBar1, redBar2, blueBar1, blueBar2)
                        timerDelay = time()
                except StopIteration:
                    display.do_sorting = False
            elif display.do_sorting and display.paused: # animation paused
                display.drawInterface(numbers, -1, -1, -1, -1)
            else: # no animation
                aSet = set(range(display.numBars))
                display.drawInterface(numbers, -1, -1, -1, -1, greenRows=aSet)
        else:
            #graph.run_graph()
            #subprocess.call("graph.py", shell=True)
            display.run_graph()
            display.graphBox.setFalse()
        
if __name__ == '__main__':
    main()
