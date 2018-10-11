import matplotlib.pyplot as plt
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np
import pandas as pd
import geopandas as gpd

def prev_over_time(save_bool, plot_bool):
    '''
    Plot prevalence of groups over time
    save_bool: 1 == save the plot, 0 == don't save it
    plot_bool: 1 == display the plot, 0 == don't display it
    '''
    df_year_count = df.groupby('year').count()['name']
    df_year_count.plot(kind='area', color='m', alpha=0.25, linewidth=3.0)
    plt.title('Prevalence of Organizations Over Time', weight='bold', size=14)
    plt.xlabel('Year', weight='bold')
    plt.ylabel('Group Count', weight='bold')
    if save_bool == 1:
        plt.savefig('Pervasiveness_over_time')
    if plot_bool == 1:
        plt.show()

def prov_over_time(save_bool, plot_bool):
    '''
    Plot count of provisions over time
    save_bool: 1 == save the plot, 0 == don't save it
    plot_bool: 1 == display the plot, 0 == don't display it
    '''
    df_year_count_prov = df.groupby('year').sum()['total']
    df_year_count_prov.plot(kind='area', color='g', alpha=0.25, linewidth=3.0)
    plt.title('Total Provisions Over Time', weight='bold', size=14)
    plt.xlabel('Year', weight='bold')
    plt.ylabel('Provision Count', weight='bold')
    plt.tight_layout()
    if save_bool == 1:
        plt.savefig('Provisions_over_time')
    if plot_bool == 1:
        plt.show()

def make_pie(save_bool, plot_bool):
    '''
    Plot pie chart of different provision types, across time, and across groups
    save_bool: 1 == save the plot, 0 == don't save it
    plot_bool: 1 == display the plot, 0 == don't display it
    '''
    df_sum = df.sum()
    df_prov_pie = df_sum[['religion','infrastructure', 'health', 'education', 'finance', 'security', 'society']]
    title = plt.title('Sum of Provisions in Full Dataset, By Type', weight='bold', size=14)
    plt.gca().axis('equal')
    pie = plt.pie(df_prov_pie, startangle=0, autopct='%1.0f%%')
    labels = ['religion','infrastructure', 'health', 'education', 'finance', 'security', 'society']
    plt.legend(pie[0], labels, bbox_to_anchor=(1,0.5), loc='center right', fontsize=10,
    bbox_transform=plt.gcf().transFigure, title='Provision Type')
    plt.subplots_adjust(left=0.0, bottom=0.1, right=0.8)
    plt.ylabel('')
    if save_bool == 1:
        plt.savefig('Pie_prov')
    if plot_bool == 1:
        plt.show()

def make_world(save_bool, plot_bool):
        world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
        ax = world.plot(figsize=(20,5))
        ax.axis('off')
        world.head()
        if save_bool == 1:
            plt.savefig('World')
            world.head().to_csv('world_head.csv')
        if plot_bool == 1:
            plt.show()

def clean_then_plot_heatmap(df):
    '''
    Stacking country names when there are multiple names per cell that are separated by a comma. This results in a df that has rows of countries and years, where each row is representative of a non-state group. e.g., if there are 20 different groups in one country in a given year, there will be 20 country entries for that year
    df: original pandas df
    '''
    df_base = df[['base', 'year']]
    df_base_disaggr = pd.DataFrame(df_base.base.str.split(',').tolist(), index=df_base.year).stack()
    df_base_disaggr = df_base_disaggr.reset_index()[[0, 'year']] # var1 variable is currently labeled 0
    df_base_disaggr.columns = ['base', 'year'] # renaming var1
    df_base_disaggr['base'] = df_base_disaggr['base'].apply(remove_spaces) # for .apply don't have to pass in a parameter; it knows to check row by row
    # return df_base_disaggr.head()
    count_countries(df_base_disaggr)

def remove_spaces(row):
    '''
    A function to remove remaining weird spaces in country names:
    Remove spaces from column of type string
    row: don't have to pass in parameter here, because .apply automatically knows to check data row by row
    '''
    country = row.split()
    cleaned_lst = []
    for name in country:
        name = name.replace(" ","")
        if len(name) > 1:
            cleaned_lst.append(name)
    return " ".join(cleaned_lst)

