#!/user/bin/env python3
#===============================================================================
# life_satisfaction.py
#===============================================================================

# Imports ======================================================================

import argparse
import pandas as pd
import seaborn as sns




# Functions ====================================================================

def parse_arguments():
    parser = argparse.ArgumentParser(
        description='plot life satisfaction'
    )
    parser.add_argument(
        'file',
        metavar='<path/to/file.{pdf,png,svg}>',
        help='path to output file'
    )
    return parser.parse_args()


def main():
    args = parse_arguments()
    sns.set(style='whitegrid')
    life_satisfaction = pd.DataFrame(
        { 
            'Division': ('Biological Sciences',) * 3 + ('Jacobs School of Engineering',) * 3,
            'Response': ('Unsatisfied', 'Satisfied', 'Highly Satisfied') * 2,
            'Percent': (30, 48, 22, 24, 57, 19)
        }
    )
    sns.set_color_codes('muted')
    ax = sns.barplot(
        x='Division', y='Percent', data=life_satisfaction, hue='Response',
        palette=(sns.color_palette()[i] for i in (3, 9, 0))
    )
    ax.set_title('Life Satisfaction')
    ax.legend(ncol=3, loc='upper left', frameon=True)
    ax.set(ylabel='% of Total Number of Records')
    for p in ax.patches:
        height = p.get_height()
        ax.text(
            p.get_x()+p.get_width()/2.,
            height - 6,
            '{:1.0f}%'.format(height),
            ha='center',
            color='w'
        ) 
    fig = ax.get_figure()
    fig.savefig(args.file, format=args.file.split('.')[1])





# Execute ======================================================================

if __name__ == '__main__':
    main()
