#!/user/bin/env python3
#===============================================================================
# food_security.py
#===============================================================================

# Imports ======================================================================

import argparse
import pandas as pd
import seaborn as sns




# Functions ====================================================================

def parse_arguments():
    parser = argparse.ArgumentParser(
        description='plot financial confidence'
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
            'Population': ('Graduate students',) * 2 + ('General population',) * 2,
            'Condition': ('Anxiety', 'Depression') * 2,
            'Percent': (41, 39, 6, 6)
        }
    )
    sns.set_color_codes('muted')
    ax = sns.barplot(
        x='Population', y='Percent', data=life_satisfaction, hue='Condition',
        palette=(sns.color_palette()[i] for i in (0, 3))
    )
    ax.set_title('Prevalence of anxiety and depression')
    ax.legend(ncol=3, loc='upper right', frameon=True)
    ax.set(ylabel='Prevalence')
    for p in ax.patches:
        height = p.get_height()
        ax.text(
            p.get_x()+p.get_width()/2.,
            height - 3,
            '{:1.0f}%'.format(height),
            ha='center',
            color='w'
        ) 
    fig = ax.get_figure()
    fig.savefig(args.file, format=args.file.split('.')[1])





# Execute ======================================================================

if __name__ == '__main__':
    main()