def count_countries(df):
    '''
    Counting the number of country instances, across years
    df: original pandas df
    '''
    # print('Doing it')
    df_base_count = df['year'].groupby(df['base']).count()
    # print(df_base_count.head())
    df_base_count = df_base_count.reset_index()
    df_base_count.rename(columns ={'year':'count'}, inplace = True)
    df_base_count.rename(columns ={'base':'name'}, inplace = True)
    df_base_count = df_base_count.sort_values('count', ascending = False)
    df_base_count.reset_index(drop=True, inplace = True)
    final_clean(df_base_count)

def final_clean(df):
    '''
    Making sure spelling/wording for countries in original df is consistent with that of the world dataset
    df: df from count_countries
    '''
    dict_cleaned = {'West Bank/Gaza':'Israel',
    'Northern Ireland (UK)':'Ireland',
    'Kashmir':'India',
    'Democratic Republic of the Congo':'Congo',
    'Burma (Myanmar)':'Myanmar',
    'Northern Ireland':'Ireland',
    'United Kingdom)':'United Kingdom',
    'Chechnya':'Russia',
    'Federal Republic of Germany':'Germany',
    'German Democratic Republic':'Germany',
    'Western Sahara':'W. Sahara',
    'Namibia (South West Africa)':'Namibia',
    'Republic of Macedonia':'Macedonia',
    'Burma (myanmar)':'Myanmar',
    'Rhodesia':'Zimbabwe',
    'chile':'Chile',
    'Gaza/Westbank':'Israel',
    "Cote d'Ivoire":"Côte d'Ivoire",
    'FRY (Kosovo)':'Kosovo',
    'Bosnia':'Bosnia and Herz.',
    'Bahrain':'Saudi Arabia',
    'Serbia and Montenegro':'Serbia',
    'Kyrgyztan':'Kyrgyzstan',
    'Singapore':'Malaysia',
    'Guadeloupe':'Dominican Rep.',
    'Corsica':'Italy',
    'Colmbia':'Colombia',
    'Laos':'Lao PDR'}
    df['name'] = df['name'].replace(dict_cleaned)
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    # print(world.info())
    country_names = world[['name', 'continent', 'geometry', 'iso_a3']]
    world_merged = country_names.merge(df, on='name')
    # print(world_merged.describe())
    plot_heatmap(world_merged)

def plot_heatmap(df):
    '''
    Plot the heatmap
    df: df from final_clean()
    '''
    df.plot(column='count', cmap='Reds', linewidth=0.5, edgecolor='black', legend=True,
     figsize=(20,20), scheme='quantiles')
    plt.savefig('Heatmap')

def US_groups(df):
    '''list of all organizations in the U.S.'''
    df_US = df[df['base'].str.contains("United States")]
    df_US['name'].value_counts().to_csv('US_group_list.csv')

def sep_dfs(df, group_list, base_str='United States'):
    '''
    This function will take in an original dataframe, and create separate dataframes for all groups in group_list
    df: original dataframe
    group_list: list of groups to observe
    base_str: country of interest, defaults to United States
    '''
    df_list = []
    for str in group_list:
        df_for_merge = df[(df['base'].str.contains(base_str)) & (df['name'].str.contains(str))]
        df_list.append(df_for_merge)
    return df_list
    # (df_list, group_list, groupby, to_sum)

def sum_one_var(df_list, groupby, to_sum):
    '''
    This function will take in a list of dataframes, each for a different group, group by some variable (groupby),
    and sum up another variable (to_sum), and return the grouped and summed dfs
    df_list: list of dfs created in sep_dfs
    groupby: variable to group on
    to_sum: variable to sum up
    '''
    sum_list = []
    for df in df_list:
        grouped = df.groupby(groupby).sum()[to_sum]
        sum_list.append(grouped)
    return sum_list

def sum_mult_vars(df_list, groupby, to_sum_list):
    '''
    This function will take in a list of dataframes, each for a different group (can also be a list containing only one group),
    group by some variable (groupby), and sum up a group of variables, separately (to_sum_list), and return the grouped and summed dfs
    df_list: list of dfs created in sep_dfs
    groupby: variable to group on
    to_sum: list of variables to sum up
    '''
    sum_list = []
    for df in df_list:
        for item in to_sum_list:
            grouped = df.groupby(groupby).sum()[item]
            sum_list.append(grouped)
    return sum_list

