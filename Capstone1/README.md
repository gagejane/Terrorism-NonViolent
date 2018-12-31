# **Exploring Data on 45 years of Service Provisions Among Non-state Actors**
# Jane Stout, Ph.D.


## Background

![OEF](images/OEF.jpg) ![OEFR](images/OEFR.jpg)


One Earth Future(OEF) is a non-profit in Broomfield, CO, whose mission is to foster sustainable peace by building effective networks and resilient societies in fragile and post-conflict environments around the world. OEF has a research department (OEF Research) aiming to produce actionable, empirical research that speaks to how a world without war can be achieved. One line of research at OEF focuses on the role of terrorist and insurgent groups (heretofore referred to as “non-state actors") in times of conflict. In particular, OEF studies non-state actors’ use of social services during times of conflict. According to OEF researchers, non-violent activities of violent groups are correlated with many important outcomes and enhance our understanding of the internal functions of terrorist organizations. For instance, some violent groups seek legitimacy and international support through service provision (see Heger & Jung, 2017).

## Data Description
For this project, I used OEF’s Terrorist and Insurgent Organizations’ Service Provision across time dataset (TIOS 2.0; for more information, see Heger, Jung, and Wagstaff, 2018). The TIOS 2.0 dataset provides indicators associated with whether and how more than 400 violent non-state actors provide public goods and services across more than four decades (1969–2013). Accoring to OEF researchers, an underlying assumption of these data is that service-providing groups will have, on average, more stories mentioning service provision compared with groups that provide fewer or no services (Heger & Jung, 2017). To the best of OEF’s knowledge, this dataset represents the widest coverage across both time and groups for this type of data.

Data were collected from a predetermined list of approximately 400 non-state groups (detailed in Cronin, 2011). Data were pulled from all English language print news coverage available on LexisNexis. As of 2006, LexisNexis has the world's largest electronic database for legal and public-records related information. For each group in the sample, OEF searched within new stories for words and phrases that correlate with service provisions (see _Describing the Data_ section for details).

#### **From the TIOS 2.0 codebook:**

_"Each observation in the dataset is a group-year. There are, broadly speaking, four sets of variables. The first are the raw counts of keywords. The values for these variables equal the number of times that keyword was mentioned in all of the .txt files for that group-year. The second set of variables are manipulations of the raw counts. These variables include the combinations of the raw counts into sectors as well as taking the mean of all within-sector variables. These give a broader sense of the types of services each group provides each year. The third set of variables provide a sense of coverage using two metrics. The first of these is the word count for each group-year. The second is the article count for each group-year. The last set of variables includes the identifiers for each observation and includes variables suited to merging these data with other commonly used conflict datasets."_

## Capstone1 Goals
+ Enhance my visualization skills.
+ Explore the TIOS 2.0 data, with an eye toward future potential research questions that will use inferential statistics/model testing. This could be accomplished by merging the TIOS 2.0 with other datasets (e.g., the Global Terrorism Database).

## Describing the Data
N = 6659 group-years

Exploration consisted of a few key factors:
+ **Time** (1969-2013)
+ **Groups** (e.g., Taliban, Ku Klux Klan)
+ **Base** (country in which group is located)
+ **Provisions** (types and counts):
  + Religion: church, mosque
  + Infrastructure: reconstruction, trash
  + Health: hospital, medic
  + Education: school, teacher
  + Finance: loan, microloan
  + Security: militia
  + Society: cultural, sport

## Data Visualization
I first created an area graph of group prevalence over time. Figure 1 represents a count of unique organization names in the dataset for each year.

![Pervasiveness_over_time](Pervasiveness_over_time.png)

**Figure 1. The number of unique organization names in the dataset, over time.**

I also created an area graph of provisions rendered over time. Figure 2 provides a count of the total number of provisions documented in the dataset for each year.

![Provisions over time](/Users/janestout/Dropbox/Galvanize/DSI/Capstones/FinalWork/Provisions_over_time.png)

**Figure 2. The number of provisions in the dataset, over time.**


<!-- + A plot of these on the same graph reveals they their range is very different (prev max is 250, prov max is 2000000 [mil], see Provision_Type_over_time). Because social provisions were on much larger range than the rest of the provisions, I created a line graph of provisions by type over time, omitting social provisions. This graph represents a count of the number of specific provisions in the dataset for each year, omitting social provisions. (see Provision_Type_over_time_noSoc) -->
Next, I created a pie graph of the count of each type of provision in the dataset, collapsed across year. As seen in Figure 3, social provisions are by far the most popular provisions.

![Pie provisions](Pie_prov.png)

**Figure 3. Type and relative amount of provisions in the dataset, collapsed across time.**

Next, I explored data on the base country for each non-state actor. I used GeoPandas to create a heatmap of the number of times non-state actors provided services, collapsed across time. To do this, I used the GeoPandas built-in "world" dataframe, which contains country names, geometric shapes of those countries, and spatial location of those shapes on the world map. See Table 1 for the first five rows of the built-in world dataframe.



| pop_est  | continent     | name                 | iso_a3 | gdp_md_est | geometry                                                     |
|----------|---------------|----------------------|--------|------------|--------------------------------------------------------------|
| 28400000 | Asia          | Afghanistan          | AFG    | 22270      | POLYGON ((61.21081709172574 35.65007233330923,...))          |
| 12799293 | Africa        | Angola               | AGO    | 110300     | MULTIPOLYGON (((16.32652835456705 -5.877470391466218,...)))  |
| 3639453  | Europe        | Albania              | ALB    | 21810      | POLYGON ((20.59024743010491 41.85540416113361,...))          |
| 4798491  | Asia          | United Arab Emirates | ARE    | 184300     | POLYGON ((51.57951867046327 24.24549713795111,...))          |
| 40913584 | South America | Argentina            | ARG    | 573900     | MULTIPOLYGON (((-65.50000000000003 -55.19999999999996,...))) |

**Table 1. The first five rows of the GeoPands built-in "world" dataframe.**

Using the world dataframe, GeoPandas builds a template that can be applied to a researcher's own data (see Figure 4 for template).

![World](World.png)

**Figure 4. World template using GeoPandas built-in "world" dataframe.**

To work with this template, I merged my pandas dataframe with the world dataframe, matching on country name. My dataframe contained the count of the total number of times non-state actors provided services, aggregated across year. See Figure 5 for the resulting heatmap, which represents the prevalence of non-state actors' services over the past 45 years.

![heatmap](Heatmap.png)

**Figure 5. Heatmap displaying the number of unique groups in each country, summed over time. Heat is displayed in quadrants.**

I noticed a lot of "heat" in the U.S., so I explored the prevalence of groups in the U.S. and their provision rate. Table 2 displays a count of U.S. non-state actors over time. N = 45 indicates a group has provided services for each year in the dataset (i.e., 45 years).


<!-- ![UG_group_list](UG_group_list.jpg) -->

| Groups in the United States                     | N Years |
|-------------------------------------------------|---------|
| Jewish Defense League (JDL)                     | 45      |
| Ku Klux Klan (KKK)                              | 44      |
| Black Panthers                                  | 44      |
| Omega-7                                         | 37      |
| El Rukn                                         | 36      |
| Army of God                                     | 35      |
| Order II                                        | 33      |
| Aryan Nations (AN)                              | 31      |
| Armed Forces of National Liberation             | 24      |
| Hammerskin Nation                               | 21      |
| al-Fuqra                                        | 21      |
| Covenant Sword and Arm of the Lord (CSA)        | 20      |
| Islamic Salvation Front                         | 14      |
| Croatian Freedom Fighters (CFF)                 | 13      |
| Nation of Yahweh                                | 13      |
| Cambodian Freedom Fighters (CFF)                | 13      |
| Yemen Islamic Jihad                             | 10      |
| Justice Commandos for the Armenian Genocide     | 9       |
| Armenian Revolutionary Army                     | 9       |
| Hector Riobe Brigade                            | 2       |
| Black Revolutionary Assault Team                | 1       |
| Independent Armed Revolutionary Movement (MIRA) | 1       |    

**Table 2. A count of the number of years U.S. groups appear in articles.**


Next, I explored data on the top three U.S. groups see in Table 2:
* Jewish Defense League
* Ku Klux Klan
* Black Panthers

Figure 6 shows a count of the number of articles in which groups were mentioned over time.

![US article count over time](USgroup_art_count_over_time.png)

**Figure 6. A count of the number of articles for three U.S. groups.**

Given that the Ku Klux Klan is the most prevalent group in the U.S. (as a function of article count), I explored their provision rate by type, over time. As seen in Figure 7, social provisions were by far the most prevalent provision.

![Provision_Type_over_time_KKK](KKK_prov_type_over_time.png)

**Figure 7. Provisions provided by the Ku Klux Klan by type over time.**

To take a closer look at the prevalence of non-society related provisions for the Ku Klux Klan, I re-plotted Figure 7, this time omitting society provisions.

![Provision_Type_over_time_KKK_noSoc](KKK_prov_type_over_time_no_soc.png)

**Figure 8. Provisions provided by the Ku Klux Klan by type over time, omitting society provisions.**

I noticed a spike in religious provisions for the KKK in the 90s, so I zoomed in on that (see Figure 9).

![KKK in the 90s](KKK_prov_type_over_time_no_soc_90s.png)

**Figure 9. Provisions provided by the Ku Klux Klan by type during the 1990's, omitting society provisions.**

What was going on around 1996?
+ 1996: Election year
+ 1995: O.J. Simpson trial
+ 1995: Million Man March; conceived by Nation of Islam leader Louis Farrakhan



## Future Directions
One possible future direciton is to use the TIOS 2.0 data to make predictive models. One way to do this would be to merge the TIOS 2.0 data with another dataset(s) so that provision prevalence and type could be treated as predictors. This type of analysis could address questions like: _Do provisions increase group membership? Do provisions increase public favor/perceptions of legitimacy? If so, which provisions are most influential?_

Another future direction is to continue to focus on domestic forms of terrorism. To continue this line of inquiry, I plan to work with the Global Terrorism Database (GTD), which is an open-source database that provides information on terrorist events around the world from 1970 through 2017. The GTD has the following characteristics:
+ Contains information on over 180,000 terrorist attacks, from 1970-2017
+ More than 4,000,000 news articles and 25,000 news sources were reviewed to collect incident data from 1998 to 2017 alone
+ Includes information on at least 45 variables for each case, with more recent incidents including information on more than 120 variables
  + Target Type, Perpetrator, Attack Type, Weapon Type

## References
Cronin, A. K. (2011) _How Terrorism Ends: Understanding the Decline and Demise of Terrorist Campaigns._ Princeton, NJ: Princeton University Press.

Heger, Lindsay L. and Danielle F. Jung (2015) Negotiating with rebels: The effect of rebel service provision on conflict negotiations. _Journal of Conflict Resolution, 61,_ 1203-1229.

Heger, L. L., Jung, D. F., & Wagstaff, W. A. (2018) _Longitudinal indicators of service provisions by terrorist and insurgent oranizations._ One Earth Future Research, Broomfield, CO.
