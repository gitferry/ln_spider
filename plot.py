import numpy as np
import matplotlib
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

def data_from_file(filename):
    fl = open(filename)
    fileArray = fl.readlines()

    channel_counts = []

    for line in fileArray:
        channel_counts.append(int(line.strip()))

    sum_counts = process_data(channel_counts)

    return sum_counts

def process_data(channel_counts):
    sum_count = 0
    total_counts = []
    for count in channel_counts:
        sum_count += count
        total_counts.append(sum_count/2000.0)

    return total_counts

def process_index(number):
    index = []
    for i in range(number):
        index.append(float((i+1))/float(number))

    return index



def do_plot(channel_counts):
    lenghth = len(channel_counts)
    print(lenghth)
    print(channel_counts[-1])
    index = process_index(lenghth)

    fig, ax = plt.subplots()
    ax.set_xlabel("Fraction of Hosts Needed to Provide Channels")
    ax.set_ylabel("Number of Channels ($\\times10^3$)")
    ax.set_xlim(0,1.0,0.1)
    ax.set_ylim(0,30)
    channel_plot = ax.plot(index, channel_counts)
    y = channel_counts[144]
    print(y)
    x_plot = ax.plot([0.05, 0.05], [y,0], 'k--', lw=1.5)
    y_plot = ax.plot([0.05, 0], [y,y], 'k--', lw=1.5)
    yyplot = ax.plot([1.0,0], [channel_counts[-1], channel_counts[-1]], 'k--', lw=1.5)

    plt.grid(True)
    plt.xticks([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
    plt.annotate(r'14.05', xy=(0.05,y), xycoords='data', xytext=(+30,-30), textcoords='offset points', fontsize=16, arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=0.2'))
    plt.annotate(r'27.33', xy=(0,channel_counts[-1]), xycoords='data', xytext=(+20,-50), textcoords='offset points', fontsize=16, arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=0.2'))
    # plt.show()
    plt.savefig('reproduce.pdf', format='pdf')

if __name__ == '__main__':
    filename = './data.txt'
    channel_counts = data_from_file(filename)
    do_plot(channel_counts)