def multi_line_plot(df_sum_list, legend_list, title, xlab, ylab, save_bool, plot_bool, save_as, legend_title, xrestrict_lower=0, xrestrict_upper=0, yrestrict_upper=0):
    '''
    This function will create a set of line graphs in a single space.
    df_sum_list: list of dfs that have been grouped and summed on some variable in function sum_var
    group_list: list of groups/categories to observe (this is the multi-category variable in the legend)
    title: title for plot
    xlab: x axis label for plot
    ylab: y axis label for plot
    save_bool: 1 == save the plot, 0 == don't save it
    plot_bool: 1 == display the plot, 0 == don't display it
    '''
    for df, item in zip(df_sum_list, legend_list):
        line = df.plot(kind = 'area', label=item, alpha=0.25, linewidth=2.0)
        line.set_label(item)
    plt.legend(title=legend_title, loc='upper left')
    plt.title(title, weight='bold')
    if xrestrict_lower > 0 & xrestrict_upper > 0:
        plt.xlim(xrestrict_lower, xrestrict_upper)
    if yrestrict_upper > 0:
        plt.ylim(0, yrestrict_upper)
    # if save_as == 'Ku Klux Klan Provisions Over Time':
    # if ylim == 1:
    #     plt.ylim(0,20000)
    plt.xlabel(xlab, weight='bold')
    plt.ylabel(ylab, weight='bold')
    if save_bool == 1:
        plt.savefig(save_as)
    if plot_bool == 1:
        plt.show()

def merge_dfs(list_of_dfs):
    merged = pd.DataFrame()
    for df in list_of_dfs:
        merged = merged.append(df, ignore_index=True)
    return merged



if __name__ == '__main__':
    #install ConvertToUTF8 package in ATOM for editing and saving files in order to open
    df = pd.read_csv("data/TIOS_data_v2.csv")
    # print(prev_over_time(1,0))
    # print(prov_over_time(1,1))
    # print(make_pie(1,0))
    # print(make_world(1,0))
    # print(clean_then_plot_heatmap(df))
    # print(US_groups(df))

    '''Plotting three line graphs in one space'''
    top3list = ['Ku Klux Klan', 'Jewish Defense League', 'Black Panthers']
    make_separate_dfs = sep_dfs(df, top3list)
    make_sums_one_var = sum_one_var(make_separate_dfs, 'year', 'artcount')
    # print(multi_line_plot(make_sums_one_var, top3list, 'Article Appearances Over Time, By U.S. Group', 'Year', 'Article Count', 1, 0, 'USgroup_art_count_over_time', 'U.S. Group'))

    '''Plot provisions for a single group over time and by type'''
    group_list = ['KKK']
    prov_list = ['religion','infrastructure', 'health', 'education', 'finance', 'security', 'society']
    prov_list_no_soc = ['religion','infrastructure', 'health', 'education', 'finance', 'security']
    make_separate_dfs = sep_dfs(df, group_list)

    '''Plot with Society'''
    make_sums_mult_vars = sum_mult_vars(make_separate_dfs, 'year', prov_list)
    print(multi_line_plot(make_sums_mult_vars, prov_list, 'Ku Klux Klan Provisions Over Time', 'Year', 'Provision Count', 1, 0, 'KKK_prov_type_over_time', 'Provision Type', 0, 0, yrestrict_upper=25000))

    '''Plot without Society'''
    make_sums_mult_vars_no_soc = sum_mult_vars(make_separate_dfs, 'year', prov_list_no_soc)
    # print(multi_line_plot(make_sums_mult_vars_no_soc, prov_list_no_soc, 'Ku Klux Klan Provisions Over Time (without Social)', 'Year', 'Provision Count', 1, 0, 'KKK_prov_type_over_time_no_soc', 'Provision Type'))
    # print(multi_line_plot(make_sums_mult_vars_no_soc, prov_list_no_soc, 'Ku Klux Klan Provisions During the 1990s (without Social)', 'Year', 'Provision Count', 1, 0, 'KKK_prov_type_over_time_no_soc_90s', 'Provision Type', 1990, 1999, 0, 0))
