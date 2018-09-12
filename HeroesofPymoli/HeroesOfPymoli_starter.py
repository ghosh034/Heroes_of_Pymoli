
# coding: utf-8

# ### Heroes Of Pymoli Data Analysis
# * Of the 1163 active players, the vast majority are male (84%). There also exists, a smaller, but notable proportion of female players (14%).
# 
# * Our peak age demographic falls between 20-24 (44.8%) with secondary groups falling between 15-19 (18.60%) and 25-29 (13.4%).  
# -----

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[158]:


# Dependencies and Setup
import pandas as pd
import numpy as np

# Raw data file
file_to_load = "Resources/purchase_data.csv"

# Read purchasing file and store into pandas data frame
purchase_data = pd.read_csv(file_to_load)
purchase_data.head()


# ## Player Count

# * Display the total number of players
# 

# In[159]:


totalplayers = purchase_data["SN"].nunique()
totalplayers
totalplayers_df = pd.DataFrame({"Total Players":[totalplayers]})
totalplayers_df


# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[160]:


totaluniqueitems = purchase_data["Item ID"].nunique()
totaluniqueitems
averageprice = purchase_data["Price"].mean()
averageprice
numberofpurchases = purchase_data["Purchase ID"].count()
numberofpurchases
totalrevenue = purchase_data["Price"].sum()
totalrevenue
purchaseanalysis_df = pd.DataFrame({"Number of Unique Items":[totaluniqueitems],"Average Price":[averageprice],"Number of Purchases":[numberofpurchases],"Total Revenue": [totalrevenue]})
purchaseanalysis_df["Average Price"] = purchaseanalysis_df["Average Price"].map("${:.2f}".format)
purchaseanalysis_df


# ## Gender Demographics

# * Percentage and Count of Male Players
# 
# 
# * Percentage and Count of Female Players
# 
# 
# * Percentage and Count of Other / Non-Disclosed
# 
# 
# 

# In[162]:


totalgendercount = purchase_data["Gender"].count()
gendercount = purchase_data["Gender"].value_counts()
gendercount
genderpercent = round(gendercount / totalgendercount*100, 2)
genderpercent
genderdemographics_df = pd.DataFrame({"Percentage of players":genderpercent,"Total Count":gendercount})
genderdemographics_df


# 
# ## Purchasing Analysis (Gender)

# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# 
# 
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[163]:


purchase_groupbygender = purchase_data.groupby(["Gender"])
purchase_groupbygender.count().head(10)
purchasecount_bygender = purchase_groupbygender["Price"].count()
purchasecount_bygender
averageprice_bygender = round(purchase_groupbygender["Price"].mean(),2)
averageprice_bygender
totalpurchase_bygender = round(purchase_groupbygender["Price"].sum(),2)
totalpurchase_bygender
averagepurchasetotalPP_bygender = round(totalpurchase_bygender/purchasecount_bygender,2)
averagepurchasetotalPP_bygender
purchaseanalysis_bygender_df = pd.DataFrame({"Purchase Count":purchasecount_bygender,"Average Purchase Price": averageprice_bygender, "Total Purchase Value":totalpurchase_bygender, "Average Purchase Total per Person": averagepurchasetotalPP_bygender})
purchaseanalysis_bygender_df


# ## Age Demographics

# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# In[164]:


# Establish bins for ages
age_bins = [0, 9.90, 14.90, 19.90, 24.90, 29.90, 34.90, 39.90, 99999]
group_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]
purchase_data["Age Group"] = pd.cut(purchase_data["Age"], age_bins, labels=group_names)
agegroup_count = purchase_data["Age Group"].value_counts()
agegroup_count
agegroup_percentage = round(agegroup_count/totalplayers*100,2)
agegroup_percentage
agedemographics_df = pd.DataFrame({"Percentage of Players":agegroup_percentage, "Total Count": agegroup_count})
agedemographics_df


# ## Purchasing Analysis (Age)

# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[165]:


agegroup_df = purchase_data.groupby("Age Group") 
agegroup_df.count().head(10)
purchasecount_byagegroup = agegroup_df["Price"].count()
purchasecount_byagegroup
averageprice_byagegroup = round(agegroup_df["Price"].mean(),2)
averageprice_byagegroup
totalpurchase_byagegroup = round(agegroup_df["Price"].sum(),2)
totalpurchase_byagegroup
averagepurchasetotalPP_byagegroup = round(totalpurchase_byagegroup/purchasecount_byagegroup,2)
averagepurchasetotalPP_byagegroup
purchaseanalysis_byagegroup_df = pd.DataFrame({"Purchase Count":purchasecount_byagegroup,"Average Purchase Price": averageprice_byagegroup, "Total Purchase Value":totalpurchase_byagegroup, "Average Purchase Total per Person": averagepurchasetotalPP_byagegroup})
purchaseanalysis_byagegroup_df


# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[166]:


SN_df = purchase_data.groupby("SN")
purchasecount_bySN = SN_df["Price"].count()
purchasecount_bySN
averageprice_bySN = round(SN_df["Price"].mean(),2)
averageprice_bySN
totalpurchase_bySN = round(SN_df["Price"].sum(),2)
totalpurchase_bySN
topspenders_df = pd.DataFrame({"Purchase Count":purchasecount_bySN,"Average Purchase Price": averageprice_bySN, "Total Purchase Value":totalpurchase_bySN})
Topspenders_df = topspenders_df.sort_values(["Total Purchase Value"], ascending=False)
Topspenders_df.head(5)


# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[167]:


items_df = purchase_data[["Item ID", "Item Name", "Price"]]
items_df.head()
purchasedata_groupbyitems = items_df.groupby(["Item ID", "Item Name"])
purchasedata_groupbyitems.head()
purchasecount_byitem = purchasedata_groupbyitems["Price"].count()
purchasecount_byitem
totalprice_byitem = round(purchasedata_groupbyitems["Price"].sum(),2)
totalprice_byitem
price_peritem = round(totalprice_byitem/purchasecount_byitem,2)
price_peritem
popularitems_df = pd.DataFrame({"Purchase Count":purchasecount_byitem,"Item Price": price_peritem, "Total Purchase Value":totalprice_byitem})
Popularitems_df = popularitems_df.sort_values(["Purchase Count"], ascending=False)
Popularitems_df.head()


# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

# In[168]:


Profitableitems_df = popularitems_df.sort_values(["Total Purchase Value"], ascending=False)
Profitableitems_df.head()

