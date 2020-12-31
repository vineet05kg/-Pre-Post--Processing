##############################################################################################################
#                             BAR-GRAPH FOR THE P-VALUE OF NIST STATISTICAL TEST                             #
##############################################################################################################

# To call the different related libraries required for the program//
import matplotlib.pyplot as plt

##############################################################################################################
# To describe the bars//

barWidth = 0.9  # To determine the width of the bar//
bars = [0.544515, 0.480032, 0.732717, 0.894694, 0.485698, 0.152105, 0.457296, 0.834508, 0.643127, 0.853442,
        0.09382, 0.865675, 0.964953, 0.739831, 0.801199]  # Values of each bar//
r = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]  # To determine the position of the bars//

w = 7
h = 7
d = 60
plt.figure(figsize=(w, h), dpi=d) # To plot the figure//
plt.bar(r, bars, width=barWidth, color='#557f2d') # To plot the bar graph//

'''
    For reference related to this program check the mentioned URL's attached herein below:
    https://python-graph-gallery.com/10-barplot-with-number-of-observation/
    https://python-graph-gallery.com/11-grouped-barplot/
'''

plt.xticks([r + barWidth for r in range(len(r))],
           ['Frequency', 'Block Frequency', 'Cumulative Sums', 'Runs', 'Longest Runs', 'Rank', 'FFT',
            'NonOverlapping Template', 'Overlapping Template', 'Universal', 'Approximate Entropy',
            'Random Excursions', 'Random Excursions Variant', 'Serial', 'Linear Complexity'],
           rotation=90, size = 12) # To determine the name of the bars and the related parametrical descriptions//

ax = plt.subplot()
ax.set_yscale('log')  # To determine the logarathmic scale of the vertical axis//
ax.hlines(y=0.01, xmin=0, xmax=16, linewidth=1.5, color='r')  # To insert the significance level in the graph//
plt.subplots_adjust(bottom=0.35, top=0.98)  # To adjust the space below and above of the graph//
plt.show()  # To display the graph//
